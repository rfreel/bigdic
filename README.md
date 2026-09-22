# BigDic

BigDic contains a parametric consequence map, a browser dictionary, a finite operator compiler, and a source-indexed tower. Use an ordinary request to direct an agent. Dictionary words are optional handles, not proof that an action happened.

| Need | Start here | What it does |
| --- | --- | --- |
| Find the move that could change the result | [Consequence map](docs/consequence-map.html) and [admission rules](docs/consequence-system.md) | Organizes 180 frontier positions and 72 domain positions by their possible state change and required bindings. It is a parametric working model. |
| Find senses and compose an instruction draft | [Browser toolkit](dist/bigdic.html) or `node cli.mjs search VERIFY` | Searches 794 lexemes and 1,000 signatures, compares senses, and exports drafts. It does not execute them. |
| Inspect a conditional controller and measured experiment lanes | [Compiler](docs/BIGGESTDIC.md) | Plans over 18 operator families with applicability and budget checks. Its finite measurements and small local-model smoke have declared scopes. |
| Inspect the historical source inventory | [Operator towers](docs/operator-towers.html) | Places 794 V2 records and nine local extensions on linked levels and frontiers. Its old score is a family-weighted browsing proxy; it does not rank consequences. |

The canonical source is [`data/dictionary-v2.md`](data/dictionary-v2.md), SHA-256 `1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f`. The tower generator also pins the source benchmark table in `data/dictionary_benchmark.html`.

Use `python3 operator_system.py lookup FALSIFIER` to inspect a consequence role, or `python3 operator_system.py consequences --frontier Challenge` to list a frontier. `list` browses the V2 index alphabetically by default; `--sort proxy` opts into the old family-weighted order.

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
python3 scripts/build_consequence_map.py
```

The compiler suite requires `pytest`; the toolkit and map scripts have no package dependencies beyond Node and Python. CI checks the parts separately. The [100-check record](docs/review-100.md) reports structural probes of the V2 index, and `verify_source.py` reconciles its records. The consequence map is a separate parametric design. None of these checks establishes task-level performance or browser layout quality.

## Agent entry point

Read [AGENTS.md](AGENTS.md) for the working contract. The [architecture](docs/system.md) distinguishes source words, typed programs, executed actions, verified results, and durable capability. [Benchmarks](docs/benchmarks.md) defines comparisons and targets; [TODO](TODO.md) tracks work that has not been completed. The CLI's `packet` command retrieves possible moves from words in a request. It does not execute, grant authority, or verify anything.
