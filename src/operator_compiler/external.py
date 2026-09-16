from __future__ import annotations
from dataclasses import dataclass
from .measurements import MeasurementStore

@dataclass(frozen=True)
class ExternalEvidenceState:
    status: str
    provider: str | None
    model: str | None
    trials_executed: int
    error: str | None


def external_evidence_state(store: MeasurementStore) -> ExternalEvidenceState:
    r=store.external_receipt
    return ExternalEvidenceState(
        status=r.get('status','UNKNOWN'),
        provider=r.get('provider'),
        model=r.get('model'),
        trials_executed=int(r.get('model_trials_executed',0)),
        error=r.get('error'),
    )
