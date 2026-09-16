from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json
import re

OPERATORS = (
    "COMPILE", "ACQUIRE", "INSPECT", "REPRESENT", "SPLIT", "EXPAND",
    "COMPARE", "INFER", "CHALLENGE", "TEST", "UPDATE", "EVALUATE",
    "SELECT", "TRANSFORM", "ACT", "VERIFY", "CONTROL", "CLOSE",
)

@dataclass(frozen=True)
class OperatorContract:
    operator: str
    preconditions: str
    transition: str
    postconditions: str
    admissibility: str
    evidence_obligations: str
    authority_requirements: str
    capability_requirements: str
    effect_profile: str
    failure_rules: str
    status_rule: str
    verification_rules: str
    closure_rules: str

    def to_dict(self):
        return asdict(self)

_FIELDS = {
    "Preconditions": "preconditions",
    "Transition": "transition",
    "Postconditions": "postconditions",
    "Admissibility": "admissibility",
    "Evidence obligations": "evidence_obligations",
    "Authority requirements": "authority_requirements",
    "Capability requirements": "capability_requirements",
    "Effect profile": "effect_profile",
    "Failure rules": "failure_rules",
    "Status rule": "status_rule",
    "Verification rules": "verification_rules",
    "Closure rules": "closure_rules",
}

def compile_contracts(path: str | Path) -> dict[str, OperatorContract]:
    path = Path(path)
    if path.suffix.lower() == ".json":
        seed = json.loads(path.read_text(encoding="utf-8"))
        common = seed.get("common", {})
        operators = seed.get("operators", {})
        missing = set(OPERATORS) - set(operators)
        if missing:
            raise ValueError(f"missing operators in normalized seed: {sorted(missing)}")
        result: dict[str, OperatorContract] = {}
        for op in OPERATORS:
            vals = dict(common)
            vals.update(operators[op])
            result[op] = OperatorContract(operator=op, **vals)
        return result

    text = path.read_text(encoding="utf-8")
    result: dict[str, OperatorContract] = {}
    for op in OPERATORS:
        m = re.search(rf"^### Contract {re.escape(op)}\s*$", text, re.M)
        if not m:
            raise ValueError(f"missing Contract {op}")
        end = re.search(r"^### Contract ", text[m.end():], re.M)
        block = text[m.end(): m.end() + end.start()] if end else text[m.end():]
        vals = {}
        for label, attr in _FIELDS.items():
            mm = re.search(rf"^{re.escape(label)}:\s*(.+)$", block, re.M)
            if not mm:
                raise ValueError(f"{op} missing {label}")
            vals[attr] = mm.group(1).strip()
        result[op] = OperatorContract(operator=op, **vals)
    return result

def write_contracts(dictionary_path: str | Path, output_path: str | Path) -> None:
    data = {k: v.to_dict() for k, v in compile_contracts(dictionary_path).items()}
    Path(output_path).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
