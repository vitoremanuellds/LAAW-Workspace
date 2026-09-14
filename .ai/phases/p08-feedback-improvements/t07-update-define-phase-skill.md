# T07: Update define-phase skill

## Context

[Phase P08: Feedback Implementation Improvements](phase.md)

## Implementation

### Objective

Ensure the `define-phase` skill always creates the task table (with header row) as part of phase file creation — no waiting for the first task. This satisfies R05.

### In scope

- Update the `define-phase` skill file to always create the task table with its header row during phase file creation.

### Out of scope

- Changing how tasks are populated in the table (that's define-task's job).
- Updating skills that reference the task table format.

### Files to modify

- `.ai/workflow/skills/define-phase/SKILL.md` — Step 2 of the skill's procedure currently says to leave the task table empty. Update to always include the header row `| ID | Title | Purpose | Depends on | Status |`.

### Steps

1. Read the current `.ai/workflow/skills/define-phase/SKILL.md` file.
2. Locate Step 2 in the Procedure section where the phase file is written. The current text says:
   ```
   - **Tasks** — a table, initially with **no rows** (or, if
     replanning, only the rows that already existed): `| ID | Title |
     Purpose | Depends on | Status |`. Leave it empty/unchanged here —
     `define-task` populates it, not you.
   ```
3. Replace this with text that instructs the skill to always create the task table with the header row, even for new phases:
   ```
   - **Tasks** — a table with the header row `| ID | Title | Purpose |
     Depends on | Status |`. For new phases, start with an empty table
   (header only, no data rows); for replanning, keep existing rows
   unchanged. `define-task` populates the data rows, not you.
   ```
4. Verify the change is consistent with the skill's output section (which should also be updated to reflect that the task table header is always created).
5. Verify no other skill or workflow document contradicts this change.

### Automatic validations

- Grep `.ai/workflow/skills/define-phase/SKILL.md` for the task table header pattern `| ID | Title | Purpose | Depends on | Status |` and confirm it appears in the Step 2 description.
- Confirm the word "empty" no longer appears in the context of "task table" in the Step 2 description (replaced with "header only" or similar).

### Manual validations

- Does the updated instruction clearly distinguish between creating the header (define-phase's job) and populating rows (define-task's job)?
- Is the language consistent with how other skills describe table creation?
