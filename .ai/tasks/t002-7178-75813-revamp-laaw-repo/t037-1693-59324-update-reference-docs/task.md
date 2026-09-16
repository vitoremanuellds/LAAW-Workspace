# Update reference docs

**ID:** t037-1693-59324       **Status:** done



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
  - [Validations](#validations)

</details>


## Description

Rewrite all five `LAAW/reference/` files to the new single-context,
two-gate, tasks-with-subtasks model. Each file is re-anchored to the
new `workflow.md` sections and the new directory structure — no phase
language, no constitution folder, no decisions folder, no five-gate
residue. The router skill (step 5) is referenced in `reread-skill-discipline.md`.

## TL;DR

- Rewrite all 5 reference files: `status-and-info.md`,
  `directory-and-links.md`, `scaffold-on-first-use.md`,
  `starting-without-a-plan.md`, `reread-skill-discipline.md`.
- Remove phase/constitution/decisions folder language.
- Update cross-references to new `workflow.md` sections.
- Router-aware in `reread-skill-discipline.md`.

## Context

### Before

- Parent task [t002-7178-75813](../task.md) — the LAAW revamp.
  Depends on t037-1693-16386 (workflow.md rewrite, done).
- Five reference files, all on the old model:
  - `status-and-info.md` — old statuses (`not-planned`, `awaiting-plan-review`,
    `reviewing`, `complete`), old skills (`define-phase`), old status locations
    (phase files, `phases.md`).
  - `directory-and-links.md` — old directory structure (6 layers:
    constitution, context, decisions, phases, tasks, workbench),
    old layer-ownership table.
  - `scaffold-on-first-use.md` — old layer table (constitution, phases,
    tasks, context, decisions, workbench), old owning skills.
  - `starting-without-a-plan.md` — phase-based example (stubbing phases).
  - `reread-skill-discipline.md` — no router mention, references old
    skill-reading pattern.
- `workflow.md` (§3, §11) already has the new structure and statuses
  — references just need updating.

### After

<!-- Filled in by implement-task after implementation -->

## In scope

- **`LAAW/reference/status-and-info.md`** — rewrite:
  - Status table: `define-task` sets `not-started` → `planned`;
    `implement-task` sets `in-progress`; `propagate-context` sets `done`.
    (No `define-phase`, no `validate-work`/`review-work` setting
    `reviewing`.)
  - Status locations: task rows in `tasks.md`, subtask rows in parent
    task file's Subtasks table. No phase file status.
  - Remove "plan-review vs. reviewing" section (two gates, not one
    review with two states).
  - Update "ID order ≠ execution order" to reference the new
    `tasks.md` + Subtasks table pattern.
  - Cross-reference `workflow.md §11`.

- **`LAAW/reference/directory-and-links.md`** — rewrite:
  - New directory structure: `.ai/workflow/`, `.ai/info.md`,
    `.ai/context/` (single folder, merged), `.ai/tasks/` (mandatory),
    `.ai/workbench/` (optional). No constitution/decisions/phases
    folders.
  - Update "why every path must be .ai/-prefixed" — keep the lesson,
    update examples.
  - Update "why cross-references are .ai/workflow/-anchored" — keep
    the lesson, update for the new file set.
  - Update "every layer but .ai/tasks/ is optional" — list the new
    optional layers (context, workbench).
  - Update layer permanent record: `context/` via `context.md`'s
    table (no `phases.md`, no `decisions.md`).
  - Cross-reference `workflow.md §3`.

- **`LAAW/reference/scaffold-on-first-use.md`** — rewrite:
  - New layer table:
    | Layer | Directory | Starter file | Owning skill |
    |---|---|---|---|
    | Gate authority | `.ai/info.md` | `templates/info-template.md` | `create-constitution` |
    | Context | `.ai/context/` | `templates/context-template.md` | `build-context` / `propagate-context` |
    | Workbench | `.ai/workbench/` | `templates/workbench-readme-template.md` | first skill writing into it |
    - (No constitution layer, no phases, no decisions — these are
      all folded into context or eliminated.)
  - Tasks always come into existence with the first task via
    `define-task` (no scaffold needed, just the directory).
  - Cross-reference `workflow.md §3`.

- **`LAAW/reference/starting-without-a-plan.md`** — rewrite:
  - Remove phase-based example entirely.
  - New example: starting without every task planned — `define-task`
    drafts one task (or a parent with subtasks), approved, implemented,
    then the next task is drafted. Normal to plan incrementally.
  - Cross-reference `workflow.md §5`.

- **`LAAW/reference/reread-skill-discipline.md`** — rewrite:
  - Keep the core lesson (read the skill file fresh every time).
  - Add router awareness: when the user says "plan a task" or "implement
    X", the agent first reads `route/SKILL.md`, which points to the
    correct operation skill; then the agent reads that operation skill
    file fresh. The router itself is also read fresh every time.
  - Cross-reference `workflow.md §2`.

## Out of scope

- Changes to `workflow.md` itself — already done by t037-1693-16386.
- Changes to skill files — covered by steps 3–4.
- Changes to templates — covered by step 7.
- Changes to the README — covered by step 8.
- Changes to sync scripts — covered by step 9.

## Steps

1. Rewrite `LAAW/reference/status-and-info.md` — new statuses, new
   skill mappings, new status locations, remove phase/old-gate content.
2. Rewrite `LAAW/reference/directory-and-links.md` — new directory
   structure, new layer table, new permanent record.
3. Rewrite `LAAW/reference/scaffold-on-first-use.md` — new layer table
   (gate authority, context, workbench), tasks always via define-task.
4. Rewrite `LAAW/reference/starting-without-a-plan.md` — task-based
   example, no phase language.
5. Rewrite `LAAW/reference/reread-skill-discipline.md` — router-aware.
6. Verify all cross-references in reference/ point to existing
   `workflow.md` sections and existing reference files.
7. Grep `LAAW/reference/` for stale concepts (`phase`, `constitution`
   as a folder, `decisions`, `awaiting-plan-review`, `reviewing`,
   `complete` as statuses, `define-phase`) — all should be gone or
   explained.

## Validations

- All five reference files exist and follow the new model.
- No phase language, no constitution folder, no decisions folder,
  no `define-phase` references.
- Status table in `status-and-info.md` matches the new four-value
  enum (`not-started`, `planned`, `in-progress`, `done`).
- `scaffold-on-first-use.md` layer table matches the new layers.
- `reread-skill-discipline.md` mentions the router skill.
- All `workflow.md` cross-references point to valid sections (§1–§14).
- Grep for `phase` (as a layer), `constitution` (as a folder),
  `decisions`, `awaiting-plan-review`, `reviewing`, `complete` —
  all hits are explained or gone.
