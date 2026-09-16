from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv
from collections import defaultdict

@dataclass(frozen=True)
class TransferResult:
    by_regime: dict[str, dict[str,float]]
    transfer_ratio: float
    sign_reversal_rate: float


def evaluate_transfer(path: str | Path) -> TransferResult:
    vals=defaultdict(lambda:defaultdict(list))
    with Path(path).open(newline="",encoding="utf-8") as f:
        for r in csv.DictReader(f): vals[r["regime"]][r["split"]].append(float(r["ate"]))
    by={reg:{split:sum(xs)/len(xs) for split,xs in splits.items()} for reg,splits in vals.items()}
    ratios=[]; reversals=0; comparable=0
    for reg,d in by.items():
        if "train" in d and "heldout" in d:
            tr,ho=d["train"],d["heldout"]
            if abs(tr)>1e-12: ratios.append(abs(ho/tr))
            if abs(tr)>1e-12 and abs(ho)>1e-12:
                comparable+=1; reversals += (tr*ho<0)
    return TransferResult(by, sum(ratios)/len(ratios) if ratios else 0.0, reversals/comparable if comparable else 0.0)
