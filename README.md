# BigDic: agent operator system

A source-indexed operator vocabulary, an executable routing interface, and a plan for turning useful words into durable agent capabilities.

**Current status:** the full V2 lexical index (794 words) and nine local extensions are indexed. The routing CLI proposes candidates from visible cues; it does not execute work or prove performance. The [linked tower](docs/operator-towers.html) contains all 803 entries and a transparent default proxy. The proxy is for browsing, not an observed effect per word.

## Start

```sh
python3 operator_system.py check
python3 operator_system.py lookup RIVALIZE
python3 operator_system.py list --frontier Verification --limit 20
python3 operator_system.py packet 'Repair the failing code and verify the result'
python3 -m unittest discover -s tests -v
```

Read [AGENTS.md](AGENTS.md) before changing the system. [Architecture](docs/system.md) gives the state and evidence model. [Benchmarks](docs/benchmarks.md) distinguishes completed checks from ambitious short and long horizon targets. [TODO](TODO.md) orders the work into independently reviewable assets.

The normal user interface is an ordinary request. An agent should infer the desired result, choose an adequate program, execute available actions, inspect the result, and write back reusable evidence. `packet` is only an initial candidate retrieval aid. Never pass its output off as the completed request.

## Governing distinction

A lexical entry, typed signature, proposed program, actual execution, passing check, and reusable capability are separate states. A word in a prompt can specify a move; it cannot award itself evidence, authorization, or success. The historical source is indexed by its SHA-256 in `data/catalog.json`; nine additions are marked `LOCAL`.
