from __future__ import annotations
from dataclasses import dataclass
from ..contracts import OPERATORS
from ..interactions import InteractionModel
from ..measurements import MeasurementStore
from ..state import OperatorState
from ..value import ApplicabilityModel, ValueEstimator

@dataclass(frozen=True)
class AlternativeStep:
    operator: str
    expected_value: float
    expected_cost: float
    applicability: str

@dataclass(frozen=True)
class NextStep:
    operator: str | None
    bindings: dict[str,str]
    expected_value: float
    expected_cost: float
    alternatives: tuple[AlternativeStep,...]
    discriminator: str | None
    stop_if: str
    evidence_basis: tuple[str,...]

class OperatorController:
    def __init__(self, store: MeasurementStore):
        self.store=store
        self.values=ValueEstimator(store)
        self.app=ApplicabilityModel()
        self.interactions=InteractionModel(store)

    def next(self,state:OperatorState)->NextStep:
        scored=[]
        for op in OPERATORS:
            a=self.app.assess(op,state)
            v=self.values.marginal_value(op,state)
            scored.append(AlternativeStep(op,v.net_value,v.expected_cost,a.status))
        scored.sort(key=lambda x:(x.applicability=="APPLICABLE",x.expected_value,-x.expected_cost,x.operator),reverse=True)
        applicable=[x for x in scored if x.applicability=="APPLICABLE" and x.expected_cost<=state.budget]
        chosen=applicable[0] if applicable else None
        if state.solved or (chosen and chosen.expected_value<=0):
            close=next((x for x in scored if x.operator=="CLOSE" and x.applicability=="APPLICABLE"),None)
            chosen=close
        op=chosen.operator if chosen else None
        evidence=("operator_value_tensor:FINITE_EXACT","pairwise_interactions:FINITE_EXACT",f"external_model:{self.store.external_receipt.get('status')}")
        return NextStep(
            operator=op,
            bindings={"target":state.target,"objective":state.objective,"representation":state.representation},
            expected_value=chosen.expected_value if chosen else 0.0,
            expected_cost=chosen.expected_cost if chosen else 0.0,
            alternatives=tuple(scored[:5]),
            discriminator=state.discriminators[0] if state.discriminators else None,
            stop_if="required result invariant across live alternatives or no positive admissible continuation value",
            evidence_basis=evidence,
        )
