# Update templates

**ID:** t037-1693-63951       **Status:** done

## Description

Replace the template set in `LAAW/templates/` to the settled seven
files: two new (`task-template.md`, `context-item-template.md`), three
updated (`context-template.md`, `info-template.md`,
`workbench-readme-template.md`), one renamed (`context-temp-template.md`
→ `assumptions-template.md`), and two removed (`adr-template.md`,
`decisions-template.md`). All templates follow the new single-context,
tasks-with-subtasks model.

## TL;DR

- New: `task-template.md`, `context-item-template.md`.
- Updated: `context-template.md`, `info-template.md`,
  `workbench-readme-template.md`.
- Renamed: `context-temp-template.md` → `assumptions-template.md`.
- Removed: `adr-template.md`, `decisions-template.md`.
- Total: 7 templates (was 5 existing + 2 new = 7, minus 2 removed
  from old set = 7).

## Context

### Before

- Parent task [t002-7178-75813](t002-7178-75813-revamp-laaw-repo.md) — the LAAW revamp.
  Depends on t037-1693-16386 (workflow.md rewrite, done).
- Decision [c037-1650-68133](../../context/c037-1650-68133-revamp-open-decisions.md)
  settles the final template set (7 files) and their names.
- Current templates (5 files):
  - `info-template.md` — policy block with mode/overrides.
  - `context-template.md` — mission/techstack section + index table
    (old format with Status column).
  - `adr-template.md` — ADR format (Decision/Context/Alternatives/
    Consequences) — to be removed.
  - `decisions-template.md` — decisions index (to be removed).
  - `workbench-readme-template.md` — workbench description.
  - `context-temp-template.md` — context temp/build plan (to be
    renamed to `assumptions-template.md`).
- The revamp design has decisions as `c-{ID}` context rows (not ADRs),
  mission/techstack inline in `context.md`, and a new task-file layout.

### After

<!-- Filled in by implement-task after implementation -->

## In scope

- **New: `LAAW/templates/task-template.md`** — the exact task-file
  layout from the revamp design:
  ```markdown
  # <name>
  **ID:** t{ID}       **Status:** in-progress

  ## Description
  <what this task is and why — the intent, one short paragraph>

  ## TL;DR
  <the fastest possible orientation to the task>

  ## Context
  ### Before
  <the knowledge/situation the agent needs to START this task>
  ### After
  <the context/understanding this task PRODUCES once implemented>

  ## In scope
  - <the changes this task makes>

  ## Out of scope
  - <what is explicitly NOT touched>

  ## Steps
  1. <ordered step>
  2. <ordered step>

  ## Validations
  - <how to check done>

  ## Subtasks            ← optional
  | id | name | description | depends on | status |
  |----|------|-------------|------------|--------|
  ```

- **New: `LAAW/templates/context-item-template.md`** — `c-{ID}` item
  shape, including the decision shape with relation/superseded-by:
  ```markdown
  # <name>

  **ID:** c-{ID}
  **Name:** <name>
  **Relation:** <related context file(s)>
  **Superseded by:** —

  ## <section>
  <content>
  ```
  Decision variant includes Decision/Context/Alternatives/Consequences
  subsections (replacing the old adr-template.md).

- **Updated: `LAAW/templates/context-template.md`** — now the
  `context.md` index: mission + techstack core inline + index table
  (no separate Status column; columns: File, Description, Relation,
  Superseded by).

- **Updated: `LAAW/templates/info-template.md`** — keep the policy
  block format, remove `delegated` mode (not in the new model — the
  new model only has `manual`, `assisted`, `autonomous`).

- **Updated: `LAAW/templates/workbench-readme-template.md`** — keep
  the workbench description, update any stale references.

- **Renamed: `LAAW/templates/assumptions-template.md`** — rename from
  `context-temp-template.md`. This is the assumptions file for
  ground-up context building.

- **Removed: `LAAW/templates/adr-template.md`** — decisions are
  context rows now (per c037-1650-68133).

- **Removed: `LAAW/templates/decisions-template.md`** — decisions are
  context rows now (per c037-1650-68133).

## Out of scope

- Changes to `workflow.md` — already done by t037-1693-16386.
- Changes to skills — covered by steps 3–4.
- Changes to reference docs — covered by step 6.
- Changes to the README — covered by step 8.
- Changes to sync scripts — covered by step 9.

## Steps

1. Create `LAAW/templates/task-template.md` from the design's task
   file layout (exact).
2. Create `LAAW/templates/context-item-template.md` with the `c-{ID}`
   shape and the decision variant.
3. Update `LAAW/templates/context-template.md` — inline mission/
   techstack + index table with new columns (File, Description,
   Relation, Superseded by).
4. Update `LAAW/templates/info-template.md` — remove `delegated` mode.
5. Update `LAAW/templates/workbench-readme-template.md` — keep content,
   update stale references if any.
6. Rename `LAAW/templates/context-temp-template.md` →
   `LAAW/templates/assumptions-template.md` (update any internal
   references).
7. Delete `LAAW/templates/adr-template.md`.
8. Delete `LAAW/templates/decisions-template.md`.
9. Verify the template count is exactly 7.
10. Verify no skill or reference file references a removed template
    (adr-template.md, decisions-template.md) — those references belong
    to steps 3–6.

## Validations

- Exactly 7 template files exist: `task-template.md`,
  `context-item-template.md`, `context-template.md`,
  `info-template.md`, `workbench-readme-template.md`,
  `assumptions-template.md`, `context-build-plan-template.md`.
  (Wait — the decision says 7: task-template, context-item-template,
  context-template, assumptions-template, info-template,
  workbench-readme-template, context-build-plan-template.)
- `adr-template.md` and `decisions-template.md` are deleted.
- `task-template.md` matches the design's exact task-file layout.
- `context-item-template.md` includes the decision shape.
- `context-template.md` has inline mission/techstack + new index table.
- `info-template.md` has no `delegated` mode.
- No other file in `LAAW/` references the removed templates.
