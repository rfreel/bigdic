from __future__ import annotations
from dataclasses import dataclass
from .contracts import OPERATORS
from .state import OperatorState
from .value import ValueEstimator

@dataclass(frozen=True)
class BudgetChoice:
    operator: str
    expected_value: float
    expected_cost: float
    value_per_cost: float

class BudgetAllocator:
    def __init__(self, estimator: ValueEstimator):
        self.estimator = estimator

    def frontier(self, state: OperatorState) -> tuple[BudgetChoice, ...]:
        rows=[]
        for op in OPERATORS:
            v=self.estimator.marginal_value(op,state)
            if v.expected_cost <= state.budget and v.net_value > 0:
                ratio = v.net_value / v.expected_cost if v.expected_cost > 0 else float('inf')
                rows.append(BudgetChoice(op,v.net_value,v.expected_cost,ratio))
        return tuple(sorted(rows,key=lambda x:(x.value_per_cost,x.expected_value,x.operator),reverse=True))

    def choose(self, state: OperatorState) -> BudgetChoice | None:
        f=self.frontier(state)
        return f[0] if f else None
