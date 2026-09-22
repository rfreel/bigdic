# Dictionary V2: Finite-Artifact Understanding Atlas

## Status

Finite-artifact characterization is **SOLVED** for source SHA-256 `1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f`.

Open-world semantic completeness is **UNRESOLVED**. Model-general behavioral validation is **UNRESOLVED**. Hugging Face is not used or required.

## Frozen object

The exact source has 19,192 lines, 794 lexical records, 1,000 semantic signatures, 18 operator-family anchors, 19 structural model types, 18 common operator contracts plus MODIFIER and STATUS, 31 modifier axes, and 20 explicit macro expressions.

The canonical relation is:

`Lexeme -> SemanticSignature[] -> bound operational contract`

A lexeme is a lookup node, not proof that all uses are equivalent. A signature is a contextual interpretation. A contract supplies inherited operational constraints. Local signature conditions refine the inherited contract and cannot be silently erased.

## What the dictionary is

It is four systems superimposed:

1. A lexical index of canonical terms and surface forms.
2. A semantic dispatch layer mapping occurrences to operators, operand roles, correctness obligations, context, transitions, provenance, and contracts.
3. An operational kernel of 18 operator contracts plus MODIFIER and STATUS.
4. An epistemic-control model separating requirements, evidence, authority, capability, effects, execution, verification, status, uncertainty, failure, closure, and equivalence.

The fourth layer is fundamental. It prevents requested, designed, implemented, dispatched, executed, observed, passed, verified, generalized, robust, complete, and closed from becoming one status variable.

## Operator distribution

Signature counts are: COMPILE 471, CONTROL 66, TRANSFORM 51, VERIFY 50, REPRESENT 50, ACT 38, TEST 35, INFER 31, ACQUIRE 23, SELECT 23, EVALUATE 23, COMPARE 22, EXPAND 22, INSPECT 22, CHALLENGE 20, UPDATE 20, SPLIT 17, CLOSE 16.

These counts are not importance scores. COMPILE is inflated by 449 modifier signatures. The ordinary COMPILE contract itself accounts for only 22 signatures; the other 449 COMPILE-operated signatures inherit MODIFIER.

VERIFY similarly bifurcates: 26 signatures use VERIFY and 24 use STATUS. This separates performing/evaluating a verification operation from interpreting a status word as an evidence-scoped assessment.

## Operand topology

The dominant transition is RULE -> COMPILE -> RULE with 449 modifier signatures. The non-modifier kernel is typed around evidence, representation, candidate, proposition, test specification, action, artifact, world state, and status objects.

Canonical dominant flows include ACQUIRE evidence->evidence, INSPECT evidence->representation, REPRESENT representation->representation, SPLIT candidate->candidate, EXPAND candidate->candidate, COMPARE/EVALUATE candidate->representation, INFER evidence->proposition, CHALLENGE proposition->test specification, TEST test specification->evidence, UPDATE status->status, SELECT candidate->action, TRANSFORM artifact->artifact, ACT action->world state, VERIFY status->status, CONTROL action->action, and CLOSE status->status.

Rare alternate role flows are retained. Roles are semantic views, not necessarily disjoint physical types.

## Correctness obligations

The 1,000 signatures encode these obligation expressions: CONSTRAINT_SATISFACTION 740; SEMANTIC_PRESERVATION 74; DECISION_ADMISSIBILITY 47; SOURCE_FIDELITY 43; EXTERNAL_POSTCONDITION 38; COMMUNICATIVE_EFFECT|SEMANTIC_PRESERVATION 27; FORMAL_ENTAILMENT 12; EXECUTABLE_BEHAVIOR 7; EMPIRICAL_SUPPORT 7; CAUSAL_IDENTIFICATION 2; COMMUNICATIVE_EFFECT 2; PREDICTIVE_PERFORMANCE 1.

These are not collapsed. Formal entailment, empirical support, causal identification, predictive performance, external postcondition success, and semantic preservation require different evidence.

## Modifier system

There are 449 MODIFIER-contract signatures over 31 axes. The largest are POSITIVE_EXTREME_TAIL_LEXICON 38, NEGATIVE_EXTREME_TAIL_LEXICON 30, BINDING_FORCE 21, DETERMINISM 19, DETAIL 18, DEPTH 18, RIGOR 18, ASSERTION_FORCE 16, BREADTH 16, DANGEROUS_PSEUDO_STRENGTH_MODIFIERS 16, COMPLETENESS 14, CONSERVATISM 13, ABSTRACTION 12, AUTONOMY 12, CREATIVITY 12, ROBUSTNESS 12, and 15 additional axes.

The source does not assert calibrated interval scales or universal total orders for these axes. Requested intensity changes procedure or presentation, not evidence, authority, achieved verification status, or actual capability.

The DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis explicitly contains rhetoric such as ABSOLUTELY-CERTAIN, NEVER-WRONG, PERFECT, UNLIMITED, and USE-ALL-INTELLIGENCE so that such language is not misread as an evidence upgrade.

## Polysemy

121 lexemes have multiple signatures. 68 dispatch to more than one operator; 53 have multiple contextual signatures inside one operator.

Highest-cardinality cases include NORMAL 13 signatures; VERIFY 7; EXHAUSTIVE 7 across CLOSE/COMPILE/VERIFY; ROBUST 5 across COMPILE/VERIFY; TEST 5; BRANCH 5 across CONTROL/SELECT/SPLIT; EXPLAIN 5 across INFER/REPRESENT; DEFER 5 across CLOSE/CONTROL/SELECT; ROLLBACK 5 across ACT/CONTROL/UPDATE; COMPLETE 5 across CLOSE/COMPILE/CONTROL; and TRANSLATE 5 across REPRESENT/TRANSFORM.

Other critical forks include PROVE as INFER versus VERIFY, VALIDATE as TEST versus VERIFY, IMPORT as ACQUIRE versus ACT, LOCALIZE as SPLIT versus TRANSFORM, and IMPLEMENT as TRANSFORM/ACT/CONTROL.

No branch may be discarded merely because the spelling is identical.

## Provenance

934 signatures are SOURCE_MAPPED_CANDIDATE. 66 are AUTHORED_MIGRATION_PROPOSAL. The authored proposals touch 30 lexemes. Only DEPENDENCY-MAP, MITIGATE, and RETEST are proposal-only; the other 27 proposal-bearing lexemes also retain source-mapped senses.

Provenance therefore belongs to the signature, not just the lexeme. Agreement between source-derived and authored structures remains internal consistency, not independent corroboration.

## Structural reuse

The exhaustive benchmark found 32 repeated term-erased signature-template clusters covering 346 lexemes. The largest cluster contains 37 terms including ABSOLUTE, ALL, ALWAYS, ATOMIC, CANONICAL, COMPLETE, COMPREHENSIVE, DETERMINISTIC, EXACT, EXHAUSTIVE, EXPLICIT, FORMAL, FULLY, INDEPENDENT, MAXIMAL, PAINSTAKING, RIGOROUS, SATURATED, STRICT, SYSTEMATIC, UNAMBIGUOUS, and ZERO-DEVIATION.

The next largest contains 29 low-intensity/permissive forms such as APPROXIMATE, BARE-MINIMUM, BRIEF, COARSE, CURSORY, FLEXIBLE, GIST-ONLY, INFORMAL, LIGHTWEIGHT, MINIMAL, PARTIAL, ROUGH, SHALLOW, TENTATIVE, TERSE, UNCHECKED, UNVERIFIED, and VAGUE.

A shared term-erased template is a review discriminator. It is not proof of synonymy.

## Lexical-neighbor risk

The executed TF-IDF benchmark reports mean nearest-neighbor similarity 0.510069 and maximum 0.994706. Twenty lexemes exceed 0.85. MUST/MUST-NOT and SHOULD/SHOULD-NOT are the clearest counterexamples to similarity-as-equivalence because a small lexical change reverses polarity. Other high-similarity pairs include PREFER/STRONGLY-PREFER, AVOID/STRONGLY-AVOID, HIGHLY-NOVEL/NOVEL, HIGHLY-SUPPORTED/SUPPORTED, and ONE-SOURCE/ONE-SOURCE-CLASS.

## Status and uncertainty

39 lexemes require evidence/status handling. 24 signatures inherit STATUS. Status is represented as a product of artifact, execution, check, verification, robustness, generalization, and resolution assessments, not a scalar ladder.

UNRESOLVED means active work remains. OPEN means a material uncertainty witness exists but no adequate known resolution path is available. BLOCKED means a resolution path is known but unavailable. UNKNOWN requires a scoped non-identifiability, underdetermination, undecidability, or impossibility basis.

## Authority, capability, execution, and effects

33 lexemes require authority/effect checks. Direct mutation vocabulary includes ACT, APPLY, CALL, CONFIGURE, COPY, CREATE, DELETE, DEPLOY, DISABLE, EDIT, ENABLE, EXECUTE, EXPORT, IMPLEMENT, IMPORT, INSTALL, INVOKE, MIGRATE, MODIFY, MOVE, PUBLISH, RESTART, ROLLBACK, RUN, SAVE, SCHEDULE, SEND, SIMULATE, START, STOP, SUBMIT, TRIGGER, and WRITE.

The ACT contract separates permission, capability, dispatch, observed effects, and verified postconditions. A timeout does not imply non-execution. An ambiguous mutation receipt is not safe grounds for blind retry. Restoring an artifact does not necessarily undo disclosure or other residual effects.

## Closure

CLOSE is scoped stopping, not a demand for a single confident answer. The source separates process termination, requirements completion, finite registry completion, observed generation plateau, reachable saturation, and semantic completeness.

Therefore this mission can legitimately close finite-artifact characterization while leaving open-world semantic completeness unresolved.

## Macro/control layer

There are 20 explicit macro expressions: ANALYZE, AUDIT, DEBUG, DECIDE, DEPLOY, DESIGN, FORECAST, IMPLEMENT, INVESTIGATE, MIGRATE, OPTIMIZE, PLAN, PREMORTEM, REFACTOR, RESEARCH, REVIEW, SOLVE, SYNTHESIZE, TEACH, and TROUBLESHOOT.

Only five lexemes have benchmark class MACRO_WORKFLOW because many macro-bearing terms have additional senses and are classified MULTI_SENSE. Macro count and benchmark-class count are distinct.

The macros are ordered compositions, not evidence. Intermediate terms may themselves be polysemous and require binding.

## Review frontier

486 lexemes have at least one observable review dimension. The dimensions overlap: 121 multi-sense, 378 context-binding-required, 33 authority/effect-sensitive, 39 status/evidence-sensitive, 346 in repeated term-erased templates, and 20 above the lexical-similarity threshold. 308 lexemes have none of those six current flags.

No aggregate semantic-quality score is emitted because these dimensions require different discriminators.

## Internal integrity

The supplied exhaustive benchmark reports zero hard lexeme structural failures, zero hard signature structural failures, zero normalized cross-lexeme surface collisions, 794/794 detected lexeme deletion mutants, 1,000/1,000 detected signature deletion mutants, and no exact signature fingerprint shared by another lexeme.

These establish finite structural accounting. They do not establish ontological minimality, universal completeness, behavioral optimality, or semantic correctness in every future context.

## Closure attack

The characterization was attacked against source identity, cardinality, provenance, polysemy, operator/contract dispatch, role flow, correctness obligations, modifier axes, status/effect boundaries, repeated templates, lexical similarity, macros, and the source evidence boundary.

For this exact revision, every lexeme and signature is accounted for under the encoded schema. The independent replay script checks the source hash and directly recounts lexemes, signatures, operators, axes, provenance classes, polysemy, and macro expressions from the pinned source.

**SOLVED:** complete deterministic characterization of the supplied finite Dictionary V2 artifact under its encoded schema and benchmark projections.

**UNRESOLVED:** whether the 18 families are minimal or universally complete; calibrated modifier magnitudes; universal correctness of authored proposals; model-general behavioral equivalence/effects; ACT postconditions without execution; coverage of every future instruction; and any finite quotient claimed to preserve all admissible future continuations.
