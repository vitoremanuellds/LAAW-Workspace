# P03 — Workbench directory & context-build temp-file lifecycle

## Context

Part of the mission's third goal (workflow-mechanics evolution — see
[`mission.md`](../constitution/mission.md#goals)), decided via
[ADR02](../decisions/adr02-workbench-directory.md), which this phase
file expands into concrete plan steps — read the ADR first for the
actual decision and its reasoning; this section doesn't repeat it.

Today, `.ai/` has no directory for informal, non-permanent-record
content — every existing subdirectory
([`workflow.md` §3](../workflow/workflow.md#3-directory-structure))
is part of the permanent record with its own schema (`context/`
tracked via `context.md`'s table, `phases/`/`tasks/` tracked via
Status, `decisions/` tracked via `decisions.md`'s table). Separately,
[`build-context-full`](../workflow/skills/build-context-full/SKILL.md)
already writes two ephemeral files —
[`context.temp.md`](../workflow/templates/context-temp-template.md)
and
[`build-plan.md`](../workflow/templates/context-build-plan-template.md)
— but writes them into `.ai/context/` itself, alongside real content,
and its `.iterate` sub-operation currently ends a finished run by
asking the human whether to archive or delete them (see that skill's
"queue is now empty" step) rather than doing either automatically.

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

## Automatic validations

- `grep -rn "context\.temp\.md\|build-plan\.md" .ai/workflow/` —
  every match resolves to an `.ai/workbench/`-rooted path; none
  reference `.ai/context/`.
- `.ai/workbench/` is documented in `workflow.md` §3's directory
  diagram.

## Manual validations

- Run `build-context-full` end to end against a small fixture project
  and confirm `context.temp.md`/`build-plan.md` land in and get
  deleted from `.ai/workbench/`, with `.ai/context/*.md` content
  unaffected in shape.
- Read `workflow.md` §3 and `reference/directory-and-links.md` after
  the edit and confirm `.ai/workbench/`'s "not part of the permanent
  record" framing reads coherently next to the other directories'
  descriptions, not as an afterthought tacked on the end.

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
