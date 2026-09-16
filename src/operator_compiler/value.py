from __future__ import annotations
from dataclasses import dataclass
from .contracts import OPERATORS
from .measurements import MeasurementStore
from .state import OperatorState

@dataclass(frozen=True)
class Applicability:
    operator: str
    status: str
    reason: str

@dataclass(frozen=True)
class ValueEstimate:
    operator: str
    kind: str
    expected_gain: float
    expected_cost: float
    net_value: float
    evidence_basis: tuple[str, ...]

    @property
    def expected_value(self) -> float:
        return self.expected_gain

class ApplicabilityModel:
    OBSERVATIONAL = {"ACQUIRE", "INSPECT", "TEST", "VERIFY"}
    MUTATING = {"ACT", "TRANSFORM", "UPDATE"}

    def assess(self, operator: str, state: OperatorState) -> Applicability:
        if operator not in OPERATORS:
            return Applicability(operator, "INADMISSIBLE", "unknown operator")
        if state.budget <= 0 and operator != "CLOSE":
            return Applicability(operator, "UNAVAILABLE", "no budget")
        if state.solved and operator != "CLOSE":
            return Applicability(operator, "ALREADY_SATURATED", "state already solved")
        if operator == "CLOSE":
            if state.unresolved:
                return Applicability(operator, "IRRELEVANT", "material alternatives remain")
            return Applicability(operator, "APPLICABLE", "no material branch remains")
        if operator in {"TEST", "INSPECT", "VERIFY"}:
            cap = operator.lower()
            if cap not in state.capabilities:
                return Applicability(operator, "UNAVAILABLE", f"capability {cap} absent")
            if operator == "TEST" and "test" not in state.authority:
                return Applicability(operator, "INADMISSIBLE", "test authority absent")
        if operator == "ACT" and "act" not in state.authority:
            return Applicability(operator, "INADMISSIBLE", "act authority absent")
        if operator == "TEST" and not (state.discriminators or state.unresolved):
            return Applicability(operator, "IRRELEVANT", "no result-changing test target")
        if operator == "SPLIT" and len(state.live_alternatives) < 2:
            return Applicability(operator, "IRRELEVANT", "nothing material to split")
        return Applicability(operator, "APPLICABLE", "preconditions represented")

class ValueEstimator:
    INFO = {"ACQUIRE", "INSPECT", "TEST", "VERIFY"}
    COMPUTE = {"COMPILE", "REPRESENT", "SPLIT", "EXPAND", "COMPARE", "INFER", "CHALLENGE", "UPDATE", "EVALUATE", "SELECT", "CONTROL", "CLOSE"}

    def __init__(self, store: MeasurementStore):
        self.store = store
        self.applicability = ApplicabilityModel()

    def _state_factor(self, operator: str, s: OperatorState) -> float:
        if s.solved:
            return 0.0 if operator != "CLOSE" else 1.0
        factor = 1.0
        if s.unresolved and operator in {"SPLIT", "COMPARE", "INFER", "CHALLENGE", "TEST", "VERIFY", "EXPAND"}:
            factor += 0.35
        if s.discriminators and operator in {"TEST", "INSPECT", "ACQUIRE"}:
            factor += 0.30
        if s.required_operators and operator in s.required_operators:
            factor += 0.50
        if s.history:
            prev = s.history[-1]
            pair = self.store.pair(prev, operator)
            factor += max(-0.4, min(0.4, float(pair["synergy"])))
            factor += 0.01 * self.store.macro_edges.get((prev, operator), 0)
        return max(0.0, factor)

    def marginal_value(self, operator: str, state: OperatorState) -> ValueEstimate:
        app = self.applicability.assess(operator, state)
        cost = self.store.base_cost(operator)
        if app.status != "APPLICABLE":
            return ValueEstimate(operator, "MARGINAL", 0.0, cost, -cost, (f"applicability:{app.status}", app.reason))
        base_gain = max(0.0, self.store.tensor_value(operator, "POSITIVE", "gross_effect"))
        if not base_gain:
            base_gain = max(0.0, self.store.shapley.get(operator, 0.0))
        gain = base_gain * self._state_factor(operator, state)
        if cost > state.budget:
            return ValueEstimate(operator, "MARGINAL", 0.0, cost, -cost, ("budget:insufficient",))
        return ValueEstimate(operator, "MARGINAL", gain, cost, gain - cost, ("tensor:FINITE_EXACT", f"shapley:{self.store.shapley.get(operator, 0.0):.6f}", f"state_factor:{self._state_factor(operator, state):.3f}"))

    def value_of_computation(self, operator: str, state: OperatorState) -> ValueEstimate:
        m = self.marginal_value(operator, state)
        gain = m.expected_gain * (0.85 if operator in self.COMPUTE else 0.55)
        return ValueEstimate(operator, "VOC", gain, m.expected_cost, gain - m.expected_cost, m.evidence_basis + ("kind:computation",))

    def evsi(self, operator: str, state: OperatorState) -> ValueEstimate:
        m = self.marginal_value(operator, state)
        if operator not in self.INFO:
            return ValueEstimate(operator, "EVSI", 0.0, m.expected_cost, -m.expected_cost, m.evidence_basis + ("kind:not-information-operator",))
        decision_relevance = 1.0 if state.unresolved else 0.2
        discriminator_bonus = 1.2 if state.discriminators else 1.0
        gain = m.expected_gain * 0.7 * decision_relevance * discriminator_bonus
        return ValueEstimate(operator, "EVSI", gain, m.expected_cost, gain - m.expected_cost, m.evidence_basis + ("kind:decision-sensitive-information",))
