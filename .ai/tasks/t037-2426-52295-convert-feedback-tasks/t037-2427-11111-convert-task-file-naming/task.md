# convert-task-file-naming
**ID:** t037-2427-11111       **Status:** in-progress



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Description](#description)
  - [TL;DR](#tldr)
  - [Context](#context)
    - [Before](#before)
    - [After](#after)
  - [Context After](#context-after)
  - [In scope](#in-scope)
  - [Out of scope](#out-of-scope)
  - [Steps](#steps)
  - [Validations](#validations)
  - [Rule](#rule)

</details>
## Description
Convert all task file references from the old `t{ID}-{name}.md` naming to the
new `task.md` convention across the LAAW repo, `.ai/workflow/`, and
`.agents/skills/`. Then sync LAAW repo changes into `.agents/skills/` and
`.ai/workflow/`, and migrate all existing `.ai/` task files to the new
folder+`task.md` structure.

## TL;DR
- Update LAAW skills (define-task, implement-task) for `task.md` naming
- Update LAAW skills to always use `tools/generate-id.py` for ID generation
- Update LAAW workflow.md and README.md for `task.md` naming
- Sync LAAW → `.agents/skills/` and `.ai/workflow/`
- Migrate `.ai/` task files from `t{id}-{name}.md` to `task.md`

## Context
### Before
- Every skill and workflow file references `t{ID}-{name}.md` as the task file
  name inside a task folder.
- The old leaf-task format was `tasks/t{ID}-{name}.md` (a bare file).
- The old subtask format was
  `tasks/t{parent-ID}-{parent-name}/t{subtask-ID}-{subtask-name}.md`.
- The new format is:
  - Leaf task: `tasks/t{ID}-{name}/task.md`
  - Parent with subtasks:
    `tasks/t{ID}-{name}/task.md` + subtask folders below
  - Subtask: `tasks/t{ID}-{name}/t{sub-ID}-{sub-name}/task.md`

### After
- All skills and workflow files reference `task.md` as the task file name.
- All task folders follow the `t{ID}-{name}/task.md` pattern.
- `.agents/skills/` and `.ai/workflow/` are synced from LAAW repo.

## Context After
- The task file naming convention is `t{ID}-{name}/task.md` for all tasks (leaf and parent).
- All LAAW skills include the generate-id instruction requiring `tools/generate-id.py --prefix t` for task IDs and `--prefix c` for context IDs.
- `.ai/tasks/tasks.md` links point to `task.md` files.
- LAAW repo, `.agents/skills/`, and `.ai/workflow/` are in sync with the task.md naming convention.

## In scope
- Update `LAAW/skills/define-task/SKILL.md` — replace all `t{ID}-{name}.md`
  and `t{parent-ID}-{parent-name}/t{subtask-ID}-{subtask-name}.md` references
  with `task.md` equivalents.
- Update `LAAW/skills/implement-task/SKILL.md` — same replacement pattern.
- Update all LAAW repo skills to include the generate-id instruction:
  "Always use `tools/generate-id.py --prefix t` to generate IDs for any
  project file that requires an ID. Never hardcode, guess, or manually
  construct IDs — the script is the single source of truth for ID generation
  across the entire project."
- Update `LAAW/workflow.md` §3 directory structure — replace task file
  references with `task.md` format.
- Update `LAAW/README.md` directory structure section — same replacement.
- Sync LAAW repo changes into `.agents/skills/` (copy all SKILL.md files).
- Sync LAAW repo changes into `.ai/workflow/` (copy workflow.md, README.md,
  skills/, reference/, templates/, tools/).
- Migrate `.ai/` task files: rename `t{id}-{name}.md` to `task.md` inside
  existing task folders; update all internal links (tasks.md, sibling task
  files).

## Out of scope
- Fixing the define-task description bug (handled by
  t037-2427-22222-fix-define-task-description).
- Adding Table of Contents to multi-section markdown files (handled by
  t037-2427-44444-add-section-index-to-all-md-files).
- Reviewing context files for ID pattern compliance (handled by
  t037-2427-33333-review-context-id-pattern).

## Steps
1. Update `LAAW/skills/define-task/SKILL.md`
   - Replace `tasks/t{ID}-{name}.md` → `tasks/t{ID}-{name}/task.md`
   - Replace `t{ID}-{name}.md` → `task.md` (standalone references)
   - Replace `t{parent-ID}-{parent-name}/t{subtask-ID}-{subtask-name}.md` →
     `t{parent-ID}-{parent-name}/t{subtask-ID}-{subtask-name}/task.md`
   - Update frontmatter description to use `task.md` format
   - Add generate-id instruction to the skill
   - Verify no remaining `t{ID}-{name}.md` references

2. Update `LAAW/skills/implement-task/SKILL.md`
   - Replace `tasks/t{ID}-{name}.md` → `tasks/t{ID}-{name}/task.md`
   - Replace `tasks/t{ID}-{name}/t{ID}-{name}.md` →
     `tasks/t{ID}-{name}/task.md`
   - Replace `tasks/t{parent-ID}-{parent-name}/t{sub-ID}-{sub-name}.md` →
     `tasks/t{parent-ID}-{parent-name}/t{sub-ID}-{sub-name}/task.md`
   - Add generate-id instruction to the skill

3. Add generate-id instruction to ALL remaining LAAW repo skills
   - For each SKILL.md in `LAAW/skills/`:
     - Add: "Always use `tools/generate-id.py --prefix t` to generate IDs
       for any project file that requires an ID. Never hardcode, guess, or
       manually construct IDs — the script is the single source of truth
       for ID generation across the entire project."
     - Also add: "Always use `tools/generate-id.py --prefix c` to generate
       IDs for context files."
     - Verify no hardcoded IDs exist in subtask tables or elsewhere

3. Update `LAAW/workflow.md` §3 (directory structure)
   - Replace `t{ID}-{name}.md (leaf)` → `t{ID}-{name}/task.md`
   - Replace `parent file t{ID}-{name}.md` → `parent file task.md`

4. Update `LAAW/README.md` directory structure section
   - Same replacements as workflow.md

5. Commit LAAW repo changes
   - Stage all modified LAAW files
   - Commit with message describing the naming convention update

6. Sync LAAW → `.agents/skills/`
   - Copy all SKILL.md files from `LAAW/skills/` to `.agents/skills/`
   - Overwrite existing files

7. Sync LAAW → `.ai/workflow/`
   - Copy `LAAW/workflow.md` → `.ai/workflow/workflow.md`
   - Copy `LAAW/README.md` → `.ai/workflow/README.md`
   - Copy `LAAW/skills/` → `.ai/workflow/skills/`
   - Copy `LAAW/reference/` → `.ai/workflow/reference/`
   - Copy `LAAW/templates/` → `.ai/workflow/templates/`
   - Copy `LAAW/tools/` → `.ai/workflow/tools/`

8. Migrate `.ai/` task files to `task.md` format
   - For each existing task folder `t{ID}-{name}/` in `.ai/tasks/`:
     - Rename `t{ID}-{name}.md` → `task.md`
   - Update `.ai/tasks/tasks.md` links to point to `task.md`
   - Update any sibling task file links that reference renamed tasks

9. Commit `.ai/` migration changes
   - Stage all renamed/modified `.ai/` files
   - Commit with message describing the task file format migration

## Validations
- All LAAW skills (define-task, implement-task) reference `task.md` — no
  remaining `t{ID}-{name}.md` references
- All LAAW repo skills include the generate-id instruction
- All `.agents/skills/` files match LAAW repo
- `.ai/workflow/workflow.md` and `.ai/workflow/README.md` use `task.md` naming
- All `.ai/tasks/t{ID}-{name}/` folders contain `task.md` (not `t{ID}-{name}.md`)
- `.ai/tasks/tasks.md` links point to correct `task.md` paths
- No broken internal links to task files

## Rule
- **Always use `tools/generate-id.py --prefix t` to generate IDs for
  any project file that requires an ID.** Never hardcode, guess, or
  manually construct IDs — the script is the single source of truth
  for ID generation across the entire project.
