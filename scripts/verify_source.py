"""Reconcile every catalog V2 record with its pinned source and benchmark row."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'data/dictionary-v2.md').read_text(encoding='utf-8').splitlines()
benchmark = (ROOT / 'data/dictionary_benchmark.html').read_text(encoding='utf-8')
match = re.search(r'const rows=(\[.*?\]); const summary=', benchmark, re.S)
if not match:
    raise ValueError('Pinned benchmark rows not found')
rows = json.loads(match.group(1))
entries = [e for e in json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))['entries'] if e['origin'] == 'V2']
if len(rows) != len(entries) or len(rows) != 794:
    raise ValueError('V2 inventory differs from pinned benchmark')
by_name = {r['canonical_term']: r for r in rows}
if len(by_name) != len(rows):
    raise ValueError('Duplicate benchmark term')
signature_total = 0
for e in entries:
    r = by_name[e['name']]
    start, end = e['source_lines']
    block = '\n'.join(source[start - 1:end])
    signatures = len(re.findall(r'^#### SIG-', block, re.M))
    fields = {'id': 'lexeme_id', 'kind': 'benchmark_class', 'roles': 'roles',
              'axes': 'axes', 'requires_context_binding': 'requires_context_binding',
              'requires_authority_or_effect_check': 'requires_authority_or_effect_check',
              'evidence_bound': 'requires_evidence_status_check',
              'flags': 'review_flags', 'neighbor': 'nearest_neighbor',
              'neighbor_similarity': 'nearest_similarity'}
    if (source[start - 1].strip() != '### ' + e['name']
            or f'ID: `{e["id"]}`' not in block
            or signatures != r['signature_count'] or e['signatures'] != signatures
            or e['ops'] != (r['operators'].split('|') if r['operators'] else [])
            or any(e[k] != r[v] for k, v in fields.items())
            or any(f'Operator: `{op}`' not in block for op in e['ops'])
            or any(d not in block for d in e['descriptions'] if not d.startswith('No single transition'))):
        raise ValueError('Source mismatch: ' + e['name'])
    signature_total += signatures
if signature_total != 1000:
    raise ValueError(f'Expected 1,000 contextual signatures, found {signature_total}')
print(f'Reconciled {len(entries)} V2 entries and {signature_total} signature references with pinned source and benchmark')
