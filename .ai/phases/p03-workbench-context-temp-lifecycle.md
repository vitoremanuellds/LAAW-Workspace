# P03 — Workbench directory & context-build temp-file lifecycle

## Context

Part of the mission's third goal (workflow-mechanics evolution — see
[`mission.md`](../constitution/mission.md#goals)), decided via
[ADR02](../decisions/adr02-workbench-directory.md), which this phase
file expands into concrete plan steps — read the ADR first for the
actual decision and its reasoning; this section doesn't repeat it.

**Every file this phase's Plan touches is `full`'s actual source
content, edited in `Full-Local-Model-Agent-Workflow/`'s own checkout
and committed to *its own* git history — never this repo's
`.ai/workflow/` copy, which stays a frozen bootstrap snapshot (see
`mission.md`'s Boundaries; this was gotten wrong once already, in
P03-T01, and corrected).** Below, `workflow.md`,
`reference/directory-and-links.md`, `build-context-full/SKILL.md`, and
the two templates all mean the copies under
`Full-Local-Model-Agent-Workflow/`.

Today, `.ai/` (in any project that bootstraps `full`) has no directory
for informal, non-permanent-record content — every existing
subdirectory (`workflow.md` §3) is part of the permanent record with
its own schema (`context/` tracked via `context.md`'s table,
`phases/`/`tasks/` tracked via Status, `decisions/` tracked via
`decisions.md`'s table). Separately, `build-context-full` already
writes two ephemeral files — `context.temp.md` and `build-plan.md`,
from their own templates — but writes them into `.ai/context/` itself,
alongside real content, and its `.iterate` sub-operation currently
ends a finished run by asking the human whether to archive or delete
them (see that skill's "queue is now empty" step) rather than doing
either automatically.

## In scope

- A new `.ai/workbench/` directory: freeform, no fixed file schema, no
  `info.md`/roadmap pointer into it, excluded from every skill's
  "read only what the current task needs" input list.
- Documenting `.ai/workbench/` in `workflow.md` §3 and
  `reference/directory-and-links.md`.
- Relocating `build-context-full`'s `context.temp.md` and
  `build-plan.md` (and their templates' copy targets) from
  `.ai/context/` to `.ai/workbench/`.
- Changing `build-context.iterate`'s "queue empty" step from
  "ask whether to archive or delete" to automatic deletion, per ADR02.
- A `workbench-readme-template.md` template, copied into a newly
  bootstrapped project's `.ai/workbench/README.md` by
  `create-constitution-full`'s first-run step — the same pattern
  already used for `info-template.md`/`context-template.md`/
  `decisions-template.md`. Added 2026-08-29 at the user's suggestion.

## Out of scope

- The `sync-context` skill — [P04](p04-context-sync-from-git-history.md).
- Concurrency/status-model changes — [P05](p05-concurrency-safe-phase-task-planning.md).
- Any skill's temp output other than `build-context-full`'s two files
  — a future skill that grows its own temp file can adopt
  `.ai/workbench/` directly, per ADR02's Consequences, without a new
  phase.

## Requirements

- `.ai/workbench/` exists as a documented, freeform convention in
  `workflow.md` and `reference/directory-and-links.md`.
- `build-context-full` reads/writes `context.temp.md` and
  `build-plan.md` under `.ai/workbench/`, never `.ai/context/`.
- A finished `build-context.iterate` run (empty queue) deletes both
  files without a per-run human confirmation step.
- No skill treats `.ai/workbench/` content as an input it depends on —
  it stays outside the permanent-record hierarchy
  ([`workflow.md` §4](../workflow/workflow.md#4-artifact-hierarchy--context-rule)).
- A newly bootstrapped project gets `.ai/workbench/README.md`
  automatically on first run, the same way it already gets
  `.ai/info.md`/`.ai/context/context.md`/`.ai/decisions/decisions.md`.

## Plan

1. Update `workflow.md` §3 (directory structure diagram) and
   `reference/directory-and-links.md` to document `.ai/workbench/` —
   freeform, disposable, not read as a dependency by any skill.
2. Update `context-temp-template.md` and
   `context-build-plan-template.md`: change their stated copy target
   from `.ai/context/context.temp.md` / `.ai/context/build-plan.md` to
   `.ai/workbench/context.temp.md` / `.ai/workbench/build-plan.md`.
3. Update `build-context-full/SKILL.md`: every reference to
   `.ai/context/context.temp.md` or `.ai/context/build-plan.md` (in
   `.assess`, `.plan`, and `.iterate`) becomes `.ai/workbench/...`.
4. Update `build-context.iterate`'s final step (currently: "ask
   whether `context.temp.md` should be archived or deleted") to:
   delete both `.ai/workbench/context.temp.md` and
   `.ai/workbench/build-plan.md`, commit the deletion, and report
   completion — no human confirmation gate for this specific deletion,
   per ADR02.
5. Add `templates/workbench-readme-template.md` (short — mirrors
   `context-template.md`'s entry-point style: what `.ai/workbench/` is
   for, that nothing in it is part of the permanent record). Update
   `create-constitution-full/SKILL.md`'s step 2 ("first run only")
   to copy it to `.ai/workbench/README.md`, alongside the existing
   three template copies, only if it doesn't exist yet.

## Automatic validations

- `grep -rn "context\.temp\.md\|build-plan\.md" Full-Local-Model-Agent-Workflow/`
  (run from this repo's root) — every match resolves to an
  `.ai/workbench/`-rooted path; none reference `.ai/context/`.
- `.ai/workbench/` is documented in `workflow.md` §3's directory
  diagram.
- `templates/workbench-readme-template.md` exists;
  `create-constitution-full/SKILL.md`'s step 2 references it alongside
  the other three first-run template copies.

## Manual validations

- Run `build-context-full` end to end against a small fixture project
  (copy the updated `Full-Local-Model-Agent-Workflow/` content into
  that fixture's own `.ai/workflow/`, the same way any real consuming
  project would bootstrap it) and confirm `context.temp.md`/`build-plan.md`
  land in and get deleted from `.ai/workbench/`, with `.ai/context/*.md`
  content unaffected in shape.
- Read `workflow.md` §3 and `reference/directory-and-links.md` after
  the edit and confirm `.ai/workbench/`'s "not part of the permanent
  record" framing reads coherently next to the other directories'
  descriptions, not as an afterthought tacked on the end.

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
| P03-T01 | Document `.ai/workbench/` in workflow.md and directory-and-links.md | Establish the directory and its freeform/disposable convention before anything writes into it | — | complete |
| P03-T02 | Repoint `context-temp-template.md`/`context-build-plan-template.md` copy targets to `.ai/workbench/` | Templates declare the new location before the skill that uses them is updated | — | complete |
| P03-T03 | Update `build-context-full/SKILL.md` to read/write `.ai/workbench/context.temp.md` and `.ai/workbench/build-plan.md` | Point the skill's `.assess`/`.plan`/`.iterate` steps at the new location | P03-T01, P03-T02 | complete |
| P03-T04 | Make `build-context.iterate`'s finished-queue step delete both workbench files automatically | Replace the old ask-before-deleting step per ADR02 | P03-T03 | awaiting-plan-review |
| P03-T05 | Add `workbench-readme-template.md` and wire it into `create-constitution-full`'s first-run bootstrap step | New projects get `.ai/workbench/README.md` automatically, same as the other three first-run templates | — | complete |
