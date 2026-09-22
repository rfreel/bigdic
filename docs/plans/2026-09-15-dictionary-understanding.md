# Dictionary Understanding Mission Implementation Plan

> **For agentic workers:** execute this plan task-by-task. Every upward status change requires a receipt.

**Goal:** Fully characterize the supplied Dictionary V2 revision as it exists, without Hugging Face, while preserving source/proposal, lexical/signature, structural/semantic, and executed/unexecuted distinctions.

**Architecture:** Treat the dictionary as a typed corpus, not a bag of words. Build deterministic projections from the exact 19,192-line source and the already executed 794-lexeme/1,000-signature benchmark. Produce an atlas that makes every lexeme, signature, operator, contract, axis, role transition, obligation, provenance class, template cluster, multi-sense branch, status/effect boundary, and unresolved semantic dependency inspectable. Do not use model agreement as evidence of meaning.

**Tech stack:** Python 3.12 standard library + pandas for offline analysis; GitHub Actions for independent replay. No Hugging Face Jobs or hosted inference is required.

**Source:** `Dictionary_V2_Working_Draft (1).md`, SHA-256 `1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f`, 19,192 lines. Exact source is also present on branch `codex/dictionary-toolkit` as `data/dictionary-v2.md`.

## Global constraints

- Preserve `Lexeme -> SemanticSignature[] -> bound operational contract`.
- Never equate lexical identity, signature identity, operator family, or term-erased template without an explicit equivalence witness.
- Keep `SOURCE_MAPPED_CANDIDATE` distinct from `AUTHORED_MIGRATION_PROPOSAL`.
- Structural integrity is not semantic quality.
- A modifier axis is not a calibrated numeric scale unless the source supplies one.
- Authority, capability, execution, observation, verification, status, and closure remain separate.
- UNKNOWN is not emitted merely because semantic work is difficult.
- No Hugging Face dependency.

## Prewalk

1. **Freeze source identity.** Recompute source hash and line count; reject analysis on mismatch.
2. **Reproduce corpus cardinalities.** Require exactly 794 lexemes, 1,000 signatures, and 18 family anchors.
3. **Map the document grammar.** Inventory top-level sections, 19 structural types, 18 common operator contracts, MODIFIER and STATUS contracts, lexical records, signature records, and evidence-boundary section.
4. **Build the lexeme atlas.** One row per lexeme with role classes, source forms, signature/branch/operator counts, contracts, axes, provenance, context/effect/status requirements, nearest neighbor, template cluster, and review flags.
5. **Build the signature atlas.** One row per signature with source/proposal provenance, operator, input/output roles, correctness obligations, transition, axis/destination, macro expression, and source line span.
6. **Characterize operator families.** For each of 18 operators measure signature/lexeme coverage, role transitions, obligations, provenance mix, multi-sense participation, context binding, effect requirements, and status requirements.
7. **Characterize contracts.** Separate 18 operator contracts from MODIFIER/STATUS contracts and measure operator-to-contract deviations such as VERIFY signatures using STATUS.
8. **Characterize operand flow.** Build the directed input-role -> operator -> output-role topology and enumerate rare role transitions.
9. **Characterize correctness obligations.** Build operator x obligation and role-transition x obligation matrices; do not collapse conjunctions.
10. **Characterize modifier space.** Enumerate every axis, destination, member count, provenance, and cross-axis multi-sense lexeme. Treat source-order ladders as display data only.
11. **Characterize polysemy.** Exhaust all 121 multi-signature lexemes; distinguish same-operator contextual branching from cross-operator branching. Highlight high-cardinality cases such as NORMAL, VERIFY, EXHAUSTIVE, BRANCH, COMPLETE, and ROLLBACK.
12. **Characterize provenance.** Account for all 934 source-mapped and 66 authored-proposal signatures and identify which semantic distinctions exist only as authored proposals.
13. **Characterize template reuse.** Enumerate all repeated term-erased templates and their member lexemes. Treat them as structural similarity classes, not synonym classes.
14. **Characterize lexical-neighbor risk.** Preserve nearest-neighbor TF-IDF pairs and flag high-similarity pairs where polarity, modality, scope, or status can reverse behavior.
15. **Characterize status semantics.** Enumerate STATUS-contract and status-role signatures; preserve artifact/execution/check/verification/robustness/generalization/resolution products rather than a scalar ladder.
16. **Characterize authority/effect semantics.** Enumerate the 33 lexemes requiring authority/effect checks and distinguish ACT/world mutation from epistemic or representational operations.
17. **Characterize closure semantics.** Extract CLOSE, closure-related modifiers/statuses, saturation terms, and evidence-boundary claims; distinguish finite completion from open-world semantic completeness.
18. **Characterize macros and control.** Enumerate macro workflows, macro expressions, CONTROL signatures, ordering/branch/iteration terms, and dependencies between operators.
19. **Construct the semantic topology.** Emit machine-readable nodes/edges linking lexeme -> signature -> operator -> contract -> roles -> obligations -> axis/destination -> provenance.
20. **Construct the ambiguity frontier.** Rank by observable review burden only: multi-sense, context binding, authority/effect, status evidence, template reuse, and high lexical similarity. Do not fabricate a semantic quality score.
21. **Run invariance checks.** Prove every source lexeme/signature appears exactly once in the atlas, every referenced operator/contract/axis is accounted for, and aggregate counts reconcile to source benchmarks.
22. **Write the understanding report.** State what the dictionary is, how it is structured, what each layer means, dominant patterns, exceptional cases, and all remaining non-identifiability/validation boundaries.
23. **Write machine receipts.** Record source hash, counts, generated artifact hashes, checks performed, pass/fail state, and unresolved claims.
24. **Independent replay.** Add/extend CI so atlas generation and invariance checks execute from repository data without hosted inference.
25. **Closure attack.** Attempt to falsify the claim that the dictionary is fully characterized *as a finite artifact*. Search for unaccounted records, unresolved internal references, hidden source/proposal merges, unexplained clusters, and aggregate mismatches. Close only finite-artifact characterization; leave open-world semantic completeness unresolved.

## Required outputs

- `docs/DICTIONARY_UNDERSTANDING.md`: human-readable exhaustive atlas and interpretation.
- `results/understanding/summary.json`: canonical counts and boundaries.
- `results/understanding/operator_atlas.csv`: all 18 families.
- `results/understanding/axis_atlas.csv`: every modifier axis.
- `results/understanding/polysemy_atlas.csv`: all multi-signature lexemes.
- `results/understanding/provenance_atlas.csv`: source/proposal distribution.
- `results/understanding/template_clusters.csv`: all repeated term-erased templates.
- `results/understanding/ambiguity_frontier.csv`: observable review burden, no quality score.
- `results/understanding/role_flow.csv`: role transition topology.
- `results/understanding/operator_obligation_matrix.csv`: correctness-obligation coverage.
- `results/understanding/semantic_topology.json`: graph representation.
- `results/understanding/receipt.json`: replayable closure receipt.

## Acceptance

Accept finite-artifact understanding only if source hash matches, 794/794 lexemes and 1,000/1,000 signatures reconcile, all 18 operators and all observed contracts/axes/roles/obligations/provenance classes are represented, all 121 multi-signature lexemes are explicitly preserved, all repeated template clusters are retained without synonym collapse, and CI can regenerate the atlas. Open-world semantic completeness remains `UNRESOLVED` by construction.