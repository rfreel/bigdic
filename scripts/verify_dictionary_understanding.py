#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, re, collections
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/"data/dictionary-v2.md"
out=ROOT/"results/understanding"
raw=source.read_bytes(); text=raw.decode()
EXPECTED="1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f"
assert hashlib.sha256(raw).hexdigest()==EXPECTED
assert len(text.splitlines())==19192
lexical=text.split("## Lexical dictionary",1)[1].split("## Evidence boundary and remaining work",1)[0]
lexemes=re.findall(r"^### (.+)$",lexical,re.M)
signatures=re.findall(r"^#### (SIG-[^\n]+)$",lexical,re.M)
operators=re.findall(r"^Operator: `([^`]+)`\.",lexical,re.M)
axes=re.findall(r"^Axis: `([^`]+)`\.",lexical,re.M)
origins=re.findall(r"^Origin: ([A-Z_]+)\.",lexical,re.M)
macros=re.findall(r"^Macro expression: `([^`]+)`\.",lexical,re.M)
counts=collections.Counter()
current=None
for line in lexical.splitlines():
    if line.startswith("### "): current=line[4:]
    elif line.startswith("#### SIG-") and current: counts[current]+=1
assert len(lexemes)==794
assert len(signatures)==1000 and len(set(signatures))==1000
assert len(set(operators))==18
assert len(set(axes))==31
assert sum(v>1 for v in counts.values())==121
assert origins.count("SOURCE_MAPPED_CANDIDATE")==934
assert origins.count("AUTHORED_MIGRATION_PROPOSAL")==66
assert len(macros)==20
summary=json.loads((out/"summary.json").read_text())
for key,value in {"lexemes":794,"signatures":1000,"operators":18,"axes":31,"multi_signature_lexemes":121,"source_mapped_signatures":934,"authored_migration_proposals":66,"explicit_macro_signatures":20}.items(): assert summary[key]==value,(key,summary[key])
receipt=json.loads((out/"receipt.json").read_text()); assert receipt["all_checks_pass"] is True
print("PASS source=19192 lexemes=794 signatures=1000 operators=18 axes=31 polysemy=121 provenance=934+66 macros=20")
