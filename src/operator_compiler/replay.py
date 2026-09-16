from __future__ import annotations
from dataclasses import dataclass
from .measurements import MeasurementStore

@dataclass(frozen=True)
class CounterfactualDelta:
    kind: str
    variant: tuple[str, ...]
    delta: float

@dataclass(frozen=True)
class ReplayResult:
    baseline: float
    deletions: tuple[CounterfactualDelta, ...]
    reorderings: tuple[CounterfactualDelta, ...]


def counterfactual_replay(sequence: tuple[str, ...], store: MeasurementStore) -> ReplayResult:
    base=store.sequence_value(sequence)
    deletions=[]
    for i in range(len(sequence)):
        v=sequence[:i]+sequence[i+1:]
        deletions.append(CounterfactualDelta("delete",v,base-store.sequence_value(v)))
    reorder=[]
    for i in range(len(sequence)-1):
        v=list(sequence); v[i],v[i+1]=v[i+1],v[i]
        vt=tuple(v)
        reorder.append(CounterfactualDelta("swap",vt,base-store.sequence_value(vt)))
    return ReplayResult(base,tuple(deletions),tuple(reorder))
