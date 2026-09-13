# P08-T05: Update LAAW files for phase-folder structure

## Context

See [phase.md](phase.md) for the phase context, requirements, and plan.

This task updates the LAAW/ source files (the actual workflow repository)
to reflect the new phase-folder structure. The mirror workspace
(`.ai/`) was restructured in P08-T04; now the LAAW/ source must match.

The new structure is:
```
.ai/phases/
  p{NN}-{name}/
    phase.md
    t{NN}-{name}.md
.ai/tasks/
  t{NN}-{name}.md  ← orphans stay flat
```

## Implementation

### Objective

Update all LAAW/ source files that reference the old flat task/phase
structure to use the new phase-folder layout. This ensures agents
reading the LAAW workflow source see the correct structure.

### In scope

- Update `LAAW/workflow.md` — all references to task/phase file paths.
- Update `LAAW/skills/define-task/SKILL.md` — file paths and structure.
- Update `LAAW/skills/implement-task/SKILL.md` — task file path references.
- Update `LAAW/skills/define-phase/SKILL.md` — phase file path references.
- Update `LAAW/skills/bootstrap/SKILL.md` — phase/file references.
- Update `LAAW/skills/propagate-context/SKILL.md` — phase/file references.
- Update `LAAW/templates/` — any templates that reference task/phase paths.
- Update `LAAW/reference/` — any reference files that reference task/phase paths.

### Out of scope

- Migrating existing IDs to the new format (deferred).
- Changes to this mirror workspace's `.ai/` structure (done in P08-T04).
- Changes to the git history or rewriting of existing commits.

### Files to modify

- `LAAW/workflow.md` — Update §3 directory structure, §4 artifact
  hierarchy, §11 status references to reflect phase-folder layout.
- `LAAW/skills/define-task/SKILL.md` — Update all file path references:
  - Task files: `tasks/p{NN}-t{NN}-{name}.md` → `phases/p{NN}-{name}/t{NN}-{name}.md`
  - Phase files: `.ai/phases/p{NN}-{name}.md` → `.ai/phases/p{NN}-{name}/phase.md`
  - Task→phase links: `../phases/p{NN}-{name}.md` → `phase.md`
- `LAAW/skills/implement-task/SKILL.md` — Update task file path references.
- `LAAW/skills/define-phase/SKILL.md` — Update phase file path references:
  - Phase file creation: `.ai/phases/p{NN}-{name}.md` → `.ai/phases/p{NN}-{name}/phase.md`
  - Task references in task table.
- `LAAW/skills/bootstrap/SKILL.md` — Update phase/file references.
- `LAAW/skills/propagate-context/SKILL.md` — Update phase/file references.
- `LAAW/templates/adr-template.md` — Check for any path references.
- `LAAW/templates/info-template.md` — Check for any path references.
- `LAAW/templates/context-template.md` — Check for any path references.
- `LAAW/reference/directory-and-links.md` — Update if it references paths.
- `LAAW/reference/status-and-info.md` — Update if it references paths.

### Files to create

- None.

### Steps

1. **Update `LAAW/workflow.md`** — Change all references to the new
   structure:
   - §3 directory structure:
     ```
     .ai/phases/         phases.md (index) + p{NN}-{name}/phase.md
                         (phase file in its folder) +
                         t{NN}-{name}.md (phase-linked tasks in same folder)
                         — optional
     .ai/tasks/          tasks.md (orphan index) +
                         t{NN}-{name}.md (orphan, flat) —
                         the one mandatory layer
     ```
   - §4 artifact hierarchy: update task file shape description:
     ```
     `.ai/tasks/` holds orphan task files: `t{NN}-{name}.md` (no phase
     parent). Phase-linked tasks live in their phase folders:
     `phases/p{NN}-{name}/t{NN}-{name}.md`.
     ```
   - §11 status: update ID order reasoning to reference phase folders.

2. **Update `LAAW/skills/define-task/SKILL.md`** — Change all references:
   - Frontmatter description: `tasks/p{NN}-t{NN}-{name}.md` →
     `phases/p{NN}-{name}/t{NN}-{name}.md`
   - Step 3 (phase-linked): task file path → `phases/p{NN}-{name}/t{NN}-{name}.md`
   - Step 4 (task file body): Context link → `phase.md`
   - Orphan path: stays `tasks/t{NN}-{name}.md`
   - Phase file path: `.ai/phases/p{NN}-{name}.md` → `.ai/phases/p{NN}-{name}/phase.md`

3. **Update `LAAW/skills/implement-task/SKILL.md`** — Change:
   - Step 2: task file path → `phases/p{NN}-{name}/t{NN}-{name}.md`

4. **Update `LAAW/skills/define-phase/SKILL.md`** — Change:
   - Step 2: phase file creation → `.ai/phases/p{NN}-{name}/phase.md`
   - Task table references.

5. **Update `LAAW/skills/bootstrap/SKILL.md`** — Change:
   - Phase creation references.
   - Task file path references.

6. **Update `LAAW/skills/propagate-context/SKILL.md`** — Change:
   - Phase file path references.
   - Task file path references.

7. **Check `LAAW/templates/`** — Update any templates that reference
   task/phase file paths (adr-template, info-template, context-template).

8. **Check `LAAW/reference/`** — Update any reference files that
   reference task/phase file paths (directory-and-links, status-and-info).

9. **Verify all changes** — Run:
   ```bash
   grep -rn "tasks/p{NN}-t{NN}" LAAW/
   grep -rn "p{NN}-t{NN}" LAAW/
   grep -rn "\.ai/phases/p{NN}-[^/]" LAAW/
   ```
   Verify no results (all old flat references updated).

### Dependencies

- P08-T04 (mirror workspace restructured first).
- P08-T01 (ID format defined).

### Expected result

- `LAAW/workflow.md` references the new phase-folder structure.
- All skills reference task files as `phases/p{NN}-{name}/t{NN}-{name}.md`.
- All skills reference phase files as `phases/p{NN}-{name}/phase.md`.
- No stale flat path references remain in LAAW/.

### Automatic validations

- Run `grep -rn "tasks/p{NN}-t{NN}" LAAW/` and verify it returns no results.
- Run `grep -rn "\.ai/phases/p{NN}-[^/]" LAAW/` and verify it returns no results (no flat phase file references).
- Run `grep -rn "phase\.md" LAAW/ | wc -l` and verify it returns > 0 (phase folder references present).
- Run `grep -rn "t{NN}-" LAAW/skills/ | grep "phases/" | wc -l` and verify it returns > 0 (task files in phase folders).

### Manual validations

- Do the updated file paths feel clear and consistent?
- Are there any edge cases missed in the skill files?
- Is the template/ reference file update sufficient?
