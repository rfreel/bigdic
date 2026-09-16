from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv
import json
from collections import defaultdict

@dataclass
class MeasurementStore:
    tensor: list[dict]
    pairwise: dict[tuple[str, str], dict]
    shapley: dict[str, float]
    macro_edges: dict[tuple[str, str], int]
    external_receipt: dict

    @classmethod
    def from_directory(cls, path: str | Path) -> "MeasurementStore":
        p = Path(path)
        with (p / "operator_value_tensor.csv").open(newline="", encoding="utf-8") as f:
            tensor = list(csv.DictReader(f))
        with (p / "pairwise_interactions.csv").open(newline="", encoding="utf-8") as f:
            pairwise_rows = list(csv.DictReader(f))
        pairwise = {(r["a"], r["b"]): r for r in pairwise_rows}
        with (p / "shapley.csv").open(newline="", encoding="utf-8") as f:
            shapley = {r["operator"]: float(r["mc_shapley"]) for r in csv.DictReader(f)}
        edges_raw = json.loads((p / "macro_edges.json").read_text(encoding="utf-8"))
        macro_edges = {(r["from"], r["to"]): int(r["count"]) for r in edges_raw}
        receipt = json.loads((p / "external_model_receipt.json").read_text(encoding="utf-8"))
        return cls(tensor=tensor, pairwise=pairwise, shapley=shapley, macro_edges=macro_edges, external_receipt=receipt)

    def tensor_value(self, operator: str, regime: str = "POSITIVE", metric: str = "evo") -> float:
        vals = [float(r["value"]) for r in self.tensor if r["operator"] == operator and r["regime"] == regime and r["metric"] == metric]
        return sum(vals) / len(vals) if vals else 0.0

    def base_cost(self, operator: str) -> float:
        gross = self.tensor_value(operator, "POSITIVE", "gross_effect")
        evo = self.tensor_value(operator, "POSITIVE", "evo")
        return max(0.0, gross - evo) if gross or evo else 0.05

    def pair(self, a: str, b: str) -> dict:
        if (a, b) in self.pairwise:
            return self.pairwise[(a, b)]
        if (b, a) in self.pairwise:
            row = dict(self.pairwise[(b, a)])
            row["order_effect"] = str(-float(row["order_effect"]))
            return row
        return {"synergy": "0", "order_effect": "0", "macro_ab": "0", "macro_ba": "0"}

    def sequence_value(self, sequence: tuple[str, ...] | list[str]) -> float:
        seq = tuple(sequence)
        if not seq:
            return 0.0
        total = sum(max(0.0, self.shapley.get(op, self.tensor_value(op))) for op in seq)
        for a, b in zip(seq, seq[1:]):
            row = self.pair(a, b)
            total += float(row["synergy"])
            total += 0.02 * self.macro_edges.get((a, b), 0)
        return total
