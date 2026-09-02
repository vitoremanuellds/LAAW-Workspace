# Task: P07-T03 — Simplify status sequence across workflow and skills

## Context

See [p07-feedback-implementation-improvements](../phases/p07-feedback-implementation-improvements.md).

The current status sequence is too granular:
`not-planned → awaiting-plan-review → plan-approved → in-progress
→ validating → reviewing → complete`

The feedback wants it simplified to:
`not-planned → awaiting-plan-review → in-progress → reviewing →
complete`

Two changes:
1. **Remove `plan-approved`**: When a plan is approved, the status
   moves directly to `in-progress`. The approval is handled by the
   gate mechanism, not a separate status.
2. **Merge `validating` into `reviewing`**: The completion-review
   gate has two internal checks (validation, then review), but the
   status only needs one value: `reviewing`. The validation check
   happens first, then the review check — both happen while the
   status is `reviewing`.

## Implementation

### Objective

Update the status enum, all transitions, and all references across
the workflow documentation and skill files to use the simplified
five-value sequence.

### In scope

- `.ai/workflow/workflow.md` §11 (status sequence, enum, table)
- `.ai/workflow/workflow.md` §4 (lifecycle diagram)
- `.ai/workflow/reference/status-and-info.md` (lookup table, enum)
- All skill files that set or check status values

### Out of scope

- Changes to which gates exist (constitution-review, phase-review,
  task-review, task-completion-review, phase-completion-review
  remain as-is).
- Changes to the `blocked` status (it stays unchanged).
- Changes to project source code or `.ai/context/`.

### Files to modify

- `.ai/workflow/workflow.md`
- `.ai/workflow/reference/status-and-info.md`
- `.ai/workflow/skills/define-phase/SKILL.md`
- `.ai/workflow/skills/define-task/SKILL.md`
- `.ai/workflow/skills/implement-task/SKILL.md`
- `.ai/workflow/skills/validate-work/SKILL.md`
- `.ai/workflow/skills/review-work/SKILL.md`
- `.ai/workflow/skills/propagate-context/SKILL.md`
- `.ai/workflow/skills/create-constitution/SKILL.md`
- `.ai/workflow/skills/bootstrap/SKILL.md`
- `.ai/workflow/skills/build-context/SKILL.md`

### Steps

1. **Update workflow.md §11:**
   - Change the status sequence from:
     `not-planned → awaiting-plan-review → plan-approved → in-progress
     → validating → reviewing → complete`
     to:
     `not-planned → awaiting-plan-review → in-progress → reviewing →
     complete`
   - Update the Status enum list to the new five values.
   - Update the lifecycle diagram in §4 to remove `plan-approved`
     from the task lifecycle (phase lifecycle keeps `awaiting-plan-review`
     → `in-progress`).
   - Update the "Where each value lives" section in status-and-info.md.

2. **Update workflow.md §4 (lifecycle diagram):**
   - Remove `plan-approved` from the lifecycle:
     `Constitution → Constitution Review → Phase → Phase Plan Review
     → Tasks → Task Plan Review → Implement → Task Completion Review
     (validate, then review) → Context Evaluation → Task Complete`
   - The diagram already groups validation and review under
     "Task Completion Review" — this is consistent with the merge.

3. **Update reference/status-and-info.md:**
   - Change the lookup table:
     - Remove `plan-approved` row entirely.
     - Change `validating` row: merge into `reviewing` row.
       The `reviewing` row now covers both validation and review
       completion checks.
     - Update the "Which skill sets which status value" table.
   - Update the Status enum reference throughout.

4. **Update skill files — status transitions:**

   **define-phase:**
   - Remove all references to setting Status to `plan-approved`.
   - Step 8: When approval comes back, set Status to `in-progress`
     (not `plan-approved`). This is the signal that task planning
     is starting.

   **define-task:**
   - Remove all references to setting Status to `plan-approved`.
   - Phase-linked step 8: When approval comes back, set Status to
     `in-progress` (not `plan-approved`).
   - Orphan step 7: When approval comes back, set Status to
     `in-progress` (not `plan-approved`).

   **implement-task:**
   - Remove all references to `plan-approved` status check.
   - Step 3: Change the check from "It should be `plan-approved`"
     to "It should be `in-progress` — task planning has begun."
   - Update the Status enum list to the new five values.

   **validate-work:**
   - Remove the `validating` status.
   - Step 1: Instead of setting Status to `validating`, set it to
     `reviewing`. Validation is the first part of the review process.
   - Step 4 (failure): Set Status back to `in-progress` (same as now).
   - Update the Status enum reference in the skill header.

   **review-work:**
   - Keep `reviewing` status (it stays).
   - The procedure already sets Status to `reviewing` in step 1.
   - Update the Status enum reference in the skill header.
   - The two internal checks (validation, review) happen while
     Status is `reviewing` — this is the intended design.

   **propagate-context:**
   - Remove references to checking Status `reviewing` as a
     precondition (it stays the same — the task/phase should be
     `reviewing` with approved completion-review).
   - Step 3 (task): Set Status to `complete` (unchanged).
   - Step 4 (phase): Set Status to `complete` (unchanged).
   - Update the Status enum reference in the skill header.

   **create-constitution:**
   - No direct status changes needed (constitution doesn't use the
     phase/task status sequence).
   - Update any Status enum references in the skill header.

   **bootstrap:**
   - No direct status changes needed (bootstrap doesn't set status
     values).
   - Update any Status enum references in the skill header.

   **build-context:**
   - No direct status changes needed (build-context doesn't set
     task/phase status values).
   - Update any Status enum references in the skill header.

5. **Update phases.md task table:**
   - Ensure any existing phase-linked task tables don't reference
     `plan-approved` or `validating` statuses.
   - Update any phases that have tasks with old statuses to use the
     new ones (if any exist; most are already `complete` or
     `not-planned`).

6. **Verify consistency:**
   - `grep -r "plan-approved" .ai/workflow/` returns zero matches.
   - `grep -r "validating" .ai/workflow/` returns zero matches
     (except "task-validation" / "phase-validation" gate names).
   - All skills that set Status have a valid value from the new
     five-value enum.

### Automatic validations

- `grep -r "plan-approved" .ai/workflow/` returns zero matches.
- `grep -r "validating" .ai/workflow/` returns zero matches
  (except gate names like "task-validation", "phase-validation").
- The new Status enum in workflow.md §11 has exactly five values
  (not counting `blocked`).
- All skill files that set Status reference the new enum.

### Manual validations

- The removal of `plan-approved` doesn't break the "unlocking ≠
  starting" principle — the gate still blocks, the status just
  jumps directly to `in-progress`.
- Merging `validating` into `reviewing` doesn't lose information —
  the two internal checks still happen in order, they just share
  one status value.
- The status sequence is clear and easy to remember.
