from __future__ import annotations

import argparse
import csv
from pathlib import Path

FIELDS = [
    "lexeme_id", "canonical_term", "operators", "benchmark_class",
    "requires_context_binding", "requires_authority_or_effect_check",
    "requires_evidence_status_check", "branch_count", "signature_count", "review_flags",
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("source", help="lexeme_benchmark.csv from the exhaustive dictionary benchmark")
    p.add_argument("output", help="destination sweep manifest CSV")
    args = p.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with open(args.source, newline="", encoding="utf-8") as src, out.open("w", newline="", encoding="utf-8") as dst:
        reader = csv.DictReader(src)
        missing = [f for f in FIELDS if f not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"missing required fields: {missing}")
        writer = csv.DictWriter(dst, fieldnames=FIELDS)
        writer.writeheader()
        for row in reader:
            writer.writerow({k: row[k] for k in FIELDS})
            count += 1
    if count != 794:
        raise ValueError(f"expected 794 lexemes, got {count}")
    print(f"wrote {count} lexemes to {out}")


if __name__ == "__main__":
    main()
