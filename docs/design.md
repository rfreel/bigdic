# Design and scope

The user redirected the task from a decision workbench to a toolkit for the supplied dictionary in rfreel/bigdic. No decision-workbench code is included.

## Contract

Deliver a usable, offline dictionary browser and authoring toolkit. Preserve source bytes and contextual senses. Provide search, intersecting facets, explicit sense comparison, ordered composition, binding checks, source traceability, portable exports, and an automatic recoverable workspace history. Keep the repository's existing license. Do not claim execution of composed instructions.

## Representation choices

The original Markdown is authoritative input. The derived index is computed with a deterministic parser. Lexical records link to every signature, each signature links to a common contract, and both source spans and source-claimed references are retained. No aliasing beyond declared source forms and separator/case normalization is inferred. Normalization is for retrieval, not semantic merging.

Search filters constrain the same signature. Selecting a term displays a sense; adding it to a sequence is an explicit user operation. The compiler preserves operator order and does not infer missing operands. It reports missing bindings and adjacent role mismatches without asserting semantic invalidity. It retains common contracts and local refinements separately, leaving substantive conflict resolution to the user/agent.

## Visual system

A generated concept established the black/offwhite/lime palette, three-column dictionary, uppercase wordmark, monospaced controls, large sans-serif heading, bordered sense inspector, and bottom sequence strip. Implementation replaces generated fictional dictionary facts and provider labels with canonical source data. Intentional deviations: actual counts and sense names; no window-control decoration or invented affiliation; real role and axis dropdowns instead of invented category counts. Build/Compare/Inspect use the same visual system. Layout stacks responsively on narrow screens.

## Resource and persistence choices

A single self-contained HTML output avoids network dependency, account setup, and installation. Modular JavaScript remains the editable source. No framework is needed for this bounded document-authoring surface. Node's built-in test runner and crypto are sufficient for core checks.

History records complete draft snapshots so restoration is simple and auditable. The app appends a new record for corrections and verifies loaded history before allowing writes. A backup carries its dictionary fingerprint and chain head. This protects against accidental mutation relative to a trusted copy, not a malicious owner rewriting all anchors. Maximum 100 steps, 2,000 history events, 20,000 prompt characters, 4,000 characters per binding, and 10 MB imports bound local workloads.
