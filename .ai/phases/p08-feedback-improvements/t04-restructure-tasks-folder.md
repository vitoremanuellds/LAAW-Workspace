# P08-T04: Restructure tasks/ folder

## Context

See [phase.md](phase.md)
for the phase context, requirements, and plan.

This task restructures the `.ai/` directory from a flat layout to a
phase-folder layout. The correct structure is:

```
.ai/phases/
  p01-design-light-profile/
    phase.md
    t01-design-light-profile.md
  p02-non-submodule-bootstrap-mechanism/
    phase.md
    t01-version-stamp-convention.md
    t02-copy-resync-script.md
    ...
.ai/tasks/
  tasks.md
  t01-split-workflow-md-into-layer-references.md  ← orphans stay flat
```

Phase files move into their own folders under `.ai/phases/` as `phase.md`.
All phase-linked tasks for a phase live alongside the phase file in the
same folder. Orphan tasks remain flat in `.ai/tasks/`.

Relevant prior work: P08-T01 designed the ID format; P08-T02 created the
ID generation script; P08-T03 updated `LAAW/workflow.md`.

## Implementation

### Objective

Restructure `.ai/` from the current flat layout to the phase-folder layout,
reducing crowding while keeping orphan tasks flat. This is a
reorganization only — no content changes to task or phase files themselves.

### In scope

- Move each existing phase file from `.ai/phases/p{NN}-{name}.md` to
  `.ai/phases/p{NN}-{name}/phase.md` (create the folder, rename the file).
- Move phase-linked task files from `.ai/tasks/p{NN}-t{NN}-{name}.md` to
  `.ai/phases/p{NN}-{name}/t{NN}-{name}.md` (alongside the phase file).
- Keep orphan task files (`t{NN}-{name}.md`) flat in `.ai/tasks/`.
- Update all internal relative links:
  - Task files linking to the phase file: change `../phases/p{NN}-{name}.md`
    to `phase.md` (same folder).
  - Phase files linking to task files: update paths from
    `../../tasks/p{NN}-t{NN}-{name}.md` to `t{NN}-{name}.md`.
  - Phase files linking to other phases or context: update from
    `../phases/...` to `../p{NN}-{name}/phase.md` or `../../context/...`.
- Update `.ai/context/full-directory-structure.md` to reflect the new
  phase-folder layout.

### Out of scope

- Migrating existing ID formats (deferred — existing IDs remain valid).
- Restructuring existing phase files' content (only the folder layout
  changes; only new phases adopt the new folder layout per the phase
  requirements).
- Changes to `LAAW/` source files (that's a separate concern).
- Changes to the git history or rewriting of existing commits.

### Files to create

- `.ai/phases/p01-design-light-profile/phase.md` (rename from `.ai/phases/p01-design-light-profile.md`)
- `.ai/phases/p01-design-light-profile/t01-design-light-profile.md` (rename from `.ai/tasks/p01-t01-design-light-profile.md`)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism/phase.md` (rename from `.ai/phases/p02-non-submodule-bootstrap-mechanism.md`)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism/t01-version-stamp-convention.md` (rename from `.ai/tasks/p02-t01-version-stamp-convention.md`)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism/t02-copy-resync-script.md` (rename from `.ai/tasks/p02-t02-copy-resync-script.md`)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism/t03-update-laaw-readme.md` (rename from `.ai/tasks/p02-t03-update-laaw-readme.md`)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism/t04-update-workspace-docs.md` (rename from `.ai/tasks/p02-t04-update-workspace-docs.md`)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism/t05-dogfood-workspace-resync.md` (rename from `.ai/tasks/p02-t05-dogfood-workspace-resync.md`)
- `.ai/phases/p03-workbench-context-temp-lifecycle/phase.md` (rename from `.ai/phases/p03-workbench-context-temp-lifecycle.md`)
- `.ai/phases/p03-workbench-context-temp-lifecycle/t01-document-workbench-directory.md` (rename from `.ai/tasks/p03-t01-document-workbench-directory.md`)
- `.ai/phases/p03-workbench-context-temp-lifecycle/t02-repoint-context-temp-templates.md` (rename from `.ai/tasks/p03-t02-repoint-context-temp-templates.md`)
- `.ai/phases/p03-workbench-context-temp-lifecycle/t03-repoint-build-context-full-skill.md` (rename from `.ai/tasks/p03-t03-repoint-build-context-full-skill.md`)
- `.ai/phases/p03-workbench-context-temp-lifecycle/t04-automate-workbench-cleanup.md` (rename from `.ai/tasks/p03-t04-automate-workbench-cleanup.md`)
- `.ai/phases/p03-workbench-context-temp-lifecycle/t05-workbench-readme-template.md` (rename from `.ai/tasks/p03-t05-workbench-readme-template.md`)
- `.ai/phases/p04-context-sync-from-git-history/phase.md` (rename from `.ai/phases/p04-context-sync-from-git-history.md`)
- `.ai/phases/p05-concurrency-safe-phase-task-planning/phase.md` (rename from `.ai/phases/p05-concurrency-safe-phase-task-planning.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/phase.md` (rename from `.ai/phases/p06-redesign-laaw-modular-workflow.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/t01-scaffold-convention-and-workflow-rewrite.md` (rename from `.ai/tasks/p06-t01-scaffold-convention-and-workflow-rewrite.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/t02-constitution-and-bootstrap-skills.md` (rename from `.ai/tasks/p06-t02-constitution-and-bootstrap-skills.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/t03-phase-and-task-planning-skills.md` (rename from `.ai/tasks/p06-t03-phase-and-task-planning-skills.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/t04-remaining-skills-rename-and-update.md` (rename from `.ai/tasks/p06-t04-remaining-skills-rename-and-update.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/t05-templates-and-reference-updates.md` (rename from `.ai/tasks/p06-t05-templates-and-reference-updates.md`)
- `.ai/phases/p06-redesign-laaw-modular-workflow/t06-validation-and-size-check.md` (rename from `.ai/tasks/p06-t06-validation-and-size-check.md`)
- `.ai/phases/p07-feedback-implementation-improvements/phase.md` (rename from `.ai/phases/p07-feedback-implementation-improvements.md`)
- `.ai/phases/p07-feedback-implementation-improvements/t01-gitignore-discipline-for-all-skills.md` (rename from `.ai/tasks/p07-t01-gitignore-discipline-for-all-skills.md`)
- `.ai/phases/p07-feedback-implementation-improvements/t02-define-task-default-to-single-task.md` (rename from `.ai/tasks/p07-t02-define-task-default-to-single-task.md`)
- `.ai/phases/p07-feedback-implementation-improvements/t03-simplify-status-sequence.md` (rename from `.ai/tasks/p07-t03-simplify-status-sequence.md`)
- `.ai/phases/p08-feedback-improvements/phase.md` (rename from `.ai/phases/p08-feedback-improvements.md`)
- `.ai/phases/p08-feedback-improvements/t01-design-id-format.md` (rename from `.ai/tasks/p08-t01-design-id-format.md`)
- `.ai/phases/p08-feedback-improvements/t02-id-generation-script.md` (rename from `.ai/tasks/p08-t02-id-generation-script.md`)
- `.ai/phases/p08-feedback-improvements/t03-update-workflow.md` (rename from `.ai/tasks/p08-t03-update-workflow.md`)
- `.ai/phases/p08-feedback-improvements/t04-restructure-tasks-folder.md` (rename from `.ai/tasks/p08-t04-restructure-tasks-folder.md`)

### Files to modify

- `.ai/phases/p01-design-light-profile.md` — rename to `phase.md` inside
  new folder; update links to tasks.
- `.ai/phases/p02-non-submodule-bootstrap-mechanism.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/phases/p03-workbench-context-temp-lifecycle.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/phases/p04-context-sync-from-git-history.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/phases/p05-concurrency-safe-phase-task-planning.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/phases/p06-redesign-laaw-modular-workflow.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/phases/p07-feedback-implementation-improvements.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/phases/p08-feedback-improvements.md` — rename to
  `phase.md` inside new folder; update links to tasks.
- `.ai/tasks/p08-t04-restructure-tasks-folder.md` — update Context link
  from `../phases/p08-feedback-improvements.md` to
  `../../phases/p08-feedback-improvements/phase.md`.
- `.ai/context/full-directory-structure.md` — Update the `.ai/phases/`
  and `.ai/tasks/` snapshots to show the new phase-folder layout.

### Files to delete

- `.ai/phases/p01-design-light-profile.md` (renamed to `phase.md` in folder)
- `.ai/phases/p02-non-submodule-bootstrap-mechanism.md` (renamed to `phase.md` in folder)
- `.ai/phases/p03-workbench-context-temp-lifecycle.md` (renamed to `phase.md` in folder)
- `.ai/phases/p04-context-sync-from-git-history.md` (renamed to `phase.md` in folder)
- `.ai/phases/p05-concurrency-safe-phase-task-planning.md` (renamed to `phase.md` in folder)
- `.ai/phases/p06-redesign-laaw-modular-workflow.md` (renamed to `phase.md` in folder)
- `.ai/phases/p07-feedback-implementation-improvements.md` (renamed to `phase.md` in folder)
- `.ai/phases/p08-feedback-improvements.md` (renamed to `phase.md` in folder)
- `.ai/tasks/p01-t01-design-light-profile.md` (moved to p01/)
- `.ai/tasks/p02-t01-version-stamp-convention.md` (moved to p02/)
- `.ai/tasks/p02-t02-copy-resync-script.md` (moved to p02/)
- `.ai/tasks/p02-t03-update-laaw-readme.md` (moved to p02/)
- `.ai/tasks/p02-t04-update-workspace-docs.md` (moved to p02/)
- `.ai/tasks/p02-t05-dogfood-workspace-resync.md` (moved to p02/)
- `.ai/tasks/p03-t01-document-workbench-directory.md` (moved to p03/)
- `.ai/tasks/p03-t02-repoint-context-temp-templates.md` (moved to p03/)
- `.ai/tasks/p03-t03-repoint-build-context-full-skill.md` (moved to p03/)
- `.ai/tasks/p03-t04-automate-workbench-cleanup.md` (moved to p03/)
- `.ai/tasks/p03-t05-workbench-readme-template.md` (moved to p03/)
- `.ai/tasks/p06-t01-scaffold-convention-and-workflow-rewrite.md` (moved to p06/)
- `.ai/tasks/p06-t02-constitution-and-bootstrap-skills.md` (moved to p06/)
- `.ai/tasks/p06-t03-phase-and-task-planning-skills.md` (moved to p06/)
- `.ai/tasks/p06-t04-remaining-skills-rename-and-update.md` (moved to p06/)
- `.ai/tasks/p06-t05-templates-and-reference-updates.md` (moved to p06/)
- `.ai/tasks/p06-t06-validation-and-size-check.md` (moved to p06/)
- `.ai/tasks/p07-t01-gitignore-discipline-for-all-skills.md` (moved to p07/)
- `.ai/tasks/p07-t02-define-task-default-to-single-task.md` (moved to p07/)
- `.ai/tasks/p07-t03-simplify-status-sequence.md` (moved to p07/)
- `.ai/tasks/p08-t01-design-id-format.md` (moved to p08/)
- `.ai/tasks/p08-t02-id-generation-script.md` (moved to p08/)
- `.ai/tasks/p08-t03-update-workflow.md` (moved to p08/)
- `.ai/tasks/p08-t04-restructure-tasks-folder.md` (moved to p08/)

### Steps

1. **Create phase subdirectories** — For each phase that has tasks,
   create a subdirectory under `.ai/phases/`:
   ```bash
   mkdir -p .ai/phases/p01-design-light-profile
   mkdir -p .ai/phases/p02-non-submodule-bootstrap-mechanism
   mkdir -p .ai/phases/p03-workbench-context-temp-lifecycle
   mkdir -p .ai/phases/p04-context-sync-from-git-history
   mkdir -p .ai/phases/p05-concurrency-safe-phase-task-planning
   mkdir -p .ai/phases/p06-redesign-laaw-modular-workflow
   mkdir -p .ai/phases/p07-feedback-implementation-improvements
   mkdir -p .ai/phases/p08-feedback-improvements
   ```

2. **Move phase files into their folders** — Rename each phase file
   from `.ai/phases/p{NN}-{name}.md` to `.ai/phases/p{NN}-{name}/phase.md`:
   ```bash
   mv .ai/phases/p01-design-light-profile.md .ai/phases/p01-design-light-profile/phase.md
   mv .ai/phases/p02-non-submodule-bootstrap-mechanism.md .ai/phases/p02-non-submodule-bootstrap-mechanism/phase.md
   mv .ai/phases/p03-workbench-context-temp-lifecycle.md .ai/phases/p03-workbench-context-temp-lifecycle/phase.md
   mv .ai/phases/p04-context-sync-from-git-history.md .ai/phases/p04-context-sync-from-git-history/phase.md
   mv .ai/phases/p05-concurrency-safe-phase-task-planning.md .ai/phases/p05-concurrency-safe-phase-task-planning/phase.md
   mv .ai/phases/p06-redesign-laaw-modular-workflow.md .ai/phases/p06-redesign-laaw-modular-workflow/phase.md
   mv .ai/phases/p07-feedback-implementation-improvements.md .ai/phases/p07-feedback-implementation-improvements/phase.md
   mv .ai/phases/p08-feedback-improvements.md .ai/phases/p08-feedback-improvements/phase.md
   ```

3. **Move phase-linked task files into their phase folders** — For each
   phase, move files from `.ai/tasks/p{NN}-t{NN}-{name}.md` to
   `.ai/phases/p{NN}-{name}/t{NN}-{name}.md`:
   ```bash
   # P01 tasks
   mv .ai/tasks/p01-t01-design-light-profile.md .ai/phases/p01-design-light-profile/t01-design-light-profile.md

   # P02 tasks
   mv .ai/tasks/p02-t01-version-stamp-convention.md .ai/phases/p02-non-submodule-bootstrap-mechanism/t01-version-stamp-convention.md
   mv .ai/tasks/p02-t02-copy-resync-script.md .ai/phases/p02-non-submodule-bootstrap-mechanism/t02-copy-resync-script.md
   mv .ai/tasks/p02-t03-update-laaw-readme.md .ai/phases/p02-non-submodule-bootstrap-mechanism/t03-update-laaw-readme.md
   mv .ai/tasks/p02-t04-update-workspace-docs.md .ai/phases/p02-non-submodule-bootstrap-mechanism/t04-update-workspace-docs.md
   mv .ai/tasks/p02-t05-dogfood-workspace-resync.md .ai/phases/p02-non-submodule-bootstrap-mechanism/t05-dogfood-workspace-resync.md

   # P03 tasks
   mv .ai/tasks/p03-t01-document-workbench-directory.md .ai/phases/p03-workbench-context-temp-lifecycle/t01-document-workbench-directory.md
   mv .ai/tasks/p03-t02-repoint-context-temp-templates.md .ai/phases/p03-workbench-context-temp-lifecycle/t02-repoint-context-temp-templates.md
   mv .ai/tasks/p03-t03-repoint-build-context-full-skill.md .ai/phases/p03-workbench-context-temp-lifecycle/t03-repoint-build-context-full-skill.md
   mv .ai/tasks/p03-t04-automate-workbench-cleanup.md .ai/phases/p03-workbench-context-temp-lifecycle/t04-automate-workbench-cleanup.md
   mv .ai/tasks/p03-t05-workbench-readme-template.md .ai/phases/p03-workbench-context-temp-lifecycle/t05-workbench-readme-template.md

   # P06 tasks
   mv .ai/tasks/p06-t01-scaffold-convention-and-workflow-rewrite.md .ai/phases/p06-redesign-laaw-modular-workflow/t01-scaffold-convention-and-workflow-rewrite.md
   mv .ai/tasks/p06-t02-constitution-and-bootstrap-skills.md .ai/phases/p06-redesign-laaw-modular-workflow/t02-constitution-and-bootstrap-skills.md
   mv .ai/tasks/p06-t03-phase-and-task-planning-skills.md .ai/phases/p06-redesign-laaw-modular-workflow/t03-phase-and-task-planning-skills.md
   mv .ai/tasks/p06-t04-remaining-skills-rename-and-update.md .ai/phases/p06-redesign-laaw-modular-workflow/t04-remaining-skills-rename-and-update.md
   mv .ai/tasks/p06-t05-templates-and-reference-updates.md .ai/phases/p06-redesign-laaw-modular-workflow/t05-templates-and-reference-updates.md
   mv .ai/tasks/p06-t06-validation-and-size-check.md .ai/phases/p06-redesign-laaw-modular-workflow/t06-validation-and-size-check.md

   # P07 tasks
   mv .ai/tasks/p07-t01-gitignore-discipline-for-all-skills.md .ai/phases/p07-feedback-implementation-improvements/t01-gitignore-discipline-for-all-skills.md
   mv .ai/tasks/p07-t02-define-task-default-to-single-task.md .ai/phases/p07-feedback-implementation-improvements/t02-define-task-default-to-single-task.md
   mv .ai/tasks/p07-t03-simplify-status-sequence.md .ai/phases/p07-feedback-implementation-improvements/t03-simplify-status-sequence.md

   # P08 tasks
   mv .ai/tasks/p08-t01-design-id-format.md .ai/phases/p08-feedback-improvements/t01-design-id-format.md
   mv .ai/tasks/p08-t02-id-generation-script.md .ai/phases/p08-feedback-improvements/t02-id-generation-script.md
   mv .ai/tasks/p08-t03-update-workflow.md .ai/phases/p08-feedback-improvements/t03-update-workflow.md
   mv .ai/tasks/p08-t04-restructure-tasks-folder.md .ai/phases/p08-feedback-improvements/t04-restructure-tasks-folder.md
   ```

4. **Verify orphan tasks remain flat** — Confirm orphan tasks are
   untouched:
   ```bash
   ls .ai/tasks/t01-split-workflow-md-into-layer-references.md
   ls .ai/tasks/t02-fix-laaw-submodule-mislabel.md
   ls .ai/tasks/t03-explicit-gate-skip-for-missing-layers.md
   ```
   These three files should still be directly in `.ai/tasks/`.

5. **Update internal links in moved task files** — Each moved task file
   has a Context section linking to the phase file via `../phases/p{NN}-{name}.md`.
   Since the task file now lives in the same folder as the phase file,
   change the link to `phase.md`:
   
   For each moved task file, change:
   ```markdown
   See [../phases/p{NN}-{name}.md](../phases/p{NN}-{name}.md)
   ```
   to:
   ```markdown
   See [phase.md](phase.md)
   ```
   
   This applies to all 25 moved task files (P01: 1, P02: 5, P03: 5,
   P06: 6, P07: 3, P08: 4).

6. **Update internal links in phase files** — Each phase file has links
   to its tasks and possibly to context/decisions. Update:
   - Links to tasks: change `../../tasks/p{NN}-t{NN}-{name}.md` to
     `t{NN}-{name}.md` (same folder).
   - Links to context: change `../context/...` to `../../context/...`.
   - Links to decisions: change `../decisions/...` to `../../decisions/...`.
   - Links to other phases: change `../phases/p{NN}-{name}.md` to
     `../p{NN}-{name}/phase.md`.

7. **Update `.ai/context/full-directory-structure.md`** — Update the
   `.ai/phases/` and `.ai/tasks/` snapshots to show the new structure:
   ```
   .ai/phases/         phases.md (index) + p{NN}-{name}/phase.md
                       (phase file in its folder) +
                       t{NN}-{name}.md (phase-linked tasks in same folder)
   .ai/tasks/          tasks.md (orphan index) +
                       t{NN}-{name}.md (orphan, flat) —
                       the one mandatory layer
   ```

8. **Verify the final structure** — Run:
   ```bash
   find .ai/phases/ -type f -name '*.md' | sort
   find .ai/tasks/ -type f -name '*.md' | sort
   ```
   Verify:
   - Each phase has its own folder with `phase.md` and `tNN-*.md` files.
   - Orphan files `t01-*.md`, `t02-*.md`, `t03-*.md` are flat in
     `.ai/tasks/`.
   - No `.md` files remain directly in `.ai/phases/` (except `phases.md`).
   - No `pNN-tNN-*.md` files remain in `.ai/tasks/` (except `tasks.md`).

### Dependencies

- None — this is a self-contained reorganization.

### Expected result

- `.ai/phases/` has phase subdirectories (`p01/`, `p02/`, `p03/`,
  `p04/`, `p05/`, `p06/`, `p07/`, `p08/`) each containing a `phase.md`
  and their respective task files.
- Orphan tasks (`t01-`, `t02-`, `t03-`) remain flat in `.ai/tasks/`.
- All internal links in moved task files and phase files are updated correctly.
- `full-directory-structure.md` reflects the new layout.

### Automatic validations

- Run `find .ai/phases/ -maxdepth 1 -name '*.md' | wc -l` and verify it returns 1 (only `phases.md`).
- Run `find .ai/phases/ -name 'phase.md' | wc -l` and verify it returns 8 (one per phase).
- Run `find .ai/phases/ -name 't*-*.md' | wc -l` and verify it returns 25 (all phase-linked tasks moved).
- Run `ls .ai/tasks/t*.md` and verify it shows exactly 3 orphan files.
- Run `grep -l '\.\./phases/p' .ai/phases/*/t*-*.md | wc -l` and verify it returns 0 (no stale `../phases/p` links in task files).
- Run `grep -l '^\s*See \[phase.md\]' .ai/phases/*/t*-*.md | wc -l` and verify it returns 25 (all task files reference `phase.md`).

### Manual validations

- Does the phase-folder structure improve navigability?
- Are there any task files with links that break after the move?
- Is the orphan task flat layout still intuitive?
