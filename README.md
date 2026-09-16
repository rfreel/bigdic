# bigdic

`bigdic` is an executable operator dictionary and measurement workspace. This branch adds **Operator Compiler v1** and the first **BiggestDic** expansion layer: a transparent state-conditioned controller plus provider-neutral causal experimentation over the 18 canonical operator families.

The exact Dictionary V2 source is pinned at `data/dictionary-v2.md` with SHA-256 `1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f`.

See `docs/DICTIONARY_UNDERSTANDING.md` for the exhaustive finite-artifact characterization and `docs/BIGGESTDIC.md` for the expansion program.

## What is implemented

```text
Dictionary V2
  -> typed operator contracts
  -> OperatorState IR
  -> applicability model
  -> marginal value / VOC / EVSI estimators
  -> conditional interaction model
  -> motif + macro induction
  -> greedy / beam / A* / branch-and-bound planners
  -> adaptive budget frontier
  -> counterfactual replay
  -> cross-regime transfer report
  -> runtime controller
  -> provider-neutral causal backends
  -> lexeme / pair / triple experiment frontier
```

The epistemic kernel is not optimized away. Source distinctions, authority/capability boundaries, unresolved branches, and external evidence boundaries remain explicit.

## Evidence lanes

- `FINITE_EXACT`: deterministic operator measurements under `data/measurements/`.
- `REPLAY`: deterministic provider-neutral causal fixtures used by GitHub Actions.
- `LOCAL_TRANSFORMERS`: isolated GitHub-hosted CPU inference. It downloads open weights directly and does not use Hugging Face Jobs.
- `OPENAI_COMPATIBLE`: optional OpenRouter, Groq, and Gemini-compatible transports when their API-key environment variables are supplied.

Hugging Face Jobs is not required.

## Run

```bash
python -m pytest -q
PYTHONPATH=src python scripts/build_artifacts.py
python -m compileall -q src tests scripts
```

Status distinctions are literal: designed, implemented, executed, passed, independently verified, and generalized are not interchangeable. Open-world semantic completeness remains unresolved.