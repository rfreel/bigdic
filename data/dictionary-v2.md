# Canonical Prompt Operator and Modifier Dictionary V2

Working draft. Source inventory and local checks executed. Semantic closure remains UNRESOLVED.

This is a source-preserving migration of the frozen V1 file, not a newly invented word list. The source has 580 heading-delimited blocks across 3,211 lines. The migrated index contains 794 lexical records and 1,000 source-indexed or context-specific signature records. These counts do not denote that many independent primitive meanings: they include modifiers, policies, statuses, repeated source senses and proposed refinements.

V1 SHA-256: `ea6f8fc56b3582735af0d7761789683a470194cccf636e7b680fc3772a72e964`.

The 18 operator families are retained as navigational and typing anchors. Their minimality or universal completeness is not established. The source prose is archived byte-for-byte. Every source block and lexical record has a migration disposition. Exact source preservation is a mechanical result; preservation of meaning under every possible future context is not.

The current validation run records 13/13 passing check groups, 30/30 passing authored case pairs, and 30/30 detected guard-deletion mutants. These test the local representation and guard implementation. They are not tests of an external world or independent verification of all English meanings.

No V1 file was overwritten. No external research, independent reproduction, live-system enforcement or formal proof is claimed.

## Reading the dictionary

`Lexeme -> SemanticSignature[] -> bound operational contract`.

A lexical record is a lookup node, not a proof that all its usages are equivalent. Each signature records the operation, operand roles, correctness obligations, source or proposal origin and a contract reference. A signature inherits its named common contract. Its own transition, context-specific evidence requirement, status rule and closure rule refine that contract. A material conflict between inherited and specific conditions must be reported rather than silently overridden.

Source-mapped signatures preserve V1 family placement and wording. Authored migration proposals are labeled separately. Role and context parameters must be bound to the actual task before execution. A dictionary definition does not grant authority, supply missing evidence or prove its own applicability.

Source references such as `SRC-0042` resolve through `data/dictionary_v2.json` to exact raw text, parent heading, line range and hash. Raw source text is historical evidence, not automatic endorsement of superseded status or strength claims.

The source source-order modifier ladders are retained as lexical/display data. No measured frequency distribution, calibrated interval scale, universal total ordering or extreme-tail probability is asserted.

## Structural model

### Lexeme
How is the expression written?

Fields: `id, canonical_term, surface_forms, lexical_classes, signature_ids, source_occurrences`.

Canonical spelling is a lookup convention. Equal spelling does not prove equal meaning; different spellings are not made aliases without an explicit mapping.

Concrete instance: LOCALIZE has a failure-isolation sense and an audience-adaptation sense.

### OperatorSignature
What contextual operation is requested?

Fields: `id, operator, input_roles, output_roles, correctness_obligations, context_profile, requirements, contract_ref, transition, provenance_kind`.

The 18 source families remain vocabulary anchors, not a proven irreducible basis. Source-derived signatures and authored refinements are explicitly distinguished. Parent contracts are inherited and must not erase a more specific source condition.

Concrete instance: VERIFY a source date and VERIFY a deployment endpoint have different target properties and evidence.

### OperandKind
What role does the object play in this operation?

Fields: `kind, identity, revision, role, representation, refinements`.

Roles are semantic views, not necessarily disjoint physical types. A document can be an artifact, an evidence object or an output representation. The relevant role is bound at invocation.

Concrete instance: A proof file is an ARTIFACT to save and evidence for a formal assessment after checking.

### CorrectnessObligationSet
Which properties make the result acceptable?

Fields: `obligations, target_properties, scope, assumptions, acceptance_rule`.

Allow conjunctions, alternatives and conditional obligations. A named regime is a convenient profile, not an exclusive exhaustive label. Source fidelity does not by itself establish target-world truth.

Concrete instance: A translation may require both source fidelity and preservation of obligations.

### ContextProfile
Which conditions change the applicable contract?

Fields: `temporal_constraints, observability, outcome_model, actors_and_channels, threat_model, stake_constraints, preference_model, privacy_constraints`.

These are compositional constraints, not mutually exclusive enums. Bind them to a target and time. Formal reasoning over a stochastic model is valid; privacy requirements can constrain both reads and disclosures.

Concrete instance: A distributed, stochastic, adversarial workflow needs all three constraints, not one winning regime label.

### RequirementSet
What is required, permitted, forbidden or preferred?

Fields: `issuer, applicability, modality, predicate, quantifier, scope, priority, tolerance, temporal_operator`.

MUST, ONLY, EXACTLY and ALWAYS are different constructs. Modality is not quantification, precision is not priority, and repeated emphasis does not create authority. Conflicting obligations require conflict handling, not quiet deletion.

Concrete instance: Must inspect obliges an action; only inspect A restricts scope; inspect exactly two imposes cardinality.

### EvidenceRecord
What observation or record supports which assertion?

Fields: `id, kinds, target, target_revision, content_ref, provenance, method, observed_at, scope, dependencies, assumptions, validity_constraints`.

One record can have multiple evidence roles. Dependence, corroboration, independence and reproduction are relations with their own grounds. Record historical evidence immutably and derive current admissibility from target version and conditions.

Concrete instance: A simulator log proves a simulator ran, not that the real modeled action ran.

### AuthorityCapabilitySet
Which actor may perform this action on this target?

Fields: `grants, issuer, principal, actions, resources, limits, expiry, revocation_state, delegation_chain`.

Authority is action-, actor-, target- and time-scoped. Capabilities such as READ and PUBLISH are not ranks. Reading a document does not convert its embedded requests into permissions.

Concrete instance: An actor may execute a private test but lack permission to publish its data.

### CapabilityState
Can the permitted operation actually be performed here?

Fields: `operation, target, availability, conditions, observed_at, supporting_record`.

AVAILABLE, UNAVAILABLE, DEGRADED and UNKNOWN_AVAILABILITY are task capability states. UNKNOWN_AVAILABILITY is not the terminal epistemic status UNKNOWN. Availability never grants authorization.

Concrete instance: A user can authorize a deployment while the required endpoint is inaccessible.

### EffectProfile
What changes, and what remains after an attempted undo?

Fields: `effect_locus, side_effects, undo_mechanism, undo_preconditions, undo_cost, undo_window, residual_effects`.

Effects are target-indexed. Dry runs can consume resources or create logs. Transactional abort, compensating action and restoration differ; no scalar reversibility score is assumed.

Concrete instance: Restoring a deleted file does not undo a disclosure that already occurred.

### ExecutionState
What actually happened to this attempt?

Fields: `attempt_id, target, target_revision, phase, outcome, dispatch_record, observed_effects, postcondition_assessments`.

Keep phase separate from outcome and remote effect. Preserve ambiguous receipt states. A timeout does not imply the target action failed to execute, so retry safety needs idempotence or reconciliation.

Concrete instance: A payment request times out after the service may have committed it.

### VerificationRecord
Which property was checked by which method?

Fields: `id, target, target_revision, property, scope, method, phase, outcome, evidence_refs, checker, dependence_claims, limitations`.

Use per-check outcomes PASS, FAIL, ERROR, INCONCLUSIVE, NOT_RUN or NOT_APPLICABLE. A schema check establishes structural conformity only. Formal verification and empirical replication are not globally ordered.

Concrete instance: A passing unit check cannot erase a failed integration requirement.

### StatusProduct
Which supported assessments coexist?

Fields: `artifact_records, execution_records, check_records, verification_assessments, robustness_assessments, generalization_assessments, resolution_assessments`.

Retain target- and scope-indexed records, not a single ladder. Do not assume this product is a total order or a lattice with every meet and join. Display labels are derived projections and may coexist across distinct scopes.

Concrete instance: The code is implemented, the unit test passed, the integration test failed, and production remains untested.

### UncertaintyRecord
Which material alternatives remain and how can they be resolved?

Fields: `state, live_alternatives, material_consequence, discriminator_space, known_resolution_path, availability, evidence_refs, reopen_trigger, nonidentifiability_certificate`.

Use UNRESOLVED for active remaining work; OPEN for a material witness without an adequate known path; BLOCKED for a known unavailable path. UNKNOWN requires a scoped non-identifiability or impossibility basis, not difficult search or absent tools.

Concrete instance: Two consistent worlds requiring different actions remain BRANCHED even if neither world contains a rule conflict.

### FailureRecord
Which operation failed and what does that invalidate?

Fields: `kind, operation, attempt, evidence_refs, dependencies, affected_assessments, recoverability, continuation`.

Method failure is not automatically evidence against a world. Retain unaffected results and alternate sufficient support sets. Partial failures need observed-effect accounting before recovery.

Concrete instance: A source fetch failure does not invalidate an already verified calculation based on another source.

### ClosureCertificate
What exact stopping claim is supported?

Fields: `kind, requested_scope, established_scope, live_classes, remaining_obligations, coverage_method, support_refs, assessment, issued, reopen_trigger`.

Separate delivery closure, resource stop, finite registry completion, observed generation plateau, reachable saturation and semantic completeness. A document called a certificate is not itself proof that its claim holds.

Concrete instance: All 580 source blocks can be accounted for while open-world semantic completeness remains unresolved.

### EquivalenceSpec
Under what relation may two cases be collapsed?

Fields: `objective, projection, scope, admissible_continuations, relation_definition, relation_properties, evidence_refs, assessment`.

Distinguish lexical lookup identity, output agreement, decision validity and continuation-preserving equivalence. Approximate closeness need not be transitive. No semantic merges are executed in this migration.

Concrete instance: Under tolerance 0.1, 0 is close to 0.09 and 0.09 to 0.18, but 0 is not close to 0.18.

## Common operator contracts

Contracts below are proposed normative definitions. They are not receipts that any invocation has satisfied them.

### Contract COMPILE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Interpret intent as a scoped task contract; preserve materially different parses.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Reconstruct the source requirements and preserve quantifier, negation, scope, priority and authority.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Reconstruct the source requirements and preserve quantifier, negation, scope, priority and authority.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: INFER

Concrete example: Parse "only summarize section 2" as a scope restriction, not permission to rewrite section 1.

Abstract principle: Interpret intent as a scoped task contract; preserve materially different parses.

### Contract ACQUIRE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Obtain relevant records and provenance; do not silently assert their contents are true.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Match returned identifiers and content to the requested source and record acquisition side effects.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Match returned identifiers and content to the requested source and record acquisition side effects.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: INFER

Concrete example: Retrieve the specified contract revision and record its identifier.

Abstract principle: Obtain relevant records and provenance; do not silently assert their contents are true.

### Contract INSPECT

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Record accessible properties with an observation procedure and a stated boundary.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Separate the observed reading from interpretations and instrument assumptions.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Separate the observed reading from interpretations and instrument assumptions.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: INFER

Concrete example: Read "3 failed" from a test log without inferring overall product quality.

Abstract principle: Record accessible properties with an observation procedure and a stated boundary.

### Contract REPRESENT

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Re-encode protected content under an explicit preservation projection.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Compare protected propositions, quantities, relations, modality and provenance before and after.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Compare protected propositions, quantities, relations, modality and provenance before and after.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: TRANSFORM

Concrete example: Convert a dependency list into graph edges while preserving their direction.

Abstract principle: Re-encode protected content under an explicit preservation projection.

### Contract SPLIT

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Separate components or cases with a declared partition or decomposition relation.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Record a material witness or task-required component; do not assert disjointness for an overlapping decomposition.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Record a material witness or task-required component; do not assert disjointness for an overlapping decomposition.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: EXPAND

Concrete example: Keep purchased and leased equipment in separate decision cases when costs differ.

Abstract principle: Separate components or cases with a declared partition or decomposition relation.

### Contract EXPAND

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Extend a specified candidate frontier without upgrading generated claims to observed facts.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Record generation operations, new candidates, comparison projection and residual search space.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Record generation operations, new candidates, comparison projection and residual search space.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: ACQUIRE

Concrete example: Generate a second failure hypothesis consistent with the same log.

Abstract principle: Extend a specified candidate frontier without upgrading generated claims to observed facts.

### Contract COMPARE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Compute similarities, differences or a relation under declared criteria and scope.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Check alignment, units, relation properties and any requested continuation equivalence.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Check alignment, units, relation properties and any requested continuation equivalence.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: SELECT

Concrete example: Compare two designs on the same latency and availability requirements without choosing.

Abstract principle: Compute similarities, differences or a relation under declared criteria and scope.

### Contract INFER

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Derive a proposition using explicit premises, rules, assumptions and scope.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Check entailment or evidential adequacy for the chosen correctness obligation; retain defeaters.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Check entailment or evidential adequacy for the chosen correctness obligation; retain defeaters.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: INSPECT

Concrete example: Infer a candidate failure cause from symptoms, labeling it a hypothesis.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

### Contract CHALLENGE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Construct a potentially defeating case, rival or objection tied to a material requirement.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Show how the proposed defeater could change the result; a rhetorical objection is not a failed test.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Show how the proposed defeater could change the result; a rhetorical objection is not a failed test.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: TEST

Concrete example: Propose an expired-authorization case against an automatic deployment policy.

Abstract principle: Construct a potentially defeating case, rival or objection tied to a material requirement.

### Contract TEST

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Execute a defined check and record observations, outcome, scope, target version and method.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Compare observed and expected results; record PASS, FAIL, ERROR, INCONCLUSIVE or NOT_RUN separately.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Compare observed and expected results; record PASS, FAIL, ERROR, INCONCLUSIVE or NOT_RUN separately.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: VERIFY

Concrete example: Run a regression fixture against a specific build and retain its output.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

### Contract UPDATE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Revise current projections using new evidence while preserving immutable historical records.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Recompute only affected claims, including alternate sufficient support sets and changed scope.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Recompute only affected claims, including alternate sufficient support sets and changed scope.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: TRANSFORM

Concrete example: Invalidate a stale test certificate while preserving unrelated source extractions.

Abstract principle: Revise current projections using new evidence while preserving immutable historical records.

### Contract EVALUATE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Assess candidates against mandatory requirements and then declared optional objectives.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Keep feasibility, admission, value and ordering distinct; preserve incomparable objectives.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Keep feasibility, admission, value and ordering distinct; preserve incomparable objectives.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: SELECT

Concrete example: Score two feasible bids on declared criteria without silently imposing weights.

Abstract principle: Assess candidates against mandatory requirements and then declared optional objectives.

### Contract SELECT

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Return an authorized choice, robust shared option or explicit conditional alternatives.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Check choice validity across live cases and distinguish conflicts within a case from lack of a universal action.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Check choice validity across live cases and distinguish conflicts within a case from lack of a universal action.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: ACT

Concrete example: Preserve buy-versus-lease branches until utilization is determined.

Abstract principle: Return an authorized choice, robust shared option or explicit conditional alternatives.

### Contract TRANSFORM

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Create a changed candidate under specified protected invariants and improvement criteria.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Check both intended changes and protected properties, including semantic loss budgets.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Check both intended changes and protected properties, including semantic loss budgets.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: SELECT

Concrete example: Refactor a function while preserving its declared input-output behavior.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

### Contract ACT

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Revalidate permission, capability, target version and mandatory conditions before dispatch; inspect postconditions.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Revalidate permission, capability, target version and mandatory conditions before dispatch; inspect postconditions.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: SELECT

Concrete example: Write a new draft file without overwriting its predecessor.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

### Contract VERIFY

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Bind the assessment to target, property, version, method, evidence, dependencies and remaining obligations.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Bind the assessment to target, property, version, method, evidence, dependencies and remaining obligations.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: TEST

Concrete example: Check that a deployment endpoint serves the intended version rather than trusting a dispatch receipt.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

### Contract CONTROL

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Change sequencing, branching, iteration or coordination while preserving semantic and effect constraints.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Check dependencies, stale bases, retry safety, resource bounds and conflicting concurrent effects.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Check dependencies, stale bases, retry safety, resource bounds and conflicting concurrent effects.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: ACT

Concrete example: Retry a read operation after failure; do not blindly retry a payment with an ambiguous receipt.

Abstract principle: Change sequencing, branching, iteration or coordination while preserving semantic and effect constraints.

### Contract CLOSE

Preconditions: Bind target, objective, scope, relevant revision and actor.; Resolve or explicitly branch material interpretations before committing.

Transition: Stop the current work with a scoped assessment, explicit residuals and reopening conditions.

Postconditions: Return the requested typed result with provenance and scoped status.; Preserve unresolved distinctions and unaffected source information.

Admissibility: Satisfy applicable hard requirements; distinguish evidence from permission.; A missing governing fact requires a branch, deferral or bound discriminator, not an invented fact.

Evidence obligations: Distinguish process termination, requirements completion, finite coverage, semantic saturation and certification.; Record actual method, observations, dependencies and target scope; generated content is not new empirical evidence.

Authority requirements: Every protected read, disclosure or mutation requires a valid actor-action-target grant; no family name grants authority.

Capability requirements: Bind the actual available method or tool; technical access is distinct from permission.

Effect profile: {"binding_required": true, "fields": ["effect_locus", "side_effects", "undo_mechanism", "undo_cost", "undo_window", "residual_effects"], "rule": "Do not infer zero effects from an epistemic verb, simulation or dry-run label."}

Failure rules: Record failure reason and observed effects; do not replay an ambiguous mutation blindly.; Invalidate only dependent assessments; retain immutable records and alternate sufficient support.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Verification rules: Distinguish process termination, requirements completion, finite coverage, semantic saturation and certification.; Assess the exact required property; a structural schema check is not external-world verification.

Closure rules: Close only at the requested evidence boundary or with explicit residual branches and reopen conditions.; Finite examples or repeated candidates do not certify open semantic closure.

Nearest non equivalents: CONTROL

Concrete example: Finish a finite source inventory while leaving open-world synonym coverage unresolved.

Abstract principle: Stop the current work with a scoped assessment, explicit residuals and reopening conditions.

### Contract MODIFIER

Bind a modifier occurrence to an axis-specific operational constraint, preference or evidence-derived attribute.

Requested intensity changes procedure or presentation, not evidence, authority or achieved verification status.

### Contract STATUS

Interpret a status word as a scoped assessment over identified records, not as a requested evidence upgrade.

Retain the target, property, revision, method, outcome, dependencies and evidence references for each assessment.

## Lexical dictionary

### A/B-TEST

ID: `LEX-a-b-test`. Roles: specialized_operator.

Source forms: `A/B-TEST`.

#### SIG-a-b-test-SRC-0239

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0239 / V1 lines 941-943

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Compare two alternatives empirically.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ABDUCE

ID: `LEX-abduce`. Roles: specialized_operator.

Source forms: `ABDUCE`.

#### SIG-abduce-SRC-0180

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0180 / V1 lines 726-728

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer plausible explanations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ABSOLUTE

ID: `LEX-absolute`. Roles: modifier_surface.

Source forms: `absolute`.

#### SIG-absolute-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "absolute" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ABSOLUTELY

ID: `LEX-absolutely`. Roles: context_bound_attribute_surface.

Source forms: `absolutely`.

#### SIG-absolutely-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "absolutely" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ABSOLUTELY-CERTAIN

ID: `LEX-absolutely-certain`. Roles: modifier_surface.

Source forms: `absolutely certain`.

#### SIG-absolutely-certain-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "absolutely certain" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ABSTRACT

ID: `LEX-abstract`. Roles: specialized_operator.

Source forms: `ABSTRACT`.

#### SIG-abstract-SRC-0105

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0105 / V1 lines 464-466

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Suppress irrelevant detail.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ABSTRACTION

ID: `LEX-abstraction`. Roles: execution_modifier.

Source forms: `ABSTRACTION`.

#### SIG-abstraction-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate abstraction using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ACCEPT

ID: `LEX-accept`. Roles: modifier_surface, specialized_operator.

Source forms: `ACCEPT`, `accept`.

#### SIG-accept-SRC-0296

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0296 / V1 lines 1134-1136

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Retain as satisfying requirements.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-accept-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "accept" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ACCEPTANCE-DEFINE

ID: `LEX-acceptance-define`. Roles: specialized_operator.

Source forms: `ACCEPTANCE-DEFINE`.

#### SIG-acceptance-define-SRC-0033

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0033 / V1 lines 236-240

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Specify exactly what constitutes satisfactory completion.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ACCEPTANCE-TEST

ID: `LEX-acceptance-test`. Roles: specialized_operator.

Source forms: `ACCEPTANCE-TEST`.

#### SIG-acceptance-test-SRC-0234

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0234 / V1 lines 926-928

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test requirements defining completion.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ACCEPTANCE-VERIFY

ID: `LEX-acceptance-verify`. Roles: specialized_operator.

Source forms: `ACCEPTANCE-VERIFY`.

#### SIG-acceptance-verify-SRC-0388

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0388 / V1 lines 1454-1456

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Verify completion against acceptance criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ACQUIRE

ID: `LEX-acquire`. Roles: family.

Source forms: `ACQUIRE`.

#### SIG-acquire-SRC-0035

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0035 / V1 lines 243-248

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Increase relevant evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ACT

ID: `LEX-act`. Roles: family.

Source forms: `ACT`.

#### SIG-act-SRC-0342

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0342 / V1 lines 1294-1297

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Cause an actual artifact, system, environment, account, or external-world state transition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADAPT

ID: `LEX-adapt`. Roles: specialized_operator.

Source forms: `ADAPT`.

#### SIG-adapt-SRC-0324

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0324 / V1 lines 1229-1231

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Modify for a different context.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADEQUATE

ID: `LEX-adequate`. Roles: context_bound_attribute_surface.

Source forms: `adequate`.

#### SIG-adequate-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "adequate" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADMISSIBILITY-CHECK

ID: `LEX-admissibility-check`. Roles: specialized_operator.

Source forms: `ADMISSIBILITY-CHECK`.

#### SIG-admissibility-check-SRC-0283

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0283 / V1 lines 1089-1091

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Evaluate mandatory constraints.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADMIT

ID: `LEX-admit`. Roles: specialized_operator.

Source forms: `ADMIT`.

#### SIG-admit-SRC-0298

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0298 / V1 lines 1140-1142

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Permit progression.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADVERSARIAL

ID: `LEX-adversarial`. Roles: semantic_policy_or_attribute.

Source forms: `ADVERSARIAL`.

#### SIG-adversarial-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate adversarial using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADVERSARIAL-EXAMPLE

ID: `LEX-adversarial-example`. Roles: specialized_operator.

Source forms: `ADVERSARIAL-EXAMPLE`.

#### SIG-adversarial-example-SRC-0215

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0215 / V1 lines 854-856

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Construct an input designed to expose failure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADVERSARIAL-TEST

ID: `LEX-adversarial-test`. Roles: specialized_operator.

Source forms: `ADVERSARIAL-TEST`.

#### SIG-adversarial-test-SRC-0209

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0209 / V1 lines 836-838

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Construct difficult cases intentionally.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-adversarial-test-SRC-0246

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0246 / V1 lines 962-964

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Use intentionally difficult inputs.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADVERSARIALLY-ROBUST

ID: `LEX-adversarially-robust`. Roles: modifier_surface, status.

Source forms: `ADVERSARIALLY ROBUST`, `adversarially robust`.

#### SIG-adversarially-robust-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "adversarially robust" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-adversarially-robust-SRC-0546

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0546 / V1 lines 2771-2773

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Answer survived deliberately difficult admissible challenges.

Assessment dimension: robustness_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADVERSARIALLY-TEST

ID: `LEX-adversarially-test`. Roles: modifier_surface.

Source forms: `adversarially test`.

#### SIG-adversarially-test-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "adversarially test" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ADVISORY

ID: `LEX-advisory`. Roles: modifier_surface.

Source forms: `advisory`.

#### SIG-advisory-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "advisory" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AGGRESSIVE

ID: `LEX-aggressive`. Roles: modifier_surface.

Source forms: `aggressive`.

#### SIG-aggressive-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "aggressive" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AGGRESSIVELY-RESOLVE

ID: `LEX-aggressively-resolve`. Roles: modifier_surface.

Source forms: `aggressively resolve`.

#### SIG-aggressively-resolve-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "aggressively resolve" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALIGN

ID: `LEX-align`. Roles: specialized_operator.

Source forms: `ALIGN`.

#### SIG-align-SRC-0157

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0157 / V1 lines 647-649

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Establish mappings.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALL

ID: `LEX-all`. Roles: modifier_surface.

Source forms: `all`.

#### SIG-all-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "all" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALL-ADMISSIBLE-WORK-REQUIRED-FOR-CLOSURE

ID: `LEX-all-admissible-work-required-for-closure`. Roles: modifier_surface.

Source forms: `all admissible work required for closure`.

#### SIG-all-admissible-work-required-for-closure-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "all admissible work required for closure" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALL-RELEVANT

ID: `LEX-all-relevant`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `all relevant`.

#### SIG-all-relevant-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "all relevant" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-all-relevant-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "all relevant" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-all-relevant-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "all relevant" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALTERNATE-METHOD

ID: `LEX-alternate-method`. Roles: modifier_surface.

Source forms: `alternate method`.

#### SIG-alternate-method-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "alternate method" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALTERNATE-PROMPT

ID: `LEX-alternate-prompt`. Roles: modifier_surface.

Source forms: `alternate prompt`.

#### SIG-alternate-prompt-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "alternate prompt" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALTERNATE-REPRESENTATION

ID: `LEX-alternate-representation`. Roles: modifier_surface.

Source forms: `alternate representation`.

#### SIG-alternate-representation-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "alternate representation" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ALWAYS

ID: `LEX-always`. Roles: modifier_surface.

Source forms: `always`.

#### SIG-always-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "always" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ANALOGIZE

ID: `LEX-analogize`. Roles: communication_operator, specialized_operator.

Source forms: `ANALOGIZE`.

#### SIG-analogize-SRC-0147

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0147 / V1 lines 607-609

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Generate structurally related cases from another domain.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-analogize-SRC-0454

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0454 / V1 lines 1673-1675

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Use structural correspondence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ANALYZE

ID: `LEX-analyze`. Roles: macro, modifier_surface.

Source forms: `ANALYZE`, `analyze`.

#### SIG-analyze-SRC-0474

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0474 / V1 lines 1734-1737

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: INSPECT -> SPLIT -> REPRESENT -> COMPARE -> INFER

Macro source expression: `INSPECT -> SPLIT -> REPRESENT -> COMPARE -> INFER`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-analyze-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "analyze" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ANSWER

ID: `LEX-answer`. Roles: communication_operator.

Source forms: `ANSWER`.

#### SIG-answer-SRC-0446

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0446 / V1 lines 1649-1651

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Return a response.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ANSWER-ONLY

ID: `LEX-answer-only`. Roles: modifier_surface.

Source forms: `answer only`.

#### SIG-answer-only-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "answer only" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### APPARENTLY-UNPRECEDENTED

ID: `LEX-apparently-unprecedented`. Roles: context_bound_attribute_surface.

Source forms: `apparently unprecedented`.

#### SIG-apparently-unprecedented-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "apparently unprecedented" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### APPLY

ID: `LEX-apply`. Roles: specialized_operator.

Source forms: `APPLY`.

#### SIG-apply-SRC-0346

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0346 / V1 lines 1307-1309

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Apply a transformation or rule.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### APPROXIMATE

ID: `LEX-approximate`. Roles: modifier_surface, specialized_operator.

Source forms: `APPROXIMATE`, `approximate`.

#### SIG-approximate-SRC-0190

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0190 / V1 lines 756-758

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Substitute a sufficiently close representation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-approximate-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "approximate" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-approximate-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "approximate" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ARCHIVE

ID: `LEX-archive`. Roles: specialized_operator.

Source forms: `ARCHIVE`.

#### SIG-archive-SRC-0439

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0439 / V1 lines 1622-1624

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Preserve inactive state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ARGUE

ID: `LEX-argue`. Roles: communication_operator.

Source forms: `ARGUE`.

#### SIG-argue-SRC-0469

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0469 / V1 lines 1718-1720

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Construct supporting reasoning.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASK-BEFORE-EVERY-STEP

ID: `LEX-ask-before-every-step`. Roles: modifier_surface.

Source forms: `ask before every step`.

#### SIG-ask-before-every-step-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "ask before every step" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASSERTION-FORCE

ID: `LEX-assertion-force`. Roles: semantic_policy_or_attribute.

Source forms: `ASSERTION FORCE`.

#### SIG-assertion-force-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate assertion force using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASSERTION-STRENGTH-IS-OUTPUT-STATUS-DERIVED-FROM-EVIDENCE.

ID: `LEX-assertion-strength-is-output-status-derived-from-evidence`. Roles: context_bound_attribute_surface.

Source forms: `Assertion strength is output status derived from evidence.`.

#### SIG-assertion-strength-is-output-status-derived-from-evidence-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "Assertion strength is output status derived from evidence." on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASSERTIVE

ID: `LEX-assertive`. Roles: modifier_surface.

Source forms: `assertive`.

#### SIG-assertive-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "assertive" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASSESS

ID: `LEX-assess`. Roles: specialized_operator.

Source forms: `ASSESS`.

#### SIG-assess-SRC-0270

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0270 / V1 lines 1050-1052

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Determine quality or suitability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASSUME

ID: `LEX-assume`. Roles: modifier_surface, proposed_procedure.

Source forms: `ASSUME`, `assume`.

#### SIG-assume-P-source-macro-binding

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Introduce a proposition as an explicit conditional premise or scenario, not as observed truth; preserve alternatives when it can change the result.

Evidence required: Apply the common contract to the explicitly bound target, property and scope.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Closure rule: Use the common contract and preserve remaining obligations.

Concrete instance: Assume failure only inside a premortem branch while retaining the actual observed project status.

Abstract principle: Interpret intent as a scoped task contract; preserve materially different parses.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-assume-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "assume" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ASSUMPTION-CHALLENGE

ID: `LEX-assumption-challenge`. Roles: specialized_operator.

Source forms: `ASSUMPTION-CHALLENGE`.

#### SIG-assumption-challenge-SRC-0203

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0203 / V1 lines 818-820

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Remove or invert assumptions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AT-A-GLANCE

ID: `LEX-at-a-glance`. Roles: modifier_surface.

Source forms: `at-a-glance`.

#### SIG-at-a-glance-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "at-a-glance" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ATOMIC

ID: `LEX-atomic`. Roles: modifier_surface.

Source forms: `atomic`.

#### SIG-atomic-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "atomic" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-atomic-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "atomic" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ATOMIZE

ID: `LEX-atomize`. Roles: specialized_operator.

Source forms: `ATOMIZE`.

#### SIG-atomize-SRC-0121

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0121 / V1 lines 514-516

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Decompose to the smallest unit required by the objective.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ATTEST

ID: `LEX-attest`. Roles: specialized_operator.

Source forms: `ATTEST`.

#### SIG-attest-SRC-0387

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0387 / V1 lines 1451-1453

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Formally state witnessed status when authorized.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ATTRIBUTE

ID: `LEX-attribute`. Roles: specialized_operator.

Source forms: `ATTRIBUTE`.

#### SIG-attribute-SRC-0185

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0185 / V1 lines 741-743

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Assign an effect to a cause or source.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUDIT

ID: `LEX-audit`. Roles: macro, specialized_operator.

Source forms: `AUDIT`.

#### SIG-audit-SRC-0384

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0384 / V1 lines 1442-1444

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Systematically trace requirements to evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-audit-SRC-0483

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0483 / V1 lines 1770-1773

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: COMPILE REQUIREMENTS -> INSPECT -> TRACE -> TEST -> CHALLENGE -> REPORT

Macro source expression: `COMPILE REQUIREMENTS -> INSPECT -> TRACE -> TEST -> CHALLENGE -> REPORT`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUDIT-LOG-READ

ID: `LEX-audit-log-read`. Roles: specialized_operator.

Source forms: `AUDIT-LOG-READ`.

#### SIG-audit-log-read-SRC-0074

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0074 / V1 lines 369-373

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Inspect historical records of transitions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUGMENT

ID: `LEX-augment`. Roles: specialized_operator.

Source forms: `AUGMENT`.

#### SIG-augment-SRC-0337

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0337 / V1 lines 1268-1270

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Add useful capability or information.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUTONOMOUS-ON-REVERSIBLE-WORK

ID: `LEX-autonomous-on-reversible-work`. Roles: modifier_surface.

Source forms: `autonomous on reversible work`.

#### SIG-autonomous-on-reversible-work-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "autonomous on reversible work" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUTONOMOUS-UNTIL-MATERIAL-BOUNDARY

ID: `LEX-autonomous-until-material-boundary`. Roles: modifier_surface.

Source forms: `autonomous until material boundary`.

#### SIG-autonomous-until-material-boundary-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "autonomous until material boundary" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUTONOMOUS-WITHIN-BOUNDS

ID: `LEX-autonomous-within-bounds`. Roles: modifier_surface.

Source forms: `autonomous within bounds`.

#### SIG-autonomous-within-bounds-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "autonomous within bounds" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUTONOMOUS-WITHIN-DECLARED-BOUNDS

ID: `LEX-autonomous-within-declared-bounds`. Roles: modifier_surface.

Source forms: `autonomous within declared bounds`.

#### SIG-autonomous-within-declared-bounds-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "autonomous within declared bounds" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AUTONOMY

ID: `LEX-autonomy`. Roles: semantic_policy_or_attribute.

Source forms: `AUTONOMY`.

#### SIG-autonomy-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate autonomy using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### AVOID

ID: `LEX-avoid`. Roles: constraint_surface.

Source forms: `avoid`.

#### SIG-avoid-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "avoid" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BACKCAST

ID: `LEX-backcast`. Roles: specialized_operator.

Source forms: `BACKCAST`.

#### SIG-backcast-SRC-0197

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0197 / V1 lines 777-779

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer prior conditions from a later state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BACKTRACK

ID: `LEX-backtrack`. Roles: control_operator.

Source forms: `BACKTRACK`.

#### SIG-backtrack-SRC-0409

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0409 / V1 lines 1530-1532

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Return to a prior decision.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BALANCED

ID: `LEX-balanced`. Roles: modifier_surface.

Source forms: `balanced`.

#### SIG-balanced-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "balanced" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BALLPARK

ID: `LEX-ballpark`. Roles: modifier_surface.

Source forms: `ballpark`.

#### SIG-ballpark-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "ballpark" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BARE-MINIMUM

ID: `LEX-bare-minimum`. Roles: modifier_surface.

Source forms: `bare minimum`.

#### SIG-bare-minimum-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "bare minimum" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BARRIER

ID: `LEX-barrier`. Roles: control_operator.

Source forms: `BARRIER`.

#### SIG-barrier-SRC-0406

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0406 / V1 lines 1521-1523

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Require multiple prerequisites.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BASIC

ID: `LEX-basic`. Roles: modifier_surface.

Source forms: `basic`.

#### SIG-basic-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "basic" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BATCH

ID: `LEX-batch`. Roles: control_operator.

Source forms: `BATCH`.

#### SIG-batch-SRC-0419

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0419 / V1 lines 1560-1562

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Group operations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BE-CERTAIN

ID: `LEX-be-certain`. Roles: modifier_surface.

Source forms: `be certain`.

#### SIG-be-certain-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "be certain" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BENCHMARK

ID: `LEX-benchmark`. Roles: specialized_operator.

Source forms: `BENCHMARK`.

#### SIG-benchmark-SRC-0230

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0230 / V1 lines 914-916

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Measure using reference procedures.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-benchmark-SRC-0275

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0275 / V1 lines 1065-1067

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Compare against references.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BIND

ID: `LEX-bind`. Roles: specialized_operator.

Source forms: `BIND`.

#### SIG-bind-SRC-0026

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0026 / V1 lines 215-217

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Associate a variable or role with a particular value.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BINDING-FORCE

ID: `LEX-binding-force`. Roles: semantic_policy_or_attribute.

Source forms: `BINDING FORCE`.

#### SIG-binding-force-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate binding force using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BLOCKED

ID: `LEX-blocked`. Roles: status.

Source forms: `BLOCKED`.

#### SIG-blocked-SRC-0550

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0550 / V1 lines 2783-2785

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Resolution path exists but cannot presently be executed.

Assessment dimension: resolution_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BOUND

ID: `LEX-bound`. Roles: specialized_operator.

Source forms: `BOUND`.

#### SIG-bound-SRC-0021

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0021 / V1 lines 200-202

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Establish limits.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BOUNDARY-TEST

ID: `LEX-boundary-test`. Roles: specialized_operator.

Source forms: `BOUNDARY-TEST`.

#### SIG-boundary-test-SRC-0213

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0213 / V1 lines 848-850

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Test near regime changes and thresholds.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BRAINSTORM

ID: `LEX-brainstorm`. Roles: specialized_operator.

Source forms: `BRAINSTORM`.

#### SIG-brainstorm-SRC-0135

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0135 / V1 lines 571-573

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Generate with relaxed early filtering.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BRANCH

ID: `LEX-branch`. Roles: context_specific_operator, control_operator, specialized_operator.

Source forms: `BRANCH`.

#### SIG-branch-P-control

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Execute different continuations according to an evaluated condition.

Evidence required: Branch condition, selected path and execution trace.

Status rule: Path dispatched separately from path success.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Use different parsers depending on a known input format.

Abstract principle: Change sequencing, branching, iteration or coordination while preserving semantic and effect constraints.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-branch-P-uncertainty

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Preserve conditional results that depend on an unresolved material discriminator.

Evidence required: Live alternatives, conditions and required differing actions.

Status rule: BRANCHED, not selected by default.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Keep two purchase recommendations conditional on utilization.

Abstract principle: Return an authorized choice, robust shared option or explicit conditional alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-branch-SRC-0128

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0128 / V1 lines 535-537

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Preserve condition-dependent alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-branch-SRC-0305

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0305 / V1 lines 1161-1163

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Retain conditional alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-branch-SRC-0400

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0400 / V1 lines 1503-1505

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Use condition-dependent paths.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BRANCH-CLOSE

ID: `LEX-branch-close`. Roles: specialized_operator.

Source forms: `BRANCH-CLOSE`.

#### SIG-branch-close-SRC-0444

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0444 / V1 lines 1637-1646

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Close with explicit conditional results.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BRANCH-WHENEVER-MATERIAL

ID: `LEX-branch-whenever-material`. Roles: modifier_surface.

Source forms: `branch whenever material`.

#### SIG-branch-whenever-material-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "branch whenever material" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BRANCHED

ID: `LEX-branched`. Roles: status.

Source forms: `BRANCHED`.

#### SIG-branched-SRC-0547

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0547 / V1 lines 2774-2776

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Multiple outcomes remain under explicit conditions.

Assessment dimension: resolution_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BREADTH

ID: `LEX-breadth`. Roles: execution_modifier.

Source forms: `BREADTH`.

#### SIG-breadth-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate breadth using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BRIEF

ID: `LEX-brief`. Roles: modifier_surface.

Source forms: `brief`.

#### SIG-brief-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "brief" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BROAD

ID: `LEX-broad`. Roles: modifier_surface.

Source forms: `broad`.

#### SIG-broad-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "broad" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BROAD-EXPLORATION

ID: `LEX-broad-exploration`. Roles: modifier_surface.

Source forms: `broad exploration`.

#### SIG-broad-exploration-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "broad exploration" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### BUDGET

ID: `LEX-budget`. Roles: control_operator.

Source forms: `BUDGET`.

#### SIG-budget-SRC-0417

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0417 / V1 lines 1554-1556

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Limit resources.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CALCULATE

ID: `LEX-calculate`. Roles: specialized_operator.

Source forms: `CALCULATE`.

#### SIG-calculate-SRC-0182

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0182 / V1 lines 732-734

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Produce numerical or symbolic results.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CALIBRATE

ID: `LEX-calibrate`. Roles: specialized_operator.

Source forms: `CALIBRATE`.

#### SIG-calibrate-SRC-0326

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0326 / V1 lines 1235-1237

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Align against known references.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CALL

ID: `LEX-call`. Roles: specialized_operator.

Source forms: `CALL`.

#### SIG-call-SRC-0366

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0366 / V1 lines 1367-1369

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Invoke a function or endpoint.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CANARY

ID: `LEX-canary`. Roles: specialized_operator.

Source forms: `CANARY`.

#### SIG-canary-SRC-0240

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0240 / V1 lines 944-946

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test in limited scope before expansion.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CANONICAL

ID: `LEX-canonical`. Roles: modifier_surface.

Source forms: `canonical`.

#### SIG-canonical-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "canonical" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CANONICAL-AND-UNAMBIGUOUS

ID: `LEX-canonical-and-unambiguous`. Roles: modifier_surface.

Source forms: `canonical and unambiguous`.

#### SIG-canonical-and-unambiguous-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "canonical and unambiguous" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CANONICAL-LEXICAL-OR-NUMERIC-ORDERING

ID: `LEX-canonical-lexical-or-numeric-ordering`. Roles: modifier_surface.

Source forms: `canonical lexical or numeric ordering`.

#### SIG-canonical-lexical-or-numeric-ordering-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "canonical lexical or numeric ordering" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CANONICALIZE

ID: `LEX-canonicalize`. Roles: specialized_operator.

Source forms: `CANONICALIZE`.

#### SIG-canonicalize-SRC-0103

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0103 / V1 lines 458-460

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Select one deterministic representative from an equivalence class.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CAREFUL

ID: `LEX-careful`. Roles: modifier_surface.

Source forms: `careful`.

#### SIG-careful-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "careful" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-careful-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "careful" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CASE-SPLIT

ID: `LEX-case-split`. Roles: specialized_operator.

Source forms: `CASE-SPLIT`.

#### SIG-case-split-SRC-0127

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0127 / V1 lines 532-534

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Create explicit paths for differing conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CATALOG

ID: `LEX-catalog`. Roles: specialized_operator.

Source forms: `CATALOG`.

#### SIG-catalog-SRC-0068

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0068 / V1 lines 351-353

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Inventory plus systematic identifiers or metadata.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CATEGORIZE

ID: `LEX-categorize`. Roles: specialized_operator.

Source forms: `CATEGORIZE`.

#### SIG-categorize-SRC-0168

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0168 / V1 lines 680-682

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Organize conceptually.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CAUSAL-DEPTH

ID: `LEX-causal-depth`. Roles: semantic_policy_or_attribute.

Source forms: `CAUSAL DEPTH`.

#### SIG-causal-depth-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate causal depth using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CAUSAL-GRAPH

ID: `LEX-causal-graph`. Roles: specialized_operator.

Source forms: `CAUSAL-GRAPH`.

#### SIG-causal-graph-SRC-0089

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0089 / V1 lines 416-418

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent hypothesized causal relationships.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CAUSAL-MODEL

ID: `LEX-causal-model`. Roles: modifier_surface.

Source forms: `causal model`.

#### SIG-causal-model-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "causal model" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CAUTIOUS

ID: `LEX-cautious`. Roles: modifier_surface.

Source forms: `cautious`.

#### SIG-cautious-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "cautious" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CERTAINLY

ID: `LEX-certainly`. Roles: context_bound_attribute_surface.

Source forms: `certainly`.

#### SIG-certainly-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "certainly" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CERTIFICATE-BACKED

ID: `LEX-certificate-backed`. Roles: modifier_surface.

Source forms: `certificate-backed`.

#### SIG-certificate-backed-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "certificate-backed" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CERTIFY

ID: `LEX-certify`. Roles: specialized_operator.

Source forms: `CERTIFY`.

#### SIG-certify-SRC-0386

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0386 / V1 lines 1448-1450

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Assign authoritative verified status when authorized.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHAIN

ID: `LEX-chain`. Roles: control_operator.

Source forms: `CHAIN`.

#### SIG-chain-SRC-0393

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0393 / V1 lines 1482-1484

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Feed outputs into later operations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHALLENGE

ID: `LEX-challenge`. Roles: family, modifier_surface.

Source forms: `CHALLENGE`, `challenge`.

#### SIG-challenge-SRC-0200

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0200 / V1 lines 798-811

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Actively search for conditions under which a candidate fails.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-challenge-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "challenge" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHAOS-TEST

ID: `LEX-chaos-test`. Roles: specialized_operator.

Source forms: `CHAOS-TEST`.

#### SIG-chaos-test-SRC-0247

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0247 / V1 lines 965-967

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Inject failures to inspect resilience.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHECK

ID: `LEX-check`. Roles: modifier_surface, specialized_operator.

Source forms: `CHECK`, `check`.

#### SIG-check-SRC-0223

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0223 / V1 lines 884-886

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Evaluate a condition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-check-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "check" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHECKED

ID: `LEX-checked`. Roles: status.

Source forms: `CHECKED`.

#### SIG-checked-SRC-0534

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0534 / V1 lines 2735-2737

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: At least one criterion was evaluated.

Assessment dimension: check_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHECKPOINT

ID: `LEX-checkpoint`. Roles: control_operator.

Source forms: `CHECKPOINT`.

#### SIG-checkpoint-SRC-0407

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0407 / V1 lines 1524-1526

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Persist recoverable state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CHOOSE

ID: `LEX-choose`. Roles: specialized_operator.

Source forms: `CHOOSE`.

#### SIG-choose-SRC-0294

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0294 / V1 lines 1128-1130

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Select one or more.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CITE

ID: `LEX-cite`. Roles: communication_operator.

Source forms: `CITE`.

#### SIG-cite-SRC-0464

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0464 / V1 lines 1703-1705

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Attach provenance.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLARIFY

ID: `LEX-clarify`. Roles: specialized_operator.

Source forms: `CLARIFY`.

#### SIG-clarify-SRC-0018

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0018 / V1 lines 191-193

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Reduce ambiguity.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLASSIFY

ID: `LEX-classify`. Roles: specialized_operator.

Source forms: `CLASSIFY`.

#### SIG-classify-SRC-0167

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0167 / V1 lines 677-679

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Assign predefined or derived classes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLEAN

ID: `LEX-clean`. Roles: specialized_operator.

Source forms: `CLEAN`.

#### SIG-clean-SRC-0329

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0329 / V1 lines 1244-1246

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Remove noise or invalid structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLOSE

ID: `LEX-close`. Roles: family.

Source forms: `CLOSE`.

#### SIG-close-SRC-0433

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0433 / V1 lines 1603-1606

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Terminate with justified status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLOSURE-CERTIFIED

ID: `LEX-closure-certified`. Roles: context_bound_attribute_surface.

Source forms: `closure-certified`.

#### SIG-closure-certified-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure-certified" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLOSURE-COMPLETE

ID: `LEX-closure-complete`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `closure-complete`.

#### SIG-closure-complete-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure-complete" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-closure-complete-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure-complete" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-closure-complete-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure-complete" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLOSURE-DEPTH

ID: `LEX-closure-depth`. Roles: modifier_surface.

Source forms: `closure-depth`.

#### SIG-closure-depth-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure-depth" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLOSURE-DIRECTED

ID: `LEX-closure-directed`. Roles: modifier_surface.

Source forms: `closure-directed`.

#### SIG-closure-directed-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure-directed" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLOSURE-OVER-SPEED

ID: `LEX-closure-over-speed`. Roles: modifier_surface.

Source forms: `closure over speed`.

#### SIG-closure-over-speed-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "closure over speed" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CLUSTER

ID: `LEX-cluster`. Roles: specialized_operator.

Source forms: `CLUSTER`.

#### SIG-cluster-SRC-0166

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0166 / V1 lines 674-676

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Discover similarity-based groups.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COARSE

ID: `LEX-coarse`. Roles: modifier_surface.

Source forms: `coarse`.

#### SIG-coarse-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "coarse" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-coarse-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "coarse" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COLLECT

ID: `LEX-collect`. Roles: specialized_operator.

Source forms: `COLLECT`.

#### SIG-collect-SRC-0043

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0043 / V1 lines 270-272

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Accumulate according to an inclusion rule.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMBINE

ID: `LEX-combine`. Roles: specialized_operator.

Source forms: `COMBINE`.

#### SIG-combine-SRC-0333

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0333 / V1 lines 1256-1258

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Join components.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMMIT

ID: `LEX-commit`. Roles: specialized_operator.

Source forms: `COMMIT`.

#### SIG-commit-SRC-0310

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0310 / V1 lines 1176-1189

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Make selection binding for downstream work.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMMITMENT-ONLY-UNDER-INVARIANT-RESULT

ID: `LEX-commitment-only-under-invariant-result`. Roles: modifier_surface.

Source forms: `commitment only under invariant result`.

#### SIG-commitment-only-under-invariant-result-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "commitment only under invariant result" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPARE

ID: `LEX-compare`. Roles: family.

Source forms: `COMPARE`.

#### SIG-compare-SRC-0154

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0154 / V1 lines 637-640

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Determine similarities, differences, equivalences, and discriminators.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPETING-CAUSAL-MODEL-COMPARISON

ID: `LEX-competing-causal-model-comparison`. Roles: modifier_surface.

Source forms: `competing causal model comparison`.

#### SIG-competing-causal-model-comparison-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "competing causal model comparison" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPILE

ID: `LEX-compile`. Roles: family.

Source forms: `COMPILE`.

#### SIG-compile-SRC-0014

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0014 / V1 lines 170-181

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Convert intent into explicit operational structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPLETE

ID: `LEX-complete`. Roles: context_bound_attribute_surface, context_specific_operator, modifier_surface, specialized_operator.

Source forms: `COMPLETE`, `complete`.

#### SIG-complete-P-process

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Finish a process even if the substantive result remains branched or unresolved.

Evidence required: Termination record plus explicit unresolved obligations.

Status rule: Process finished, not necessarily solved.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: End the allocated run and preserve its unresolved branches.

Abstract principle: Change sequencing, branching, iteration or coordination while preserving semantic and effect constraints.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-complete-P-requirements

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Declare required deliverables complete only when their scoped checks meet the acceptance rule.

Evidence required: Requirement coverage and actual assessments.

Status rule: Requirements complete within scope.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Complete all requested export formats.

Abstract principle: Stop the current work with a scoped assessment, explicit residuals and reopening conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-complete-SRC-0435

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0435 / V1 lines 1610-1612

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Satisfy declared completion criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-complete-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "complete" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-complete-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "complete" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPLETENESS

ID: `LEX-completeness`. Roles: semantic_policy_or_attribute.

Source forms: `COMPLETENESS`.

#### SIG-completeness-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate completeness using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPREHENSIVE

ID: `LEX-comprehensive`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `comprehensive`.

#### SIG-comprehensive-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "comprehensive" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-comprehensive-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "comprehensive" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-comprehensive-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "comprehensive" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-comprehensive-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "comprehensive" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPRESS

ID: `LEX-compress`. Roles: specialized_operator.

Source forms: `COMPRESS`.

#### SIG-compress-SRC-0112

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0112 / V1 lines 485-487

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Reduce representation size while preserving declared information.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-compress-SRC-0318

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0318 / V1 lines 1211-1213

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Reduce representation size.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COMPUTE

ID: `LEX-compute`. Roles: specialized_operator.

Source forms: `COMPUTE`.

#### SIG-compute-SRC-0183

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0183 / V1 lines 735-737

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Execute an algorithmic transformation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONCISE

ID: `LEX-concise`. Roles: modifier_surface.

Source forms: `concise`.

#### SIG-concise-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "concise" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONCISION

ID: `LEX-concision`. Roles: execution_modifier.

Source forms: `CONCISION`.

#### SIG-concision-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate concision using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONCRETE-INSTANCE

ID: `LEX-concrete-instance`. Roles: modifier_surface.

Source forms: `concrete instance`.

#### SIG-concrete-instance-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "concrete instance" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONCRETE-INSTANCE-<->-ABSTRACT-PRINCIPLE

ID: `LEX-concrete-instance-abstract-principle`. Roles: modifier_surface.

Source forms: `concrete instance <-> abstract principle`.

#### SIG-concrete-instance-abstract-principle-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "concrete instance <-> abstract principle" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONCRETIZE

ID: `LEX-concretize`. Roles: specialized_operator.

Source forms: `CONCRETIZE`.

#### SIG-concretize-SRC-0106

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0106 / V1 lines 467-469

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Introduce specific values, examples, mechanisms, or instances.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONFIGURE

ID: `LEX-configure`. Roles: specialized_operator.

Source forms: `CONFIGURE`.

#### SIG-configure-SRC-0362

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0362 / V1 lines 1355-1357

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Set operational parameters.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONFIRM

ID: `LEX-confirm`. Roles: specialized_operator.

Source forms: `CONFIRM`.

#### SIG-confirm-SRC-0376

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0376 / V1 lines 1418-1420

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Establish presence of an expected property.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSERVATISM

ID: `LEX-conservatism`. Roles: semantic_policy_or_attribute.

Source forms: `CONSERVATISM`.

#### SIG-conservatism-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate conservatism using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSERVATIVE

ID: `LEX-conservative`. Roles: modifier_surface.

Source forms: `conservative`.

#### SIG-conservative-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "conservative" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-conservative-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "conservative" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSIDER-EVERYTHING

ID: `LEX-consider-everything`. Roles: modifier_surface.

Source forms: `consider everything`.

#### SIG-consider-everything-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "consider everything" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSIDER-LITERALLY-EVERYTHING

ID: `LEX-consider-literally-everything`. Roles: modifier_surface.

Source forms: `consider literally everything`.

#### SIG-consider-literally-everything-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "consider literally everything" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSIDERED

ID: `LEX-considered`. Roles: modifier_surface.

Source forms: `considered`.

#### SIG-considered-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "considered" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSTRAIN

ID: `LEX-constrain`. Roles: specialized_operator.

Source forms: `CONSTRAIN`.

#### SIG-constrain-SRC-0022

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0022 / V1 lines 203-205

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Reduce admissible operations or outputs.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONSTRAINT-SYSTEM

ID: `LEX-constraint-system`. Roles: specialized_operator.

Source forms: `CONSTRAINT-SYSTEM`.

#### SIG-constraint-system-SRC-0098

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0098 / V1 lines 443-445

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent admissibility through explicit constraints.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONTINUE

ID: `LEX-continue`. Roles: control_operator.

Source forms: `CONTINUE`.

#### SIG-continue-SRC-0411

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0411 / V1 lines 1536-1538

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Proceed from current state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONTRAST

ID: `LEX-contrast`. Roles: specialized_operator.

Source forms: `CONTRAST`.

#### SIG-contrast-SRC-0155

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0155 / V1 lines 641-643

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Emphasize differences.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONTRIBUTING-FACTOR

ID: `LEX-contributing-factor`. Roles: modifier_surface.

Source forms: `contributing factor`.

#### SIG-contributing-factor-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "contributing factor" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONTROL

ID: `LEX-control`. Roles: family.

Source forms: `CONTROL`.

#### SIG-control-SRC-0391

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0391 / V1 lines 1475-1478

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Govern execution topology.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONVENTIONAL

ID: `LEX-conventional`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `conventional`.

#### SIG-conventional-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "conventional" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-conventional-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "conventional" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONVENTIONAL-ONLY

ID: `LEX-conventional-only`. Roles: modifier_surface.

Source forms: `conventional-only`.

#### SIG-conventional-only-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "conventional-only" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONVERGENT-EVIDENCE-ACROSS-DISTINCT-FAILURE-MODES

ID: `LEX-convergent-evidence-across-distinct-failure-modes`. Roles: modifier_surface.

Source forms: `convergent evidence across distinct failure modes`.

#### SIG-convergent-evidence-across-distinct-failure-modes-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "convergent evidence across distinct failure modes" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONVERSATIONAL

ID: `LEX-conversational`. Roles: modifier_surface.

Source forms: `conversational`.

#### SIG-conversational-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "conversational" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CONVERT

ID: `LEX-convert`. Roles: specialized_operator.

Source forms: `CONVERT`.

#### SIG-convert-SRC-0323

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0323 / V1 lines 1226-1228

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Change format, type, schema, or unit.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COPY

ID: `LEX-copy`. Roles: specialized_operator.

Source forms: `COPY`.

#### SIG-copy-SRC-0353

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0353 / V1 lines 1328-1330

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Duplicate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COPYEDIT

ID: `LEX-copyedit`. Roles: communication_operator.

Source forms: `COPYEDIT`.

#### SIG-copyedit-SRC-0460

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0460 / V1 lines 1691-1693

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Improve clarity and consistency.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CORRECT

ID: `LEX-correct`. Roles: specialized_operator.

Source forms: `CORRECT`.

#### SIG-correct-SRC-0254

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0254 / V1 lines 996-998

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Replace identified error.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CORRELATE

ID: `LEX-correlate`. Roles: specialized_operator.

Source forms: `CORRELATE`.

#### SIG-correlate-SRC-0162

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0162 / V1 lines 662-664

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Assess association.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CORRELATION

ID: `LEX-correlation`. Roles: modifier_surface.

Source forms: `correlation`.

#### SIG-correlation-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "correlation" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COST

ID: `LEX-cost`. Roles: specialized_operator.

Source forms: `COST`.

#### SIG-cost-SRC-0279

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0279 / V1 lines 1077-1079

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Estimate resource use.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COSTLY-ROLLBACK

ID: `LEX-costly-rollback`. Roles: modifier_surface.

Source forms: `costly rollback`.

#### SIG-costly-rollback-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "costly rollback" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COUNT

ID: `LEX-count`. Roles: specialized_operator.

Source forms: `COUNT`.

#### SIG-count-SRC-0061

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0061 / V1 lines 330-332

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Determine cardinality.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COUNTERARGUE

ID: `LEX-counterargue`. Roles: communication_operator.

Source forms: `COUNTERARGUE`.

#### SIG-counterargue-SRC-0470

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0470 / V1 lines 1721-1723

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Construct opposing reasoning.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COUNTEREXAMPLE-SEEK

ID: `LEX-counterexample-seek`. Roles: specialized_operator.

Source forms: `COUNTEREXAMPLE-SEEK`.

#### SIG-counterexample-seek-SRC-0204

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0204 / V1 lines 821-823

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Search specifically for defeating instances.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COUNTEREXAMPLE-SEEKING

ID: `LEX-counterexample-seeking`. Roles: modifier_surface.

Source forms: `counterexample-seeking`.

#### SIG-counterexample-seeking-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "counterexample-seeking" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COUNTERFACTUAL

ID: `LEX-counterfactual`. Roles: specialized_operator.

Source forms: `COUNTERFACTUAL`.

#### SIG-counterfactual-SRC-0211

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0211 / V1 lines 842-844

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Change conditions and examine consequences.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### COUNTERFACTUALIZE

ID: `LEX-counterfactualize`. Roles: specialized_operator.

Source forms: `COUNTERFACTUALIZE`.

#### SIG-counterfactualize-SRC-0146

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0146 / V1 lines 604-606

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Generate alternate worlds by changing conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CRAWL

ID: `LEX-crawl`. Roles: specialized_operator.

Source forms: `CRAWL`.

#### SIG-crawl-SRC-0052

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0052 / V1 lines 297-299

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Traverse linked information spaces systematically.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CREATE

ID: `LEX-create`. Roles: specialized_operator.

Source forms: `CREATE`.

#### SIG-create-SRC-0347

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0347 / V1 lines 1310-1312

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Produce a new object.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CREATIVE

ID: `LEX-creative`. Roles: modifier_surface.

Source forms: `creative`.

#### SIG-creative-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "creative" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CREATIVITY

ID: `LEX-creativity`. Roles: execution_modifier.

Source forms: `CREATIVITY`.

#### SIG-creativity-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate creativity using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CRITICALLY-INSPECT

ID: `LEX-critically-inspect`. Roles: modifier_surface.

Source forms: `critically inspect`.

#### SIG-critically-inspect-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "critically inspect" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CRITIQUE

ID: `LEX-critique`. Roles: specialized_operator.

Source forms: `CRITIQUE`.

#### SIG-critique-SRC-0201

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0201 / V1 lines 812-814

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Identify weaknesses.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CROSS-CHECK

ID: `LEX-cross-check`. Roles: specialized_operator.

Source forms: `CROSS-CHECK`.

#### SIG-cross-check-SRC-0379

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0379 / V1 lines 1427-1429

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Verify using another route.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CROSS-CHECKED

ID: `LEX-cross-checked`. Roles: status.

Source forms: `CROSS-CHECKED`.

#### SIG-cross-checked-SRC-0538

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0538 / V1 lines 2747-2749

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: An additional evidence path agreed.

Assessment dimension: verification_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CROSS-REFERENCE

ID: `LEX-cross-reference`. Roles: specialized_operator.

Source forms: `CROSS-REFERENCE`.

#### SIG-cross-reference-SRC-0163

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0163 / V1 lines 665-667

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Relate information across sources.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### CURSORY

ID: `LEX-cursory`. Roles: modifier_surface.

Source forms: `cursory`.

#### SIG-cursory-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "cursory" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DAG

ID: `LEX-dag`. Roles: specialized_operator.

Source forms: `DAG`.

#### SIG-dag-SRC-0095

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0095 / V1 lines 434-436

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent directed acyclic dependency relationships.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DANGEROUS-PSEUDO-STRENGTH-MODIFIERS

ID: `LEX-dangerous-pseudo-strength-modifiers`. Roles: semantic_policy_or_attribute.

Source forms: `DANGEROUS PSEUDO STRENGTH MODIFIERS`.

#### SIG-dangerous-pseudo-strength-modifiers-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate dangerous pseudo strength modifiers using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEBATE

ID: `LEX-debate`. Roles: communication_operator.

Source forms: `DEBATE`.

#### SIG-debate-SRC-0471

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0471 / V1 lines 1724-1726

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Present competing arguments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEBUG

ID: `LEX-debug`. Roles: macro, specialized_operator.

Source forms: `DEBUG`.

#### SIG-debug-SRC-0266

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0266 / V1 lines 1032-1034

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Locate and repair cause of incorrect behavior.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-debug-SRC-0481

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0481 / V1 lines 1762-1765

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: REPRODUCE -> TRACE -> ISOLATE -> HYPOTHESIZE -> TEST -> REPAIR -> RETEST

Macro source expression: `REPRODUCE -> TRACE -> ISOLATE -> HYPOTHESIZE -> TEST -> REPAIR -> RETEST`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DECIDE

ID: `LEX-decide`. Roles: macro, specialized_operator.

Source forms: `DECIDE`.

#### SIG-decide-SRC-0295

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0295 / V1 lines 1131-1133

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Commit under a decision rule.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-decide-SRC-0480

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0480 / V1 lines 1758-1761

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: COMPILE -> EXPAND -> EVALUATE -> TEST MATERIAL DISTINCTIONS -> SELECT

Macro source expression: `COMPILE -> EXPAND -> EVALUATE -> TEST MATERIAL DISTINCTIONS -> SELECT`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DECISION-TREE

ID: `LEX-decision-tree`. Roles: specialized_operator.

Source forms: `DECISION-TREE`.

#### SIG-decision-tree-SRC-0088

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0088 / V1 lines 413-415

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent conditional outcomes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DECISIVE

ID: `LEX-decisive`. Roles: modifier_surface.

Source forms: `decisive`.

#### SIG-decisive-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "decisive" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DECLARE

ID: `LEX-declare`. Roles: specialized_operator.

Source forms: `DECLARE`.

#### SIG-declare-SRC-0016

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0016 / V1 lines 185-187

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: State a convention, assumption, variable, policy, or value explicitly.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DECOMPOSE

ID: `LEX-decompose`. Roles: specialized_operator.

Source forms: `DECOMPOSE`.

#### SIG-decompose-SRC-0116

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0116 / V1 lines 499-501

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Break a problem into subproblems.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DECOUPLE

ID: `LEX-decouple`. Roles: specialized_operator.

Source forms: `DECOUPLE`.

#### SIG-decouple-SRC-0130

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0130 / V1 lines 541-545

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Remove an unnecessary dependency.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEDUCE

ID: `LEX-deduce`. Roles: specialized_operator.

Source forms: `DEDUCE`.

#### SIG-deduce-SRC-0178

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0178 / V1 lines 720-722

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `INFER`.

Transition or retained definition: Derive conclusions entailed by premises.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEDUPLICATE

ID: `LEX-deduplicate`. Roles: specialized_operator.

Source forms: `DEDUPLICATE`.

#### SIG-deduplicate-SRC-0164

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0164 / V1 lines 668-670

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Collapse actual duplicates.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-deduplicate-SRC-0330

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0330 / V1 lines 1247-1249

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Collapse proven duplicates.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEEP

ID: `LEX-deep`. Roles: modifier_surface.

Source forms: `deep`.

#### SIG-deep-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deep" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEFER

ID: `LEX-defer`. Roles: context_specific_operator, control_operator, specialized_operator.

Source forms: `DEFER`.

#### SIG-defer-P-control

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Suspend or reschedule work without promising an unavailable scheduler.

Evidence required: Preserved work state and actual scheduling receipt when applicable.

Status rule: Paused or scheduled only as observed.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Defer an operation at a permission boundary.

Abstract principle: Change sequencing, branching, iteration or coordination while preserving semantic and effect constraints.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-defer-P-decision

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Postpone a commitment while preserving live alternatives and unresolved obligations.

Evidence required: Stored alternatives and trigger for reconsideration.

Status rule: Deferred decision with explicit residual state.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Defer vendor selection until required quotations arrive.

Abstract principle: Return an authorized choice, robust shared option or explicit conditional alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-defer-SRC-0306

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0306 / V1 lines 1164-1166

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Postpone selection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-defer-SRC-0413

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0413 / V1 lines 1542-1544

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Postpone.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-defer-SRC-0443

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0443 / V1 lines 1634-1636

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Stop current work while preserving unresolved state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEFINE

ID: `LEX-define`. Roles: communication_operator, specialized_operator.

Source forms: `DEFINE`.

#### SIG-define-SRC-0015

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0015 / V1 lines 182-184

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Assign operational meaning.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-define-SRC-0449

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0449 / V1 lines 1658-1660

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `COMPILE`.

Transition or retained definition: Assign meaning.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEFINITELY

ID: `LEX-definitely`. Roles: context_bound_attribute_surface.

Source forms: `definitely`.

#### SIG-definitely-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "definitely" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DELEGATE

ID: `LEX-delegate`. Roles: control_operator.

Source forms: `DELEGATE`.

#### SIG-delegate-SRC-0403

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0403 / V1 lines 1512-1514

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Assign work elsewhere.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DELETE

ID: `LEX-delete`. Roles: specialized_operator.

Source forms: `DELETE`.

#### SIG-delete-SRC-0351

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0351 / V1 lines 1322-1324

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Remove an object.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DELIBERATE

ID: `LEX-deliberate`. Roles: modifier_surface.

Source forms: `deliberate`.

#### SIG-deliberate-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deliberate" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-deliberate-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deliberate" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DELIBERATELY-COMPRESSED

ID: `LEX-deliberately-compressed`. Roles: modifier_surface.

Source forms: `deliberately compressed`.

#### SIG-deliberately-compressed-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deliberately compressed" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DELIBERATION

ID: `LEX-deliberation`. Roles: execution_modifier.

Source forms: `DELIBERATION`.

#### SIG-deliberation-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate deliberation using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEMONSTRATE

ID: `LEX-demonstrate`. Roles: communication_operator.

Source forms: `DEMONSTRATE`.

#### SIG-demonstrate-SRC-0451

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0451 / V1 lines 1664-1666

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Show execution or worked application.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEPENDENCY-BY-DEPENDENCY

ID: `LEX-dependency-by-dependency`. Roles: modifier_surface.

Source forms: `dependency-by-dependency`.

#### SIG-dependency-by-dependency-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "dependency-by-dependency" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEPENDENCY-COMPLETE

ID: `LEX-dependency-complete`. Roles: modifier_surface.

Source forms: `dependency-complete`.

#### SIG-dependency-complete-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "dependency-complete" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEPENDENCY-GRAPH

ID: `LEX-dependency-graph`. Roles: specialized_operator.

Source forms: `DEPENDENCY-GRAPH`.

#### SIG-dependency-graph-SRC-0090

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0090 / V1 lines 419-421

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent prerequisite relations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEPENDENCY-MAP

ID: `LEX-dependency-map`. Roles: proposed_procedure.

Source forms: `DEPENDENCY-MAP`.

#### SIG-dependency-map-P-source-macro-binding

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent task prerequisites as typed dependency relations; do not require an acyclic graph unless that constraint is supplied.

Evidence required: Apply the common contract to the explicitly bound target, property and scope.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Closure rule: Use the common contract and preserve remaining obligations.

Concrete instance: Map which task outputs are required before another task can run.

Abstract principle: Re-encode protected content under an explicit preservation projection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEPLOY

ID: `LEX-deploy`. Roles: macro, specialized_operator.

Source forms: `DEPLOY`.

#### SIG-deploy-SRC-0360

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0360 / V1 lines 1349-1351

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Place into an execution environment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-deploy-SRC-0493

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0493 / V1 lines 1810-1815

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: VALIDATE -> ACT -> OBSERVE -> TEST -> VERIFY

Macro source expression: `VALIDATE -> ACT -> OBSERVE -> TEST -> VERIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEPTH

ID: `LEX-depth`. Roles: execution_modifier.

Source forms: `DEPTH`.

#### SIG-depth-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate depth using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DERIVATIVE

ID: `LEX-derivative`. Roles: context_bound_attribute_surface.

Source forms: `derivative`.

#### SIG-derivative-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "derivative" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DERIVE

ID: `LEX-derive`. Roles: specialized_operator.

Source forms: `DERIVE`.

#### SIG-derive-SRC-0181

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0181 / V1 lines 729-731

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Produce results through defined rules.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DESCRIBE

ID: `LEX-describe`. Roles: communication_operator.

Source forms: `DESCRIBE`.

#### SIG-describe-SRC-0447

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0447 / V1 lines 1652-1654

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `INSPECT`.

Transition or retained definition: State properties.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DESCRIPTION

ID: `LEX-description`. Roles: modifier_surface.

Source forms: `description`.

#### SIG-description-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "description" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DESIGN

ID: `LEX-design`. Roles: macro.

Source forms: `DESIGN`.

#### SIG-design-SRC-0478

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0478 / V1 lines 1750-1753

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: COMPILE -> EXPAND -> REPRESENT -> EVALUATE -> CHALLENGE -> SELECT -> SPECIFY

Macro source expression: `COMPILE -> EXPAND -> REPRESENT -> EVALUATE -> CHALLENGE -> SELECT -> SPECIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DESIGNED

ID: `LEX-designed`. Roles: status.

Source forms: `DESIGNED`.

#### SIG-designed-SRC-0529

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0529 / V1 lines 2720-2722

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Specification exists.

Assessment dimension: artifact_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETAIL

ID: `LEX-detail`. Roles: execution_modifier.

Source forms: `DETAIL`.

#### SIG-detail-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate detail using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETAILED

ID: `LEX-detailed`. Roles: modifier_surface.

Source forms: `detailed`.

#### SIG-detailed-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "detailed" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-detailed-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "detailed" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-detailed-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "detailed" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETECT

ID: `LEX-detect`. Roles: specialized_operator.

Source forms: `DETECT`.

#### SIG-detect-SRC-0062

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0062 / V1 lines 333-335

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Determine whether a property or pattern exists.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETERMINISM

ID: `LEX-determinism`. Roles: semantic_policy_or_attribute.

Source forms: `DETERMINISM`.

#### SIG-determinism-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate determinism using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETERMINISTIC

ID: `LEX-deterministic`. Roles: modifier_surface.

Source forms: `deterministic`.

#### SIG-deterministic-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deterministic" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-deterministic-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deterministic" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETERMINISTIC-+-CANONICAL-ORDERING-+-EXPLICIT-SECONDARY-TIE-BREAKERS

ID: `LEX-deterministic-canonical-ordering-explicit-secondary-tie-breakers`. Roles: modifier_surface.

Source forms: `deterministic + canonical ordering + explicit secondary tie-breakers`.

#### SIG-deterministic-canonical-ordering-explicit-secondary-tie-breakers-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deterministic + canonical ordering + explicit secondary tie-breakers" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETERMINISTIC-WITH-CANONICAL-ORDERING

ID: `LEX-deterministic-with-canonical-ordering`. Roles: modifier_surface.

Source forms: `deterministic with canonical ordering`.

#### SIG-deterministic-with-canonical-ordering-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deterministic with canonical ordering" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DETERMINISTIC-WITH-EXPLICIT-TIE-BREAKERS

ID: `LEX-deterministic-with-explicit-tie-breakers`. Roles: modifier_surface.

Source forms: `deterministic with explicit tie-breakers`.

#### SIG-deterministic-with-explicit-tie-breakers-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "deterministic with explicit tie-breakers" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DEVIL'S-ADVOCATE

ID: `LEX-devil-s-advocate`. Roles: specialized_operator.

Source forms: `DEVIL'S-ADVOCATE`.

#### SIG-devil-s-advocate-SRC-0218

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0218 / V1 lines 863-865

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Produce opposing arguments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIAGNOSE

ID: `LEX-diagnose`. Roles: context_specific_operator, specialized_operator.

Source forms: `DIAGNOSE`.

#### SIG-diagnose-P-causal

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CAUSAL_IDENTIFICATION`. Contract: `INFER`.

Transition or retained definition: Infer a condition from observations while retaining indistinguishable rivals.

Evidence required: Symptoms, candidate mechanisms and discriminating observations.

Status rule: Diagnostic hypothesis until required rivals are separated.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Diagnose whether a failure comes from input corruption or configuration.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-diagnose-P-localize

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `SYSTEM`. Output roles: `PROPOSITION`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `INFER`.

Transition or retained definition: Narrow a fault to a component or execution region without overclaiming root cause.

Evidence required: Reproduction, trace and isolation evidence.

Status rule: Fault localized within the tested system.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Diagnose which module first emits an invalid value.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-diagnose-SRC-0192

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0192 / V1 lines 762-764

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer an underlying condition from observations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIFF

ID: `LEX-diff`. Roles: specialized_operator.

Source forms: `DIFF`.

#### SIG-diff-SRC-0072

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0072 / V1 lines 363-365

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Expose changes between states.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIFFERENTIAL-TEST

ID: `LEX-differential-test`. Roles: specialized_operator.

Source forms: `DIFFERENTIAL-TEST`.

#### SIG-differential-test-SRC-0238

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0238 / V1 lines 938-940

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Compare independent implementations or representations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIFFERENTIATE

ID: `LEX-differentiate`. Roles: specialized_operator.

Source forms: `DIFFERENTIATE`.

#### SIG-differentiate-SRC-0158

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0158 / V1 lines 650-652

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Expose distinguishing properties.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIFFICULT-ROLLBACK

ID: `LEX-difficult-rollback`. Roles: modifier_surface.

Source forms: `difficult rollback`.

#### SIG-difficult-rollback-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "difficult rollback" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISABLE

ID: `LEX-disable`. Roles: specialized_operator.

Source forms: `DISABLE`.

#### SIG-disable-SRC-0369

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0369 / V1 lines 1376-1378

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Deactivate capability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISAMBIGUATE

ID: `LEX-disambiguate`. Roles: specialized_operator.

Source forms: `DISAMBIGUATE`.

#### SIG-disambiguate-SRC-0019

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0019 / V1 lines 194-196

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Separate interpretations that could produce different results.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISCOURAGE

ID: `LEX-discourage`. Roles: constraint_surface.

Source forms: `discourage`.

#### SIG-discourage-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "discourage" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISCOVER

ID: `LEX-discover`. Roles: context_specific_operator, specialized_operator.

Source forms: `DISCOVER`.

#### SIG-discover-P-finding

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `INFER`.

Transition or retained definition: Identify a supported pattern or phenomenon and distinguish inference from generation.

Evidence required: Observations, analysis and appropriate validation.

Status rule: Candidate finding or supported finding according to evidence.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Discover a recurring failure pattern in recorded measurements.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-discover-P-retrieve

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Locate information previously unrepresented in the task context.

Evidence required: Located source and content.

Status rule: Discovered source content, not global novelty.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Discover an overlooked exception in the supplied policy.

Abstract principle: Obtain relevant records and provenance; do not silently assert their contents are true.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-discover-SRC-0137

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0137 / V1 lines 577-579

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Find previously unrepresented structure through investigation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISCOVER-SOURCE

ID: `LEX-discover-source`. Roles: specialized_operator.

Source forms: `DISCOVER-SOURCE`.

#### SIG-discover-source-SRC-0054

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0054 / V1 lines 303-307

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Find new evidence-bearing sources rather than answers directly.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISCRIMINATE

ID: `LEX-discriminate`. Roles: specialized_operator.

Source forms: `DISCRIMINATE`.

#### SIG-discriminate-SRC-0160

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0160 / V1 lines 656-658

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Find a distinction capable of changing the required result.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISENTANGLE

ID: `LEX-disentangle`. Roles: specialized_operator.

Source forms: `DISENTANGLE`.

#### SIG-disentangle-SRC-0129

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0129 / V1 lines 538-540

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Separate intertwined causes, requirements, or mechanisms.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISTILL

ID: `LEX-distill`. Roles: specialized_operator.

Source forms: `DISTILL`.

#### SIG-distill-SRC-0336

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0336 / V1 lines 1265-1267

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Retain high-value content.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DISTINGUISH

ID: `LEX-distinguish`. Roles: specialized_operator.

Source forms: `DISTINGUISH`.

#### SIG-distinguish-SRC-0159

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0159 / V1 lines 653-655

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Show why two cases should remain separate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIVERGENT

ID: `LEX-divergent`. Roles: modifier_surface.

Source forms: `divergent`.

#### SIG-divergent-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "divergent" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIVERSE-FRONTIER

ID: `LEX-diverse-frontier`. Roles: modifier_surface.

Source forms: `diverse frontier`.

#### SIG-diverse-frontier-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "diverse frontier" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIVERSE-SOURCES

ID: `LEX-diverse-sources`. Roles: modifier_surface.

Source forms: `diverse sources`.

#### SIG-diverse-sources-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "diverse sources" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DIVERSIFY

ID: `LEX-diversify`. Roles: specialized_operator.

Source forms: `DIVERSIFY`.

#### SIG-diversify-SRC-0138

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0138 / V1 lines 580-582

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Increase candidate diversity.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DO-NOT-ANALYZE

ID: `LEX-do-not-analyze`. Roles: modifier_surface.

Source forms: `do not analyze`.

#### SIG-do-not-analyze-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "do not analyze" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DOMAIN-GENERAL-ABSTRACTION

ID: `LEX-domain-general-abstraction`. Roles: modifier_surface.

Source forms: `domain-general abstraction`.

#### SIG-domain-general-abstraction-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "domain-general abstraction" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DOMINANCE

ID: `LEX-dominance`. Roles: modifier_surface.

Source forms: `dominance`.

#### SIG-dominance-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "dominance" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DOMINANCE-CHECK

ID: `LEX-dominance-check`. Roles: specialized_operator.

Source forms: `DOMINANCE-CHECK`.

#### SIG-dominance-check-SRC-0286

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0286 / V1 lines 1098-1100

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Test whether one candidate dominates another.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DOMINANCE-COMPARE

ID: `LEX-dominance-compare`. Roles: specialized_operator.

Source forms: `DOMINANCE-COMPARE`.

#### SIG-dominance-compare-SRC-0173

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0173 / V1 lines 695-697

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Test whether one candidate is never worse and sometimes better.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DOWNGRADE

ID: `LEX-downgrade`. Roles: specialized_operator.

Source forms: `DOWNGRADE`.

#### SIG-downgrade-SRC-0259

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0259 / V1 lines 1011-1013

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Reduce confidence or status without fully retracting.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DRAFT

ID: `LEX-draft`. Roles: communication_operator.

Source forms: `DRAFT`.

#### SIG-draft-SRC-0461

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0461 / V1 lines 1694-1696

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Produce an initial complete artifact.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DRY-RUN

ID: `LEX-dry-run`. Roles: specialized_operator.

Source forms: `DRY-RUN`.

#### SIG-dry-run-SRC-0241

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0241 / V1 lines 947-949

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test without applying final mutation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### DUPLICATE

ID: `LEX-duplicate`. Roles: context_bound_attribute_surface.

Source forms: `duplicate`.

#### SIG-duplicate-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "duplicate" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EASILY-REVERSIBLE

ID: `LEX-easily-reversible`. Roles: modifier_surface.

Source forms: `easily reversible`.

#### SIG-easily-reversible-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "easily reversible" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ECONOMICAL

ID: `LEX-economical`. Roles: modifier_surface.

Source forms: `economical`.

#### SIG-economical-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "economical" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EDGE-CASE-ROBUST

ID: `LEX-edge-case-robust`. Roles: modifier_surface.

Source forms: `edge-case robust`.

#### SIG-edge-case-robust-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "edge-case robust" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EDIT

ID: `LEX-edit`. Roles: communication_operator, specialized_operator.

Source forms: `EDIT`.

#### SIG-edit-SRC-0349

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0349 / V1 lines 1316-1318

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Modify an existing artifact.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-edit-SRC-0458

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0458 / V1 lines 1685-1687

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Modify existing text.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EFFICIENT

ID: `LEX-efficient`. Roles: modifier_surface.

Source forms: `efficient`.

#### SIG-efficient-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "efficient" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-efficient-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "efficient" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-efficient-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "efficient" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ELABORATE

ID: `LEX-elaborate`. Roles: modifier_surface.

Source forms: `elaborate`.

#### SIG-elaborate-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "elaborate" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ELSE

ID: `LEX-else`. Roles: control_operator.

Source forms: `ELSE`.

#### SIG-else-SRC-0427

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0427 / V1 lines 1584-1586

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Alternative execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ENABLE

ID: `LEX-enable`. Roles: specialized_operator.

Source forms: `ENABLE`.

#### SIG-enable-SRC-0368

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0368 / V1 lines 1373-1375

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Activate capability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ENCODE

ID: `LEX-encode`. Roles: specialized_operator.

Source forms: `ENCODE`.

#### SIG-encode-SRC-0099

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0099 / V1 lines 446-448

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Translate information into a declared representational system.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ENUMERATE

ID: `LEX-enumerate`. Roles: specialized_operator.

Source forms: `ENUMERATE`.

#### SIG-enumerate-SRC-0133

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0133 / V1 lines 565-567

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: List members of a bounded candidate class.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ENUMERATE-ASSUMPTIONS

ID: `LEX-enumerate-assumptions`. Roles: specialized_operator.

Source forms: `ENUMERATE-ASSUMPTIONS`.

#### SIG-enumerate-assumptions-SRC-0150

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0150 / V1 lines 616-618

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Expand hidden or explicit assumptions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ENUMERATE-FAILURES

ID: `LEX-enumerate-failures`. Roles: specialized_operator.

Source forms: `ENUMERATE-FAILURES`.

#### SIG-enumerate-failures-SRC-0149

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0149 / V1 lines 613-615

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Expand possible failure mechanisms.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ENUMERATE-RIVALS

ID: `LEX-enumerate-rivals`. Roles: specialized_operator.

Source forms: `ENUMERATE-RIVALS`.

#### SIG-enumerate-rivals-SRC-0151

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0151 / V1 lines 619-621

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Generate alternative explanatory models.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EQUATION

ID: `LEX-equation`. Roles: specialized_operator.

Source forms: `EQUATION`.

#### SIG-equation-SRC-0096

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0096 / V1 lines 437-439

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent quantitative relationships symbolically.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EQUIVALENCE-CHECK

ID: `LEX-equivalence-check`. Roles: specialized_operator.

Source forms: `EQUIVALENCE-CHECK`.

#### SIG-equivalence-check-SRC-0161

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0161 / V1 lines 659-661

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Test whether two cases produce equivalent required outcomes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EQUIVALENCE-CLASS-COVERAGE

ID: `LEX-equivalence-class-coverage`. Roles: modifier_surface.

Source forms: `equivalence-class coverage`.

#### SIG-equivalence-class-coverage-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "equivalence-class coverage" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ESCALATE

ID: `LEX-escalate`. Roles: control_operator, specialized_operator.

Source forms: `ESCALATE`.

#### SIG-escalate-SRC-0307

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0307 / V1 lines 1167-1169

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Transfer to another authority.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-escalate-SRC-0414

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0414 / V1 lines 1545-1547

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Transfer authority.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ESTABLISHED-PATTERN-ONLY

ID: `LEX-established-pattern-only`. Roles: modifier_surface.

Source forms: `established pattern only`.

#### SIG-established-pattern-only-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "established pattern only" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ESTABLISHED-UNPRECEDENTEDNESS

ID: `LEX-established-unprecedentedness`. Roles: context_bound_attribute_surface.

Source forms: `established unprecedentedness`.

#### SIG-established-unprecedentedness-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "established unprecedentedness" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ESTIMATE

ID: `LEX-estimate`. Roles: specialized_operator.

Source forms: `ESTIMATE`.

#### SIG-estimate-SRC-0189

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0189 / V1 lines 753-755

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Produce an approximate value.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EVALUATE

ID: `LEX-evaluate`. Roles: family.

Source forms: `EVALUATE`.

#### SIG-evaluate-SRC-0269

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0269 / V1 lines 1046-1049

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Judge candidates against explicit criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EVALUATE-CONSERVATIVELY

ID: `LEX-evaluate-conservatively`. Roles: modifier_surface.

Source forms: `evaluate conservatively`.

#### SIG-evaluate-conservatively-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "evaluate conservatively" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EVERY-ADMISSIBLE-CASE

ID: `LEX-every-admissible-case`. Roles: modifier_surface.

Source forms: `every admissible case`.

#### SIG-every-admissible-case-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "every admissible case" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EVIDENCE-CONSERVATIVE

ID: `LEX-evidence-conservative`. Roles: modifier_surface.

Source forms: `evidence-conservative`.

#### SIG-evidence-conservative-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "evidence-conservative" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EVIDENTIAL-STRENGTH

ID: `LEX-evidential-strength`. Roles: modifier_surface.

Source forms: `evidential strength`.

#### SIG-evidential-strength-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "evidential strength" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXACT

ID: `LEX-exact`. Roles: modifier_surface.

Source forms: `exact`.

#### SIG-exact-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exact" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exact-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exact" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXACT-CONFORMANCE

ID: `LEX-exact-conformance`. Roles: modifier_surface.

Source forms: `exact conformance`.

#### SIG-exact-conformance-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exact conformance" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXACTLY

ID: `LEX-exactly`. Roles: constraint_surface.

Source forms: `exactly`.

#### SIG-exactly-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exactly" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXAMINE

ID: `LEX-examine`. Roles: specialized_operator.

Source forms: `EXAMINE`.

#### SIG-examine-SRC-0058

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0058 / V1 lines 321-323

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Inspect deliberately for relevant properties.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXCLUDE

ID: `LEX-exclude`. Roles: specialized_operator.

Source forms: `EXCLUDE`.

#### SIG-exclude-SRC-0299

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0299 / V1 lines 1143-1145

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Remove under a rule.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXCLUDE-ADJACENT-CASES

ID: `LEX-exclude-adjacent-cases`. Roles: modifier_surface.

Source forms: `exclude adjacent cases`.

#### SIG-exclude-adjacent-cases-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exclude adjacent cases" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXECUTE

ID: `LEX-execute`. Roles: context_specific_operator, specialized_operator.

Source forms: `EXECUTE`.

#### SIG-execute-P-external

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Dispatch a permitted external operation and reconcile actual outcome before retry.

Evidence required: Dispatch record plus target-state evidence.

Status rule: Dispatched, executed and postcondition satisfied remain separate.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Execute an authorized deployment and inspect the serving version.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-execute-P-local

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACT`. Input roles: `ACTION`. Output roles: `ARTIFACT`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `ACT`.

Transition or retained definition: Run a local procedure against a stated artifact and record outcome.

Evidence required: Process output and target revision.

Status rule: Executed local procedure, success separately checked.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Run the migration script in the isolated workspace.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-execute-SRC-0343

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0343 / V1 lines 1298-1300

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Carry out an operation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXECUTED

ID: `LEX-executed`. Roles: status.

Source forms: `EXECUTED`.

#### SIG-executed-SRC-0532

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0532 / V1 lines 2729-2731

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Operation actually ran.

Assessment dimension: execution_and_observation_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXEMPLIFY

ID: `LEX-exemplify`. Roles: communication_operator.

Source forms: `EXEMPLIFY`.

#### SIG-exemplify-SRC-0450

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0450 / V1 lines 1661-1663

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Provide examples.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXHAUSTIVE

ID: `LEX-exhaustive`. Roles: context_bound_attribute_surface, context_specific_operator, modifier_surface.

Source forms: `EXHAUSTIVE`, `exhaustive`.

#### SIG-exhaustive-P-finite-enumeration

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Establish that every member of a declared finite registry was processed.

Evidence required: Registry, inclusion rule and per-member receipts.

Status rule: Exhaustive over that registry only.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Process every source block in the frozen V1 file.

Abstract principle: Stop the current work with a scoped assessment, explicit residuals and reopening conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-P-reachable-classes

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `VERIFY`.

Transition or retained definition: Establish reachability coverage under specified generators and a sound equivalence relation.

Evidence required: Reachability argument or finite-state exhaustive check.

Status rule: Coverage over the declared model.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Check all reachable states of a finite transition system.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXHAUSTIVE-CANDIDATE-GENERATION

ID: `LEX-exhaustive-candidate-generation`. Roles: modifier_surface.

Source forms: `exhaustive candidate generation`.

#### SIG-exhaustive-candidate-generation-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive candidate generation" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXHAUSTIVE-WHERE-MATERIAL

ID: `LEX-exhaustive-where-material`. Roles: modifier_surface.

Source forms: `exhaustive where material`.

#### SIG-exhaustive-where-material-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive where material" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-exhaustive-where-material-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exhaustive where material" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPAND

ID: `LEX-expand`. Roles: family.

Source forms: `EXPAND`.

#### SIG-expand-SRC-0132

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0132 / V1 lines 548-564

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Increase a frontier when a consequential class may be absent.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPAND-REPRESENTATION

ID: `LEX-expand-representation`. Roles: specialized_operator.

Source forms: `EXPAND-REPRESENTATION`.

#### SIG-expand-representation-SRC-0113

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0113 / V1 lines 488-492

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Increase explicitness without necessarily adding underlying evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPERIMENT

ID: `LEX-experiment`. Roles: specialized_operator.

Source forms: `EXPERIMENT`.

#### SIG-experiment-SRC-0226

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0226 / V1 lines 902-904

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Manipulate conditions and observe consequences.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLAIN

ID: `LEX-explain`. Roles: communication_operator, context_specific_operator, specialized_operator.

Source forms: `EXPLAIN`.

#### SIG-explain-P-cause

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CAUSAL_IDENTIFICATION`. Contract: `INFER`.

Transition or retained definition: Produce a causal account with assumptions, rival causes and discriminators.

Evidence required: Evidence bearing on causal alternatives.

Status rule: Hypothesis or causal support, not truth from narrative coherence.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Explain why a service failed rather than only describing the symptoms.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-explain-P-communicate

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `REPRESENT`. Input roles: `PROPOSITION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT`. Contract: `REPRESENT`.

Transition or retained definition: Make a concept understandable to a specified audience without adding unsupported claims.

Evidence required: Source fidelity and, when required, audience feedback.

Status rule: Explanation produced; comprehension not assumed.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Explain a state machine to a novice.

Abstract principle: Re-encode protected content under an explicit preservation projection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-explain-P-derivation

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `REPRESENT`. Input roles: `ARTIFACT`. Output roles: `REPRESENTATION`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `REPRESENT`.

Transition or retained definition: Expose the steps and assumptions of a derivation without changing its claim.

Evidence required: Derivation and correspondence check.

Status rule: Faithful account of the proof, not an additional proof certificate.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Explain how a lemma establishes the next step.

Abstract principle: Re-encode protected content under an explicit preservation projection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-explain-SRC-0184

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0184 / V1 lines 738-740

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Produce mechanism or reason.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-explain-SRC-0448

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0448 / V1 lines 1655-1657

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Expose mechanism or reasoning structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLAIN-CAUSALLY

ID: `LEX-explain-causally`. Roles: specialized_operator.

Source forms: `EXPLAIN-CAUSALLY`.

#### SIG-explain-causally-SRC-0196

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0196 / V1 lines 774-776

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer a causal mechanism rather than merely association.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLICIT

ID: `LEX-explicit`. Roles: modifier_surface.

Source forms: `explicit`.

#### SIG-explicit-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "explicit" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLICIT-COMMAND-ONLY

ID: `LEX-explicit-command-only`. Roles: modifier_surface.

Source forms: `explicit-command-only`.

#### SIG-explicit-command-only-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "explicit-command-only" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLICIT-UNRESOLVED-STATE

ID: `LEX-explicit-unresolved-state`. Roles: modifier_surface.

Source forms: `explicit unresolved state`.

#### SIG-explicit-unresolved-state-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "explicit unresolved state" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLORATION

ID: `LEX-exploration`. Roles: execution_modifier.

Source forms: `EXPLORATION`.

#### SIG-exploration-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate exploration using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLORATORY

ID: `LEX-exploratory`. Roles: modifier_surface.

Source forms: `exploratory`.

#### SIG-exploratory-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "exploratory" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPLORE

ID: `LEX-explore`. Roles: specialized_operator.

Source forms: `EXPLORE`.

#### SIG-explore-SRC-0136

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0136 / V1 lines 574-576

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Traverse possible alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXPORT

ID: `LEX-export`. Roles: specialized_operator.

Source forms: `EXPORT`.

#### SIG-export-SRC-0355

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0355 / V1 lines 1334-1336

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Produce externally consumable output.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXTEND

ID: `LEX-extend`. Roles: specialized_operator.

Source forms: `EXTEND`.

#### SIG-extend-SRC-0338

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0338 / V1 lines 1271-1273

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Increase scope or capability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXTRACT

ID: `LEX-extract`. Roles: specialized_operator.

Source forms: `EXTRACT`.

#### SIG-extract-SRC-0047

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0047 / V1 lines 282-284

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Select specified information from material already available.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### EXTRAPOLATE

ID: `LEX-extrapolate`. Roles: specialized_operator.

Source forms: `EXTRAPOLATE`.

#### SIG-extrapolate-SRC-0145

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0145 / V1 lines 601-603

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Extend beyond the observed region.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FACTOR

ID: `LEX-factor`. Roles: specialized_operator.

Source forms: `FACTOR`.

#### SIG-factor-SRC-0119

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0119 / V1 lines 508-510

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Express a whole through constituent factors.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FALLBACK

ID: `LEX-fallback`. Roles: control_operator.

Source forms: `FALLBACK`.

#### SIG-fallback-SRC-0415

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0415 / V1 lines 1548-1550

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Switch methods after failure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FALSIFICATION-CONSERVATIVE

ID: `LEX-falsification-conservative`. Roles: modifier_surface.

Source forms: `falsification-conservative`.

#### SIG-falsification-conservative-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "falsification-conservative" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FALSIFICATION-FIRST

ID: `LEX-falsification-first`. Roles: modifier_surface, specialized_operator.

Source forms: `FALSIFICATION-FIRST`, `falsification-first`.

#### SIG-falsification-first-SRC-0219

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0219 / V1 lines 866-874

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Prioritize defeating the current candidate before accumulating supporting evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-falsification-first-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "falsification-first" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-falsification-first-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "falsification-first" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FALSIFY

ID: `LEX-falsify`. Roles: specialized_operator.

Source forms: `FALSIFY`.

#### SIG-falsify-SRC-0205

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0205 / V1 lines 824-826

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Seek evidence that would refute a proposition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FAMILIAR

ID: `LEX-familiar`. Roles: context_bound_attribute_surface.

Source forms: `familiar`.

#### SIG-familiar-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "familiar" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FASTEST-AVAILABLE

ID: `LEX-fastest-available`. Roles: modifier_surface.

Source forms: `fastest available`.

#### SIG-fastest-available-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "fastest available" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FEASIBILITY-CHECK

ID: `LEX-feasibility-check`. Roles: specialized_operator.

Source forms: `FEASIBILITY-CHECK`.

#### SIG-feasibility-check-SRC-0282

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0282 / V1 lines 1086-1088

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Evaluate executability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FETCH

ID: `LEX-fetch`. Roles: specialized_operator.

Source forms: `FETCH`.

#### SIG-fetch-SRC-0040

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0040 / V1 lines 261-263

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Mechanically retrieve from a specified source or endpoint.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FIELD-BY-FIELD

ID: `LEX-field-by-field`. Roles: modifier_surface.

Source forms: `field-by-field`.

#### SIG-field-by-field-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "field-by-field" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FILTER

ID: `LEX-filter`. Roles: specialized_operator.

Source forms: `FILTER`.

#### SIG-filter-SRC-0048

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0048 / V1 lines 285-287

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Retain items satisfying a predicate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-filter-SRC-0300

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0300 / V1 lines 1146-1148

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Select according to predicate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FINALIZE

ID: `LEX-finalize`. Roles: specialized_operator.

Source forms: `FINALIZE`.

#### SIG-finalize-SRC-0434

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0434 / V1 lines 1607-1609

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Mark artifact complete for requirements.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FIND

ID: `LEX-find`. Roles: specialized_operator.

Source forms: `FIND`.

#### SIG-find-SRC-0037

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0037 / V1 lines 252-254

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Identify something satisfying a predicate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FINE-GRAINED

ID: `LEX-fine-grained`. Roles: modifier_surface.

Source forms: `fine-grained`.

#### SIG-fine-grained-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "fine-grained" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-fine-grained-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "fine-grained" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FIRST-PRINCIPLES

ID: `LEX-first-principles`. Roles: modifier_surface.

Source forms: `first-principles`.

#### SIG-first-principles-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "first-principles" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FLAWLESS

ID: `LEX-flawless`. Roles: modifier_surface.

Source forms: `flawless`.

#### SIG-flawless-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "flawless" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FLEXIBLE

ID: `LEX-flexible`. Roles: modifier_surface.

Source forms: `flexible`.

#### SIG-flexible-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "flexible" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-flexible-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "flexible" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FLOWCHART

ID: `LEX-flowchart`. Roles: specialized_operator.

Source forms: `FLOWCHART`.

#### SIG-flowchart-SRC-0087

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0087 / V1 lines 410-412

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent process flow.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FOCUSED

ID: `LEX-focused`. Roles: modifier_surface.

Source forms: `focused`.

#### SIG-focused-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "focused" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FOR-EACH

ID: `LEX-for-each`. Roles: control_operator.

Source forms: `FOR-EACH`.

#### SIG-for-each-SRC-0430

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0430 / V1 lines 1593-1595

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Apply across members.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORBID

ID: `LEX-forbid`. Roles: specialized_operator.

Source forms: `FORBID`.

#### SIG-forbid-SRC-0024

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0024 / V1 lines 209-211

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Make a condition inadmissible.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORCE-SINGLE-ANSWER

ID: `LEX-force-single-answer`. Roles: modifier_surface.

Source forms: `force single answer`.

#### SIG-force-single-answer-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "force single answer" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORECAST

ID: `LEX-forecast`. Roles: macro, specialized_operator.

Source forms: `FORECAST`.

#### SIG-forecast-SRC-0188

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0188 / V1 lines 750-752

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Predict over a future interval.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-forecast-SRC-0487

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0487 / V1 lines 1786-1789

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: ACQUIRE -> REPRESENT -> INFER MODEL -> PROJECT -> CHALLENGE -> REPORT

Macro source expression: `ACQUIRE -> REPRESENT -> INFER MODEL -> PROJECT -> CHALLENGE -> REPORT`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORENSIC

ID: `LEX-forensic`. Roles: modifier_surface.

Source forms: `forensic`.

#### SIG-forensic-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "forensic" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-forensic-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "forensic" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORK

ID: `LEX-fork`. Roles: control_operator.

Source forms: `FORK`.

#### SIG-fork-SRC-0401

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0401 / V1 lines 1506-1508

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Create divergent paths.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMAL

ID: `LEX-formal`. Roles: modifier_surface.

Source forms: `formal`.

#### SIG-formal-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "formal" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-formal-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "formal" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMALITY

ID: `LEX-formality`. Roles: execution_modifier.

Source forms: `FORMALITY`.

#### SIG-formality-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate formality using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMALIZE

ID: `LEX-formalize`. Roles: specialized_operator.

Source forms: `FORMALIZE`.

#### SIG-formalize-SRC-0030

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0030 / V1 lines 227-229

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Express a concept through explicit rules, logic, mathematics, types, or schemas.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMALLY-ESTABLISHED

ID: `LEX-formally-established`. Roles: context_bound_attribute_surface.

Source forms: `formally established`.

#### SIG-formally-established-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "formally established" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMALLY-SPECIFIED

ID: `LEX-formally-specified`. Roles: modifier_surface.

Source forms: `formally specified`.

#### SIG-formally-specified-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "formally specified" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMALLY-VERIFIED

ID: `LEX-formally-verified`. Roles: modifier_surface, status.

Source forms: `FORMALLY VERIFIED`, `formally verified`.

#### SIG-formally-verified-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "formally verified" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-formally-verified-SRC-0542

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0542 / V1 lines 2759-2761

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Formal system established the declared property.

Assessment dimension: verification_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMALLY-VERIFY

ID: `LEX-formally-verify`. Roles: modifier_surface.

Source forms: `formally verify`.

#### SIG-formally-verify-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "formally verify" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FORMAT

ID: `LEX-format`. Roles: communication_operator, specialized_operator.

Source forms: `FORMAT`.

#### SIG-format-SRC-0101

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0101 / V1 lines 452-454

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Apply presentation structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-format-SRC-0463

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0463 / V1 lines 1700-1702

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Control presentation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FRAGMENTARY

ID: `LEX-fragmentary`. Roles: context_bound_attribute_surface.

Source forms: `fragmentary`.

#### SIG-fragmentary-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "fragmentary" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FREEZE

ID: `LEX-freeze`. Roles: specialized_operator.

Source forms: `FREEZE`.

#### SIG-freeze-SRC-0440

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0440 / V1 lines 1625-1627

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Prevent modification.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FULL-ADMISSIBLE-AUTONOMY

ID: `LEX-full-admissible-autonomy`. Roles: modifier_surface.

Source forms: `full admissible autonomy`.

#### SIG-full-admissible-autonomy-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "full admissible autonomy" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FULLY

ID: `LEX-fully`. Roles: modifier_surface.

Source forms: `fully`.

#### SIG-fully-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "fully" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FULLY-CANONICAL-UNDER-DECLARED-INPUTS

ID: `LEX-fully-canonical-under-declared-inputs`. Roles: modifier_surface.

Source forms: `fully canonical under declared inputs`.

#### SIG-fully-canonical-under-declared-inputs-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "fully canonical under declared inputs" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### FUZZ

ID: `LEX-fuzz`. Roles: specialized_operator.

Source forms: `FUZZ`.

#### SIG-fuzz-SRC-0245

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0245 / V1 lines 959-961

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Generate varied or malformed test inputs.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GATE

ID: `LEX-gate`. Roles: control_operator.

Source forms: `GATE`.

#### SIG-gate-SRC-0405

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0405 / V1 lines 1518-1520

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Prevent progression until condition satisfaction.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GATHER

ID: `LEX-gather`. Roles: specialized_operator.

Source forms: `GATHER`.

#### SIG-gather-SRC-0042

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0042 / V1 lines 267-269

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Accumulate relevant evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GENERALIZE

ID: `LEX-generalize`. Roles: context_specific_operator, specialized_operator.

Source forms: `GENERALIZE`.

#### SIG-generalize-P-design-pattern

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `REPRESENT`. Input roles: `ARTIFACT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Extract a reusable structural pattern from instances without claiming all future uses succeed.

Evidence required: Instance-to-pattern mapping and boundary cases.

Status rule: Candidate reusable pattern.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Generalize repeated implementation steps into a parameterized template.

Abstract principle: Re-encode protected content under an explicit preservation projection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-generalize-P-empirical

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `INFER`.

Transition or retained definition: Extend an inference to another population or context with explicit transport assumptions.

Evidence required: Evidence supporting transfer and limitations.

Status rule: Generalized support limited to the stated target scope.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Generalize measured behavior to a wider environment only after transfer checks.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-generalize-P-formal

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `PROPOSITION`. Output roles: `PROPOSITION`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `INFER`.

Transition or retained definition: Derive a proposition over a broader quantified domain.

Evidence required: Proof of the broader claim.

Status rule: Formal generalization only for the proved domain.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Extend a lemma from two cases to all finite sizes.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-generalize-SRC-0142

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0142 / V1 lines 592-594

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Extend structure to a broader domain.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GENERALIZED

ID: `LEX-generalized`. Roles: status.

Source forms: `GENERALIZED`.

#### SIG-generalized-SRC-0543

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0543 / V1 lines 2762-2764

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Evidence supports a broader scope than originally tested.

Assessment dimension: generalization_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GENERATE

ID: `LEX-generate`. Roles: specialized_operator.

Source forms: `GENERATE`.

#### SIG-generate-SRC-0134

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0134 / V1 lines 568-570

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Construct new candidates.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GENERATE-DIVERGENTLY

ID: `LEX-generate-divergently`. Roles: modifier_surface.

Source forms: `generate divergently`.

#### SIG-generate-divergently-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "generate divergently" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GENERATE-DIVERGENTLY,-EVALUATE-CONSERVATIVELY

ID: `LEX-generate-divergently-evaluate-conservatively`. Roles: modifier_surface.

Source forms: `generate divergently, evaluate conservatively`.

#### SIG-generate-divergently-evaluate-conservatively-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "generate divergently, evaluate conservatively" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GIST-ONLY

ID: `LEX-gist-only`. Roles: modifier_surface.

Source forms: `gist-only`.

#### SIG-gist-only-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "gist-only" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-gist-only-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "gist-only" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GRADE

ID: `LEX-grade`. Roles: specialized_operator.

Source forms: `GRADE`.

#### SIG-grade-SRC-0274

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0274 / V1 lines 1062-1064

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Map to rubric categories.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GRANULAR

ID: `LEX-granular`. Roles: modifier_surface.

Source forms: `granular`.

#### SIG-granular-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "granular" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-granular-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "granular" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GRAPH

ID: `LEX-graph`. Roles: specialized_operator.

Source forms: `GRAPH`.

#### SIG-graph-SRC-0081

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0081 / V1 lines 392-394

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent nodes and edges.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GREATER-REVERSIBILITY

ID: `LEX-greater-reversibility`. Roles: modifier_surface.

Source forms: `greater reversibility`.

#### SIG-greater-reversibility-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "greater reversibility" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GROUND

ID: `LEX-ground`. Roles: specialized_operator.

Source forms: `GROUND`.

#### SIG-ground-SRC-0032

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0032 / V1 lines 233-235

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Connect an abstract statement to observations, definitions, procedures, or evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GROUP

ID: `LEX-group`. Roles: specialized_operator.

Source forms: `GROUP`.

#### SIG-group-SRC-0165

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0165 / V1 lines 671-673

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Place similar items together.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### GUESS

ID: `LEX-guess`. Roles: modifier_surface.

Source forms: `guess`.

#### SIG-guess-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "guess" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HANDLES-COMMON-VARIATION

ID: `LEX-handles-common-variation`. Roles: modifier_surface.

Source forms: `handles common variation`.

#### SIG-handles-common-variation-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "handles common variation" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HARDEN

ID: `LEX-harden`. Roles: specialized_operator.

Source forms: `HARDEN`.

#### SIG-harden-SRC-0339

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0339 / V1 lines 1274-1276

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Increase resistance to failure or misuse.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HARVEST

ID: `LEX-harvest`. Roles: specialized_operator.

Source forms: `HARVEST`.

#### SIG-harvest-SRC-0051

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0051 / V1 lines 294-296

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Collect many structured items from a source class.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HEADLINE-ONLY

ID: `LEX-headline-only`. Roles: modifier_surface.

Source forms: `headline-only`.

#### SIG-headline-only-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "headline-only" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-headline-only-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "headline-only" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGH-LEVEL

ID: `LEX-high-level`. Roles: modifier_surface.

Source forms: `high-level`.

#### SIG-high-level-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "high-level" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGH-LEVEL-ONLY

ID: `LEX-high-level-only`. Roles: modifier_surface.

Source forms: `high-level-only`.

#### SIG-high-level-only-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "high-level-only" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGHER-INDEPENDENCE

ID: `LEX-higher-independence`. Roles: modifier_surface.

Source forms: `higher independence`.

#### SIG-higher-independence-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "higher independence" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGHLY-DIVERGENT

ID: `LEX-highly-divergent`. Roles: modifier_surface.

Source forms: `highly divergent`.

#### SIG-highly-divergent-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "highly divergent" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGHLY-NOVEL

ID: `LEX-highly-novel`. Roles: context_bound_attribute_surface.

Source forms: `highly novel`.

#### SIG-highly-novel-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "highly novel" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGHLY-SUPPORTED

ID: `LEX-highly-supported`. Roles: context_bound_attribute_surface.

Source forms: `highly supported`.

#### SIG-highly-supported-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "highly supported" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HIGHLY-VARIABLE

ID: `LEX-highly-variable`. Roles: modifier_surface.

Source forms: `highly variable`.

#### SIG-highly-variable-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "highly variable" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HOSTILE-REVIEW

ID: `LEX-hostile-review`. Roles: modifier_surface, specialized_operator.

Source forms: `HOSTILE-REVIEW`, `hostile review`.

#### SIG-hostile-review-SRC-0208

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0208 / V1 lines 833-835

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Assume reviewers are actively trying to reject unsupported claims.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-hostile-review-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "hostile review" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HYPOTHESIZE

ID: `LEX-hypothesize`. Roles: specialized_operator.

Source forms: `HYPOTHESIZE`.

#### SIG-hypothesize-SRC-0186

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0186 / V1 lines 744-746

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Create a testable proposition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### HYPOTHETICAL

ID: `LEX-hypothetical`. Roles: context_bound_attribute_surface.

Source forms: `hypothetical`.

#### SIG-hypothetical-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "hypothetical" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IDEMPOTENT-EXECUTE

ID: `LEX-idempotent-execute`. Roles: control_operator.

Source forms: `IDEMPOTENT-EXECUTE`.

#### SIG-idempotent-execute-SRC-0423

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0423 / V1 lines 1572-1574

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Ensure repeated execution produces the same final state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IDENTIFY

ID: `LEX-identify`. Roles: specialized_operator.

Source forms: `IDENTIFY`.

#### SIG-identify-SRC-0063

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0063 / V1 lines 336-338

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Associate an observed item with a label or referent.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IF

ID: `LEX-if`. Roles: control_operator.

Source forms: `IF`.

#### SIG-if-SRC-0426

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0426 / V1 lines 1581-1583

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Conditional execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMMEDIATE

ID: `LEX-immediate`. Roles: modifier_surface.

Source forms: `immediate`.

#### SIG-immediate-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "immediate" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMPLEMENT

ID: `LEX-implement`. Roles: context_specific_operator, macro, specialized_operator.

Source forms: `IMPLEMENT`.

#### SIG-implement-P-artifact

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TRANSFORM`. Input roles: `CANDIDATE`. Output roles: `ARTIFACT`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `TRANSFORM`.

Transition or retained definition: Realize a specification as an artifact; do not infer execution from existence.

Evidence required: Artifact diff and specification traceability.

Status rule: IMPLEMENTED if an actual artifact exists; testing tracked separately.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Write the specified parser.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-implement-P-operational

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Put a policy or design into actual operation using scoped authority.

Evidence required: Action records and observed deployed state.

Status rule: Operational implementation only for observed changes.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Implement a new approval workflow in the target system.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-implement-SRC-0345

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0345 / V1 lines 1304-1306

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Turn specification into actual artifact or behavior.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-implement-SRC-0490

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0490 / V1 lines 1798-1801

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: READ SPECIFICATION -> COMPILE ACTIONS -> ACT -> TEST -> VERIFY

Macro source expression: `READ SPECIFICATION -> COMPILE ACTIONS -> ACT -> TEST -> VERIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMPLEMENTED

ID: `LEX-implemented`. Roles: status.

Source forms: `IMPLEMENTED`.

#### SIG-implemented-SRC-0531

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0531 / V1 lines 2726-2728

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Operational artifact exists.

Assessment dimension: artifact_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMPORT

ID: `LEX-import`. Roles: context_specific_operator, specialized_operator.

Source forms: `IMPORT`.

#### SIG-import-P-acquire

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Bring external content into working context with provenance and access constraints.

Evidence required: Imported bytes, source reference and scope.

Status rule: Content acquired, not trusted as instructions.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Import a file as evidence.

Abstract principle: Obtain relevant records and provenance; do not silently assert their contents are true.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-import-P-mutate

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACT`. Input roles: `ARTIFACT`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Load records into a target system while checking authority and mutation effects.

Evidence required: Target receipt and post-import inspection.

Status rule: Import attempted or completed within observed scope.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Import an authorized dataset into a sandbox table.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-import-SRC-0046

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0046 / V1 lines 279-281

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Bring external information into the current system.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-import-SRC-0356

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0356 / V1 lines 1337-1339

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Bring content into a system.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMPOSSIBLE-BY-CONTRACT

ID: `LEX-impossible-by-contract`. Roles: constraint_surface.

Source forms: `impossible by contract`.

#### SIG-impossible-by-contract-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "impossible by contract" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMPROVE

ID: `LEX-improve`. Roles: specialized_operator.

Source forms: `IMPROVE`.

#### SIG-improve-SRC-0316

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0316 / V1 lines 1205-1207

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Increase quality under stated criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IMPUTE

ID: `LEX-impute`. Roles: specialized_operator.

Source forms: `IMPUTE`.

#### SIG-impute-SRC-0198

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0198 / V1 lines 780-795

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer missing values under an explicit model.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INCORPORATE

ID: `LEX-incorporate`. Roles: specialized_operator.

Source forms: `INCORPORATE`.

#### SIG-incorporate-SRC-0251

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0251 / V1 lines 987-989

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Add information.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENCE

ID: `LEX-independence`. Roles: semantic_policy_or_attribute.

Source forms: `INDEPENDENCE`.

#### SIG-independence-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate independence using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT

ID: `LEX-independent`. Roles: modifier_surface.

Source forms: `independent`.

#### SIG-independent-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT-EVIDENCE

ID: `LEX-independent-evidence`. Roles: modifier_surface.

Source forms: `independent evidence`.

#### SIG-independent-evidence-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent evidence" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT-IMPLEMENTATION

ID: `LEX-independent-implementation`. Roles: modifier_surface.

Source forms: `independent implementation`.

#### SIG-independent-implementation-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent implementation" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT-REPRODUCTION

ID: `LEX-independent-reproduction`. Roles: modifier_surface.

Source forms: `independent reproduction`.

#### SIG-independent-reproduction-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent reproduction" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-independent-reproduction-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent reproduction" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT-REPRODUCTION-WITH-DISTINCT-FAILURE-MODES

ID: `LEX-independent-reproduction-with-distinct-failure-modes`. Roles: modifier_surface.

Source forms: `independent reproduction with distinct failure modes`.

#### SIG-independent-reproduction-with-distinct-failure-modes-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent reproduction with distinct failure modes" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT-SOURCES

ID: `LEX-independent-sources`. Roles: modifier_surface.

Source forms: `independent sources`.

#### SIG-independent-sources-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independent sources" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENT-VERIFY

ID: `LEX-independent-verify`. Roles: specialized_operator.

Source forms: `INDEPENDENT-VERIFY`.

#### SIG-independent-verify-SRC-0389

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0389 / V1 lines 1457-1472

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Verify without relying on the original conclusion-producing path.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENTLY-REPRODUCE

ID: `LEX-independently-reproduce`. Roles: modifier_surface, specialized_operator.

Source forms: `INDEPENDENTLY-REPRODUCE`, `independently reproduce`.

#### SIG-independently-reproduce-SRC-0382

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0382 / V1 lines 1436-1438

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Reproduce using a materially independent evidence or execution path.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-independently-reproduce-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independently reproduce" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENTLY-REPRODUCED

ID: `LEX-independently-reproduced`. Roles: modifier_surface, status.

Source forms: `INDEPENDENTLY REPRODUCED`, `independently reproduced`.

#### SIG-independently-reproduced-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independently reproduced" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-independently-reproduced-SRC-0541

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0541 / V1 lines 2756-2758

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: A materially independent path reproduced the result.

Assessment dimension: verification_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDEPENDENTLY-VERIFY

ID: `LEX-independently-verify`. Roles: modifier_surface.

Source forms: `independently verify`.

#### SIG-independently-verify-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "independently verify" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INDUCE

ID: `LEX-induce`. Roles: specialized_operator.

Source forms: `INDUCE`.

#### SIG-induce-SRC-0179

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0179 / V1 lines 723-725

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer broader regularities from examples.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INFER

ID: `LEX-infer`. Roles: family.

Source forms: `INFER`.

#### SIG-infer-SRC-0177

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0177 / V1 lines 716-719

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Derive claims not directly observed.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INFINITE

ID: `LEX-infinite`. Roles: modifier_surface.

Source forms: `infinite`.

#### SIG-infinite-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "infinite" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INFORMAL

ID: `LEX-informal`. Roles: modifier_surface.

Source forms: `informal`.

#### SIG-informal-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "informal" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-informal-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "informal" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INFORMAL-REASONING

ID: `LEX-informal-reasoning`. Roles: modifier_surface.

Source forms: `informal reasoning`.

#### SIG-informal-reasoning-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "informal reasoning" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INGEST

ID: `LEX-ingest`. Roles: specialized_operator.

Source forms: `INGEST`.

#### SIG-ingest-SRC-0045

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0045 / V1 lines 276-278

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Load material into active context.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INITIATIVE-TAKING

ID: `LEX-initiative-taking`. Roles: modifier_surface.

Source forms: `initiative-taking`.

#### SIG-initiative-taking-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "initiative-taking" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INSPECT

ID: `LEX-inspect`. Roles: family.

Source forms: `INSPECT`.

#### SIG-inspect-SRC-0056

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0056 / V1 lines 310-317

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Expose properties without silently converting observation into inference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INSTALL

ID: `LEX-install`. Roles: specialized_operator.

Source forms: `INSTALL`.

#### SIG-install-SRC-0361

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0361 / V1 lines 1352-1354

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Add software or capability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INSTANTANEOUS

ID: `LEX-instantaneous`. Roles: modifier_surface.

Source forms: `instantaneous`.

#### SIG-instantaneous-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "instantaneous" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTEGRATE

ID: `LEX-integrate`. Roles: specialized_operator.

Source forms: `INTEGRATE`.

#### SIG-integrate-SRC-0332

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0332 / V1 lines 1253-1255

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Combine while preserving interactions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTEGRATION-TEST

ID: `LEX-integration-test`. Roles: specialized_operator.

Source forms: `INTEGRATION-TEST`.

#### SIG-integration-test-SRC-0232

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0232 / V1 lines 920-922

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test interactions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTENSIVE

ID: `LEX-intensive`. Roles: modifier_surface.

Source forms: `intensive`.

#### SIG-intensive-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "intensive" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTENTIONALLY-LOOSE

ID: `LEX-intentionally-loose`. Roles: modifier_surface.

Source forms: `intentionally loose`.

#### SIG-intentionally-loose-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "intentionally loose" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTENTIONALLY-RANDOM

ID: `LEX-intentionally-random`. Roles: modifier_surface.

Source forms: `intentionally random`.

#### SIG-intentionally-random-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "intentionally random" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTERPOLATE

ID: `LEX-interpolate`. Roles: specialized_operator.

Source forms: `INTERPOLATE`.

#### SIG-interpolate-SRC-0144

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0144 / V1 lines 598-600

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Fill intermediate cases.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTERPRET

ID: `LEX-interpret`. Roles: specialized_operator.

Source forms: `INTERPRET`.

#### SIG-interpret-SRC-0028

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0028 / V1 lines 221-223

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Assign semantic meaning to an expression.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-interpret-SRC-0193

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0193 / V1 lines 765-767

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Assign semantic meaning.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTERPRETIVE

ID: `LEX-interpretive`. Roles: modifier_surface.

Source forms: `interpretive`.

#### SIG-interpretive-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "interpretive" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTERSECT

ID: `LEX-intersect`. Roles: specialized_operator.

Source forms: `INTERSECT`.

#### SIG-intersect-SRC-0170

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0170 / V1 lines 686-688

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Retain common members.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INTERVENTION-SUPPORTED-CAUSATION

ID: `LEX-intervention-supported-causation`. Roles: modifier_surface.

Source forms: `intervention-supported causation`.

#### SIG-intervention-supported-causation-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "intervention-supported causation" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVALIDATE

ID: `LEX-invalidate`. Roles: specialized_operator.

Source forms: `INVALIDATE`.

#### SIG-invalidate-SRC-0258

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0258 / V1 lines 1008-1010

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Remove unsupported status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVARIANT

ID: `LEX-invariant`. Roles: modifier_surface.

Source forms: `invariant`.

#### SIG-invariant-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "invariant" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVARIANT-ACROSS-DECLARED-LIVE-CASES

ID: `LEX-invariant-across-declared-live-cases`. Roles: modifier_surface.

Source forms: `invariant across declared live cases`.

#### SIG-invariant-across-declared-live-cases-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "invariant across declared live cases" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVENTIVE

ID: `LEX-inventive`. Roles: modifier_surface.

Source forms: `inventive`.

#### SIG-inventive-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "inventive" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVENTORY

ID: `LEX-inventory`. Roles: specialized_operator.

Source forms: `INVENTORY`.

#### SIG-inventory-SRC-0067

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0067 / V1 lines 348-350

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Enumerate currently present objects.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVESTIGATE

ID: `LEX-investigate`. Roles: macro.

Source forms: `INVESTIGATE`.

#### SIG-investigate-SRC-0476

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0476 / V1 lines 1742-1745

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: ACQUIRE -> INSPECT -> HYPOTHESIZE -> TEST -> UPDATE

Macro source expression: `ACQUIRE -> INSPECT -> HYPOTHESIZE -> TEST -> UPDATE`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### INVOKE

ID: `LEX-invoke`. Roles: specialized_operator.

Source forms: `INVOKE`.

#### SIG-invoke-SRC-0365

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0365 / V1 lines 1364-1366

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Call a capability.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IRREDUCIBLE

ID: `LEX-irreducible`. Roles: modifier_surface.

Source forms: `irreducible`.

#### SIG-irreducible-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "irreducible" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IRREDUCIBLE-DEPENDENCY-DEPTH

ID: `LEX-irreducible-dependency-depth`. Roles: modifier_surface.

Source forms: `irreducible dependency depth`.

#### SIG-irreducible-dependency-depth-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "irreducible dependency depth" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### IRREVERSIBLE-ACTION

ID: `LEX-irreversible-action`. Roles: modifier_surface.

Source forms: `irreversible action`.

#### SIG-irreversible-action-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "irreversible action" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ISOLATE

ID: `LEX-isolate`. Roles: specialized_operator.

Source forms: `ISOLATE`.

#### SIG-isolate-SRC-0120

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0120 / V1 lines 511-513

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Separate one variable, fault, dependency, or component.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ITERATE

ID: `LEX-iterate`. Roles: control_operator.

Source forms: `ITERATE`.

#### SIG-iterate-SRC-0396

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0396 / V1 lines 1491-1493

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Use prior outputs for another cycle.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### JUDGE

ID: `LEX-judge`. Roles: specialized_operator.

Source forms: `JUDGE`.

#### SIG-judge-SRC-0276

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0276 / V1 lines 1068-1070

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Reach an evaluative conclusion.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LATTICE

ID: `LEX-lattice`. Roles: specialized_operator.

Source forms: `LATTICE`.

#### SIG-lattice-SRC-0094

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0094 / V1 lines 431-433

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent partially ordered relationships.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LEAVE-NO-STONE-UNTURNED

ID: `LEX-leave-no-stone-unturned`. Roles: modifier_surface.

Source forms: `leave no stone unturned`.

#### SIG-leave-no-stone-unturned-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "leave no stone unturned" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LIGHTWEIGHT

ID: `LEX-lightweight`. Roles: modifier_surface.

Source forms: `lightweight`.

#### SIG-lightweight-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "lightweight" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LINE-BY-LINE

ID: `LEX-line-by-line`. Roles: modifier_surface.

Source forms: `line-by-line`.

#### SIG-line-by-line-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "line-by-line" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LINT

ID: `LEX-lint`. Roles: specialized_operator.

Source forms: `LINT`.

#### SIG-lint-SRC-0242

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0242 / V1 lines 950-952

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Apply static structural rules.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LITERAL

ID: `LEX-literal`. Roles: modifier_surface.

Source forms: `literal`.

#### SIG-literal-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "literal" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-literal-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "literal" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LITERAL-REPRODUCTION

ID: `LEX-literal-reproduction`. Roles: modifier_surface.

Source forms: `literal reproduction`.

#### SIG-literal-reproduction-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "literal reproduction" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LITERAL-TOKEN/VALUE

ID: `LEX-literal-token-value`. Roles: modifier_surface.

Source forms: `literal token/value`.

#### SIG-literal-token-value-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "literal token/value" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOCALIZE

ID: `LEX-localize`. Roles: communication_operator, context_specific_operator, specialized_operator.

Source forms: `LOCALIZE`.

#### SIG-localize-P-audience

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Adapt content for a region or audience while preserving protected meanings.

Evidence required: Source-target comparison and audience requirements.

Status rule: Localized artifact with scoped fidelity checks.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Localize units and terminology for the specified audience.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-localize-P-fault

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `SPLIT`. Input roles: `SYSTEM`. Output roles: `REPRESENTATION`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `SPLIT`.

Transition or retained definition: Narrow an observed fault to a region of a system.

Evidence required: Trace and isolation evidence.

Status rule: Fault region identified, root cause not implied.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Localize the first malformed message to one pipeline stage.

Abstract principle: Separate components or cases with a declared partition or decomposition relation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-localize-SRC-0125

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0125 / V1 lines 526-528

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Narrow an effect or fault to a smaller region.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-localize-SRC-0468

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0468 / V1 lines 1715-1717

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Adapt to regional context.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOCATE

ID: `LEX-locate`. Roles: specialized_operator.

Source forms: `LOCATE`.

#### SIG-locate-SRC-0038

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0038 / V1 lines 255-257

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Determine where something exists.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOCK

ID: `LEX-lock`. Roles: control_operator.

Source forms: `LOCK`.

#### SIG-lock-SRC-0422

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0422 / V1 lines 1569-1571

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Prevent conflicting concurrent state changes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOGIC

ID: `LEX-logic`. Roles: specialized_operator.

Source forms: `LOGIC`.

#### SIG-logic-SRC-0097

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0097 / V1 lines 440-442

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent propositions and relations formally.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOOP

ID: `LEX-loop`. Roles: control_operator.

Source forms: `LOOP`.

#### SIG-loop-SRC-0395

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0395 / V1 lines 1488-1490

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Repeat.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOOSE

ID: `LEX-loose`. Roles: modifier_surface.

Source forms: `loose`.

#### SIG-loose-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "loose" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOW-COST

ID: `LEX-low-cost`. Roles: modifier_surface.

Source forms: `low-cost`.

#### SIG-low-cost-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "low-cost" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### LOWER-COST

ID: `LEX-lower-cost`. Roles: modifier_surface.

Source forms: `lower cost`.

#### SIG-lower-cost-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "lower cost" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MACHINE-CHECKABLE

ID: `LEX-machine-checkable`. Roles: modifier_surface.

Source forms: `machine-checkable`.

#### SIG-machine-checkable-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "machine-checkable" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MAP

ID: `LEX-map`. Roles: specialized_operator.

Source forms: `MAP`.

#### SIG-map-SRC-0077

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0077 / V1 lines 380-382

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent entities and relations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MATCH

ID: `LEX-match`. Roles: specialized_operator.

Source forms: `MATCH`.

#### SIG-match-SRC-0156

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0156 / V1 lines 644-646

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Assess correspondence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MATHEMATICALLY-FORMAL

ID: `LEX-mathematically-formal`. Roles: modifier_surface.

Source forms: `mathematically formal`.

#### SIG-mathematically-formal-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "mathematically formal" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MATRIX

ID: `LEX-matrix`. Roles: specialized_operator.

Source forms: `MATRIX`.

#### SIG-matrix-SRC-0080

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0080 / V1 lines 389-391

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent two-dimensional relations or cross-products.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MAXIMAL

ID: `LEX-maximal`. Roles: modifier_surface.

Source forms: `maximal`.

#### SIG-maximal-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "maximal" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MAXIMALLY

ID: `LEX-maximally`. Roles: modifier_surface.

Source forms: `maximally`.

#### SIG-maximally-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "maximally" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MAXIMIZE

ID: `LEX-maximize`. Roles: specialized_operator.

Source forms: `MAXIMIZE`.

#### SIG-maximize-SRC-0315

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0315 / V1 lines 1202-1204

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Increase quantity.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MAXIMUM-POSSIBLE

ID: `LEX-maximum-possible`. Roles: modifier_surface.

Source forms: `maximum possible`.

#### SIG-maximum-possible-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "maximum possible" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MAY

ID: `LEX-may`. Roles: constraint_surface.

Source forms: `may`.

#### SIG-may-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "may" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MEASURE

ID: `LEX-measure`. Roles: specialized_operator.

Source forms: `MEASURE`.

#### SIG-measure-SRC-0060

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0060 / V1 lines 327-329

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Produce a value under a measurement procedure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MECHANISM-HYPOTHESIS

ID: `LEX-mechanism-hypothesis`. Roles: modifier_surface.

Source forms: `mechanism hypothesis`.

#### SIG-mechanism-hypothesis-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "mechanism hypothesis" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MERGE

ID: `LEX-merge`. Roles: specialized_operator.

Source forms: `MERGE`.

#### SIG-merge-SRC-0175

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0175 / V1 lines 701-713

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Collapse states only after required equivalence is established.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-merge-SRC-0334

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0334 / V1 lines 1259-1261

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Collapse after equivalence or reconciliation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### META-PRINCIPLE

ID: `LEX-meta-principle`. Roles: modifier_surface.

Source forms: `meta-principle`.

#### SIG-meta-principle-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "meta-principle" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### METAMORPHIC-TEST

ID: `LEX-metamorphic-test`. Roles: specialized_operator.

Source forms: `METAMORPHIC-TEST`.

#### SIG-metamorphic-test-SRC-0237

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0237 / V1 lines 935-937

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test relationships expected to hold across transformed inputs.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### METHODOLOGICALLY-DISTINCT-SOURCES

ID: `LEX-methodologically-distinct-sources`. Roles: modifier_surface.

Source forms: `methodologically distinct sources`.

#### SIG-methodologically-distinct-sources-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "methodologically distinct sources" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MIGRATE

ID: `LEX-migrate`. Roles: macro, specialized_operator.

Source forms: `MIGRATE`.

#### SIG-migrate-SRC-0363

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0363 / V1 lines 1358-1360

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Transfer state between systems.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-migrate-SRC-0492

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0492 / V1 lines 1806-1809

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: INSPECT -> MAP -> TRANSFORM -> ACT -> RECONCILE -> VERIFY

Macro source expression: `INSPECT -> MAP -> TRANSFORM -> ACT -> RECONCILE -> VERIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MINIMAL

ID: `LEX-minimal`. Roles: modifier_surface.

Source forms: `minimal`.

#### SIG-minimal-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "minimal" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MINIMALLY-SUFFICIENT

ID: `LEX-minimally-sufficient`. Roles: context_bound_attribute_surface.

Source forms: `minimally sufficient`.

#### SIG-minimally-sufficient-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "minimally sufficient" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MINIMAX-EVALUATE

ID: `LEX-minimax-evaluate`. Roles: specialized_operator.

Source forms: `MINIMAX-EVALUATE`.

#### SIG-minimax-evaluate-SRC-0290

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0290 / V1 lines 1110-1112

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Optimize worst-case outcomes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MINIMIZE

ID: `LEX-minimize`. Roles: specialized_operator.

Source forms: `MINIMIZE`.

#### SIG-minimize-SRC-0314

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0314 / V1 lines 1199-1201

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Reduce quantity.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MINIMUM-VIABLE-WORK

ID: `LEX-minimum-viable-work`. Roles: modifier_surface.

Source forms: `minimum viable work`.

#### SIG-minimum-viable-work-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "minimum viable work" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MITIGATE

ID: `LEX-mitigate`. Roles: proposed_procedure.

Source forms: `MITIGATE`.

#### SIG-mitigate-P-source-macro-binding

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Construct or revise a candidate to reduce a specified failure likelihood, impact or exposure; acceptance requires a measured or supported reduction and preservation of constraints.

Evidence required: Apply the common contract to the explicitly bound target, property and scope.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Closure rule: Use the common contract and preserve remaining obligations.

Concrete instance: Add a reversible fallback to reduce impact of a failed evidence source, then test that failure case.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MODEL

ID: `LEX-model`. Roles: context_specific_operator, specialized_operator.

Source forms: `MODEL`.

#### SIG-model-P-construct

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `EXPAND`. Input roles: `RULE`. Output roles: `CANDIDATE`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `EXPAND`.

Transition or retained definition: Construct a structure satisfying the declared axioms.

Evidence required: Interpretation of symbols and satisfaction checks.

Status rule: Model witness under the formal system.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Construct a finite model satisfying the supplied constraints.

Abstract principle: Extend a specified candidate frontier without upgrading generated claims to observed facts.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-model-P-predict

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `PREDICTIVE_PERFORMANCE`. Contract: `INFER`.

Transition or retained definition: Specify or estimate a mapping from information to predictions with a horizon.

Evidence required: Training and evaluation boundaries and estimation assumptions.

Status rule: Predictive candidate until measured against its criterion.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Model next-period demand without including future inputs.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-model-P-represent

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `REPRESENT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Construct a representation whose protected relationships and abstractions are explicit.

Evidence required: Source-to-model mapping and assumptions.

Status rule: Model constructed, not yet empirically validated.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Model component dependencies as a graph.

Abstract principle: Re-encode protected content under an explicit preservation projection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-model-SRC-0078

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0078 / V1 lines 383-385

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Construct a simplified operational representation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MODEL-CHECK

ID: `LEX-model-check`. Roles: specialized_operator.

Source forms: `MODEL-CHECK`.

#### SIG-model-check-SRC-0244

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0244 / V1 lines 956-958

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Evaluate formal system states against properties.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MODIFY

ID: `LEX-modify`. Roles: specialized_operator.

Source forms: `MODIFY`.

#### SIG-modify-SRC-0350

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0350 / V1 lines 1319-1321

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Change specified properties.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MONITOR

ID: `LEX-monitor`. Roles: specialized_operator.

Source forms: `MONITOR`.

#### SIG-monitor-SRC-0050

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0050 / V1 lines 291-293

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Repeatedly acquire observations from a changing source.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MOVE

ID: `LEX-move`. Roles: specialized_operator.

Source forms: `MOVE`.

#### SIG-move-SRC-0352

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0352 / V1 lines 1325-1327

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Change location.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MULTIPLE-SOURCES

ID: `LEX-multiple-sources`. Roles: modifier_surface.

Source forms: `multiple sources`.

#### SIG-multiple-sources-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "multiple sources" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MUST

ID: `LEX-must`. Roles: constraint_surface.

Source forms: `must`.

#### SIG-must-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "must" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MUST-NOT

ID: `LEX-must-not`. Roles: constraint_surface.

Source forms: `must not`.

#### SIG-must-not-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "must not" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### MUTATE

ID: `LEX-mutate`. Roles: specialized_operator.

Source forms: `MUTATE`.

#### SIG-mutate-SRC-0148

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0148 / V1 lines 610-612

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Alter candidate components to explore nearby possibilities.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NARROW

ID: `LEX-narrow`. Roles: modifier_surface.

Source forms: `narrow`.

#### SIG-narrow-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "narrow" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-narrow-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "narrow" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NARROW-ALTERNATIVES

ID: `LEX-narrow-alternatives`. Roles: modifier_surface.

Source forms: `narrow alternatives`.

#### SIG-narrow-alternatives-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "narrow alternatives" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NEGATIVE-EXTREME-TAIL-LEXICON

ID: `LEX-negative-extreme-tail-lexicon`. Roles: semantic_policy_or_attribute.

Source forms: `NEGATIVE EXTREME TAIL LEXICON`.

#### SIG-negative-extreme-tail-lexicon-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate negative extreme tail lexicon using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NEGATIVE-TEST

ID: `LEX-negative-test`. Roles: specialized_operator.

Source forms: `NEGATIVE-TEST`.

#### SIG-negative-test-SRC-0214

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0214 / V1 lines 851-853

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Test invalid or prohibited cases.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NEUTRAL

ID: `LEX-neutral`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `neutral`.

#### SIG-neutral-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "neutral" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-neutral-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "neutral" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NEVER

ID: `LEX-never`. Roles: constraint_surface.

Source forms: `never`.

#### SIG-never-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "never" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NEVER-STOP-UNTIL-PERFECT

ID: `LEX-never-stop-until-perfect`. Roles: modifier_surface.

Source forms: `never stop until perfect`.

#### SIG-never-stop-until-perfect-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "never stop until perfect" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NEVER-WRONG

ID: `LEX-never-wrong`. Roles: modifier_surface.

Source forms: `never wrong`.

#### SIG-never-wrong-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "never wrong" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NO-VERIFICATION

ID: `LEX-no-verification`. Roles: modifier_surface.

Source forms: `no verification`.

#### SIG-no-verification-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "no verification" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NORMAL

ID: `LEX-normal`. Roles: modifier_surface.

Source forms: `normal`.

#### SIG-normal-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normal-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NORMAL-EXPLORATION

ID: `LEX-normal-exploration`. Roles: modifier_surface.

Source forms: `normal exploration`.

#### SIG-normal-exploration-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal exploration" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NORMAL-OPERATIONAL-LEVEL

ID: `LEX-normal-operational-level`. Roles: modifier_surface.

Source forms: `normal operational level`.

#### SIG-normal-operational-level-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "normal operational level" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NORMALIZE

ID: `LEX-normalize`. Roles: specialized_operator.

Source forms: `NORMALIZE`.

#### SIG-normalize-SRC-0102

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0102 / V1 lines 455-457

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Convert equivalent variants into a common form.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-normalize-SRC-0327

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0327 / V1 lines 1238-1240

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Transform to shared scale or representation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NOVEL

ID: `LEX-novel`. Roles: context_bound_attribute_surface.

Source forms: `novel`.

#### SIG-novel-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "novel" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### NOVELTY

ID: `LEX-novelty`. Roles: semantic_policy_or_attribute.

Source forms: `NOVELTY`.

#### SIG-novelty-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate novelty using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OBSERVE

ID: `LEX-observe`. Roles: context_specific_operator, specialized_operator.

Source forms: `OBSERVE`.

#### SIG-observe-P-phenomenon

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INSPECT`. Input roles: `WORLD_STATE`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `INSPECT`.

Transition or retained definition: Measure a target property using a stated observation procedure.

Evidence required: Instrument or observation record and its limitations.

Status rule: Observed measurement with scope and uncertainty.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Observe the endpoint response after the operation.

Abstract principle: Record accessible properties with an observation procedure and a stated boundary.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-observe-P-record

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Read what a record states and attribute it to that record.

Evidence required: Identified source and exact content.

Status rule: Observed source content, not necessarily the reported phenomenon.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Observe that an agent report says the job completed.

Abstract principle: Record accessible properties with an observation procedure and a stated boundary.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-observe-SRC-0059

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0059 / V1 lines 324-326

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Record directly accessible properties or events.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OBSERVED

ID: `LEX-observed`. Roles: status.

Source forms: `OBSERVED`.

#### SIG-observed-SRC-0533

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0533 / V1 lines 2732-2734

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Result was inspected.

Assessment dimension: execution_and_observation_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONE-CASE

ID: `LEX-one-case`. Roles: modifier_surface.

Source forms: `one case`.

#### SIG-one-case-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "one case" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONE-LINE

ID: `LEX-one-line`. Roles: modifier_surface.

Source forms: `one-line`.

#### SIG-one-line-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "one-line" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-one-line-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "one-line" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONE-SOURCE

ID: `LEX-one-source`. Roles: modifier_surface.

Source forms: `one source`.

#### SIG-one-source-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "one source" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONE-SOURCE-CLASS

ID: `LEX-one-source-class`. Roles: modifier_surface.

Source forms: `one source class`.

#### SIG-one-source-class-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "one source class" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONE-WORD

ID: `LEX-one-word`. Roles: modifier_surface.

Source forms: `one-word`.

#### SIG-one-word-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "one-word" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONLY

ID: `LEX-only`. Roles: constraint_surface.

Source forms: `only`.

#### SIG-only-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "only" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ONTOLOGY

ID: `LEX-ontology`. Roles: specialized_operator.

Source forms: `ONTOLOGY`.

#### SIG-ontology-SRC-0091

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0091 / V1 lines 422-424

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent types, entities, properties, and semantic relationships.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OPEN

ID: `LEX-open`. Roles: status.

Source forms: `OPEN`.

#### SIG-open-SRC-0549

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0549 / V1 lines 2780-2782

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Consequential uncertainty exists with no currently established adequate resolution path.

Assessment dimension: resolution_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OPERATIONALIZE

ID: `LEX-operationalize`. Roles: specialized_operator.

Source forms: `OPERATIONALIZE`.

#### SIG-operationalize-SRC-0029

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0029 / V1 lines 224-226

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Convert an abstract concept into measurable or executable conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OPTIMIZE

ID: `LEX-optimize`. Roles: context_specific_operator, macro, specialized_operator.

Source forms: `OPTIMIZE`.

#### SIG-optimize-P-global

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SELECT`.

Transition or retained definition: Select a global optimum only with a specified feasible domain and supporting bound or exhaustive comparison.

Evidence required: Objective, constraints, candidate and optimality certificate.

Status rule: Global optimum only within the certified domain.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Find the minimum of a fully enumerated finite cost table.

Abstract principle: Return an authorized choice, robust shared option or explicit conditional alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-optimize-P-heuristic

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TRANSFORM`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TRANSFORM`.

Transition or retained definition: Improve a candidate under a bounded search without claiming global optimality.

Evidence required: Baseline, new metric and preserved constraints.

Status rule: Measured improvement or local candidate.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Optimize a design by comparing several feasible variants.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-optimize-SRC-0313

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0313 / V1 lines 1196-1198

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Improve a declared objective.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-optimize-SRC-0485

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0485 / V1 lines 1778-1781

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: DEFINE OBJECTIVE -> DEFINE CONSTRAINTS -> EXPAND -> EVALUATE -> SELECT -> TRANSFORM -> TEST -> ITERATE

Macro source expression: `DEFINE OBJECTIVE -> DEFINE CONSTRAINTS -> EXPAND -> EVALUATE -> SELECT -> TRANSFORM -> TEST -> ITERATE`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OPTIONAL

ID: `LEX-optional`. Roles: constraint_surface.

Source forms: `optional`.

#### SIG-optional-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "optional" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORCHESTRATE

ID: `LEX-orchestrate`. Roles: control_operator.

Source forms: `ORCHESTRATE`.

#### SIG-orchestrate-SRC-0404

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0404 / V1 lines 1515-1517

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Coordinate multiple components.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORDINARY

ID: `LEX-ordinary`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `ordinary`.

#### SIG-ordinary-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "ordinary" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-ordinary-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "ordinary" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORTHOGONAL

ID: `LEX-orthogonal`. Roles: modifier_surface.

Source forms: `orthogonal`.

#### SIG-orthogonal-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "orthogonal" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORTHOGONAL-EVIDENCE

ID: `LEX-orthogonal-evidence`. Roles: modifier_surface.

Source forms: `orthogonal evidence`.

#### SIG-orthogonal-evidence-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "orthogonal evidence" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORTHOGONAL-VERIFICATION

ID: `LEX-orthogonal-verification`. Roles: modifier_surface.

Source forms: `orthogonal verification`.

#### SIG-orthogonal-verification-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "orthogonal verification" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORTHOGONAL-VERIFY

ID: `LEX-orthogonal-verify`. Roles: specialized_operator.

Source forms: `ORTHOGONAL-VERIFY`.

#### SIG-orthogonal-verify-SRC-0380

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0380 / V1 lines 1430-1432

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Use a verification mechanism with materially different failure modes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ORTHOGONALLY-VERIFIED

ID: `LEX-orthogonally-verified`. Roles: status.

Source forms: `ORTHOGONALLY VERIFIED`.

#### SIG-orthogonally-verified-SRC-0540

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0540 / V1 lines 2753-2755

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Verification used a materially different failure mode.

Assessment dimension: verification_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### OUTLINE

ID: `LEX-outline`. Roles: communication_operator, specialized_operator.

Source forms: `OUTLINE`.

#### SIG-outline-SRC-0111

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0111 / V1 lines 482-484

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Expose hierarchical structure while suppressing detail.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-outline-SRC-0462

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0462 / V1 lines 1697-1699

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Represent structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PAINSTAKING

ID: `LEX-painstaking`. Roles: modifier_surface.

Source forms: `painstaking`.

#### SIG-painstaking-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "painstaking" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-painstaking-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "painstaking" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-painstaking-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "painstaking" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARALLELIZE

ID: `LEX-parallelize`. Roles: control_operator.

Source forms: `PARALLELIZE`.

#### SIG-parallelize-SRC-0402

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0402 / V1 lines 1509-1511

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Execute independent work concurrently.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARAMETERIZE

ID: `LEX-parameterize`. Roles: specialized_operator.

Source forms: `PARAMETERIZE`.

#### SIG-parameterize-SRC-0025

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0025 / V1 lines 212-214

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Replace fixed values with explicit variables.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARAPHRASE

ID: `LEX-paraphrase`. Roles: communication_operator.

Source forms: `PARAPHRASE`.

#### SIG-paraphrase-SRC-0456

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0456 / V1 lines 1679-1681

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Restate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARETO-COMPARE

ID: `LEX-pareto-compare`. Roles: specialized_operator.

Source forms: `PARETO-COMPARE`.

#### SIG-pareto-compare-SRC-0174

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0174 / V1 lines 698-700

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Identify candidates not dominated across multiple objectives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARSE

ID: `LEX-parse`. Roles: specialized_operator.

Source forms: `PARSE`.

#### SIG-parse-SRC-0027

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0027 / V1 lines 218-220

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Transform surface syntax into structural components.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARTIAL

ID: `LEX-partial`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `partial`.

#### SIG-partial-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "partial" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-partial-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "partial" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PARTITION

ID: `LEX-partition`. Roles: specialized_operator.

Source forms: `PARTITION`.

#### SIG-partition-SRC-0117

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0117 / V1 lines 502-504

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Divide a set into mutually exclusive groups.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PASSED

ID: `LEX-passed`. Roles: status.

Source forms: `PASSED`.

#### SIG-passed-SRC-0537

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0537 / V1 lines 2744-2746

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Declared test criterion was satisfied.

Assessment dimension: check_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PATCH

ID: `LEX-patch`. Roles: specialized_operator.

Source forms: `PATCH`.

#### SIG-patch-SRC-0255

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0255 / V1 lines 999-1001

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Apply a localized correction.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PATTERN

ID: `LEX-pattern`. Roles: modifier_surface.

Source forms: `pattern`.

#### SIG-pattern-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "pattern" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PAUSE

ID: `LEX-pause`. Roles: control_operator.

Source forms: `PAUSE`.

#### SIG-pause-SRC-0412

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0412 / V1 lines 1539-1541

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Suspend without discarding state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PERFECT

ID: `LEX-perfect`. Roles: modifier_surface.

Source forms: `perfect`.

#### SIG-perfect-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "perfect" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PERMISSIVE

ID: `LEX-permissive`. Roles: modifier_surface.

Source forms: `permissive`.

#### SIG-permissive-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "permissive" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-permissive-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "permissive" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PERMITTED

ID: `LEX-permitted`. Roles: constraint_surface.

Source forms: `permitted`.

#### SIG-permitted-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "permitted" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PERMUTE

ID: `LEX-permute`. Roles: specialized_operator.

Source forms: `PERMUTE`.

#### SIG-permute-SRC-0140

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0140 / V1 lines 586-588

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Rearrange existing components.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PERSUADE

ID: `LEX-persuade`. Roles: communication_operator.

Source forms: `PERSUADE`.

#### SIG-persuade-SRC-0472

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0472 / V1 lines 1727-1731

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Optimize communication for belief or action change.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PIPELINE

ID: `LEX-pipeline`. Roles: control_operator.

Source forms: `PIPELINE`.

#### SIG-pipeline-SRC-0394

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0394 / V1 lines 1485-1487

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Create persistent stages.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PLAIN

ID: `LEX-plain`. Roles: modifier_surface.

Source forms: `plain`.

#### SIG-plain-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "plain" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PLAN

ID: `LEX-plan`. Roles: macro.

Source forms: `PLAN`.

#### SIG-plan-SRC-0479

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0479 / V1 lines 1754-1757

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: COMPILE -> SPLIT -> DEPENDENCY-MAP -> EVALUATE -> SEQUENCE

Macro source expression: `COMPILE -> SPLIT -> DEPENDENCY-MAP -> EVALUATE -> SEQUENCE`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### POLL

ID: `LEX-poll`. Roles: specialized_operator.

Source forms: `POLL`.

#### SIG-poll-SRC-0053

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0053 / V1 lines 300-302

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Repeatedly query a source for changes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### POSITIVE-EXTREME-TAIL-LEXICON

ID: `LEX-positive-extreme-tail-lexicon`. Roles: semantic_policy_or_attribute.

Source forms: `POSITIVE EXTREME TAIL LEXICON`.

#### SIG-positive-extreme-tail-lexicon-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate positive extreme tail lexicon using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRECISE

ID: `LEX-precise`. Roles: modifier_surface.

Source forms: `precise`.

#### SIG-precise-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "precise" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRECISION

ID: `LEX-precision`. Roles: execution_modifier.

Source forms: `PRECISION`.

#### SIG-precision-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate precision using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PREDICATE-BY-PREDICATE

ID: `LEX-predicate-by-predicate`. Roles: modifier_surface.

Source forms: `predicate-by-predicate`.

#### SIG-predicate-by-predicate-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "predicate-by-predicate" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PREDICT

ID: `LEX-predict`. Roles: specialized_operator.

Source forms: `PREDICT`.

#### SIG-predict-SRC-0187

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0187 / V1 lines 747-749

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Infer an unobserved or future result.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PREFER

ID: `LEX-prefer`. Roles: constraint_surface.

Source forms: `prefer`.

#### SIG-prefer-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "prefer" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PREFER-RESOLUTION

ID: `LEX-prefer-resolution`. Roles: modifier_surface.

Source forms: `prefer resolution`.

#### SIG-prefer-resolution-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "prefer resolution" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PREMORTEM

ID: `LEX-premortem`. Roles: macro, specialized_operator.

Source forms: `PREMORTEM`.

#### SIG-premortem-SRC-0210

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0210 / V1 lines 839-841

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Assume failure and derive possible causes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-premortem-SRC-0486

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0486 / V1 lines 1782-1785

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: ASSUME FAILURE -> EXPAND FAILURE PATHS -> EVALUATE -> MITIGATE

Macro source expression: `ASSUME FAILURE -> EXPAND FAILURE PATHS -> EVALUATE -> MITIGATE`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PREPARED

ID: `LEX-prepared`. Roles: status.

Source forms: `PREPARED`.

#### SIG-prepared-SRC-0530

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0530 / V1 lines 2723-2725

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Prerequisites exist.

Assessment dimension: artifact_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRESERVE

ID: `LEX-preserve`. Roles: specialized_operator.

Source forms: `PRESERVE`.

#### SIG-preserve-SRC-0303

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0303 / V1 lines 1155-1157

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Explicitly prevent information loss.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRESERVE-ALL-NON-EQUIVALENT-LIVE-CLASSES

ID: `LEX-preserve-all-non-equivalent-live-classes`. Roles: modifier_surface.

Source forms: `preserve all non-equivalent live classes`.

#### SIG-preserve-all-non-equivalent-live-classes-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "preserve all non-equivalent live classes" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRESERVE-ALTERNATIVES

ID: `LEX-preserve-alternatives`. Roles: modifier_surface.

Source forms: `preserve alternatives`.

#### SIG-preserve-alternatives-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "preserve alternatives" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRESUME

ID: `LEX-presume`. Roles: modifier_surface.

Source forms: `presume`.

#### SIG-presume-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "presume" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRINCIPLE

ID: `LEX-principle`. Roles: modifier_surface.

Source forms: `principle`.

#### SIG-principle-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "principle" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRIORITIZE

ID: `LEX-prioritize`. Roles: constraint_surface, control_operator, specialized_operator.

Source forms: `PRIORITIZE`, `prioritize`.

#### SIG-prioritize-SRC-0287

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0287 / V1 lines 1101-1103

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Order by urgency or importance.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-prioritize-SRC-0421

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0421 / V1 lines 1566-1568

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Control execution order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-prioritize-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "prioritize" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROACTIVE

ID: `LEX-proactive`. Roles: modifier_surface.

Source forms: `proactive`.

#### SIG-proactive-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "proactive" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROBE

ID: `LEX-probe`. Roles: specialized_operator.

Source forms: `PROBE`.

#### SIG-probe-SRC-0222

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0222 / V1 lines 881-883

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Perform a targeted low-cost discriminator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROFESSIONAL

ID: `LEX-professional`. Roles: modifier_surface.

Source forms: `professional`.

#### SIG-professional-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "professional" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROFILE

ID: `LEX-profile`. Roles: specialized_operator.

Source forms: `PROFILE`.

#### SIG-profile-SRC-0066

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0066 / V1 lines 345-347

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Measure a collection of properties.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROHIBITED

ID: `LEX-prohibited`. Roles: constraint_surface.

Source forms: `prohibited`.

#### SIG-prohibited-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "prohibited" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROJECT

ID: `LEX-project`. Roles: specialized_operator.

Source forms: `PROJECT`.

#### SIG-project-SRC-0191

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0191 / V1 lines 759-761

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Propagate assumptions into another state or period.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROOF-CARRYING

ID: `LEX-proof-carrying`. Roles: modifier_surface.

Source forms: `proof-carrying`.

#### SIG-proof-carrying-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "proof-carrying" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-proof-carrying-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "proof-carrying" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROOF-SYSTEM-FORMAL

ID: `LEX-proof-system-formal`. Roles: modifier_surface.

Source forms: `proof-system formal`.

#### SIG-proof-system-formal-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "proof-system formal" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROOFREAD

ID: `LEX-proofread`. Roles: communication_operator.

Source forms: `PROOFREAD`.

#### SIG-proofread-SRC-0459

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0459 / V1 lines 1688-1690

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Correct surface defects.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROPERTY-TEST

ID: `LEX-property-test`. Roles: specialized_operator.

Source forms: `PROPERTY-TEST`.

#### SIG-property-test-SRC-0236

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0236 / V1 lines 932-934

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test general invariants across cases.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROPOSED

ID: `LEX-proposed`. Roles: status.

Source forms: `PROPOSED`.

#### SIG-proposed-SRC-0528

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0528 / V1 lines 2717-2719

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Candidate exists.

Assessment dimension: artifact_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PROVE

ID: `LEX-prove`. Roles: context_specific_operator, specialized_operator.

Source forms: `PROVE`.

#### SIG-prove-P-empirical-request

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `PROPOSITION`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `VERIFY`.

Transition or retained definition: Interpret colloquial proof as an evidence request; do not equate empirical support with deductive entailment.

Evidence required: Observed data and an explicit empirical adequacy criterion.

Status rule: Empirically supported within scope, not universally proved.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Provide evidence that the intervention improved the measured outcome.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-prove-P-formal

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `PROPOSITION`. Output roles: `ARTIFACT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `INFER`.

Transition or retained definition: Derive the exact proposition under stated axioms and inference rules.

Evidence required: A derivation checked against the stated formalization.

Status rule: FORMALLY_VERIFIED only after checking, within the formal system.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Prove that a supplied finite relation is transitive.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-prove-SRC-0195

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0195 / V1 lines 771-773

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `INFER`.

Transition or retained definition: Derive formally under declared axioms and inference rules.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-prove-SRC-0385

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0385 / V1 lines 1445-1447

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `VERIFY`.

Transition or retained definition: Provide formal derivation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PRUNE

ID: `LEX-prune`. Roles: specialized_operator.

Source forms: `PRUNE`.

#### SIG-prune-SRC-0301

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0301 / V1 lines 1149-1151

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Remove branches.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### PUBLISH

ID: `LEX-publish`. Roles: specialized_operator.

Source forms: `PUBLISH`.

#### SIG-publish-SRC-0359

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0359 / V1 lines 1346-1348

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Make externally visible.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUALIFIED

ID: `LEX-qualified`. Roles: context_bound_attribute_surface.

Source forms: `qualified`.

#### SIG-qualified-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "qualified" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUERY

ID: `LEX-query`. Roles: specialized_operator.

Source forms: `QUERY`.

#### SIG-query-SRC-0041

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0041 / V1 lines 264-266

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Request information from an information-bearing system.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUESTION

ID: `LEX-question`. Roles: specialized_operator.

Source forms: `QUESTION`.

#### SIG-question-SRC-0202

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0202 / V1 lines 815-817

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Challenge an assumption or conclusion.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUESTION-EVERYTHING

ID: `LEX-question-everything`. Roles: modifier_surface.

Source forms: `question everything`.

#### SIG-question-everything-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "question everything" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUEUE

ID: `LEX-queue`. Roles: control_operator.

Source forms: `QUEUE`.

#### SIG-queue-SRC-0420

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0420 / V1 lines 1563-1565

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Order future operations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUICK

ID: `LEX-quick`. Roles: modifier_surface.

Source forms: `quick`.

#### SIG-quick-SRC-0503

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0503 / V1 lines 2072-2094

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "quick" on the DELIBERATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `DELIBERATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-quick-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "quick" on the SPEED axis under the bound requirements; do not infer achieved status from the request.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### QUOTE

ID: `LEX-quote`. Roles: communication_operator.

Source forms: `QUOTE`.

#### SIG-quote-SRC-0465

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0465 / V1 lines 1706-1708

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `ACQUIRE`.

Transition or retained definition: Reproduce exact source language.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RADICAL-EXPLORATION

ID: `LEX-radical-exploration`. Roles: modifier_surface.

Source forms: `radical exploration`.

#### SIG-radical-exploration-SRC-0502

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0502 / V1 lines 2049-2071

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "radical exploration" on the CREATIVITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `CREATIVITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RANK

ID: `LEX-rank`. Roles: specialized_operator.

Source forms: `RANK`.

#### SIG-rank-SRC-0273

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0273 / V1 lines 1059-1061

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Produce an ordering.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RATE

ID: `LEX-rate`. Roles: specialized_operator.

Source forms: `RATE`.

#### SIG-rate-SRC-0272

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0272 / V1 lines 1056-1058

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Assign scale values.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REACTIVE

ID: `LEX-reactive`. Roles: modifier_surface.

Source forms: `reactive`.

#### SIG-reactive-SRC-0506

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0506 / V1 lines 2137-2161

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "reactive" on the AUTONOMY axis under the bound requirements; do not infer achieved status from the request.

Axis: `AUTONOMY`. Destination: ControlPolicy constrained by authority and effect.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### READ

ID: `LEX-read`. Roles: specialized_operator.

Source forms: `READ`.

#### SIG-read-SRC-0057

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0057 / V1 lines 318-320

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Expose textual or structured contents.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REBASE

ID: `LEX-rebase`. Roles: specialized_operator.

Source forms: `REBASE`.

#### SIG-rebase-SRC-0264

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0264 / V1 lines 1026-1028

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Recompute from a changed foundation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECKLESS-COMMITMENT

ID: `LEX-reckless-commitment`. Roles: modifier_surface.

Source forms: `reckless commitment`.

#### SIG-reckless-commitment-SRC-0516

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0516 / V1 lines 2382-2402

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "reckless commitment" on the CONSERVATISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONSERVATISM`. Destination: SelectionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECOGNIZE

ID: `LEX-recognize`. Roles: specialized_operator.

Source forms: `RECOGNIZE`.

#### SIG-recognize-SRC-0064

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0064 / V1 lines 339-341

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Match against a known pattern.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECOMBINE

ID: `LEX-recombine`. Roles: specialized_operator.

Source forms: `RECOMBINE`.

#### SIG-recombine-SRC-0141

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0141 / V1 lines 589-591

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Construct alternatives from existing components.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECONCILE

ID: `LEX-reconcile`. Roles: specialized_operator.

Source forms: `RECONCILE`.

#### SIG-reconcile-SRC-0253

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0253 / V1 lines 993-995

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Resolve conflicting representations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECOVERABLE

ID: `LEX-recoverable`. Roles: modifier_surface.

Source forms: `recoverable`.

#### SIG-recoverable-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "recoverable" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECURSE

ID: `LEX-recurse`. Roles: control_operator.

Source forms: `RECURSE`.

#### SIG-recurse-SRC-0399

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0399 / V1 lines 1500-1502

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Apply to nested structures.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RECURSIVE

ID: `LEX-recursive`. Roles: modifier_surface.

Source forms: `recursive`.

#### SIG-recursive-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "recursive" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-recursive-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "recursive" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RED-TEAM

ID: `LEX-red-team`. Roles: modifier_surface, specialized_operator.

Source forms: `RED-TEAM`, `red-team`.

#### SIG-red-team-SRC-0207

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0207 / V1 lines 830-832

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Use an adversarial perspective.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-red-team-SRC-0500

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0500 / V1 lines 2012-2030

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "red-team" on the ADVERSARIAL axis under the bound requirements; do not infer achieved status from the request.

Axis: `ADVERSARIAL`. Destination: ChallengePolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REDUCE

ID: `LEX-reduce`. Roles: specialized_operator.

Source forms: `REDUCE`.

#### SIG-reduce-SRC-0335

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0335 / V1 lines 1262-1264

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Produce a smaller sufficient form.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REFACTOR

ID: `LEX-refactor`. Roles: macro, specialized_operator.

Source forms: `REFACTOR`.

#### SIG-refactor-SRC-0320

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0320 / V1 lines 1217-1219

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Change internal structure while preserving required behavior.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-refactor-SRC-0491

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0491 / V1 lines 1802-1805

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: INSPECT -> DEFINE PRESERVED BEHAVIOR -> TRANSFORM -> REGRESSION-TEST -> VERIFY

Macro source expression: `INSPECT -> DEFINE PRESERVED BEHAVIOR -> TRANSFORM -> REGRESSION-TEST -> VERIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REFINE

ID: `LEX-refine`. Roles: specialized_operator.

Source forms: `REFINE`.

#### SIG-refine-SRC-0267

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0267 / V1 lines 1035-1043

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Improve precision or fit.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-refine-SRC-0319

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0319 / V1 lines 1214-1216

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Increase precision or quality.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REFRAME

ID: `LEX-reframe`. Roles: specialized_operator.

Source forms: `REFRAME`.

#### SIG-reframe-SRC-0107

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0107 / V1 lines 470-472

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Change conceptual perspective.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REFRESH

ID: `LEX-refresh`. Roles: specialized_operator.

Source forms: `REFRESH`.

#### SIG-refresh-SRC-0256

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0256 / V1 lines 1002-1004

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Replace stale information.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REFUSE-UNSUPPORTED-COLLAPSE

ID: `LEX-refuse-unsupported-collapse`. Roles: modifier_surface.

Source forms: `refuse unsupported collapse`.

#### SIG-refuse-unsupported-collapse-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "refuse unsupported collapse" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REFUTE

ID: `LEX-refute`. Roles: specialized_operator.

Source forms: `REFUTE`.

#### SIG-refute-SRC-0206

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0206 / V1 lines 827-829

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Successfully defeat a proposition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REGRESSION-TEST

ID: `LEX-regression-test`. Roles: specialized_operator.

Source forms: `REGRESSION-TEST`.

#### SIG-regression-test-SRC-0235

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0235 / V1 lines 929-931

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test preservation of previously established behavior.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REGRET-EVALUATE

ID: `LEX-regret-evaluate`. Roles: specialized_operator.

Source forms: `REGRET-EVALUATE`.

#### SIG-regret-evaluate-SRC-0291

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0291 / V1 lines 1113-1121

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Compare opportunity loss against alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REJECT

ID: `LEX-reject`. Roles: specialized_operator.

Source forms: `REJECT`.

#### SIG-reject-SRC-0297

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0297 / V1 lines 1137-1139

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Exclude for failing a requirement.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REOPEN

ID: `LEX-reopen`. Roles: specialized_operator.

Source forms: `REOPEN`.

#### SIG-reopen-SRC-0261

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0261 / V1 lines 1017-1019

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Reactivate previously closed work.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPAIR

ID: `LEX-repair`. Roles: specialized_operator.

Source forms: `REPAIR`.

#### SIG-repair-SRC-0265

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0265 / V1 lines 1029-1031

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Restore validity.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPEAT

ID: `LEX-repeat`. Roles: control_operator.

Source forms: `REPEAT`.

#### SIG-repeat-SRC-0397

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0397 / V1 lines 1494-1496

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Execute again.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPLICATE

ID: `LEX-replicate`. Roles: specialized_operator.

Source forms: `REPLICATE`.

#### SIG-replicate-SRC-0229

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0229 / V1 lines 911-913

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Repeat through a materially independent implementation or setup.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-replicate-SRC-0383

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0383 / V1 lines 1439-1441

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Confirm through a distinct implementation, sample, system, or setup.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPORT

ID: `LEX-report`. Roles: specialized_operator.

Source forms: `REPORT`.

#### SIG-report-SRC-0437

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0437 / V1 lines 1616-1618

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Communicate findings and status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPRESENT

ID: `LEX-represent`. Roles: family.

Source forms: `REPRESENT`.

#### SIG-represent-SRC-0076

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0076 / V1 lines 376-379

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Change encoding so relevant structure becomes more visible or tractable.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPRODUCE

ID: `LEX-reproduce`. Roles: specialized_operator.

Source forms: `REPRODUCE`.

#### SIG-reproduce-SRC-0228

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0228 / V1 lines 908-910

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Repeat a procedure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-reproduce-SRC-0381

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0381 / V1 lines 1433-1435

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Repeat the same procedure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REPRODUCIBLE

ID: `LEX-reproducible`. Roles: modifier_surface.

Source forms: `reproducible`.

#### SIG-reproducible-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "reproducible" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REQUIRE

ID: `LEX-require`. Roles: constraint_surface, specialized_operator.

Source forms: `REQUIRE`, `require`.

#### SIG-require-SRC-0023

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0023 / V1 lines 206-208

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Make satisfaction of a condition mandatory.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-require-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "require" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REQUIREMENT-SATISFACTION

ID: `LEX-requirement-satisfaction`. Roles: modifier_surface.

Source forms: `requirement satisfaction`.

#### SIG-requirement-satisfaction-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "requirement satisfaction" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RESEARCH

ID: `LEX-research`. Roles: macro.

Source forms: `RESEARCH`.

#### SIG-research-SRC-0475

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0475 / V1 lines 1738-1741

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: COMPILE -> ACQUIRE -> INSPECT -> REPRESENT -> EXPAND -> COMPARE -> CHALLENGE -> SYNTHESIZE -> VERIFY

Macro source expression: `COMPILE -> ACQUIRE -> INSPECT -> REPRESENT -> EXPAND -> COMPARE -> CHALLENGE -> SYNTHESIZE -> VERIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RESOLVE

ID: `LEX-resolve`. Roles: context_specific_operator, specialized_operator.

Source forms: `RESOLVE`.

#### SIG-resolve-P-authority

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Settle an authorized choice by a governing decision rule without erasing factual uncertainty.

Evidence required: Decision authority and applicable rule.

Status rule: Decision settled, uncertain facts may remain uncertain.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Resolve a preference tie using an explicitly authorized preference rule.

Abstract principle: Return an authorized choice, robust shared option or explicit conditional alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-resolve-P-evidence

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `UPDATE`.

Transition or retained definition: Remove an uncertainty only to the extent warranted by new evidence.

Evidence required: Discriminator observation and supported exclusions.

Status rule: Resolved within the updated evidence partition.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Resolve which file version is active from its identifier.

Abstract principle: Revise current projections using new evidence while preserving immutable historical records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-resolve-SRC-0304

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0304 / V1 lines 1158-1160

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Obtain sufficient basis for one conclusion.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-resolve-SRC-0442

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0442 / V1 lines 1631-1633

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Close a distinction through evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RESOURCE-INTENSITY

ID: `LEX-resource-intensity`. Roles: execution_modifier.

Source forms: `RESOURCE INTENSITY`.

#### SIG-resource-intensity-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate resource intensity using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RESTART

ID: `LEX-restart`. Roles: specialized_operator.

Source forms: `RESTART`.

#### SIG-restart-SRC-0372

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0372 / V1 lines 1385-1387

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Stop and start again.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RESTORE

ID: `LEX-restore`. Roles: specialized_operator.

Source forms: `RESTORE`.

#### SIG-restore-SRC-0262

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0262 / V1 lines 1020-1022

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Return to valid prior state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RESUME

ID: `LEX-resume`. Roles: control_operator.

Source forms: `RESUME`.

#### SIG-resume-SRC-0410

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0410 / V1 lines 1533-1535

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Continue from stored state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RETAIN

ID: `LEX-retain`. Roles: specialized_operator.

Source forms: `RETAIN`.

#### SIG-retain-SRC-0302

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0302 / V1 lines 1152-1154

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Keep candidates.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RETEST

ID: `LEX-retest`. Roles: proposed_procedure.

Source forms: `RETEST`.

#### SIG-retest-P-source-macro-binding

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Execute a previously defined check again on an explicitly identified target revision; retain prior failures and record changed inputs, methods or environment.

Evidence required: Apply the common contract to the explicitly bound target, property and scope.

Status rule: Issue only scoped assessments supported by actual evidence; retain multiple incomparable certificates where warranted.

Closure rule: Use the common contract and preserve remaining obligations.

Concrete instance: Retest the repaired parser using the same empty-input acceptance case on the new build.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RETRACT

ID: `LEX-retract`. Roles: specialized_operator.

Source forms: `RETRACT`.

#### SIG-retract-SRC-0260

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0260 / V1 lines 1014-1016

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Withdraw a claim.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RETRIEVE

ID: `LEX-retrieve`. Roles: specialized_operator.

Source forms: `RETRIEVE`.

#### SIG-retrieve-SRC-0039

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0039 / V1 lines 258-260

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Obtain an already identified object.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RETRY

ID: `LEX-retry`. Roles: control_operator.

Source forms: `RETRY`.

#### SIG-retry-SRC-0398

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0398 / V1 lines 1497-1499

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Repeat after failure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RETURN

ID: `LEX-return`. Roles: specialized_operator.

Source forms: `RETURN`.

#### SIG-return-SRC-0436

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0436 / V1 lines 1613-1615

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Emit result.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REVERSIBILITY

ID: `LEX-reversibility`. Roles: semantic_policy_or_attribute.

Source forms: `REVERSIBILITY`.

#### SIG-reversibility-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate reversibility using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REVERSIBLE

ID: `LEX-reversible`. Roles: modifier_surface.

Source forms: `reversible`.

#### SIG-reversible-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "reversible" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REVIEW

ID: `LEX-review`. Roles: macro, specialized_operator.

Source forms: `REVIEW`.

#### SIG-review-SRC-0070

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0070 / V1 lines 357-359

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Inspect with quality or correctness in mind.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-review-SRC-0484

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0484 / V1 lines 1774-1777

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: INSPECT -> COMPARE -> CHALLENGE -> REPORT

Macro source expression: `INSPECT -> COMPARE -> CHALLENGE -> REPORT`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REVISE

ID: `LEX-revise`. Roles: specialized_operator.

Source forms: `REVISE`.

#### SIG-revise-SRC-0252

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0252 / V1 lines 990-992

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Modify conclusions or artifacts.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### REWRITE

ID: `LEX-rewrite`. Roles: communication_operator, specialized_operator.

Source forms: `REWRITE`.

#### SIG-rewrite-SRC-0321

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0321 / V1 lines 1220-1222

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Produce revised expression.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rewrite-SRC-0457

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0457 / V1 lines 1682-1684

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Transform language.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RIGOR

ID: `LEX-rigor`. Roles: semantic_policy_or_attribute.

Source forms: `RIGOR`.

#### SIG-rigor-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate rigor using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RIGOROUS

ID: `LEX-rigorous`. Roles: modifier_surface.

Source forms: `rigorous`.

#### SIG-rigorous-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "rigorous" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RIGOROUSLY-TEST

ID: `LEX-rigorously-test`. Roles: modifier_surface, specialized_operator.

Source forms: `RIGOROUSLY-TEST`, `rigorously test`.

#### SIG-rigorously-test-SRC-0225

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0225 / V1 lines 890-901

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Execute discriminating tests with declared conditions, expected outcomes, and failure interpretation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rigorously-test-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "rigorously test" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RISK-ASSESS

ID: `LEX-risk-assess`. Roles: specialized_operator.

Source forms: `RISK-ASSESS`.

#### SIG-risk-assess-SRC-0281

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0281 / V1 lines 1083-1085

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Evaluate downside exposure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RIVAL-MODEL

ID: `LEX-rival-model`. Roles: specialized_operator.

Source forms: `RIVAL-MODEL`.

#### SIG-rival-model-SRC-0217

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0217 / V1 lines 860-862

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Construct competing explanations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUST

ID: `LEX-robust`. Roles: context_specific_operator, modifier_surface, status.

Source forms: `ROBUST`, `robust`.

#### SIG-robust-P-adversarial

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `SYSTEM`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Assess properties against a stated attacker capability and environment.

Evidence required: Adversarial checks and explicit threat coverage.

Status rule: Adversarially tested in scope, not universally secure.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Test that an unprivileged worker cannot write a protected test resource.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-robust-P-behavior

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `ARTIFACT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `VERIFY`.

Transition or retained definition: Assess required behavior under specified perturbations.

Evidence required: Tests or proof over that perturbation class.

Status rule: Robust within the tested or proved class.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Assess parser behavior on specified malformed inputs.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-robust-P-decision

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `CANDIDATE`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `VERIFY`.

Transition or retained definition: Assess validity across declared live world cases; acceptable actions need not be identical internally.

Evidence required: Case set, validity relation and comparison projection.

Status rule: Robust for the declared cases only.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Check that one action is acceptable in every retained utilization case.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-robust-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "robust" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-robust-SRC-0545

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0545 / V1 lines 2768-2770

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Answer remains equivalent across material live cases.

Assessment dimension: robustness_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUST-->-ADVERSARIALLY-ROBUST

ID: `LEX-robust-adversarially-robust`. Roles: modifier_surface.

Source forms: `robust -> adversarially robust`.

#### SIG-robust-adversarially-robust-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "robust -> adversarially robust" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUST-CAUSAL-IDENTIFICATION-UNDER-DECLARED-MODEL

ID: `LEX-robust-causal-identification-under-declared-model`. Roles: modifier_surface.

Source forms: `robust causal identification under declared model`.

#### SIG-robust-causal-identification-under-declared-model-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "robust causal identification under declared model" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUST-INTERSECTION

ID: `LEX-robust-intersection`. Roles: specialized_operator.

Source forms: `ROBUST-INTERSECTION`.

#### SIG-robust-intersection-SRC-0308

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0308 / V1 lines 1170-1172

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Select only actions valid across every live case.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUST-INTERSECTION-CERTIFIED

ID: `LEX-robust-intersection-certified`. Roles: modifier_surface.

Source forms: `robust-intersection certified`.

#### SIG-robust-intersection-certified-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "robust-intersection certified" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUSTIFY

ID: `LEX-robustify`. Roles: specialized_operator.

Source forms: `ROBUSTIFY`.

#### SIG-robustify-SRC-0340

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0340 / V1 lines 1277-1291

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Transform to preserve acceptable behavior across broader conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUSTNESS

ID: `LEX-robustness`. Roles: semantic_policy_or_attribute.

Source forms: `ROBUSTNESS`.

#### SIG-robustness-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate robustness using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROBUSTNESS-CHECK

ID: `LEX-robustness-check`. Roles: specialized_operator.

Source forms: `ROBUSTNESS-CHECK`.

#### SIG-robustness-check-SRC-0284

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0284 / V1 lines 1092-1094

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Evaluate stability across alternative conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROLLBACK

ID: `LEX-rollback`. Roles: context_specific_operator, control_operator, specialized_operator.

Source forms: `ROLLBACK`.

#### SIG-rollback-P-external

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACT`. Input roles: `WORLD_STATE`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Apply a compensating or inverse action and inspect residual effects.

Evidence required: Undo record and target observations.

Status rule: Restored only for properties actually recovered.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Rollback a configuration while recording notifications already sent.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rollback-P-projection

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Restore an earlier working projection without deleting immutable history.

Evidence required: Checkpoint and dependency reconciliation.

Status rule: Prior projection restored, later events still recorded.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Rollback a derived status view to its last sound basis.

Abstract principle: Revise current projections using new evidence while preserving immutable historical records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rollback-SRC-0263

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0263 / V1 lines 1023-1025

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Revert state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rollback-SRC-0373

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0373 / V1 lines 1388-1398

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Apply reversal.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rollback-SRC-0408

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0408 / V1 lines 1527-1529

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Revert.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROLLBACK-GUARANTEED

ID: `LEX-rollback-guaranteed`. Roles: modifier_surface.

Source forms: `rollback guaranteed`.

#### SIG-rollback-guaranteed-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "rollback guaranteed" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROOT-CAUSE

ID: `LEX-root-cause`. Roles: modifier_surface.

Source forms: `root-cause`.

#### SIG-root-cause-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "root-cause" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ROUGH

ID: `LEX-rough`. Roles: modifier_surface.

Source forms: `rough`.

#### SIG-rough-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "rough" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-rough-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "rough" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### RUN

ID: `LEX-run`. Roles: specialized_operator.

Source forms: `RUN`.

#### SIG-run-SRC-0344

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0344 / V1 lines 1301-1303

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Start an executable process.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SAME-PATH-SELF-REVIEW

ID: `LEX-same-path-self-review`. Roles: modifier_surface.

Source forms: `same-path self-review`.

#### SIG-same-path-self-review-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "same-path self-review" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SAMPLE

ID: `LEX-sample`. Roles: specialized_operator.

Source forms: `SAMPLE`.

#### SIG-sample-SRC-0044

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0044 / V1 lines 273-275

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Acquire a subset from a larger population.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SANITY-CHECK

ID: `LEX-sanity-check`. Roles: specialized_operator.

Source forms: `SANITY-CHECK`.

#### SIG-sanity-check-SRC-0216

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0216 / V1 lines 857-859

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Use inexpensive tests for obvious inconsistency.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SATURATE

ID: `LEX-saturate`. Roles: specialized_operator.

Source forms: `SATURATE`.

#### SIG-saturate-SRC-0152

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0152 / V1 lines 622-634

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Continue until additional candidates fall into already represented equivalence classes.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-saturate-SRC-0441

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0441 / V1 lines 1628-1630

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Reach frontier closure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SATURATED

ID: `LEX-saturated`. Roles: context_bound_attribute_surface, context_specific_operator, modifier_surface.

Source forms: `SATURATED`, `saturated`.

#### SIG-saturated-P-closure-established

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `CLOSE`.

Transition or retained definition: Assert saturation only when all permitted reachable classes are covered or proven equivalent.

Evidence required: Generator space, equivalence specification and coverage proof.

Status rule: Scoped saturation when the proof obligation is met.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Certify saturation for an explicitly finite generator with complete traversal.

Abstract principle: Stop the current work with a scoped assessment, explicit residuals and reopening conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-saturated-P-observed-plateau

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: Report that a finite run produced no new represented classes without inferring unsearched closure.

Evidence required: Generator log, scope and comparison relation.

Status rule: Observed plateau only.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Record that a bounded candidate-generation pass added no new entry.

Abstract principle: Stop the current work with a scoped assessment, explicit residuals and reopening conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-saturated-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "saturated" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-saturated-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "saturated" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SATURATED-FRONTIER

ID: `LEX-saturated-frontier`. Roles: modifier_surface.

Source forms: `saturated frontier`.

#### SIG-saturated-frontier-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "saturated frontier" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SATURATION-LEVEL

ID: `LEX-saturation-level`. Roles: modifier_surface.

Source forms: `saturation-level`.

#### SIG-saturation-level-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "saturation-level" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SAVE

ID: `LEX-save`. Roles: specialized_operator.

Source forms: `SAVE`.

#### SIG-save-SRC-0354

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0354 / V1 lines 1331-1333

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Persist state.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SCAN

ID: `LEX-scan`. Roles: specialized_operator.

Source forms: `SCAN`.

#### SIG-scan-SRC-0069

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0069 / V1 lines 354-356

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Broad shallow inspection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SCHEDULE

ID: `LEX-schedule`. Roles: specialized_operator.

Source forms: `SCHEDULE`.

#### SIG-schedule-SRC-0364

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0364 / V1 lines 1361-1363

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Arrange future execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SCHEMA

ID: `LEX-schema`. Roles: specialized_operator.

Source forms: `SCHEMA`.

#### SIG-schema-SRC-0092

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0092 / V1 lines 425-427

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent valid data structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SCOPE

ID: `LEX-scope`. Roles: specialized_operator.

Source forms: `SCOPE`.

#### SIG-scope-SRC-0020

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0020 / V1 lines 197-199

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Declare what is included and excluded.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SCORE

ID: `LEX-score`. Roles: specialized_operator.

Source forms: `SCORE`.

#### SIG-score-SRC-0271

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0271 / V1 lines 1053-1055

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Assign criterion-relative values.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEARCH

ID: `LEX-search`. Roles: specialized_operator.

Source forms: `SEARCH`.

#### SIG-search-SRC-0036

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0036 / V1 lines 249-251

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Explore an information space for relevant candidates.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SECOND-PASS

ID: `LEX-second-pass`. Roles: modifier_surface.

Source forms: `second pass`.

#### SIG-second-pass-SRC-0509

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0509 / V1 lines 2219-2239

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "second pass" on the INDEPENDENCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `INDEPENDENCE`. Destination: EvidenceRelation and verification policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEGMENT

ID: `LEX-segment`. Roles: specialized_operator.

Source forms: `SEGMENT`.

#### SIG-segment-SRC-0118

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0118 / V1 lines 505-507

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Divide sequential or spatial material.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SELECT

ID: `LEX-select`. Roles: family.

Source forms: `SELECT`.

#### SIG-select-SRC-0293

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0293 / V1 lines 1124-1127

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Commit among alternatives when justified.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SELECTIVE

ID: `LEX-selective`. Roles: modifier_surface.

Source forms: `selective`.

#### SIG-selective-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "selective" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEND

ID: `LEX-send`. Roles: specialized_operator.

Source forms: `SEND`.

#### SIG-send-SRC-0357

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0357 / V1 lines 1340-1342

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Transmit.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SENSITIVITY-ANALYSIS

ID: `LEX-sensitivity-analysis`. Roles: specialized_operator.

Source forms: `SENSITIVITY-ANALYSIS`.

#### SIG-sensitivity-analysis-SRC-0285

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0285 / V1 lines 1095-1097

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Evaluate changes under parameter variation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEPARATE

ID: `LEX-separate`. Roles: specialized_operator.

Source forms: `SEPARATE`.

#### SIG-separate-SRC-0123

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0123 / V1 lines 520-522

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Prevent distinct things from being treated jointly.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEQUENCE

ID: `LEX-sequence`. Roles: control_operator, specialized_operator.

Source forms: `SEQUENCE`.

#### SIG-sequence-SRC-0084

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0084 / V1 lines 401-403

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent ordered steps.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-sequence-SRC-0392

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0392 / V1 lines 1479-1481

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Order operations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SERIALIZE

ID: `LEX-serialize`. Roles: specialized_operator.

Source forms: `SERIALIZE`.

#### SIG-serialize-SRC-0100

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0100 / V1 lines 449-451

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Convert structured information into a storable or transferable sequence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEVERAL-CANDIDATES

ID: `LEX-several-candidates`. Roles: modifier_surface.

Source forms: `several candidates`.

#### SIG-several-candidates-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "several candidates" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SEVERAL-SAME-CLASS-SOURCES

ID: `LEX-several-same-class-sources`. Roles: modifier_surface.

Source forms: `several same-class sources`.

#### SIG-several-same-class-sources-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "several same-class sources" on the SOURCE_DIVERSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SHALLOW

ID: `LEX-shallow`. Roles: modifier_surface.

Source forms: `shallow`.

#### SIG-shallow-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "shallow" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SHOULD

ID: `LEX-should`. Roles: constraint_surface.

Source forms: `should`.

#### SIG-should-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "should" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SHOULD-NOT

ID: `LEX-should-not`. Roles: constraint_surface.

Source forms: `should not`.

#### SIG-should-not-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "should not" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SIDE-EFFECT-FREE/DRY-RUN

ID: `LEX-side-effect-free-dry-run`. Roles: modifier_surface.

Source forms: `side-effect-free/dry-run`.

#### SIG-side-effect-free-dry-run-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "side-effect-free/dry-run" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SIMPLIFY

ID: `LEX-simplify`. Roles: specialized_operator.

Source forms: `SIMPLIFY`.

#### SIG-simplify-SRC-0317

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0317 / V1 lines 1208-1210

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Reduce complexity while preserving requirements.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SIMULATE

ID: `LEX-simulate`. Roles: context_specific_operator, specialized_operator.

Source forms: `SIMULATE`.

#### SIG-simulate-P-abstract-system

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `ACT`. Input roles: `REPRESENTATION`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `ACT`.

Transition or retained definition: Execute a model and record simulator state transitions, costs and outputs.

Evidence required: Simulator run and model version.

Status rule: Simulator executed; modeled world action not implied.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Simulate a queue under a specified arrival sequence.

Abstract principle: Attempt an authorized transition at a stated target and record dispatch, effects and outcomes separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-simulate-P-operational-rehearsal

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `TEST`.

Transition or retained definition: Rehearse an operation while excluding declared target mutations, not all possible effects.

Evidence required: Isolation configuration and observed rehearsal effects.

Status rule: Dry-run results within the actual isolation boundary.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Preview database changes without committing them.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-simulate-SRC-0227

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0227 / V1 lines 905-907

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test a model rather than the real target.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SINGLE-CANDIDATE

ID: `LEX-single-candidate`. Roles: modifier_surface.

Source forms: `single candidate`.

#### SIG-single-candidate-SRC-0501

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0501 / V1 lines 2031-2048

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "single candidate" on the EXPLORATION axis under the bound requirements; do not infer achieved status from the request.

Axis: `EXPLORATION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SINGLE-CASE

ID: `LEX-single-case`. Roles: modifier_surface.

Source forms: `single-case`.

#### SIG-single-case-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "single-case" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SLICE

ID: `LEX-slice`. Roles: specialized_operator.

Source forms: `SLICE`.

#### SIG-slice-SRC-0122

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0122 / V1 lines 517-519

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Extract a bounded cross-section.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SNAPSHOT

ID: `LEX-snapshot`. Roles: specialized_operator.

Source forms: `SNAPSHOT`.

#### SIG-snapshot-SRC-0073

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0073 / V1 lines 366-368

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Capture state at a particular moment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SOLVE

ID: `LEX-solve`. Roles: context_specific_operator, macro.

Source forms: `SOLVE`.

#### SIG-solve-P-decision

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Resolve an action only when its governing decision requirements are met.

Evidence required: Live cases, objective and decision rule.

Status rule: Invariant choice or explicit branches.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Solve a purchasing choice under the stated cost and use cases.

Abstract principle: Return an authorized choice, robust shared option or explicit conditional alternatives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-solve-P-design

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TRANSFORM`. Input roles: `RULE`. Output roles: `ARTIFACT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TRANSFORM`.

Transition or retained definition: Create an acceptable design or artifact under the declared brief.

Evidence required: Artifact and requirement assessments.

Status rule: Acceptable candidate, not unique or globally best by default.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Solve the layout brief with a design meeting all mandatory dimensions.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-solve-P-formal

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `INFER`. Input roles: `RULE`. Output roles: `ARTIFACT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `INFER`.

Transition or retained definition: Construct a witness or derivation satisfying declared formal conditions.

Evidence required: Checked witness or proof.

Status rule: Solved within the formal statement and assumptions.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Solve the stated system of equations.

Abstract principle: Derive a proposition using explicit premises, rules, assumptions and scope.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-solve-SRC-0477

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0477 / V1 lines 1746-1749

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: COMPILE -> REPRESENT -> SPLIT -> EXPAND -> EVALUATE/TEST -> SELECT -> VERIFY

Macro source expression: `COMPILE -> REPRESENT -> SPLIT -> EXPAND -> EVALUATE/TEST -> SELECT -> VERIFY`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SOLVED

ID: `LEX-solved`. Roles: status.

Source forms: `SOLVED`.

#### SIG-solved-SRC-0544

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0544 / V1 lines 2765-2767

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Requirements have a supported answer in declared scope.

Assessment dimension: resolution_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SORT

ID: `LEX-sort`. Roles: specialized_operator.

Source forms: `SORT`.

#### SIG-sort-SRC-0169

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0169 / V1 lines 683-685

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Order according to a key.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SOURCE-DIVERSITY

ID: `LEX-source-diversity`. Roles: semantic_policy_or_attribute.

Source forms: `SOURCE DIVERSITY`.

#### SIG-source-diversity-SRC-0519

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0519 / V1 lines 2437-2451

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate source diversity using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `SOURCE_DIVERSITY`. Destination: AcquisitionPolicy and evidence dependence graph.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPECIALIZE

ID: `LEX-specialize`. Roles: specialized_operator.

Source forms: `SPECIALIZE`.

#### SIG-specialize-SRC-0143

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0143 / V1 lines 595-597

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Derive narrower cases.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPECIFIC

ID: `LEX-specific`. Roles: modifier_surface.

Source forms: `specific`.

#### SIG-specific-SRC-0504

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0504 / V1 lines 2095-2113

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "specific" on the PRECISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `PRECISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPECIFIC-CASE

ID: `LEX-specific-case`. Roles: modifier_surface.

Source forms: `specific case`.

#### SIG-specific-case-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "specific case" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPECIFY

ID: `LEX-specify`. Roles: specialized_operator.

Source forms: `SPECIFY`.

#### SIG-specify-SRC-0017

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0017 / V1 lines 188-190

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Replace underspecification with explicit conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPECULATE

ID: `LEX-speculate`. Roles: modifier_surface.

Source forms: `speculate`.

#### SIG-speculate-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "speculate" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPECULATIVE

ID: `LEX-speculative`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `speculative`.

#### SIG-speculative-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "speculative" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-speculative-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "speculative" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPEED

ID: `LEX-speed`. Roles: execution_modifier.

Source forms: `SPEED`.

#### SIG-speed-SRC-0521

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0521 / V1 lines 2471-2487

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate speed using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `SPEED`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SPLIT

ID: `LEX-split`. Roles: family.

Source forms: `SPLIT`.

#### SIG-split-SRC-0115

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0115 / V1 lines 495-498

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Preserve materially distinct components separately.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STANDARDIZE

ID: `LEX-standardize`. Roles: specialized_operator.

Source forms: `STANDARDIZE`.

#### SIG-standardize-SRC-0104

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0104 / V1 lines 461-463

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Conform to an external or declared convention.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-standardize-SRC-0328

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0328 / V1 lines 1241-1243

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Conform to convention.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### START

ID: `LEX-start`. Roles: specialized_operator.

Source forms: `START`.

#### SIG-start-SRC-0370

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0370 / V1 lines 1379-1381

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Begin execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STATE-MACHINE

ID: `LEX-state-machine`. Roles: specialized_operator.

Source forms: `STATE-MACHINE`.

#### SIG-state-machine-SRC-0086

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0086 / V1 lines 407-409

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent states and transitions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STATE-MAP

ID: `LEX-state-map`. Roles: specialized_operator.

Source forms: `STATE-MAP`.

#### SIG-state-map-SRC-0085

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0085 / V1 lines 404-406

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent possible states.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STOP

ID: `LEX-stop`. Roles: control_operator, specialized_operator.

Source forms: `STOP`.

#### SIG-stop-SRC-0371

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0371 / V1 lines 1382-1384

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: End execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-stop-SRC-0431

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0431 / V1 lines 1596-1600

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Terminate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRATIFY

ID: `LEX-stratify`. Roles: specialized_operator.

Source forms: `STRATIFY`.

#### SIG-stratify-SRC-0126

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0126 / V1 lines 529-531

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Separate into meaningful layers.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRESS-ROBUST

ID: `LEX-stress-robust`. Roles: modifier_surface.

Source forms: `stress robust`.

#### SIG-stress-robust-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "stress robust" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRESS-TEST

ID: `LEX-stress-test`. Roles: specialized_operator.

Source forms: `STRESS-TEST`.

#### SIG-stress-test-SRC-0212

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0212 / V1 lines 845-847

Operator: `CHALLENGE`. Input roles: `PROPOSITION`. Output roles: `TEST_SPEC`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CHALLENGE`.

Transition or retained definition: Test extreme operating conditions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRICT

ID: `LEX-strict`. Roles: modifier_surface.

Source forms: `STRICT`, `strict`.

#### SIG-strict-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "strict" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-strict-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "strict" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRICTNESS

ID: `LEX-strictness`. Roles: semantic_policy_or_attribute.

Source forms: `STRICTNESS`.

#### SIG-strictness-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate strictness using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRONG

ID: `LEX-strong`. Roles: context_bound_attribute_surface.

Source forms: `strong`.

#### SIG-strong-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "strong" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRONGLY-AVOID

ID: `LEX-strongly-avoid`. Roles: constraint_surface.

Source forms: `strongly avoid`.

#### SIG-strongly-avoid-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "strongly avoid" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRONGLY-PREFER

ID: `LEX-strongly-prefer`. Roles: constraint_surface.

Source forms: `strongly prefer`.

#### SIG-strongly-prefer-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "strongly prefer" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRUCTURAL-ABSTRACTION

ID: `LEX-structural-abstraction`. Roles: modifier_surface.

Source forms: `structural abstraction`.

#### SIG-structural-abstraction-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "structural abstraction" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### STRUCTURED

ID: `LEX-structured`. Roles: modifier_surface.

Source forms: `structured`.

#### SIG-structured-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "structured" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUBMIT

ID: `LEX-submit`. Roles: specialized_operator.

Source forms: `SUBMIT`.

#### SIG-submit-SRC-0358

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0358 / V1 lines 1343-1345

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Enter into an external process.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUBSCRIBE

ID: `LEX-subscribe`. Roles: specialized_operator.

Source forms: `SUBSCRIBE`.

#### SIG-subscribe-SRC-0049

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0049 / V1 lines 288-290

Operator: `ACQUIRE`. Input roles: `EVIDENCE_OBJECT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `ACQUIRE`.

Transition or retained definition: Arrange recurring acquisition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUBSTANTIAL

ID: `LEX-substantial`. Roles: modifier_surface.

Source forms: `substantial`.

#### SIG-substantial-SRC-0522

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0522 / V1 lines 2488-2504

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "substantial" on the RESOURCE_INTENSITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `RESOURCE_INTENSITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUBTRACT

ID: `LEX-subtract`. Roles: specialized_operator.

Source forms: `SUBTRACT`.

#### SIG-subtract-SRC-0172

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0172 / V1 lines 692-694

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Remove one set from another.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUMMARIZE

ID: `LEX-summarize`. Roles: communication_operator, specialized_operator.

Source forms: `SUMMARIZE`.

#### SIG-summarize-SRC-0110

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0110 / V1 lines 479-481

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Produce a smaller representation preserving declared salient content.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-summarize-SRC-0455

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0455 / V1 lines 1676-1678

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Compress.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUMMARIZED

ID: `LEX-summarized`. Roles: modifier_surface.

Source forms: `summarized`.

#### SIG-summarized-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "summarized" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SUPPORTED

ID: `LEX-supported`. Roles: context_bound_attribute_surface.

Source forms: `supported`.

#### SIG-supported-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "supported" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SURFACE-FACTS-ONLY

ID: `LEX-surface-facts-only`. Roles: modifier_surface.

Source forms: `surface facts only`.

#### SIG-surface-facts-only-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "surface facts only" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SURFACE-ONLY

ID: `LEX-surface-only`. Roles: modifier_surface.

Source forms: `surface-only`.

#### SIG-surface-only-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "surface-only" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-surface-only-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "surface-only" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-surface-only-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "surface-only" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SYNCHRONIZE

ID: `LEX-synchronize`. Roles: specialized_operator.

Source forms: `SYNCHRONIZE`.

#### SIG-synchronize-SRC-0257

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0257 / V1 lines 1005-1007

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Align multiple states.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SYNTHESIZE

ID: `LEX-synthesize`. Roles: macro, specialized_operator.

Source forms: `SYNTHESIZE`.

#### SIG-synthesize-SRC-0194

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0194 / V1 lines 768-770

Operator: `INFER`. Input roles: `EVIDENCE_OBJECT`. Output roles: `PROPOSITION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `INFER`.

Transition or retained definition: Combine evidence into higher-order conclusions.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-synthesize-SRC-0331

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0331 / V1 lines 1250-1252

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Combine into a coherent whole.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-synthesize-SRC-0488

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0488 / V1 lines 1790-1793

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: ACQUIRE/INSPECT -> ALIGN -> RECONCILE -> INFER -> REPRESENT

Macro source expression: `ACQUIRE/INSPECT -> ALIGN -> RECONCILE -> INFER -> REPRESENT`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SYSTEM-TEST

ID: `LEX-system-test`. Roles: specialized_operator.

Source forms: `SYSTEM-TEST`.

#### SIG-system-test-SRC-0233

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0233 / V1 lines 923-925

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test complete integrated behavior.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SYSTEMATIC

ID: `LEX-systematic`. Roles: modifier_surface.

Source forms: `systematic`.

#### SIG-systematic-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "systematic" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SYSTEMATICALLY-CHECK

ID: `LEX-systematically-check`. Roles: modifier_surface, specialized_operator.

Source forms: `SYSTEMATICALLY-CHECK`, `systematically check`.

#### SIG-systematically-check-SRC-0224

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0224 / V1 lines 887-889

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Apply the same explicit checking procedure across all relevant cases.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-systematically-check-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "systematically check" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### SYSTEMATICALLY-CHECKED

ID: `LEX-systematically-checked`. Roles: status.

Source forms: `SYSTEMATICALLY CHECKED`.

#### SIG-systematically-checked-SRC-0535

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0535 / V1 lines 2738-2740

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Declared checks were applied consistently.

Assessment dimension: check_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TABLE

ID: `LEX-table`. Roles: specialized_operator.

Source forms: `TABLE`.

#### SIG-table-SRC-0079

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0079 / V1 lines 386-388

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent records across shared fields.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TAKE-AT-FACE-VALUE

ID: `LEX-take-at-face-value`. Roles: modifier_surface.

Source forms: `take at face value`.

#### SIG-take-at-face-value-SRC-0499

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0499 / V1 lines 1984-2011

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "take at face value" on the RIGOR axis under the bound requirements; do not infer achieved status from the request.

Axis: `RIGOR`. Destination: VerificationPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TAXONOMY

ID: `LEX-taxonomy`. Roles: specialized_operator.

Source forms: `TAXONOMY`.

#### SIG-taxonomy-SRC-0093

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0093 / V1 lines 428-430

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent hierarchical categories.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TEACH

ID: `LEX-teach`. Roles: communication_operator, macro.

Source forms: `TEACH`.

#### SIG-teach-SRC-0452

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0452 / V1 lines 1667-1669

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `CONTROL`.

Transition or retained definition: Structure information for learning.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-teach-SRC-0489

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0489 / V1 lines 1794-1797

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: ASSESS -> REPRESENT -> SPLIT -> EXPLAIN -> DEMONSTRATE -> TEST -> UPDATE

Macro source expression: `ASSESS -> REPRESENT -> SPLIT -> EXPLAIN -> DEMONSTRATE -> TEST -> UPDATE`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TECHNICAL

ID: `LEX-technical`. Roles: modifier_surface.

Source forms: `technical`.

#### SIG-technical-SRC-0515

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0515 / V1 lines 2367-2381

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "technical" on the FORMALITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `FORMALITY`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TEMPORAL-SEQUENCE

ID: `LEX-temporal-sequence`. Roles: modifier_surface.

Source forms: `temporal sequence`.

#### SIG-temporal-sequence-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "temporal sequence" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TENTATIVE

ID: `LEX-tentative`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `tentative`.

#### SIG-tentative-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "tentative" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-tentative-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "tentative" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TERMINATE

ID: `LEX-terminate`. Roles: specialized_operator.

Source forms: `TERMINATE`.

#### SIG-terminate-SRC-0438

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0438 / V1 lines 1619-1621

Operator: `CLOSE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CLOSE`.

Transition or retained definition: End process.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TERSE

ID: `LEX-terse`. Roles: modifier_surface.

Source forms: `terse`.

#### SIG-terse-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "terse" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-terse-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "terse" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TEST

ID: `LEX-test`. Roles: context_specific_operator, family.

Source forms: `TEST`.

#### SIG-test-P-decision-probe

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `TEST`.

Transition or retained definition: Obtain an observation capable of changing which decision branches remain.

Evidence required: Probe outcome, cost, availability and affected live alternatives.

Status rule: Decision partition updated only as the observation supports.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Measure utilization to distinguish a buy-versus-lease choice.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-test-P-empirical

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `TEST`.

Transition or retained definition: Apply a measurement or intervention protocol and record outcome.

Evidence required: Actual observations and protocol deviations.

Status rule: Executed empirical test with its outcome.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Measure the output after a controlled input change.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-test-P-formal-countermodel

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `TEST`.

Transition or retained definition: Search the declared formal scope for a violating model; failure to find one is scope-limited.

Evidence required: Enumerated scope or solver output and its interpretation.

Status rule: Counterexample found or none found in the checked scope.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Test a proposed invariant over all states of a specified finite machine.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-test-P-program

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `TEST`.

Transition or retained definition: Execute a check against the identified artifact and environment.

Evidence required: Execution output, expected result and target revision.

Status rule: PASSED or FAILED for the named check, not universal correctness.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Run a regression test for an empty input.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-test-SRC-0221

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0221 / V1 lines 877-880

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Apply a discriminator capable of changing the live partition.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TESTED

ID: `LEX-tested`. Roles: status.

Source forms: `TESTED`.

#### SIG-tested-SRC-0536

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0536 / V1 lines 2741-2743

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: A meaningful test was run.

Assessment dimension: check_records.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TESTED-MECHANISM

ID: `LEX-tested-mechanism`. Roles: modifier_surface.

Source forms: `tested mechanism`.

#### SIG-tested-mechanism-SRC-0520

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0520 / V1 lines 2452-2470

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "tested mechanism" on the CAUSAL_DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `CAUSAL_DEPTH`. Destination: Causal obligations and evidence plan.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### THINK-HARDER

ID: `LEX-think-harder`. Roles: modifier_surface.

Source forms: `think harder`.

#### SIG-think-harder-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "think harder" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### THIS-CASE-ONLY

ID: `LEX-this-case-only`. Roles: modifier_surface.

Source forms: `this case only`.

#### SIG-this-case-only-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "this case only" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### THROTTLE

ID: `LEX-throttle`. Roles: control_operator.

Source forms: `THROTTLE`.

#### SIG-throttle-SRC-0418

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0418 / V1 lines 1557-1559

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Limit rate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TIEBREAK

ID: `LEX-tiebreak`. Roles: specialized_operator.

Source forms: `TIEBREAK`.

#### SIG-tiebreak-SRC-0309

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0309 / V1 lines 1173-1175

Operator: `SELECT`. Input roles: `CANDIDATE`. Output roles: `ACTION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `SELECT`.

Transition or retained definition: Apply an explicit secondary rule.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TIMEBOX

ID: `LEX-timebox`. Roles: control_operator.

Source forms: `TIMEBOX`.

#### SIG-timebox-SRC-0416

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0416 / V1 lines 1551-1553

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Limit duration.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TIMELINE

ID: `LEX-timeline`. Roles: specialized_operator.

Source forms: `TIMELINE`.

#### SIG-timeline-SRC-0083

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0083 / V1 lines 398-400

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent ordered temporal events.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TO-CLOSURE

ID: `LEX-to-closure`. Roles: context_bound_attribute_surface.

Source forms: `to closure`.

#### SIG-to-closure-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "to closure" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TOLERATE-BRANCHES

ID: `LEX-tolerate-branches`. Roles: modifier_surface.

Source forms: `tolerate branches`.

#### SIG-tolerate-branches-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "tolerate branches" on the UNCERTAINTY_TOLERANCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRACE

ID: `LEX-trace`. Roles: specialized_operator.

Source forms: `TRACE`.

#### SIG-trace-SRC-0065

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0065 / V1 lines 342-344

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Follow a value, event, dependency, provenance path, or execution path.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRADE-OFF

ID: `LEX-trade-off`. Roles: specialized_operator.

Source forms: `TRADE-OFF`.

#### SIG-trade-off-SRC-0278

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0278 / V1 lines 1074-1076

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Expose competing objectives.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRANSACTION

ID: `LEX-transaction`. Roles: control_operator.

Source forms: `TRANSACTION`.

#### SIG-transaction-SRC-0424

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0424 / V1 lines 1575-1577

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Group changes atomically.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRANSACTIONAL

ID: `LEX-transactional`. Roles: modifier_surface.

Source forms: `transactional`.

#### SIG-transactional-SRC-0518

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0518 / V1 lines 2420-2436

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "transactional" on the REVERSIBILITY axis under the bound requirements; do not infer achieved status from the request.

Axis: `REVERSIBILITY`. Destination: EffectProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRANSCRIBE

ID: `LEX-transcribe`. Roles: communication_operator.

Source forms: `TRANSCRIBE`.

#### SIG-transcribe-SRC-0466

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0466 / V1 lines 1709-1711

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Convert speech or another modality to text.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRANSFORM

ID: `LEX-transform`. Roles: family.

Source forms: `TRANSFORM`.

#### SIG-transform-SRC-0312

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0312 / V1 lines 1192-1195

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Modify a candidate.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRANSITION-BY-TRANSITION

ID: `LEX-transition-by-transition`. Roles: modifier_surface.

Source forms: `transition-by-transition`.

#### SIG-transition-by-transition-SRC-0496

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0496 / V1 lines 1888-1922

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "transition-by-transition" on the DETAIL axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETAIL`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRANSLATE

ID: `LEX-translate`. Roles: communication_operator, context_specific_operator, specialized_operator.

Source forms: `TRANSLATE`.

#### SIG-translate-P-language

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Change language while preserving protected meaning, modality and attribution.

Evidence required: Source-target comparison in the required scope.

Status rule: Translation produced; fidelity requires checks.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Translate a warning without weakening its prohibition.

Abstract principle: Create a changed candidate under specified protected invariants and improvement criteria.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-translate-P-representation

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Map encodings under a declared semantic correspondence.

Evidence required: Mapping and round-trip or invariant checks.

Status rule: Representation translated under that correspondence.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Translate a dependency table into graph data.

Abstract principle: Re-encode protected content under an explicit preservation projection.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-translate-SRC-0108

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0108 / V1 lines 473-475

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Map meaning between representational systems.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-translate-SRC-0322

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0322 / V1 lines 1223-1225

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Convert language or representation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-translate-SRC-0467

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0467 / V1 lines 1712-1714

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Map languages.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TREE

ID: `LEX-tree`. Roles: specialized_operator.

Source forms: `TREE`.

#### SIG-tree-SRC-0082

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0082 / V1 lines 395-397

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent hierarchical structure.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TRIGGER

ID: `LEX-trigger`. Roles: specialized_operator.

Source forms: `TRIGGER`.

#### SIG-trigger-SRC-0367

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0367 / V1 lines 1370-1372

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Cause a workflow or event.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TROUBLESHOOT

ID: `LEX-troubleshoot`. Roles: macro.

Source forms: `TROUBLESHOOT`.

#### SIG-troubleshoot-SRC-0482

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0482 / V1 lines 1766-1769

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: INSPECT -> LOCALIZE -> HYPOTHESIZE -> TEST -> REPAIR

Macro source expression: `INSPECT -> LOCALIZE -> HYPOTHESIZE -> TEST -> REPAIR`. It is a workflow specification, not an observed execution.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TUNE

ID: `LEX-tune`. Roles: specialized_operator.

Source forms: `TUNE`.

#### SIG-tune-SRC-0325

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0325 / V1 lines 1232-1234

Operator: `TRANSFORM`. Input roles: `ARTIFACT`. Output roles: `ARTIFACT`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `TRANSFORM`.

Transition or retained definition: Adjust parameters.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TUTOR

ID: `LEX-tutor`. Roles: communication_operator.

Source forms: `TUTOR`.

#### SIG-tutor-SRC-0453

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0453 / V1 lines 1670-1672

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `COMMUNICATIVE_EFFECT, SEMANTIC_PRESERVATION`. Contract: `CONTROL`.

Transition or retained definition: Adapt teaching interactively.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TWO-PHASE-COMMIT

ID: `LEX-two-phase-commit`. Roles: control_operator.

Source forms: `TWO-PHASE-COMMIT`.

#### SIG-two-phase-commit-SRC-0425

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0425 / V1 lines 1578-1580

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Separate readiness from final mutation.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TYPE

ID: `LEX-type`. Roles: specialized_operator.

Source forms: `TYPE`.

#### SIG-type-SRC-0031

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0031 / V1 lines 230-232

Operator: `COMPILE`. Input roles: `REPRESENTATION`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPILE`.

Transition or retained definition: Assign categories constraining valid operations.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### TYPE-CHECK

ID: `LEX-type-check`. Roles: specialized_operator.

Source forms: `TYPE-CHECK`.

#### SIG-type-check-SRC-0243

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0243 / V1 lines 953-955

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Check type correctness.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ULTRA-TERSE

ID: `LEX-ultra-terse`. Roles: modifier_surface.

Source forms: `ultra-terse`.

#### SIG-ultra-terse-SRC-0514

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0514 / V1 lines 2346-2366

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "ultra-terse" on the CONCISION axis under the bound requirements; do not infer achieved status from the request.

Axis: `CONCISION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNAMBIGUOUS

ID: `LEX-unambiguous`. Roles: modifier_surface.

Source forms: `unambiguous`.

#### SIG-unambiguous-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "unambiguous" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNBUNDLE

ID: `LEX-unbundle`. Roles: specialized_operator.

Source forms: `UNBUNDLE`.

#### SIG-unbundle-SRC-0124

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0124 / V1 lines 523-525

Operator: `SPLIT`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `SPLIT`.

Transition or retained definition: Separate previously coupled elements.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNCERTAINTY-TOLERANCE

ID: `LEX-uncertainty-tolerance`. Roles: semantic_policy_or_attribute.

Source forms: `UNCERTAINTY TOLERANCE`.

#### SIG-uncertainty-tolerance-SRC-0517

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0517 / V1 lines 2403-2419

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Calibrate uncertainty tolerance using an explicit task-specific contract; source rankings are lexical data, not measured intervals.

Axis: `UNCERTAINTY_TOLERANCE`. Destination: ResolutionPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNCHECKED

ID: `LEX-unchecked`. Roles: modifier_surface.

Source forms: `unchecked`.

#### SIG-unchecked-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "unchecked" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNCOMMON

ID: `LEX-uncommon`. Roles: context_bound_attribute_surface.

Source forms: `uncommon`.

#### SIG-uncommon-SRC-0512

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0512 / V1 lines 2286-2308

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "uncommon" on the NOVELTY axis under the bound requirements; do not infer achieved status from the request.

Axis: `NOVELTY`. Destination: Optional search objective plus separately supported novelty assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNION

ID: `LEX-union`. Roles: specialized_operator.

Source forms: `UNION`.

#### SIG-union-SRC-0171

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0171 / V1 lines 689-691

Operator: `COMPARE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `COMPARE`.

Transition or retained definition: Combine memberships.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNIT-TEST

ID: `LEX-unit-test`. Roles: specialized_operator.

Source forms: `UNIT-TEST`.

#### SIG-unit-test-SRC-0231

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0231 / V1 lines 917-919

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Test isolated units.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNIVERSAL-WITHIN-SCOPE

ID: `LEX-universal-within-scope`. Roles: modifier_surface.

Source forms: `universal within scope`.

#### SIG-universal-within-scope-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "universal within scope" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNKNOWN

ID: `LEX-unknown`. Roles: status.

Source forms: `UNKNOWN`.

#### SIG-unknown-SRC-0551

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0551 / V1 lines 2786-2790

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Scoped non-identifiability or impossibility has been established.

Assessment dimension: resolution_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNLIMITED

ID: `LEX-unlimited`. Roles: modifier_surface.

Source forms: `unlimited`.

#### SIG-unlimited-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "unlimited" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNQUESTIONABLY

ID: `LEX-unquestionably`. Roles: context_bound_attribute_surface.

Source forms: `unquestionably`.

#### SIG-unquestionably-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "unquestionably" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNRESOLVED

ID: `LEX-unresolved`. Roles: status.

Source forms: `UNRESOLVED`.

#### SIG-unresolved-SRC-0548

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0548 / V1 lines 2777-2779

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Material work remains.

Assessment dimension: resolution_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNTIL

ID: `LEX-until`. Roles: control_operator.

Source forms: `UNTIL`.

#### SIG-until-SRC-0429

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0429 / V1 lines 1590-1592

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Continue until condition holds.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNTIL-NO-ANSWER-CHANGING-DEEPER-DISTINCTION-REMAINS

ID: `LEX-until-no-answer-changing-deeper-distinction-remains`. Roles: modifier_surface.

Source forms: `until no answer-changing deeper distinction remains`.

#### SIG-until-no-answer-changing-deeper-distinction-remains-SRC-0497

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0497 / V1 lines 1923-1951

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "until no answer-changing deeper distinction remains" on the DEPTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `DEPTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNTIL-NO-MATERIAL-CASE-REMAINS

ID: `LEX-until-no-material-case-remains`. Roles: context_bound_attribute_surface, modifier_surface.

Source forms: `until no material case remains`.

#### SIG-until-no-material-case-remains-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "until no material case remains" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-until-no-material-case-remains-SRC-0513

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0513 / V1 lines 2309-2345

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "until no material case remains" on the COMPLETENESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `COMPLETENESS`. Destination: ClosureTarget.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UNVERIFIED

ID: `LEX-unverified`. Roles: modifier_surface.

Source forms: `unverified`.

#### SIG-unverified-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "unverified" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UPDATE

ID: `LEX-update`. Roles: family.

Source forms: `UPDATE`.

#### SIG-update-SRC-0250

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0250 / V1 lines 983-986

Operator: `UPDATE`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `UPDATE`.

Transition or retained definition: Revise represented state according to new evidence.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### USE-ALL-INTELLIGENCE

ID: `LEX-use-all-intelligence`. Roles: modifier_surface.

Source forms: `use all intelligence`.

#### SIG-use-all-intelligence-SRC-0525

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0525 / V1 lines 2587-2640

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "use all intelligence" on the DANGEROUS_PSEUDO_STRENGTH_MODIFIERS axis under the bound requirements; do not infer achieved status from the request.

Axis: `DANGEROUS_PSEUDO_STRENGTH_MODIFIERS`. Destination: Translate to bounded requirements; do not promise impossible evidence status.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### UTILITY-EVALUATE

ID: `LEX-utility-evaluate`. Roles: specialized_operator.

Source forms: `UTILITY-EVALUATE`.

#### SIG-utility-evaluate-SRC-0288

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0288 / V1 lines 1104-1106

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Compare expected objective attainment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VAGUE

ID: `LEX-vague`. Roles: modifier_surface.

Source forms: `vague`.

#### SIG-vague-SRC-0524

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0524 / V1 lines 2551-2586

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "vague" on the NEGATIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `NEGATIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not an intrinsic quality score.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VALIDATE

ID: `LEX-validate`. Roles: context_specific_operator, specialized_operator.

Source forms: `VALIDATE`.

#### SIG-validate-P-model

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `REPRESENTATION`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `EMPIRICAL_SUPPORT`. Contract: `VERIFY`.

Transition or retained definition: Compare model behavior with target observations under a declared adequacy criterion.

Evidence required: External observations and explicit correspondence assumptions.

Status rule: Model adequacy within examined scope.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Validate simulated demand against held-out observations.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-validate-P-schema

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `TEST`. Input roles: `ARTIFACT`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Check structural and value constraints of a declared schema.

Evidence required: Schema, target and validator result.

Status rule: Schema conformity for tested input.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Validate a record against required fields.

Abstract principle: Execute a defined check and record observations, outcome, scope, target version and method.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-validate-SRC-0248

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0248 / V1 lines 968-980

Operator: `TEST`. Input roles: `TEST_SPEC`. Output roles: `EVIDENCE_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `TEST`.

Transition or retained definition: Check conformance against requirements.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-validate-SRC-0377

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0377 / V1 lines 1421-1423

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Establish conformance to declared requirements.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VALUE

ID: `LEX-value`. Roles: specialized_operator.

Source forms: `VALUE`.

#### SIG-value-SRC-0280

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0280 / V1 lines 1080-1082

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Estimate utility.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VARIATE

ID: `LEX-variate`. Roles: specialized_operator.

Source forms: `VARIATE`.

#### SIG-variate-SRC-0139

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0139 / V1 lines 583-585

Operator: `EXPAND`. Input roles: `CANDIDATE`. Output roles: `CANDIDATE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `EXPAND`.

Transition or retained definition: Create controlled variants.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VERIFIED

ID: `LEX-verified`. Roles: context_bound_attribute_surface, status.

Source forms: `VERIFIED`, `verified`.

#### SIG-verified-SRC-0507

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0507 / V1 lines 2162-2189

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "verified" on the ASSERTION_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `ASSERTION_FORCE`. Destination: Evidence-derived assessment plus separate rhetorical presentation preference.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verified-SRC-0539

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0539 / V1 lines 2750-2752

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `STATUS`.

Transition or retained definition: Required evidence standard was satisfied.

Assessment dimension: verification_assessments.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VERIFY

ID: `LEX-verify`. Roles: context_specific_operator, family.

Source forms: `VERIFY`.

#### SIG-verify-P-audience

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `RECIPIENT_MODEL`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `COMMUNICATIVE_EFFECT`. Contract: `VERIFY`.

Transition or retained definition: Assess recipient understanding or effect using a specified measurement.

Evidence required: Recipient response or effect measurement, not message appearance alone.

Status rule: Effect supported for observed recipients.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Verify understanding by asking the learner to solve a new example.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verify-P-external

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `WORLD_STATE`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `VERIFY`.

Transition or retained definition: Observe the external postcondition after action rather than relying on dispatch.

Evidence required: Target-state observation with time and version.

Status rule: Postcondition observed within the stated time window.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Verify that the saved record contains the requested value.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verify-P-formal

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `ARTIFACT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `FORMAL_ENTAILMENT`. Contract: `VERIFY`.

Transition or retained definition: Check a certificate for the exact proposition and declared assumptions.

Evidence required: Checker result and bound certificate.

Status rule: Formal certificate for that target and version.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Verify a proof object with its stated rules.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verify-P-runtime

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `ARTIFACT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `EXECUTABLE_BEHAVIOR`. Contract: `VERIFY`.

Transition or retained definition: Evaluate observed artifact behavior against required executable properties.

Evidence required: Executed checks tied to build, environment and property.

Status rule: Runtime verification limited to those properties and scope.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Verify that the new parser rejects malformed inputs.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verify-P-source

Origin: AUTHORED_MIGRATION_PROPOSAL. Source: Authored migration proposal, not an original quotation.

Operator: `VERIFY`. Input roles: `EVIDENCE_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `VERIFY`.

Transition or retained definition: Check that an extraction corresponds to an identified source revision.

Evidence required: Source span and comparison record.

Status rule: Verified correspondence only.

Closure rule: Close only for this sense, target, property and scope after its obligations are assessed; retain other senses when material.

Concrete instance: Verify the date printed in the specified contract.

Abstract principle: Evaluate a specified property against an evidence standard and issue a scoped assessment.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verify-SRC-0375

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0375 / V1 lines 1401-1417

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Establish what a result actually satisfies.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-verify-SRC-0378

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0378 / V1 lines 1424-1426

Operator: `VERIFY`. Input roles: `STATUS_OBJECT`. Output roles: `STATUS_OBJECT`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `VERIFY`.

Transition or retained definition: Establish a claim using the declared evidential standard.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VERY-STRICT

ID: `LEX-very-strict`. Roles: modifier_surface.

Source forms: `very strict`.

#### SIG-very-strict-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "very strict" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### VISUALIZE

ID: `LEX-visualize`. Roles: specialized_operator.

Source forms: `VISUALIZE`.

#### SIG-visualize-SRC-0109

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0109 / V1 lines 476-478

Operator: `REPRESENT`. Input roles: `REPRESENTATION`. Output roles: `REPRESENTATION`.

Correctness obligations: `SEMANTIC_PRESERVATION`. Contract: `REPRESENT`.

Transition or retained definition: Represent spatially or graphically.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WATCH

ID: `LEX-watch`. Roles: specialized_operator.

Source forms: `WATCH`.

#### SIG-watch-SRC-0071

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0071 / V1 lines 360-362

Operator: `INSPECT`. Input roles: `EVIDENCE_OBJECT`. Output roles: `REPRESENTATION`.

Correctness obligations: `SOURCE_FIDELITY`. Contract: `INSPECT`.

Transition or retained definition: Repeatedly inspect for change.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WEAKLY-REPRODUCIBLE

ID: `LEX-weakly-reproducible`. Roles: modifier_surface.

Source forms: `weakly reproducible`.

#### SIG-weakly-reproducible-SRC-0508

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0508 / V1 lines 2190-2218

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "weakly reproducible" on the DETERMINISM axis under the bound requirements; do not infer achieved status from the request.

Axis: `DETERMINISM`. Destination: Canonicalization and execution policy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WEIGH

ID: `LEX-weigh`. Roles: specialized_operator.

Source forms: `WEIGH`.

#### SIG-weigh-SRC-0277

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0277 / V1 lines 1071-1073

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Apply relative criterion importance.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WHILE

ID: `LEX-while`. Roles: control_operator.

Source forms: `WHILE`.

#### SIG-while-SRC-0428

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0428 / V1 lines 1587-1589

Operator: `CONTROL`. Input roles: `ACTION`. Output roles: `ACTION`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `CONTROL`.

Transition or retained definition: Continue while condition holds.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WIDE-RANGING

ID: `LEX-wide-ranging`. Roles: modifier_surface.

Source forms: `wide-ranging`.

#### SIG-wide-ranging-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "wide-ranging" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WITHOUT-EXCEPTION

ID: `LEX-without-exception`. Roles: constraint_surface, modifier_surface.

Source forms: `without exception`.

#### SIG-without-exception-SRC-0495

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0495 / V1 lines 1856-1887

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "without exception" on the BINDING_FORCE axis under the bound requirements; do not infer achieved status from the request.

Axis: `BINDING_FORCE`. Destination: Requirement modality, priority, quantifier, scope, tolerance and temporal operator.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-without-exception-SRC-0498

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0498 / V1 lines 1952-1983

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "without exception" on the BREADTH axis under the bound requirements; do not infer achieved status from the request.

Axis: `BREADTH`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

#### SIG-without-exception-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "without exception" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WORKED-EXAMPLE

ID: `LEX-worked-example`. Roles: modifier_surface.

Source forms: `worked example`.

#### SIG-worked-example-SRC-0511

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0511 / V1 lines 2261-2285

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "worked example" on the ABSTRACTION axis under the bound requirements; do not infer achieved status from the request.

Axis: `ABSTRACTION`. Destination: ModifierProfile.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WORKS-FOR-EXAMPLE

ID: `LEX-works-for-example`. Roles: modifier_surface.

Source forms: `works for example`.

#### SIG-works-for-example-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "works for example" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WORKS-NORMALLY

ID: `LEX-works-normally`. Roles: modifier_surface.

Source forms: `works normally`.

#### SIG-works-normally-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "works normally" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WORKS-ONCE

ID: `LEX-works-once`. Roles: modifier_surface.

Source forms: `works once`.

#### SIG-works-once-SRC-0510

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0510 / V1 lines 2240-2260

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "works once" on the ROBUSTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `ROBUSTNESS`. Destination: Acceptance predicate over a perturbation space.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WORST-CASE-EVALUATE

ID: `LEX-worst-case-evaluate`. Roles: specialized_operator.

Source forms: `WORST-CASE-EVALUATE`.

#### SIG-worst-case-evaluate-SRC-0289

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0289 / V1 lines 1107-1109

Operator: `EVALUATE`. Input roles: `CANDIDATE`. Output roles: `REPRESENTATION`.

Correctness obligations: `DECISION_ADMISSIBILITY`. Contract: `EVALUATE`.

Transition or retained definition: Compare candidates under their least favorable admissible case.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### WRITE

ID: `LEX-write`. Roles: specialized_operator.

Source forms: `WRITE`.

#### SIG-write-SRC-0348

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0348 / V1 lines 1313-1315

Operator: `ACT`. Input roles: `ACTION`. Output roles: `WORLD_STATE`.

Correctness obligations: `EXTERNAL_POSTCONDITION`. Contract: `ACT`.

Transition or retained definition: Create or modify content.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ZERO-DEVIATION

ID: `LEX-zero-deviation`. Roles: modifier_surface.

Source forms: `zero-deviation`.

#### SIG-zero-deviation-SRC-0523

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0523 / V1 lines 2505-2550

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "zero-deviation" on the POSITIVE_EXTREME_TAIL_LEXICON axis under the bound requirements; do not infer achieved status from the request.

Axis: `POSITIVE_EXTREME_TAIL_LEXICON`. Destination: Context-bound sense alternatives, not a total strength order.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

### ZERO-DEVIATION-CONSTRAINT

ID: `LEX-zero-deviation-constraint`. Roles: modifier_surface.

Source forms: `zero-deviation constraint`.

#### SIG-zero-deviation-constraint-SRC-0505

Origin: SOURCE_MAPPED_CANDIDATE. Source: SRC-0505 / V1 lines 2114-2136

Operator: `COMPILE`. Input roles: `RULE`. Output roles: `RULE`.

Correctness obligations: `CONSTRAINT_SATISFACTION`. Contract: `MODIFIER`.

Transition or retained definition: Interpret "zero-deviation constraint" on the STRICTNESS axis under the bound requirements; do not infer achieved status from the request.

Axis: `STRICTNESS`. Destination: RequirementPolicy.

Preconditions, postconditions, admissibility, authority, capability, effects, failure rules, verification and closure: inherit the referenced common contract; invocation-specific bindings remain required.

## Evidence boundary and remaining work

The JSON schema checks record structure, not truth. The finite fixture suite checks the declared guard behavior, not the meaning of every future natural-language instruction. The table, graph and structured dictionary share a source and author. Their agreement is an internal consistency result, not independent semantic corroboration.

The new draft therefore retains all source information and exposes typed contracts without certifying open-world saturation, semantic minimality or complete automatic interpretation. The unresolved obligations and non-issued saturation and closure assessments are part of the draft, not concealed omissions.

The package contains the full source archive, instruction, compiler, schema, guards, fixtures, red/green test outputs, complete migration ledgers and replay instructions. The working dictionary can be revised forward without rewriting or losing the prior source.
