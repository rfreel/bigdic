"""Run 100 named, independent assertions on the pinned index and its views.

This is a reproducible review sample, not 100 training iterations or evidence of
task-level improvement. Each result records the property checked and its scope.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))
entries = catalog['entries']
source_bytes = (ROOT / 'data/dictionary-v2.md').read_bytes()
source = source_bytes.decode('utf-8')
lines = source.splitlines()
html = (ROOT / 'docs/operator-towers.html').read_text(encoding='utf-8')
by_name = {e['name']: e for e in entries}
results = []


def check(label, predicate):
    try:
        assert predicate(), label
        results.append((label, 'PASS'))
    except (AssertionError, Exception) as error:
        results.append((label, f'FAIL: {error}'))


# Ten corpus and view invariants.
check('Source digest matches catalog', lambda: hashlib.sha256(source_bytes).hexdigest() == catalog['source_sha256'])
check('794 V2 records', lambda: sum(e['origin'] == 'V2' for e in entries) == 794)
check('Nine local records', lambda: sum(e['origin'] == 'LOCAL' for e in entries) == 9)
check('803 unique names', lambda: len(entries) == len(by_name) == 803)
check('803 unique record IDs', lambda: len({e['id'] for e in entries}) == 803)
check('1,000 V2 signatures', lambda: sum(e['signatures'] for e in entries if e['origin'] == 'V2') == 1000)
check('All ranks form one permutation', lambda: sorted(e['rank'] for e in entries) == list(range(1, 804)))
check('Every score is within 0–100', lambda: all(type(e['score']) is int and 0 <= e['score'] <= 100 for e in entries))
check('Generated page has 803 records', lambda: '803 linked words' in html and 'const data=[' in html)
check('Generated page has source hash', lambda: catalog['source_sha256'] in html)

# Sixty distributed lexical samples, checked against the actual source span.
v2 = sorted((e for e in entries if e['origin'] == 'V2'), key=lambda e: e['name'])
for i in range(60):
    e = v2[i * (len(v2) - 1) // 59]
    start, end = e['source_lines']
    block = '\n'.join(lines[start - 1:end])
    check(f'Source span {i + 1:02}: {e["name"]}', lambda e=e, start=start, end=end, block=block:
          1 <= start <= end <= len(lines)
          and lines[start - 1].strip() == '### ' + e['name']
          and f'ID: `{e["id"]}`' in block
          and len(re.findall(r'^#### SIG-', block, re.M)) == e['signatures']
          and all(f'Operator: `{op}`' in block for op in e['ops'])
          and all(desc in block for desc in e['descriptions'] if not desc.startswith('No single transition')))

# Twenty different score calculations, distributed across the ranking.
ranked = sorted(entries, key=lambda e: e['rank'])
for i in range(20):
    e = ranked[i * (len(ranked) - 1) // 19]
    check(f'Proxy recomputation {i + 1:02}: {e["name"]}', lambda e=e:
          e['score'] == max(0, min(100, 4 * sum(e[k] for k in ('D', 'T', 'C', 'E'))
                    + e['macro'] + e['sense'] - e['ambiguity'] - e['context']
                    - e['authority'] - e['pseudo'])))

# Ten link properties cover provenance, locality, and graph referential integrity.
check('No V2 claim on local records', lambda: all(e['source_lines'] is None and e['flags'] == 'NOT_IN_V2' for e in entries if e['origin'] == 'LOCAL'))
check('V2 spans present', lambda: all(e['source_lines'] is not None for e in v2))
check('No broken neighbor targets', lambda: all(not e['neighbor'] or e['neighbor'] in by_name for e in entries))
check('No broken macro targets', lambda: all(n in by_name for e in entries for n in e['macro_links']))
check('No self macro links', lambda: all(e['name'] not in e['macro_links'] for e in entries))
check('No duplicate macro links', lambda: all(len(set(e['macro_links'])) == len(e['macro_links']) for e in entries))
check('Incoming macro counts agree', lambda: all(e['macro_inbound'] == sum(e['name'] in x['macro_links'] for x in entries) for e in entries))
check('Same-placement targets agree', lambda: all(all(by_name[n]['frontier'] == e['frontier'] and by_name[n]['level'] == e['level'] for n in e['same_family']) for e in entries))
check('No self placement links', lambda: all(e['name'] not in e['same_family'] for e in entries))
check('Ties use inbound links then name', lambda: all((-ranked[i]['score'], -ranked[i]['macro_inbound'], ranked[i]['name']) <= (-ranked[i + 1]['score'], -ranked[i + 1]['macro_inbound'], ranked[i + 1]['name']) for i in range(len(ranked) - 1)))

assert len(results) == 100, len(results)
report = ROOT / 'docs/review-100.md'
report.write_text('# 100-check review record\n\n'
                  'These are 100 distinct source and projection checks on this revision. They are not 100 optimization cycles, behavioral trials, or a proof of task performance. The source samples cover 60 evenly spaced alphabetical entries; the 20 score samples cover evenly spaced ranks. Other checks cover whole collections. A passing sample does not certify every source span.\n\n'
                  '| # | Check | Result |\n| ---: | --- | --- |\n'
                  + ''.join(f'| {i:03} | {label} | {outcome} |\n' for i, (label, outcome) in enumerate(results, 1))
                  + '\nRun `python3 scripts/audit_100.py` from any directory. The source and generated index also require a byte-for-byte regeneration check before release.\n', encoding='utf-8')
print(f'{sum(outcome == "PASS" for _, outcome in results)}/100 checks passed; {report}')
if any(outcome != 'PASS' for _, outcome in results):
    raise SystemExit(1)
