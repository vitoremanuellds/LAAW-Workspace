# Flatten phases → tasks-with-subtasks

**ID:** t037-2386-49725       **Status:** not-started



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

Convert phases with completed tasks into parent tasks with subtasks,
update task IDs to the new format (t{xxx-yyyy-zzzzz}), update status
values, and delete the `phases/` folder. Phases with no tasks or that
are obsolete (P01 superseded, P04/P05 awaiting-plan-review with 0 tasks)
are deleted entirely.

## TL;DR
- Convert P02, P03, P06, P07, P08 to parent tasks with subtasks
- Delete P01 (superseded), P04 (0 tasks), P05 (0 tasks)
- Update task IDs to new format
- Update statuses to new enum (not-started/planned/in-progress/done)
- Delete phases/ folder

## Context

### Before
- `phases/` folder with 8 phases:
  - P01 (superseded, 0 tasks) → DELETE
  - P02 (complete, 5 tasks) → parent task with 5 subtasks
  - P03 (complete, 5 tasks) → parent task with 5 subtasks
  - P04 (awaiting-plan-review, 0 tasks) → DELETE
  - P05 (awaiting-plan-review, 0 tasks) → DELETE
  - P06 (complete, 6 tasks) → parent task with 6 subtasks
  - P07 (partial, 3 tasks, T03 awaiting-plan-review) → parent task with 3 subtasks
  - P08 (in-progress, 9 tasks, all complete) → parent task with 9 subtasks
- `phases/phases.md` — index table with 8 phases
- Task IDs in old format (P02-T01, P03-T01, etc.)

### After
- 5 parent task folders in `.ai/tasks/`:
  - t037-2386-13289-non-submodule-bootstrap/ (5 subtasks)
  - t037-2386-79357-workbench-context-temp-lifecycle/ (5 subtasks)
  - t037-2386-24191-redesign-laaw-modular-workflow/ (6 subtasks)
  - t037-2386-43783-feedback-implementation-improvements/ (3 subtasks)
  - t037-2386-49264-feedback-improvements/ (9 subtasks)
- `phases/` folder deleted
- All task IDs in new format

## In scope
- Convert P02, P03, P06, P07, P08 to parent tasks with subtasks
- Delete P01, P04, P05
- Update task IDs to new format
- Update status values to new enum

## Out of scope
- Restructuring tasks (separate subtask)
- Updating AGENTS.md (separate subtask)
- Any changes to the LAAW repo itself

## Steps

1. **Generate IDs:** Use the pre-generated IDs for parent tasks and subtasks.
2. **Create parent task files:** For each phase to convert (P02, P03, P06, P07, P08), create a parent task file with subtask rows.
3. **Create subtask files:** For each task within the parent phases, create a subtask file.
4. **Update tasks.md:** Reference the new parent tasks.
5. **Delete phases/:** Remove the entire `phases/` folder.
6. **Verify:** Confirm all parent tasks and subtasks exist, phases/ is deleted.

## Validations
- `phases/` folder no longer exists
- 5 parent task folders exist in `.ai/tasks/`
- All subtask files exist in their parent folders
- No phase-linked tasks remain
- `tasks.md` references the new parent tasks
