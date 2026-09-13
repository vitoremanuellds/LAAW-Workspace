# P08-T03: Update workflow.md

## Context

See [../phases/p08-feedback-improvements.md](../phases/p08-feedback-improvements.md)
for the phase context, requirements, and plan.

This task updates `LAAW/workflow.md` to reflect the new ID format
introduced in P08-T01/P08-T02. The new format is
`{prefix}{minutes:07d}{random:05d}-{name}` (e.g., `p352374948815-name`)
instead of the old sequential format (`p{NN}`, `t{NN}`).

## Implementation

### Objective

Update all ID references in `LAAW/workflow.md` to reflect the new
ID format — the 12-digit timestamp+random component instead of
sequential `{NN}`.

### In scope

- Update §3 (Directory structure) — task file name format.
- Update §4 (Artifact hierarchy) — ID format references.
- Update §11 (Status) — ID format examples and reasoning.
- Any other references to `{NN}` or sequential IDs.

### Out of scope

- Restructuring task folders (P08-T04).
- Updating `.ai/` files (this is the LAAW workflow source).
- Migrating existing IDs (deferred).

### Files to create

- None.

### Files to modify

- `LAAW/workflow.md` — Update ID format references throughout.

### Steps

1. **Update §3 (Directory structure)** — Change the task file format
   from `p{NN}-t{NN}-{name}.md` (where NN is 2-digit sequential) to
   `p{NN}-t{NN}-{name}.md` (where NN is 12-digit timestamp+random).
   Add a note explaining the new format:
   ```
   .ai/tasks/          tasks.md (orphan index) + p{NN}-t{NN}-{name}.md
                       (phase-linked) + t{NN}-{name}.md (orphan) —
                       the one mandatory layer
                       {NN} = {minutes:07d}{random:05d} (12 digits,
                       zero-padded)
   ```

2. **Update §4 (Artifact hierarchy)** — Add a note about the new ID
   format in the paragraph about task file shapes:
   ```
   `.ai/tasks/` holds two task-file shapes, distinguished by filename
   alone, each its own ID sequence: `p{NN}-t{NN}-{name}.md` (linked to a
   phase) and `t{NN}-{name}.md` (orphan). {NN} is a 12-digit
   zero-padded ID: `{minutes:07d}{random:05d}` (e.g.,
   `p352374948815-t00525960123456-name`).
   ```

3. **Update §11 (Status)** — Change the ID order reasoning paragraph:
   ```
   **ID order ≠ execution order** — a replan can insert a task/phase that
   belongs earlier but still gets the next-highest ID. Resolve
   "first/next" via Depends-on + Status, never the lowest ID; ask if
   ambiguous. The 12-digit ID is lexicographically sortable, but
   Depends-on defines actual execution order.
   ```

4. **Search for other `{NN}` references** — Grep the file for any
   remaining `{NN}` or sequential ID patterns and update them:
   ```bash
   grep -n "{NN}" LAAW/workflow.md
   ```

5. **Verify the changes** — Read the updated sections and verify:
   - All ID format references use the new 12-digit format
   - No stale `{NN}` references remain
   - The examples are consistent

### Dependencies

- `LAAW/constants.py` must exist (P08-T01).
- `LAAW/tools/generate_id.py` must exist (P08-T02).

### Expected result

- `LAAW/workflow.md` references the new ID format consistently.
- No stale `{NN}` or sequential ID references remain.
- Examples use the 12-digit format.

### Automatic validations

- Run `grep -n "{NN}" LAAW/workflow.md` and verify it returns no results.
- Run `grep -n "07d\|05d" LAAW/workflow.md` and verify it finds at least 3 matches (the new format references).
- Run `grep -n "352374948815\|{minutes:07d}{random:05d}" LAAW/workflow.md` and verify it finds at least 2 matches.

### Manual validations

- Do the ID format references feel clear and consistent?
- Are the examples helpful for agents reading the workflow?
- Is there any ambiguity left about how IDs are constructed?
