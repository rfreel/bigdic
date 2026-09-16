from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv
from collections import Counter, defaultdict

@dataclass(frozen=True)
class Motif:
    sequence: tuple[str, ...]
    support: int

@dataclass(frozen=True)
class InducedMacro:
    macro_id: str
    sequence: tuple[str, ...]
    measured_value: float
    min_deletion_value: float


def _split_chain(text: str) -> tuple[str, ...]:
    return tuple(x.strip() for x in text.split("->") if x.strip())


def mine_motifs(chain_csv: str | Path, min_length=2, max_length=3) -> list[Motif]:
    counts = Counter()
    with Path(chain_csv).open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            seq = _split_chain(row["required"])
            for n in range(min_length, max_length + 1):
                for i in range(len(seq) - n + 1):
                    counts[seq[i:i+n]] += 1
    return [Motif(k, v) for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]


def induce_macros(chain_csv: str | Path, deletion_csv: str | Path) -> list[InducedMacro]:
    mdv = defaultdict(list)
    with Path(deletion_csv).open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mdv[row["macro_id"]].append(float(row["mdv"]))
    out = []
    with Path(chain_csv).open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            values = mdv.get(row["macro_id"], [])
            if values and min(values) > 0 and float(row["best_value"]) > 0:
                out.append(InducedMacro(row["macro_id"], _split_chain(row["best_chain"]), float(row["best_value"]), min(values)))
    return out
