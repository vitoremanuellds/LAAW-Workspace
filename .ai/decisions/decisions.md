# Decisions

One row per ADR. Check here before writing a new one — a related
decision may already exist (see `.ai/workflow/workflow.md §7`).

**Kept current by whoever writes the ADR** — the constitution,
phase-planning, or implementation operation (see
`.ai/workflow/workflow.md §10`). Add the row in the same step as
creating the ADR file.

| ID | Name | Description | Status | Relations |
|---|---|---|---|---|
| ADR01 | Bootstrap workflow variants via plain copy, not git submodule | Consuming projects get `.ai/workflow/` via a copy script, not `git submodule add` — avoids submodule dirty-tree/update pain | valid | — |
| ADR02 | Add `.ai/workbench/` as a freeform, disposable directory | Freeform scratch directory for planning notes/Q&A/prompt drafts; `build-context-full`'s temp files move there and get deleted by default once reconciled | valid | gitignore carve-out clause superseded by ADR03 |
| ADR03 | Replace per-profile repos with one modular workflow | One workflow with optional layers (presence/granularity/locality axes) replaces separately-versioned `full`/`Light` repos; supersedes P01 | valid | supersedes ADR02 (workbench gitignore carve-out only) |

**Status** is `valid` or `superseded`. When a later ADR supersedes an
earlier one, update both rows' Relations column (`supersedes ADR01` /
`superseded by ADR03`) rather than deleting the old row — Git keeps
the full history either way, but the table itself should show the
current chain without needing to open every file.
