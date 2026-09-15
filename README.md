# BIGDIC

A working toolkit for the **Canonical Prompt Operator and Modifier Dictionary V2**.

**Open [`dist/bigdic.html`](dist/bigdic.html) in a modern browser.** Download the raw HTML first; GitHub's file viewer does not execute applications. No server, account, API key, package installation, or external assets are required for the app. For consistent browser storage, use the local server below.

## What you can do

- Search **794 lexemes and 1,000 signatures**, including definitions, source forms, input/output roles, obligations, and modifier axes.
- Filter by one of **20 inherited contracts**, provenance, lexical role, or axis. Facets apply to the same sense.
- Compare up to four explicit senses. Different values are highlighted without declaring them semantically incompatible.
- Compose and reorder a sequence of exact signatures. Bind objective, target, scope, actor, revision, required outputs, and evidence plans.
- Export complete Markdown instructions, a structured contract, or an editable project. Local refinements and inherited contracts are both preserved.
- Inspect a prompt for dictionary expressions, multiple senses, and nested matches. Matching does not infer negation, intent, authority, or applicability.
- Save automatically in the browser, export a hash-linked history backup, and restore an earlier draft as a new event.

The application never executes dictionary operators or calls an LLM. It is a deterministic dictionary and instruction-authoring tool.

## Run or build

Requires Node.js 20+ for the CLI, tests, and build. No runtime dependencies.

```sh
npm test
npm run build
npm start
```

Open http://127.0.0.1:4173. Set `PORT` to change the port. The server binds only to the local machine.

## Command line

```sh
node cli.mjs audit
node cli.mjs search VERIFY
node cli.mjs show SIG-verify-P-external
node cli.mjs inspect "Rigorously verify exactly two sources"
node cli.mjs compile examples/source-review.json
node cli.mjs compile examples/source-review.json --json
```

`compile` accepts an unwrapped project JSON. The browser's editable export contains `format`, `sourceHash`, and `project`; extract its `project` member for the CLI, or use the included example.

## Source integrity

The exact uploaded Markdown is retained in `data/dictionary-v2.md`.

SHA-256: `1df69d1f70f4cb66fe1fa73b8924e1d8dd06967fe494342f5385291e819cc23f`

The parser accounts for all 794 lexical records and 1,000 signature headings. This is structural coverage, not proof of semantic completeness. The source's referenced V1 archive and `data/dictionary_v2.json` were not supplied. Original source references are retained as claims from the uploaded V2; they are not falsely resolved against the V2 line numbers. The UI separately reports the actual V2 line span.

The original document reports its own prior test counts. Those historical claims are not this toolkit's test results. Current receipts are in `receipts/`.

## Honest boundaries

- `BOUND_DRAFT` means required fields have been supplied, not that their contents are true, adequate, authorized, or semantically compatible.
- Adjacent role mismatch is a review warning. Roles are semantic views, so mismatch is not automatically invalidity.
- No universal ordering optimizer, semantic conflict solver, authority checker, or automatic disambiguation is claimed.
- The prompt inspector displays longest non-overlapping matches and retains nested candidates. It does not understand English context.
- Browser history is append-only through the application, with SHA-256 links. It is **not write-once storage**. Someone who controls the entire history and its head can recompute it. Keep exported backups as independent anchors.
- Browser clearing or private-mode expiry can remove local state. Export backups for durability. File-URL storage behavior varies by browser; the local server is recommended for long-lived workspaces.
- Cross-tab writes use Web Locks where available and a stale-state comparison. Without Web Locks, simultaneous writes are not guaranteed safe; use one tab.
- Importing a history validates its chain and dictionary revision, then appends its final draft to the current workspace. It does not merge imported history into local history.
- Corrupt storage is preserved rather than overwritten. Browse and inspect remain usable. Export the raw history for recovery.

## Structure

`src/core.mjs` owns parsing, lookup, comparison, lexical inspection, binding checks, and compilation. `src/journal.mjs` owns history integrity. `src/app.mjs` owns browser interaction. `build.mjs` produces a deterministic single-file app. The canonical source is bundled locally without network loading.

See [design and scope](docs/design.md), [verification](docs/verification.md), and [operator coverage](docs/operator-coverage.md).
