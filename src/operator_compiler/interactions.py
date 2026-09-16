from __future__ import annotations
from .measurements import MeasurementStore
from .state import OperatorState

class InteractionModel:
    def __init__(self, store: MeasurementStore):
        self.store = store

    def synergy(self, a: str, b: str, state: OperatorState) -> float:
        base = float(self.store.pair(a, b)["synergy"])
        if state.history and state.history[-1] == a:
            base += 0.05 * self.store.macro_edges.get((a, b), 0)
        if state.solved:
            base *= 0.1
        return base

    def order_effect(self, a: str, b: str, state: OperatorState) -> float:
        base = float(self.store.pair(a, b)["order_effect"])
        if state.required_operators:
            try:
                ia, ib = state.required_operators.index(a), state.required_operators.index(b)
                if ia < ib:
                    base += 0.25
                elif ib < ia:
                    base -= 0.25
            except ValueError:
                pass
        return base
