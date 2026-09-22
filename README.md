# BigDic

BigDic contains three connected tools built from one pinned Dictionary V2 source: a browser dictionary, a finite operator compiler, and a linked operator map. Use an ordinary request to direct an agent. Dictionary words are optional handles, not proof that an action happened.

| Need | Start here | What it does |
| --- | --- | --- |
| Find senses and compose an instruction draft | [Browser toolkit](dist/bigdic.html) or `node cli.mjs search VERIFY` | Searches 794 lexemes and 1,000 signatures, compares senses, and exports drafts. It does not execute them. |
| Inspect a conditional controller and measured experiment lanes | [Compiler](docs/BIGGESTDIC.md) | Plans over 18 operator families with applicability and budget checks. Its finite measurements and small local-model smoke have declared scopes. |
| Browse the full ranked word map | [Operator towers](docs/operator-towers.html) | Places 794 source records and nine marked local extensions on linked levels and frontiers. Its score is a declared browsing proxy, not observed gain per word. |

The canonical source is [`data/dictionary-v2.md`](data/dictionary-v2.md), SHA-256 `1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f`. The tower generator also pins the source benchmark table in `data/dictionary_benchmark.html`.

## Run the checks

```sh
npm test
npm run build
PYTHONPATH=src python3 -m pytest -q
python3 operator_system.py check
python3 -m unittest discover -s tests -p 'test_benchmark.py' -v
python3 -m unittest discover -s tests -p 'test_operator_system.py' -v
python3 scripts/verify_source.py
python3 scripts/audit_100.py
python3 scripts/build_map.py
```

The compiler suite requires `pytest`; the toolkit and tower scripts have no package dependencies beyond Node and Python. CI checks the parts separately. The [100-check record](docs/review-100.md) reports structural probes, and `verify_source.py` reconciles all 794 V2 records and 1,000 signatures. Neither check establishes task-level performance or browser layout quality.

## Agent entry point

Read [AGENTS.md](AGENTS.md) for the working contract. The [architecture](docs/system.md) distinguishes source words, typed programs, executed actions, verified results, and durable capability. [Benchmarks](docs/benchmarks.md) defines comparisons and targets; [TODO](TODO.md) tracks work that has not been completed. The CLI's `packet` command retrieves possible moves from words in a request. It does not execute, grant authority, or verify anything.
