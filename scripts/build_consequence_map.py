"""Build the parametric consequence map without consulting Dictionary V2."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/consequence_lanes.json').read_text(encoding='utf-8'))
frontiers = data['frontiers']
domains = data['domains']
assert data['status'] == 'PARAMETRIC_WORKING_MODEL'
assert len(frontiers) == 12 and len(domains) == 6
assert len({f['name'] for f in frontiers}) == 12
assert all(len(f['lanes']) == 3 and all(len(l['terms']) == 5 for l in f['lanes']) for f in frontiers)
assert all(len(d['terms']) == 12 for d in domains)
assert all(len(set(l['terms'])) == 5 for f in frontiers for l in f['lanes'])
all_terms = {t for f in frontiers for l in f['lanes'] for t in l['terms']} | {t for d in domains for t in d['terms']}
assert set(data['term_types']) <= all_terms
additions = data['parametric_additions']
assert len(additions) == 12 and len({a['frontier'] for a in additions}) == 12
assert {a['frontier'] for a in additions} == {f['name'] for f in frontiers}
assert all(a['term'] not in all_terms and all(a[k].strip() for k in ('change','bind','failure')) for a in additions)

role_need = {
    'test_or_stop_rule': 'Claim, risky prediction, failure condition, and who can stop.',
    'discriminator': 'Two live rivals and an observation on which they disagree.',
    'repeatability_contract': 'Target, method, scope, and a replayable record.',
    'partition_rule': 'The live classes, equivalence criterion, and lost distinctions.',
    'rival_witness': 'A rival that fits current evidence and changes a possible action.',
    'pruning_rule': 'Proof that removed variants cannot change the required result.',
    'decision_standard': 'Governing criterion, evidence, decision owner, and authority.',
    'reversal_condition': 'Observation or event that would change the choice.',
    'option_guard': 'Irreversible step, option value, deadline, and trigger.',
    'task_contract': 'Object, scope, invariants, and checked acceptance property.',
    'interpretation_guard': 'Material readings, excluded readings, and the basis for exclusion.',
    'comparison_basis': 'Question, unit, success predicate, and comparison scope.',
    'representation_change': 'Old and new forms plus a mapping of protected distinctions.',
    'checkable_witness': 'The object, exact property, witness format, and checker.',
    'fidelity_guard': 'Which distinctions must survive the transformation.',
    'derivation_test': 'Premises, rule, consequence, and a possible defeating result.',
    'proof_trace': 'Each step, dependency, scope, and unresolved gap.',
    'causal_guard': 'Identification assumptions and a test that could fail them.',
    'evidence_update': 'Prior state, observation model, provenance, and update rule.',
    'provenance_contract': 'Raw observation, transformation, source, and custody.',
    'evidence_failure': 'Which apparent support fails and which claims depend on it.',
    'authority_guard': 'Actor, target, action, grant, scope, and override rule.',
    'resource_guard': 'Budget or invariant, accounting unit, and breach response.',
    'trip_condition': 'Signal, threshold, observer, and stop or recovery action.',
    'staged_action': 'Trial state, acceptance check, promotion, and side effects.',
    'recovery_action': 'What can be undone, how, and which effects remain.',
    'effect_guard': 'Precondition, effect surface, limit, and owner of a breach.',
    'state_invariant': 'Old state, new state, protected invariant, and conflict handling.',
    'repair_rule': 'Observed failure, cause, smallest repair, and regression check.',
    'invalidation_rule': 'Changed basis and exact dependent claims to reopen.',
    'verification_contract': 'Claim, target revision, checker, property, and pass condition.',
    'verification_witness': 'Raw check result, method, scope, and independent replay path.',
    'verification_limit': 'What passed, what remains open, and when the result expires.',
    'closure_predicate': 'Accepted result, checker, residue, and accountable owner.',
    'reopen_rule': 'Specific later observation that reopens the disposition.',
    'closure_failure': 'Missing witness, live rival, or residue that blocks completion.',
}
assert {l['role'] for f in frontiers for l in f['lanes']} == set(role_need)
esc = html.escape


def terms(names, default_type):
    return ''.join(f'<span class="term" data-term="{esc(name)}"><strong>{esc(name)}</strong>'
                   f'<small>{esc(data["term_types"].get(name, default_type).replace("_", " "))}</small></span>'
                   for name in names)


nav = ''.join(f'<a href="#f-{i}">{esc(f["name"])}</a>' for i, f in enumerate(frontiers, 1))
sections = []
for i, frontier in enumerate(frontiers, 1):
    lanes = ''.join(
        f'<article class="lane"><div class="lane-head"><h3>{esc(lane["name"])}</h3>'
        f'<span>{esc(lane["role"].replace("_", " "))}</span></div>'
        f'<p class="need">Bind: {esc(role_need[lane["role"]])}</p>'
        f'<div class="terms">{terms(lane["terms"], lane["role"])}</div></article>'
        for lane in frontier['lanes']
    )
    sections.append(
        f'<section class="frontier" id="f-{i}"><header><span class="index">{i:02}</span>'
        f'<div><h2>{esc(frontier["name"])}</h2><p>{esc(frontier["change"])}</p></div></header>'
        f'<p class="anchors">Existing handles: {esc(", ".join(frontier["anchors"]))}</p>'
        f'<div class="lanes">{lanes}</div></section>'
    )
domain_sections = ''.join(
    f'<section class="domain"><h3>{esc(d["name"])}</h3><div class="terms">{terms(d["terms"], "domain_concept")}</div></section>'
    for d in domains
)
addition_sections = ''.join(
    f'<article class="lane"><h3>{esc(a["frontier"])}</h3>{terms([a["term"]], "parametric_extension")}'
    f'<p><strong>Change:</strong> {esc(a["change"])}</p>'
    f'<p><strong>Bind:</strong> {esc(a["bind"])}</p>'
    f'<p><strong>Failure:</strong> {esc(a["failure"])}</p></article>'
    for a in additions
)
counts = {'frontiers': len(frontiers), 'lanes': sum(len(f['lanes']) for f in frontiers),
          'frontier_positions': sum(len(l['terms']) for f in frontiers for l in f['lanes']),
          'domain_positions': sum(len(d['terms']) for d in domains),
          'parametric_additions': len(additions)}
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Words by consequence | BigDic</title>
<style>
:root{color-scheme:light;--ink:#172931;--muted:#52636a;--line:#c7d1d2;--paper:#f5f6f3;--accent:#125869}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 system-ui,-apple-system,sans-serif}a{color:var(--accent)}.top{background:#182e37;color:white;padding:28px max(16px,calc((100vw - 1200px)/2))}.top h1{font-size:clamp(2rem,6vw,3.7rem);line-height:1.08;margin:0}.top p{max-width:80ch}.top a{color:#d3eeee}main{max-width:1200px;padding:20px 16px 80px;margin:auto}p{max-width:88ch}.intro{border:1px solid var(--line);background:white;padding:18px 22px}.intro strong{display:block}.search{display:block;width:100%;padding:12px;margin:22px 0;font:inherit;border:1px solid #81959b;min-height:48px}nav{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0}nav a{background:white;border:1px solid var(--line);padding:7px 10px;text-decoration:none}.frontier{border-top:2px solid var(--ink);padding-top:17px;margin:34px 0 50px}.frontier>header{display:flex;gap:15px;align-items:baseline}.frontier h2{font-size:1.75rem;margin:0}.frontier header p{margin:3px 0}.index{font:700 1rem ui-monospace,monospace;color:var(--accent)}.anchors{font-size:.89rem;color:var(--muted)}.lanes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.addition-grid,.domain-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.lane,.domain{border:1px solid var(--line);background:#fff;padding:14px 16px}.lane-head{display:flex;flex-wrap:wrap;gap:5px;align-items:baseline;justify-content:space-between}.lane h3,.domain h3{font-size:1.08rem;margin:0}.lane-head span{font-size:.77rem;color:var(--muted)}.need{font-size:.88rem;color:#41565d;margin:9px 0 13px}.terms{display:flex;flex-wrap:wrap;gap:7px}.term{display:inline-flex;flex-direction:column;gap:2px;border:1px solid #aabfc1;background:#edf3f2;padding:7px 9px;font:.82rem/1.3 ui-monospace,monospace;overflow-wrap:anywhere}.term small{font:400 .71rem/1.2 system-ui,sans-serif;color:var(--muted)}.domain h3{margin:0 0 12px}.note{border-left:4px solid var(--accent);padding:12px 16px;background:white;margin:22px 0}.hidden,[hidden]{display:none!important}@media(max-width:850px){.lanes{grid-template-columns:1fr}.addition-grid,.domain-grid{grid-template-columns:1fr}.top{padding:24px 16px}}@media print{.search,nav{display:none}.frontier{break-inside:avoid}}
</style></head><body><div class="top"><h1>Words by consequence</h1><p>__COUNT__ proposed frontier positions and __DOMAIN_COUNT__ domain positions. A term earns a place here by the change it could make in a bound task. Placement is a design hypothesis, not a claim of execution, authority, or measured effect.</p><a href="consequence-system.md">Rules, counterexamples, and scope</a></div><main>
<div class="intro"><strong>Read the governing change first.</strong><p>The lanes separate interventions, decision rules, constraints, witnesses, and failure labels. The “Bind” line names information needed before a term can do that job. These labels may share spelling or appear in multiple domains; that does not make the corresponding methods equivalent.</p><p>Conditional dominance requires the same task, admissible moves, protected requirements, and a comparison of effects and costs. The word list alone establishes none of those.</p></div><input id="search" class="search" type="search" aria-label="Find a term" placeholder="Find a term, role, or frontier"><p id="match-count" aria-live="polite"></p><nav aria-label="Frontiers">__NAV__<a href="#additions">12 further cuts</a></nav><div id="frontiers">__FRONTIERS__</div>
<section id="additions" class="frontier"><header><span class="index">+</span><div><h2>12 further cuts</h2><p>Parametric additions. Each identifies a possible state change and a failure to guard.</p></div></header><div class="addition-grid">__ADDITIONS__</div></section>
<section class="frontier"><header><span class="index">13</span><div><h2>Professional vocabularies</h2><p>Domain-specific concepts. Their technical assumptions remain attached.</p></div></header><p class="anchors">A doctrine, measure, diagnosis, or control name is not a generic command.</p><div class="domain-grid">__DOMAINS__</div></section>
<div class="note"><strong>One useful composition:</strong> request → live hypotheses → candidate common action and probe-value check → act or discriminate → observed result → scoped disposition or unresolved branch → reopen predicate. A common action does not by itself make probing wasteful. <a href="consequence-system.md">See the admission rules.</a></div></main><script>
const query=document.getElementById('search'),counter=document.getElementById('match-count');
function filter(){const term=query.value.trim().toLocaleLowerCase();let count=0;for(const section of document.querySelectorAll('.frontier')){let visible=0;for(const card of section.querySelectorAll('.lane,.domain')){const metadata=(card.querySelector('h3')?.textContent||'')+' '+(card.querySelector('.lane-head span')?.textContent||'')+' '+(section.querySelector('h2')?.textContent||'');let hits=0;for(const chip of card.querySelectorAll('[data-term]')){const hit=!term||chip.dataset.term.toLocaleLowerCase().includes(term)||metadata.toLocaleLowerCase().includes(term);chip.hidden=!hit;if(hit)hits++}card.hidden=hits===0;visible+=hits}section.hidden=visible===0;count+=visible}counter.textContent=count+' positions shown'}query.addEventListener('input',filter);filter();
</script></body></html>'''
page = (page.replace('__COUNT__', str(counts['frontier_positions']))
        .replace('__DOMAIN_COUNT__', str(counts['domain_positions']))
        .replace('__NAV__', nav).replace('__FRONTIERS__', ''.join(sections))
        .replace('__DOMAINS__', domain_sections).replace('__ADDITIONS__', addition_sections))
(ROOT / 'docs/consequence-map.html').write_text(page, encoding='utf-8')
print(json.dumps(counts, sort_keys=True))
