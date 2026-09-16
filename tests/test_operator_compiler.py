import json
from pathlib import Path

import pytest

from operator_compiler.contracts import OPERATORS, compile_contracts
from operator_compiler.interactions import InteractionModel
from operator_compiler.measurements import MeasurementStore
from operator_compiler.motifs import induce_macros, mine_motifs
from operator_compiler.planner.astar import AStarPlanner
from operator_compiler.planner.beam import BeamPlanner
from operator_compiler.planner.branch_bound import BranchBoundPlanner
from operator_compiler.planner.greedy import GreedyPlanner
from operator_compiler.replay import counterfactual_replay
from operator_compiler.runtime.controller import OperatorController
from operator_compiler.state import OperatorState
from operator_compiler.transfer import evaluate_transfer
from operator_compiler.value import ApplicabilityModel, ValueEstimator

ROOT = Path(__file__).parents[1]
DATA = ROOT / "data"
MEASUREMENTS = DATA / "measurements"


def store():
    return MeasurementStore.from_directory(MEASUREMENTS)


def test_01_state_ir_round_trip_and_invariants():
    state = OperatorState(
        target="x",
        objective="resolve",
        live_alternatives=("a", "b"),
        evidence=("e1",),
        decision_partition=(("a",), ("b",)),
        requirements=("r1",),
        discriminators=("probe",),
        budget=2.0,
        authority=frozenset({"read"}),
        capabilities=frozenset({"inspect"}),
        history=("COMPILE",),
        representation="prose",
        closure_state="OPEN",
    )
    restored = OperatorState.from_dict(state.to_dict())
    assert restored == state
    with pytest.raises(ValueError):
        OperatorState(target="x", objective="y", budget=-1)


def test_02_compile_all_18_dictionary_contracts():
    contracts = compile_contracts(DATA / "contracts_seed.json")
    assert set(contracts) == set(OPERATORS)
    for op, contract in contracts.items():
        assert contract.operator == op
        assert contract.transition
        assert contract.preconditions
        assert contract.postconditions
        assert contract.evidence_obligations
        assert contract.failure_rules
        assert contract.closure_rules


def test_03_applicability_has_distinct_states():
    model = ApplicabilityModel()
    s = OperatorState(
        target="x", objective="decide", live_alternatives=("a", "b"),
        decision_partition=(("a",), ("b",)), discriminators=("p",), budget=1.0,
        capabilities=frozenset({"test", "inspect", "verify"}), authority=frozenset({"read", "test"}),
    )
    assert model.assess("TEST", s).status == "APPLICABLE"
    assert model.assess("CLOSE", s).status == "IRRELEVANT"
    unavailable = OperatorState(target="x", objective="decide", live_alternatives=("a", "b"), decision_partition=(("a",), ("b",)), discriminators=("p",), budget=1.0)
    assert model.assess("TEST", unavailable).status == "UNAVAILABLE"


def test_04_state_conditioned_value_changes_with_state():
    est = ValueEstimator(store())
    useful = OperatorState(target="x", objective="decide", live_alternatives=("a", "b"), decision_partition=(("a",), ("b",)), discriminators=("p",), budget=2.0, capabilities=frozenset({"test"}), authority=frozenset({"test"}))
    closed = OperatorState(target="x", objective="decide", live_alternatives=("a",), decision_partition=(("a",),), budget=2.0, closure_state="SOLVED")
    assert est.marginal_value("TEST", useful).expected_value > est.marginal_value("TEST", closed).expected_value


def test_05_voc_is_net_of_cost():
    est = ValueEstimator(store())
    s = OperatorState(target="x", objective="reason", live_alternatives=("a", "b"), decision_partition=(("a",), ("b",)), budget=1.0)
    v = est.value_of_computation("INFER", s)
    assert v.net_value == pytest.approx(v.expected_gain - v.expected_cost)


def test_06_evsi_uses_decision_sensitive_fields():
    est = ValueEstimator(store())
    s = OperatorState(target="x", objective="decide", live_alternatives=("a", "b"), decision_partition=(("a",), ("b",)), discriminators=("probe",), budget=1.0, capabilities=frozenset({"test"}), authority=frozenset({"test"}))
    evsi = est.evsi("TEST", s)
    assert evsi.expected_gain >= 0
    assert evsi.net_value <= evsi.expected_gain


def test_07_interactions_are_conditioned_on_predecessor_and_state():
    model = InteractionModel(store())
    base = OperatorState(target="x", objective="test", history=(), budget=2)
    after = OperatorState(target="x", objective="test", history=("TEST",), budget=2)
    assert model.synergy("TEST", "UPDATE", base) != model.synergy("TEST", "UPDATE", after)


def test_08_motif_mining_finds_known_dictionary_sequences():
    motifs = mine_motifs(MEASUREMENTS / "chain_search.csv", min_length=2, max_length=3)
    assert any(m.sequence[:2] == ("INSPECT", "SPLIT") for m in motifs)


def test_09_macro_induction_requires_positive_deletion_value():
    macros = induce_macros(
        MEASUREMENTS / "chain_search.csv",
        MEASUREMENTS / "marginal_deletion_value.csv",
    )
    assert macros
    assert all(m.measured_value > 0 and m.min_deletion_value > 0 for m in macros)


@pytest.mark.parametrize("planner_cls", [GreedyPlanner, BeamPlanner, AStarPlanner, BranchBoundPlanner])
def test_10_planners_return_required_sequence(planner_cls):
    planner = planner_cls(ValueEstimator(store()), InteractionModel(store()))
    s = OperatorState(target="x", objective="workflow", required_operators=("COMPILE", "EXPAND", "EVALUATE", "TEST", "SELECT"), budget=10.0)
    result = planner.plan(s)
    assert set(s.required_operators).issubset(set(result.sequence))
    assert result.total_cost <= s.budget


def test_11_budget_allocation_stops_on_nonpositive_value():
    controller = OperatorController(store())
    s = OperatorState(target="x", objective="done", live_alternatives=("a",), decision_partition=(("a",),), closure_state="SOLVED", budget=0.1)
    nxt = controller.next(s)
    assert nxt.operator in {"CLOSE", None}


def test_12_counterfactual_replay_distinguishes_delete_and_reorder():
    result = counterfactual_replay(("CHALLENGE", "TEST", "UPDATE"), store())
    assert result.deletions
    assert result.reorderings
    assert any(d.delta != 0 for d in result.deletions)


def test_13_transfer_keeps_regime_sign_reversals_visible():
    t = evaluate_transfer(MEASUREMENTS / "transfer_by_regime.csv")
    assert t.by_regime
    assert "POSITIVE" in t.by_regime and "ADVERSARIAL" in t.by_regime
    assert t.sign_reversal_rate >= 0


def test_14_external_model_lane_is_not_imputed():
    receipt = json.loads((MEASUREMENTS / "external_model_receipt.json").read_text())
    assert receipt["status"] == "BLOCKED_EXTERNAL_MODEL"
    assert receipt["model_trials_executed"] == 0


def test_15_runtime_controller_returns_inspectable_decision():
    controller = OperatorController(store())
    s = OperatorState(
        target="x", objective="resolve",
        live_alternatives=("a", "b"), decision_partition=(("a",), ("b",)),
        discriminators=("probe",), budget=2.0,
        authority=frozenset({"read", "test"}), capabilities=frozenset({"inspect", "test", "verify"}),
    )
    nxt = controller.next(s)
    assert nxt.operator in OPERATORS
    assert nxt.expected_cost >= 0
    assert nxt.evidence_basis
    assert nxt.alternatives


def test_16_budget_frontier_is_value_per_cost_ordered():
    from operator_compiler.budget import BudgetAllocator
    est=ValueEstimator(store())
    s=OperatorState(target="x", objective="resolve", live_alternatives=("a","b"), decision_partition=(("a",),("b",)), discriminators=("p",), budget=2.0, authority=frozenset({"test","act","read"}), capabilities=frozenset({"test","inspect","verify"}))
    f=BudgetAllocator(est).frontier(s)
    assert f
    assert all(f[i].value_per_cost >= f[i+1].value_per_cost for i in range(len(f)-1))


def test_17_external_evidence_state_preserves_blocker():
    from operator_compiler.external import external_evidence_state
    e=external_evidence_state(store())
    assert e.status == "BLOCKED_EXTERNAL_MODEL"
    assert e.trials_executed == 0
