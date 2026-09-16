# Convert Feedback Tasks
**ID:** t037-2426-52295       **Status:** in-progress

## Description
Address feedback from `.ai/workbench/feedback.md` by converting all existing
tasks to the new `task.md` naming convention, fixing the broken define-task
description, and reviewing context files that don't follow the ID pattern.

## TL;DR
- Rename all task files from `t{id}-{name}.md` to `task.md` inside their folders
- Fix define-task description that complains about "{}" and ":"
- Review context files (architecture.md, full-directory-structure.md, purpose.md)
  for ID pattern compliance

## Context
### Before
- All tasks use the old naming: `t{id}-{name}.md` inside `t{id}-{name}/`
- define-task description has a bug complaining about "{}" and ":"
- 3 context files don't follow the `c{ID}-{name}.md` pattern

### After
<!-- Filled in by implement-task after implementation; propagate-context
     reads this section to promote reusable knowledge to context/ -->

## In scope
- Convert all existing task files to `task.md` naming
- Fix define-task description bug
- Review and fix context files not following ID pattern

## Out of scope
- Changes to task content or logic (only file renaming and description fix)
- New task creation or deletion

## Steps
1. Rename all task files from `t{id}-{name}.md` to `task.md`
   - For each folder in `.ai/tasks/t*/`, rename the `.md` file to `task.md`
   - Update all internal references (links in other task files, tasks.md)
2. Fix define-task description bug
   - Read `.agents/skills/define-task/SKILL.md` to identify the "{}" and ":" issue
   - Fix the description to not trigger the complaint
3. Review context files not following ID pattern
   - Check `architecture.md`, `full-directory-structure.md`, `purpose.md`
   - If necessary: convert to `c{ID}-{name}.md` format
   - If not necessary: delete them

## Validations
- All task folders contain `task.md` (not `t{id}-{name}.md`)
- All links to task files are updated
- `.ai/tasks/tasks.md` references are correct
- define-task description no longer complains about "{}" and ":"
- Context files either follow `c{ID}-{name}.md` pattern or are deleted

## Subtasks
| id | name | description | depends on | status |
|---|---|---|---|---|
| t037-2427-11111 | convert-task-file-naming | Rename all task files from `t{id}-{name}.md` to `task.md` and update all references | — | not-started |
| t037-2427-22222 | fix-define-task-description | Fix the broken define-task description that complains about "{}" and ":" | — | not-started |
| t037-2427-33333 | review-context-id-pattern | Review context files not following ID pattern and convert or delete as needed | t037-2427-11111 | not-started |
