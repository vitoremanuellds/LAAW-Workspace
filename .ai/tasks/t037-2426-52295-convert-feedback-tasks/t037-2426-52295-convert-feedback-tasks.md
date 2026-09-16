# Convert Feedback Tasks
**ID:** t037-2426-52295       **Status:** in-progress

## Description
Address feedback from `.ai/workbench/feedback.md` by converting all existing
tasks to the new `task.md` naming convention, fixing the broken define-task
description, and reviewing context files that don't follow the ID pattern.

## TL;DR
- Update LAAW repo skills/instructions for task.md format, then sync
- Fix define-task description bug in LAAW repo, then sync
- Migrate .ai folder to new task.md format
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
- Update LAAW repo skills/instructions for task.md format
- Fix define-task description bug in LAAW repo
- Sync skills after LAAW repo changes
- Migrate .ai folder to new task.md format
- Review context files not following ID pattern

## Out of scope
- Changes to task content or logic (only file renaming and description fix)
- New task creation or deletion

## Steps
1. Update LAAW repo skills for task.md format
   - Read `LAAW/skills/` and update task-related instructions to use `task.md` naming
   - Commit changes in LAAW repo
2. Fix define-task description bug in LAAW repo
   - Read `LAAW/skills/define-task/SKILL.md`
   - Fix the description that complains about "{}" and ":"
   - Commit changes in LAAW repo
3. Sync skills from LAAW repo to `.agents/skills/`
4. Migrate .ai folder to new task.md format
   - Rename all task files from `t{id}-{name}.md` to `task.md`
   - Update all internal references (links in other task files, tasks.md)
5. Review context files not following ID pattern
   - Check `architecture.md`, `full-directory-structure.md`, `purpose.md`
   - If necessary: convert to `c{ID}-{name}.md` format
   - If not necessary: delete them

## Validations
- LAAW repo skills use task.md naming convention
- LAAW repo define-task description no longer complains about "{}" and ":"
- `.agents/skills/` synced from LAAW repo
- All .ai task folders contain `task.md` (not `t{id}-{name}.md`)
- All links to task files are updated
- `.ai/tasks/tasks.md` references are correct
- Context files either follow `c{ID}-{name}.md` pattern or are deleted

## Subtasks
| id | name | description | depends on | status |
|---|---|---|---|---|
| t037-2427-11111 | convert-task-file-naming | Update LAAW repo skills/instructions for task.md format, sync, then migrate .ai folder | — | not-started |
| t037-2427-22222 | fix-define-task-description | Fix define-task skill in LAAW repo, then sync | — | not-started |
| t037-2427-33333 | review-context-id-pattern | Review context files not following ID pattern and convert or delete as needed | t037-2427-11111 | not-started |
