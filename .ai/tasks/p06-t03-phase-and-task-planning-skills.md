# P06-T03 — Update phase- and task-planning skills for `phases.md`/orphan tasks

## Context

See [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md)
and [ADR03](../decisions/adr03-single-modular-workflow.md). Depends on
P06-T01.

**LAAW's actual source files, edited in
`LAAW/`'s own checkout, committed to *its
own* git history.**

## Implementation

### Objective

`define-phase` reads/writes `.ai/phases/phases.md` instead of
`.ai/constitution/roadmap.md`, with its own scaffold-on-first-use step.
`define-task-full` becomes `define-task`, gains the orphan-task
convention.

### In scope

- `define-phase/SKILL.md`: every `roadmap.md` reference becomes
  `phases.md`; add a first step that scaffolds `.ai/phases/` +
  `phases.md` (empty table) if the directory doesn't exist yet, per
  `reference/scaffold-on-first-use.md`; Status values/enum unchanged.
- `git mv skills/define-task-full skills/define-task`; update
  frontmatter.
- `define-task/SKILL.md`: document both task file naming conventions —
  `p{NN}-t{NN}-{name}.md` (phase-linked, unchanged) and
  `t{NN}-{name}.md` (orphan, own sequential counter). Add a step:
  when drafting an orphan task, scaffold `.ai/tasks/tasks.md` (index
  table: `| ID | Title | Purpose | Depends on | Status |`) if it
  doesn't exist yet, and add/update this task's row there as its
  permanent record (phase-linked tasks keep using their phase file's
  own task table, unchanged, never duplicated into `tasks.md`).
  Confirm no `Source`/ticket-link field is part of the task file
  template — task files stay agnostic to where the description
  originated (ADR03).

### Out of scope

- Any other skill — T02, T04.
- `info-template.md`/other templates — T05.

### Files to modify

- `LAAW/skills/define-phase/SKILL.md`
- `LAAW/skills/define-task-full/SKILL.md`
  (moved to `define-task/SKILL.md`)

### Files to create

None.

### Steps

1. In `define-phase/SKILL.md`, replace every `roadmap.md` reference
   with `phases.md`; add the scaffold-on-first-use step as the new
   step 1 (renumber existing steps).
2. `git mv skills/define-task-full skills/define-task`.
3. Rewrite `define-task/SKILL.md`: frontmatter name/description; add
   the orphan-task naming + `tasks.md` scaffold/update step; keep the
   phase-linked path exactly as today otherwise.

### Dependencies

P06-T01.

### Expected result

`define-phase` and `define-task` both work with the new
`phases.md`/`tasks.md` layer files and the orphan-task convention.

### Automatic validations

- `test -f LAAW/skills/define-task/SKILL.md`
- `test ! -d LAAW/skills/define-task-full`
- `grep -n roadmap.md LAAW/skills/define-phase/SKILL.md`
  — no hits.
- `grep -n "t{NN}-{name}" LAAW/skills/define-task/SKILL.md`
  — at least one hit (orphan convention documented).

### Manual validations

- Walk through drafting one orphan task and one phase-linked task by
  hand against the rewritten `define-task/SKILL.md` — confirm neither
  path leaves an ambiguous "which table gets this row" question.
