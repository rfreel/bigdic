#!/usr/bin/env python3
from pathlib import Path
import csv, json, hashlib, re
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/"data/dictionary-v2.md"
out=ROOT/"results/understanding"
raw=source.read_bytes()
text=raw.decode()
assert hashlib.sha256(raw).hexdigest()=="1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f"
assert len(text.splitlines())==19192
lexical=text.split("## Lexical dictionary",1)[1].split("## Evidence boundary and remaining work",1)[0]
lexemes=re.findall(r"^### (.+)$",lexical,re.M)
signatures=re.findall(r"^#### (SIG-[^\n]+)$",lexical,re.M)
operators=re.findall(r"^Operator: `([^`]+)`\.",lexical,re.M)
assert len(lexemes)==794, len(lexemes)
assert len(signatures)==1000, len(signatures)
assert len(set(signatures))==1000
assert len(set(operators))==18
summary=json.loads((out/"summary.json").read_text())
assert summary["lexemes"]==794 and summary["signatures"]==1000 and summary["operators"]==18
with (out/"operator_atlas.csv").open(newline="") as f: assert len(list(csv.DictReader(f)))==18
with (out/"axis_atlas.csv").open(newline="") as f: assert len(list(csv.DictReader(f)))==31
with (out/"polysemy_atlas.csv").open(newline="") as f: assert len(list(csv.DictReader(f)))==121
with (out/"ambiguity_frontier.csv").open(newline="") as f: assert len(list(csv.DictReader(f)))==486
top=json.loads((out/"semantic_topology.json").read_text())
assert len(top["lexemes"])==794 and len(top["signatures"])==1000
receipt=json.loads((out/"receipt.json").read_text())
assert receipt["all_checks_pass"] is True
print("PASS source=19192 lines lexemes=794 signatures=1000 operators=18 axes=31 polysemy=121 frontier=486")
