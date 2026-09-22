"""A small, inspectable operator index and candidate router.

Routing proposes macro candidates. It does not execute actions, grant authority,
verify a claim, or promote a capability. No third-party packages are required.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / 'data' / 'catalog.json'
CONSEQUENCE_MAP = ROOT / 'data' / 'consequence_lanes.json'

MACROS = {
    'UNDERSTAND': ('parse', 'bind objective', 'preserve material interpretations'),
    'REIFY': ('identify roles', 'expose distinctions', 'map relations'),
    'RIVALIZE': ('expose default', 'generate rival outputs', 'find discriminator'),
    'PREWALK': ('simulate sequence', 'trace effects', 'reorder prerequisites'),
    'RESEARCH': ('find sources', 'inspect', 'reconcile evidence'),
    'DIAGNOSE': ('reproduce', 'trace', 'probe candidate causes'),
    'DESIGN': ('compile requirements', 'generate structures', 'compare'),
    'BUILD': ('inspect environment', 'implement', 'run', 'check artifact'),
    'REPAIR': ('reproduce', 'isolate cause', 'fix', 'retest'),
    'COMPARE': ('bind criteria', 'align options', 'preserve tradeoffs'),
    'PLAN': ('decompose', 'map prerequisites', 'prewalk'),
    'VERIFY': ('bind target property', 'choose checker', 'inspect result'),
    'OPTIMIZE': ('bind objective', 'find bottleneck', 'intervene', 'measure'),
    'RELEASE': ('check acceptance', 'package', 'observe delivery'),
}
# Retrieval cues are a modest, reviewable first pass, not claims of semantic parsing.
CUES = {
    'REPAIR': (r'\b(fix|repair|broken|regression|bug|fails?|crash)\b',),
    'RESEARCH': (r'\b(research|study|find sources|look up|investigate)\b',),
    'REIFY': (r'\b(reify|distinctions|relations|properties|ontology)\b',),
    'RIVALIZE': (r'\b(rivals?|alternatives|silent defaults?|competing interpretations)\b',),
    'PREWALK': (r'\b(prewalk|premortem|before executing|walk through the plan)\b',),
    'COMPARE': (r'\b(compare|versus|tradeoffs?|difference between)\b',),
    'VERIFY': (r'\b(verify|validate|prove|check the result)\b',),
    'OPTIMIZE': (r'\b(optimi[sz]e|performance|reduce cost|bottleneck)\b',),
    'DESIGN': (r'\b(design|architect|specify a system)\b',),
    'BUILD': (r'\b(build|create|implement|write a document|make a file)\b',),
    'PLAN': (r'\b(plan|roadmap|todo|sequence the work)\b',),
    'RELEASE': (r'\b(release|publish|deploy|deliver)\b',),
    'DIAGNOSE': (r'\b(diagnose|why did|root cause)\b',),
}

def catalog(path: Path = CATALOG) -> dict:
    data = json.loads(path.read_text(encoding='utf-8'))
    source = ROOT / 'data' / data['source_file']
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != data['source_sha256']:
        raise ValueError('V2 source digest differs from the catalog basis')
    entries = data['entries']
    names = [e['name'] for e in entries]
    if len(entries) != 803 or len(set(names)) != 803:
        raise ValueError('Catalog record count or unique identity changed; regenerate and review')
    for e in entries:
        if e['score'] != calculate_score(e):
            raise ValueError('Proxy mismatch: ' + e['name'])
        if e['origin'] not in ('V2','LOCAL'):
            raise ValueError('Unrecognized provenance: ' + e['name'])
    return data

def calculate_score(e: dict) -> int:
    return max(0, min(100, 4*sum(e[k] for k in ('D','T','C','E'))
        + e['macro'] + e['sense'] - e['ambiguity'] - e['context']
        - e['authority'] - e['pseudo']))

def candidates(request: str) -> list[dict]:
    """Return candidate macro routes with visible evidence; never claim execution."""
    result=[]
    for macro, patterns in CUES.items():
        hits=[p for p in patterns if re.search(p, request, re.I)]
        if hits:
            result.append({'macro':macro,'cue':hits,'steps':list(MACROS[macro]),'status':'PROPOSED'})
    return result

def packet(request: str) -> dict:
    hits=candidates(request)
    return {'request':request,'request_sha256':hashlib.sha256(request.encode()).hexdigest(),
        'routing':'CANDIDATE_ONLY','macro_candidates':hits,
        'next_action':'Bind task context and execute the smallest adequate route' if hits else
                      'Interpret the desired outcome directly; no lexical route selected',
        'receipt':None,'verified':False,'authority_granted':False,
        'note':'A cue never grants permission or proves a task was completed.'}

def consequence_lookup(term: str) -> list[dict]:
    """Find proposed consequence roles without claiming V2 membership or execution."""
    data=json.loads(CONSEQUENCE_MAP.read_text(encoding='utf-8'))
    kinds=data['term_types']
    matches=[]
    for frontier in data['frontiers']:
        for lane in frontier['lanes']:
            for word in lane['terms']:
                if word.casefold()==term.casefold():
                    matches.append({'term':word,'frontier':frontier['name'],'change':frontier['change'],
                                    'lane':lane['name'],'role':lane['role'],
                                    'term_type':kinds.get(word,lane['role']),'status':data['status']})
    for domain in data['domains']:
        for word in domain['terms']:
            if word.casefold()==term.casefold():
                matches.append({'term':word,'domain':domain['name'],'term_type':kinds.get(word,'domain_concept'),'status':data['status'],
                                'note':'Domain vocabulary; its technical assumptions still apply'})
    return matches

def main(argv=None):
    p=argparse.ArgumentParser(description='Inspect the dictionary or emit a proposed route')
    sub=p.add_subparsers(dest='command',required=True)
    q=sub.add_parser('lookup');q.add_argument('term')
    q=sub.add_parser('list');q.add_argument('--frontier');q.add_argument('--level');q.add_argument('--limit',type=int,default=30);q.add_argument('--sort',choices=('name','proxy'),default='name')
    q=sub.add_parser('packet');q.add_argument('request')
    q=sub.add_parser('check')
    q=sub.add_parser('consequences');q.add_argument('--frontier')
    a=p.parse_args(argv)
    if a.command=='packet': result=packet(a.request)
    elif a.command=='consequences':
        d=json.loads(CONSEQUENCE_MAP.read_text(encoding='utf-8'))
        result={'status':d['status'],'frontiers':[f for f in d['frontiers'] if not a.frontier or f['name'].casefold()==a.frontier.casefold()],
                'domains':d['domains'] if not a.frontier else []}
    else:
        c=catalog()
        if a.command=='check': result={'records':len(c['entries']),'source_sha256':c['source_sha256'],'status':c['status'],'valid':True}
        elif a.command=='lookup':
            found=[x for x in c['entries'] if x['name'].casefold()==a.term.casefold()]
            proposed=consequence_lookup(a.term)
            result={'term':a.term,'source_entries':found,'consequence_roles':proposed,'found':bool(found or proposed)}
        else:
            xs=[x for x in c['entries'] if (not a.frontier or x['frontier']==a.frontier)
                and (not a.level or x['level']==int(a.level))]
            order=(lambda x:x['name']) if a.sort=='name' else (lambda x:x['rank'])
            result={'total':len(xs),'sort':a.sort,'proxy_note':'Family-weighted browsing prior; no measured consequence or effect',
                'entries':[{'name':x['name'],'score':x['score'],'rank':x['rank'],
                'frontier':x['frontier'],'level':x['level']} for x in sorted(xs,key=order)[:max(0,a.limit)]]}
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
