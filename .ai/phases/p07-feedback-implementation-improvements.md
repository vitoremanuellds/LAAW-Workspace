# Phase: P07 — Feedback Implementation Improvements

## Context

Source: `.ai/workbench/feedback.md`

This phase addresses three implementation feedback points from the workflow
skills' actual behavior vs. intended design. The changes are all
internal to the `.ai/workflow/` system — no project source code is touched.

- **Git ignore discipline** (point 1): The workflow §12 already states
  "Applies only to non-gitignored files" but the skills explicitly
  ask for commits without checking `.gitignore` first. Make this
  explicit in every skill's commit step.
- **define-task default scope** (point 2): `define-task` currently
  drafts all tasks in scope by default. Change the default to draft
  only one task; only draft all when the user explicitly asks.
- **Status sequence simplification** (point 3): The current sequence
  (`not-planned → awaiting-plan-review → plan-approved → in-progress
  → validating → reviewing → complete`) is too granular. Simplify to:
  `not-planned → awaiting-plan-review → in-progress → reviewing →
  complete` — remove `plan-approved`, merge `validating` into
  `reviewing`.

## In scope

- Git ignore checks added to all skill commit steps
- `define-task` default behavior changed to single-task
- Status enum, transitions, and all references updated across
  workflow.md, reference files, and all skills
- No changes to `.ai/context/`, `.ai/constitution/`, or project
  source code

## Out of scope

- Any changes to the phase/task planning lifecycle gates
- Changes to constitution, context, or decisions layers
- Changes to project source code
- Changes to the `bootstrap` or `build-context` skills' behavior
  (beyond what's needed for gitignore discipline)

## Requirements

1. Every skill's commit step checks `.gitignore` and skips
   gitignored files explicitly in the procedure text.
2. `define-task`'s default changes from "draft all in scope" to
   "draft one"; the "draft all" path requires explicit user request.
3. The status enum is exactly: `not-planned`, `awaiting-plan-review`,
   `in-progress`, `reviewing`, `complete`.
4. All references to `plan-approved` and `validating` statuses are
   removed and replaced with the correct new status.
5. All skills that set or check status values are updated
   consistently.
6. The workflow.md lifecycle diagram and status table are updated.
7. The reference/status-and-info.md lookup table is updated.

## Plan

1. Update all skill commit steps for gitignore discipline
2. Change `define-task` default behavior to single-task
3. Simplify status sequence across workflow.md, references, and skills

## Automatic validations

- `git diff` shows no untracked or modified files outside `.ai/workflow/`
- `grep -r "plan-approved" .ai/workflow/` returns zero matches
- `grep -r "validating" .ai/workflow/` returns zero matches (except in
  the word "validating" as part of "task-validation" or "phase-validation"
  which are gate names, not status values)
- All skills that set `Status to` have a valid status value from the
  new enum

## Manual validations

- Review the gitignore discipline text in each skill — does it clearly
  state what to skip and why?
- Review `define-task`'s new default — does "draft one" feel natural
  as the default?
- Review the status sequence — does removing `plan-approved` and
  merging `validating` into `reviewing` preserve the meaning?

## Tasks

| ID | Title | Depends on | Status |
|---|---|---|---|
| P07-T01 | Add gitignore discipline to all skill commit steps | — | complete |
| P07-T02 | Change define-task default to single-task | — | complete |
| P07-T03 | Simplify status sequence across workflow and skills | — | awaiting-plan-review |
