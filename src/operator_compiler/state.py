from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass(frozen=True)
class OperatorState:
    target: str
    objective: str
    live_alternatives: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    decision_partition: tuple[tuple[str, ...], ...] = ()
    requirements: tuple[str, ...] = ()
    discriminators: tuple[str, ...] = ()
    budget: float = 0.0
    authority: frozenset[str] = field(default_factory=frozenset)
    capabilities: frozenset[str] = field(default_factory=frozenset)
    history: tuple[str, ...] = ()
    representation: str = "native"
    closure_state: str = "OPEN"
    required_operators: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self):
        if self.budget < 0:
            raise ValueError("budget must be nonnegative")
        flattened = [x for group in self.decision_partition for x in group]
        if len(flattened) != len(set(flattened)):
            raise ValueError("decision partition contains duplicate alternatives")

    @property
    def unresolved(self) -> bool:
        return len(self.decision_partition) > 1 or len(self.live_alternatives) > 1

    @property
    def solved(self) -> bool:
        return self.closure_state in {"SOLVED", "ROBUST"}

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["authority"] = sorted(self.authority)
        d["capabilities"] = sorted(self.capabilities)
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "OperatorState":
        x = dict(d)
        tuple_fields = ["live_alternatives", "evidence", "requirements", "discriminators", "history", "required_operators", "metadata"]
        for key in tuple_fields:
            if key in x:
                x[key] = tuple(tuple(v) if isinstance(v, list) and key == "metadata" else v for v in x[key])
        if "decision_partition" in x:
            x["decision_partition"] = tuple(tuple(g) for g in x["decision_partition"])
        x["authority"] = frozenset(x.get("authority", ()))
        x["capabilities"] = frozenset(x.get("capabilities", ()))
        return cls(**x)
