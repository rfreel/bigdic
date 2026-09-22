from __future__ import annotations
from dataclasses import dataclass
from itertools import permutations
from ..state import OperatorState
from ..value import ValueEstimator
from ..interactions import InteractionModel
from ..value import ApplicabilityModel

@dataclass(frozen=True)
class PlanResult:
    sequence: tuple[str, ...]
    total_value: float
    total_cost: float
    planner: str
    feasible: bool = True

class PlannerBase:
    name = "base"
    def __init__(self, estimator: ValueEstimator, interactions: InteractionModel):
        self.estimator = estimator
        self.interactions = interactions
        self.applicability = ApplicabilityModel()

    def score_sequence(self, seq: tuple[str, ...], state: OperatorState) -> PlanResult:
        cost = sum(self.estimator.store.base_cost(op) for op in seq)
        value = sum(self.estimator.store.shapley.get(op, 0.0) for op in seq)
        for a,b in zip(seq, seq[1:]):
            value += self.interactions.synergy(a,b,state)
            value += self.interactions.order_effect(a,b,state)
            value += 0.02 * self.estimator.store.macro_edges.get((a,b),0)
        return PlanResult(seq, value - cost, cost, self.name)

    def feasible(self, seq, state):
        return (sum(self.estimator.store.base_cost(op) for op in seq) <= state.budget
                and all(self.applicability.assess(op, state).status == 'APPLICABLE' for op in seq))

    def infeasible(self) -> PlanResult:
        return PlanResult((), 0.0, 0.0, self.name, False)
