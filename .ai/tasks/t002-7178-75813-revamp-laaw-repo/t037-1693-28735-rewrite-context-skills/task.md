# Rewrite context skills

**ID:** t037-1693-28735       **Status:** done



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Description](#description)
  - [TL;DR](#tldr)
  - [Context](#context)
    - [Before](#before)
    - [After](#after)
  - [In scope](#in-scope)
  - [Out of scope](#out-of-scope)
  - [Steps](#steps)
    - [Step 1 — Rewrite `create-constitution`](#step-1-rewrite-create-constitution)
    - [Step 2 — Rewrite `build-context`](#step-2-rewrite-build-context)
    - [Step 3 — Rewrite `propagate-context`](#step-3-rewrite-propagate-context)
    - [Step 4 — Rewrite `bootstrap`](#step-4-rewrite-bootstrap)
  - [Dependencies](#dependencies)
  - [Expected result](#expected-result)
  - [Automatic validations](#automatic-validations)
  - [Manual validations](#manual-validations)

</details>


## Description

Rewrite LAAW's four context skills (`create-constitution`, `build-context`,
`propagate-context`, `bootstrap`) to the single-context-folder model.
`create-constitution` scaffolds `info.md` + `context/context.md` with
inline mission/techstack core + index table; `build-context` fills
`c-{ID}.md` items directly; `propagate-context` does single-folder
promote/finalize with no phase-file routing; `bootstrap` gets a new
layer menu (no phases, no decisions).

## TL;DR

Replace the old constitution-folder + three-gate + decisions-folder model
with a single `context/` folder that holds everything: mission, techstack,
architecture, decisions (as `c-{ID}.md` rows). Rewrite all four context
skills to this model.

## Context

### Before

- `LAAW/skills/create-constitution/SKILL.md` — writes `mission.md` +
  `techstack.md` to `.ai/constitution/`; writes ADRs to
  `.ai/decisions/`; scaffolds `.ai/info.md` on first run.
- `LAAW/skills/build-context/SKILL.md` — three sub-operations
  (`.assess` → `.plan` → `.iterate`); uses `.ai/workbench/` for temp
  files (`context.temp.md`, `build-plan.md`); writes to
  `.ai/context/` with `context.md` index table.
- `LAAW/skills/propagate-context/SKILL.md` — three sub-operations
  (`.task`, `.phase`, `.project`); routes phase-linked task context to
  phase file's Context section; promotes to `context/` only at phase
  completion; updates `tasks.md` or phase file's task table.
- `LAAW/skills/bootstrap/SKILL.md` — layer menu includes
  constitution/context/decisions/phases/workbench; triggers each
  layer's own scaffold step.
- `LAAW/templates/` — `context-template.md` (context.md index),
  `context-temp-template.md` (assumptions),
  `context-build-plan-template.md` (iteration plan),
  `decisions-template.md` (ADR index), `adr-template.md` (ADR shape).

### After

- `create-constitution` — scaffolds `.ai/info.md` (first run) +
  `.ai/context/context.md` with inline mission/techstack core + index
  table; writes `c-{ID}-{name}.md` for project-level decisions; no
  `.ai/constitution/` folder, no `.ai/decisions/` folder.
- `build-context` — simplified: reads real files, writes `c-{ID}-{name}.md`
  items directly to `context/`; no temp files, no workbench, no
  `.assess`/`.plan`/`.iterate` sub-operations; just "read files, write
  context".
- `propagate-context` — single sub-operation (`.task`); writes directly
  to `context/` (no phase-file routing); updates `context.md`'s index
  table; sets task status to `done`.
- `bootstrap` — new layer menu: constitution/context/workbench (no
  phases, no decisions); triggers each chosen layer's own scaffold step.
- `LAAW/templates/` — `context-template.md` updated to single-folder
  index with mission/techstack inline; `context-temp-template.md` and
  `context-build-plan-template.md` removed (no temp files);
  `decisions-template.md` removed (decisions are context rows).

## In scope

- `LAAW/skills/create-constitution/SKILL.md` — full rewrite.
- `LAAW/skills/build-context/SKILL.md` — full rewrite.
- `LAAW/skills/propagate-context/SKILL.md` — full rewrite.
- `LAAW/skills/bootstrap/SKILL.md` — full rewrite.
- `LAAW/templates/context-template.md` — updated to single-folder index.
- `LAAW/templates/context-temp-template.md` — delete (no temp files).
- `LAAW/templates/context-build-plan-template.md` — delete (no temp
  files).
- `LAAW/templates/decisions-template.md` — delete (decisions are context
  rows).

## Out of scope

- Rewriting `define-task`, `implement-task`, `validate-work`,
  `review-work` — that's t037-1693-17315 (already done).
- Adding the router skill — t037-1693-50470.
- Updating `reference/` files — t037-1693-59324.
- Updating `templates/` beyond the four context templates above —
  t037-1693-63951 (task-template.md, assumptions-template.md, etc.).
- README rewrite — t037-1693-66263.
- Sync scripts — t037-1693-73540.
- Any change to `tools/` or `workflow.md` itself.

## Steps

### Step 1 — Rewrite `create-constitution`

Rewrite `LAAW/skills/create-constitution/SKILL.md` for the single-context
model:

1. **Frontmatter:** Update `name` and `description` — remove all
   constitution-folder and decisions-folder references; single-context
   model with inline mission/techstack.
2. **Can/Must/Cannot:** Update the operation contract:
   - **Can:** context artifacts (mission, techstack, decisions as
     `c-{ID}.md`), ask clarification.
   - **Must:** write `c-{ID}-{name}.md` for project-level decisions;
     first run, bootstrap `info.md` unedited, never overwrite existing.
   - **Cannot:** touch code; invent unsupported requirements; scaffold
     any layer other than `info.md` + `context/` — that's each other
     layer's own owning skill.
3. **When to use:** Creating or updating `.ai/context/context.md`
   (mission/techstack inline + index table). On a brand-new project,
   this also bootstraps `.ai/info.md`.
4. **Inputs:** Remove references to `constitution/` and `decisions/`
   templates. Keep `info-template.md`. Add reference to
   `context-template.md` (now the single-folder index).
5. **Procedure:**
   - Step 1: Read existing context files if present — do not overwrite
     blind.
   - Step 2: **First run only:** if `.ai/info.md` doesn't exist, copy
     `templates/info-template.md` there unedited. Never overwrite if
     it already exists.
   - Step 3: Ask the user for anything missing (mission, techstack).
   - Step 4: Write `.ai/context/context.md`: inline mission/techstack
     core + index table (columns: File, Description, Status,
     Relations). Keep it stable — this file should rarely need to
     change.
   - Step 5: Ask the user whether there's anything else to add before
     requesting review.
   - Step 6: If a project-level decision was made, write a
     `c-{ID}-{name}.md` context row (use `tools/generate-id.py --prefix
     c`) and add its index row in `context.md`'s table. No
     `.ai/decisions/` directory.
   - Step 7: Commit — stage `context/context.md` (and `info.md` if
     just created), plus any `c-{ID}.md` files; the message should say
     what was drafted or updated. Stop for `task-review` gate.
     **When approval comes back:** in `manual`/`assisted` mode, report
     and explicitly ask whether to proceed.
6. **Output:** `.ai/context/context.md` (always). `.ai/info.md` — first
   run only. A new `c-{ID}-{name}.md` context row if a project-level
   decision was made.

### Step 2 — Rewrite `build-context`

Rewrite `LAAW/skills/build-context/SKILL.md` for the simplified
single-context model:

1. **Frontmatter:** Update `name` and `description` — remove all
   `.assess`/`.plan`/`.iterate` sub-operations, workbench references,
   and temp-file references; simplified: reads real files, writes
   `c-{ID}.md` items directly.
2. **Can/Must/Cannot:**
   - **Can:** read project files; write `c-{ID}-{name}.md` to
     `context/`; update `context.md`'s index table.
   - **Must:** get human review of context content before committing;
     never delete a `[ASSUMPTION]` or `[QUESTION]` line unilaterally.
   - **Cannot:** copy task history; duplicate info; record reasoning.
3. **When to use:** `context/` is thin or doesn't exist — this skill
   builds it by surveying the codebase. Not a required step of
   bootstrap; invoked when the human wants context built up deliberately.
4. **Procedure:** Simplified to a single path (no sub-operations):
   - Step 1: If `.ai/context/` doesn't exist, scaffold it (copy
     `templates/context-template.md` to `context.md`).
   - Step 2: Run a recursive directory listing of the project, excluding
     `.git/`, `.ai/workflow/`, and build/dependency directories.
   - Step 3: For each file (or batch of files, if the user specifies a
     batch size):
     - Read the file in full.
     - Write or update a `c-{ID}-{name}.md` context file in `context/`.
     - Update `context.md`'s index table in the same step.
   - Step 4: Ask the user whether to process more files, or stop.
   - Step 5: Commit — stage the updated `context/*.md` files and
     `context.md`'s table; the message should say which files were
     processed. Stop for `task-review` gate.
5. **Output:** Updated `context/*.md` files, `context.md`'s index table,
   plus any `c-{ID}.md` files created.

### Step 3 — Rewrite `propagate-context`

Rewrite `LAAW/skills/propagate-context/SKILL.md` for the single-folder
model:

1. **Frontmatter:** Update `name` and `description` — remove all
   phase-file routing, `.phase`/`.project` sub-operations, and old
   status values; single sub-operation (`.task`), direct-to-context
   propagation.
2. **Can/Must/Cannot:**
   - **Can:** propagate reusable knowledge to `context/`; update
     `context.md`'s index table; set task status to `done`.
   - **Must:** verify the `task-completion-review` gate was approved
     before marking complete; never write to `context/` without
     approval.
   - **Cannot:** copy task history; duplicate info; record reasoning.
3. **When to use:** After a task's `task-completion-review` passes —
   this skill promotes what the task learned into `context/`.
4. **Procedure:** Single sub-operation (`.task`):
   - Step 1: Inspect what the task actually produced.
   - Step 2: Ask: does anything discovered here matter *beyond this
     task itself*? If not, skip to step 3. If yes, write directly to
     `context/` (new or existing `c-{ID}-{name}.md` file, plus its row
     in `context.md`'s table), scaffolding `context/` first per
     `reference/scaffold-on-first-use.md` if it doesn't exist yet.
   - Step 3: Set the task's Status to `done` in `.ai/tasks/tasks.md`.
   - Step 4: Commit — stage the updated `context/*.md` files and
     `context.md`'s table, plus the updated Status row; the message
     should say which task completed. Stop for `task-review` gate (if
     the project uses it for propagation).
   - Step 5: Ask whether a related follow-up task should be defined
     now — a plain question, not a gate.
5. **Status enum:** `not-started` · `planned` · `in-progress` · `done`
   (+`blocked`). No `complete`, `reviewing`, or `awaiting-plan-review`.
6. **Output:** Updated `context/*.md` files, `context.md`'s index table,
   updated Status row in `tasks.md`.

### Step 4 — Rewrite `bootstrap`

Rewrite `LAAW/skills/bootstrap/SKILL.md` for the new layer menu:

1. **Frontmatter:** Update `name` and `description` — remove
   decisions/phases from the layer menu; new menu:
   constitution/context/workbench.
2. **Can/Must/Cannot:** Same as before, but updated for the new layer
   menu.
3. **When to use:** Same as before — a human wants to set up several
   optional layers deliberately.
4. **Inputs:** Update to reflect the new layer menu.
5. **Procedure:**
   - Step 1: If `.ai/info.md` doesn't exist, create it via
     `create-constitution`'s own info.md-bootstrap step (copy
     `templates/info-template.md` unedited).
   - Step 2: Check which optional layers already exist (constitution,
     context, workbench — each per
     `reference/scaffold-on-first-use.md`'s directory column). Ask the
     user only about the ones that don't exist yet.
   - Step 3: For each layer the user chooses:
     - **Constitution** — run `create-constitution`'s full procedure
       now (the mission/techstack interview happens as part of this
       choice, not deferred) — including its own commit and
       `task-review` gate at the end.
     - **Context** — create `.ai/context/` and copy
       `templates/context-template.md` to `context.md` unedited.
       An empty, ready-to-use scaffold — an actual codebase survey is
       `build-context`'s own, separate, larger operation, run later if
       wanted.
     - **Workbench** — create `.ai/workbench/` and copy
       `templates/workbench-readme-template.md` to `README.md`
       unedited.
   - Step 4: Commit — stage everything scaffolded this run (excluding
     whatever constitution's own procedure already committed itself in
     step 3); the message should say which layers were set up. No gate
     of its own for the non-constitution layers.
6. **Output:** `.ai/info.md` — always, first run only. Any subset of
   `.ai/context/context.md` (via `create-constitution`, with its own
   gate), `.ai/workbench/README.md` — whichever layers were chosen.

## Dependencies

- `t037-1693-16386` (rewrite-workflow-md) — `workflow.md` must be
  rewritten first so skills can reference the correct directory structure
  and context model.

## Expected result

A clean set of four context skills:
- `create-constitution` — single-context model; inline mission/techstack
  in `context.md`; decisions as `c-{ID}.md` rows.
- `build-context` — simplified: read files, write `c-{ID}.md` items.
- `propagate-context` — single sub-operation; direct-to-context; no
  phase-file routing.
- `bootstrap` — new layer menu (constitution/context/workbench).
- `templates/` — `context-template.md` updated; `context-temp`,
  `context-build-plan`, `decisions` templates deleted.

No references to `.ai/constitution/`, `.ai/decisions/`, `.ai/phases/`,
or old status values remain in these four files.

## Automatic validations

- `grep -r 'constitution' LAAW/skills/create-constitution/SKILL.md` →
  **no hits** (except in the skill name and the layer name "constitution"
  as a menu option).
- `grep -r 'decisions/' LAAW/skills/create-constitution/SKILL.md` →
  **no hits** (decisions are context rows now).
- `grep -r 'phase' LAAW/skills/propagate-context/SKILL.md` →
  **no hits** (no phase-file routing).
- `grep -r 'decisions\|decisions/' LAAW/skills/bootstrap/SKILL.md` →
  **no hits** (decisions not in layer menu).
- `grep -r 'phase\|phases' LAAW/skills/bootstrap/SKILL.md` →
  **no hits** (phases not in layer menu).
- `grep -r '.assess\|.plan\|.iterate' LAAW/skills/build-context/SKILL.md`
  → **no hits** (no sub-operations).
- `grep -r '.phase\|.project' LAAW/skills/propagate-context/SKILL.md`
  → **no hits** (no phase/project sub-operations).
- `grep -r 'complete\b\|reviewing\b\|awaiting-plan-review' LAAW/skills/propagate-context/SKILL.md`
  → **no hits** (old status values).
- `ls LAAW/templates/context-temp-template.md LAAW/templates/context-build-plan-template.md LAAW/templates/decisions-template.md`
  → **files do not exist** (deleted).
- `grep -c 'c-{ID}' LAAW/skills/create-constitution/SKILL.md` →
  **≥ 1** (decisions are context rows).
- `grep -c 'task-review' LAAW/skills/create-constitution/SKILL.md` →
  **≥ 1** (constitution goes through task-review gate).
- `grep -c 'task-completion-review' LAAW/skills/propagate-context/SKILL.md`
  → **≥ 1** (propagation happens after task-completion-review).
- `grep -c 'not-started\|planned\|in-progress\|done' LAAW/skills/propagate-context/SKILL.md`
  → **≥ 1** (new status enum).

## Manual validations

- A fresh agent reading `workflow.md` + `context.md` of a freshly
  synced scratch project can understand the single-context model from
  these four skills alone, without reading reference files.
- The `context.md` index table has the correct columns (File, Description,
  Status, Relations) and matches the shape used by all four skills.
- The status enum is the same across all four skills and matches
  `workflow.md` §11.
