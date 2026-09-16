# Rewrite core skills

**ID:** t037-1693-17315       **Status:** done

## Description

Rewrite LAAW's four core operation skills (`define-task`, `implement-task`,
`validate-work`, `review-work`) to the two-gate, no-phase, single-context
model, and delete `skills/define-phase/`. Each skill is re-anchored to the
new lifecycle: `task-review` (plan approval) and `task-completion-review`
(validate + judgment).

## TL;DR

Replace the phase-linked/orphan dual-path model with a single task model;
install the new task file layout (Context Before/After, In scope, Out of
scope, Steps, Validations, optional Subtasks table); update all status
enums to the four-value list; drop ADR-writing from `implement-task`
(decisions are context rows now); drop phase validation from
`validate-work`; drop phase review from `review-work`; delete
`skills/define-phase/`.

## Context

### Before

- `LAAW/skills/define-task/SKILL.md` — 17.5 KB; dual path (phase-linked
  + orphan); phase-linked IDs `P{NN}-t{NN}-{name}`; orphan IDs
  `t{NN}-{name}`; status enum `not-planned`/`awaiting-plan-review`/
  `in-progress`/`reviewing`/`complete`/`blocked`; writes to
  `.ai/phases/` and `.ai/tasks/`; ADR-writing via `implement-task`;
  phase-file Tasks table as the status home for phase-linked tasks.
- `LAAW/skills/implement-task/SKILL.md` — 7 KB; dual path; writes ADRs
  into `.ai/decisions/`; reads phase file or orphan task; six-value
  status enum.
- `LAAW/skills/validate-work/SKILL.md` — 4.7 KB; task + phase validation
  procedures; six-value status enum.
- `LAAW/skills/review-work/SKILL.md` — 5.6 KB; task + phase review;
  reads ADRs from `.ai/decisions/`; six-value status enum.
- `LAAW/skills/define-phase/SKILL.md` — to be deleted entirely.
- Parent task [t002-7178-75813](../task.md)
  step 3.
- Already-done subtasks:
  [t037-1693-02727](../task.md) (new id system),
  [t037-1693-16386](../task.md) (workflow.md
  rewrite).
- Reference files are still the old versions — this task does not update
  them (that is step 6 of the parent task).

### After

- `define-task` — single task model; new task file layout matching the
  revamp design; recursive folder rule (`tasks/t{ID}-{name}.md` leaf,
  `tasks/t{ID}-{name}/` folder with parent + subtasks); subtask table
  columns id/name/description/depends-on/status; no phase link, no
  orphan concept; status enum `not-started`/`planned`/`in-progress`/
  `done` (+`blocked`); writes to `.ai/tasks/` only; updates
  `tasks.md` or parent task file's subtask table.
- `implement-task` — single task model; no ADR-writing (decisions are
  context rows, written by `create-constitution` or `implement-task` at
  the moment of decision — but the ADR file-creation pattern is gone);
  deviations recorded inline in the task file; status enum updated;
  context propagation flagged for `propagate-context`.
- `validate-work` — task-only validation (no phase validation); status
  enum updated; no phase-file routing.
- `review-work` — task-only review (no phase review); status enum
  updated; reads context rows from `context/` instead of ADRs from
  `.ai/decisions/`; no phase-file routing.
- `skills/define-phase/` — deleted.

## In scope

- `LAAW/skills/define-task/SKILL.md` — full rewrite.
- `LAAW/skills/implement-task/SKILL.md` — full rewrite.
- `LAAW/skills/validate-work/SKILL.md` — full rewrite.
- `LAAW/skills/review-work/SKILL.md` — full rewrite.
- `LAAW/skills/define-phase/` — delete the entire directory.

## Out of scope

- Rewriting `create-constitution`, `build-context`, `propagate-context`
  — those are context skills (step 4 of the parent task).
- Adding the router skill — step 5 of the parent task.
- Updating reference/ files — step 6 of the parent task.
- Updating templates/ — step 7 of the parent task.
- README rewrite — step 8 of the parent task.
- Sync scripts — step 9 of the parent task.
- Any change to `tools/` or `workflow.md` itself.

## Files to modify

- `LAAW/skills/define-task/SKILL.md` — entire file rewritten.
- `LAAW/skills/implement-task/SKILL.md` — entire file rewritten.
- `LAAW/skills/validate-work/SKILL.md` — entire file rewritten.
- `LAAW/skills/review-work/SKILL.md` — entire file rewritten.

## Files to create

None.

## Files to delete

- `LAAW/skills/define-phase/SKILL.md` and `LAAW/skills/define-phase/`
  directory.

## Steps

### Step 1 — Rewrite `define-task`

Rewrite `LAAW/skills/define-task/SKILL.md` for the single-task model:

1. **Frontmatter:** Update `name` and `description` — remove all phase
   and orphan references; one-sentence description: "Break a phase
   file's Plan section into individual tasks (tasks/t{ID}-{name}.md),
   or draft a standalone task with no phase parent
   (tasks/t{ID}-{name}.md, indexed in tasks/tasks.md)."
2. **When to use:** Single path only — task planning. No phase-linked
   vs. orphan distinction. Always writes to `.ai/tasks/`.
3. **Inputs:** Only the task's description, `.ai/tasks/tasks.md` (if it
   exists), `.ai/context/` files, and project source files the task
   touches. No phase file.
4. **Procedure:** Replace the dual-path procedure with a single path:
   - Step 1: If `.ai/tasks/tasks.md` doesn't exist, scaffold it per
     [reference/scaffold-on-first-use.md](reference/scaffold-on-first-use.md)
     (empty table with columns id/name/description/depends-on/status).
     If `.ai/tasks/` itself doesn't exist, create it.
   - Step 2: Mint the next id using `tools/generate-id.py --prefix t`
     (the new id format from t037-1693-02727).
   - Step 3: If the task has subtasks, create the folder
     `tasks/t{ID}-{name}/` with the parent file
     `t{ID}-{name}.md` inside it. If it's a leaf task, create the
     single file `tasks/t{ID}-{name}.md`. This is the **recursive
     folder rule** — every task follows the same shape.
   - Step 4: Write the task file body per the **new layout** (see
     Task file body below).
   - Step 5: Note dependencies on other tasks explicitly if they exist.
   - Step 6: Update `tasks.md` (or the parent task file's Subtasks
     table) with the new row — Status `planned` (the new status, not
     `awaiting-plan-review`).
   - Step 7: Ask the user whether to draft the next task now, or stop.
   - Step 8: Commit everything; stop for `task-review` gate. When
     approval comes back, set Status to `in-progress`.
5. **Task file body** — the new layout from the revamp design:
   ```markdown
   # <name>
   **ID:** t{ID}       **Status:** in-progress

   ## Description
   <what this task is and why — the intent, one short paragraph>

   ## TL;DR
   - <topic — the fastest possible orientation, as bullets, not prose>
   - <topic>

   ## Context
   ### Before
   <the knowledge/situation the agent needs to START this task>
   ### After
   <the context/understanding this task PRODUCES once implemented>

   ## In scope
   - <the changes this task makes>

   ## Out of scope
   - <what is explicitly NOT touched>

   ## Steps
   1. <ordered step>
   2. <ordered step>
      - <pseudocode here where it helps>

   ## Validations
   - <how to check done>

   ## Subtasks            ← optional; omit for a leaf task
   | id | name | description | depends on | status |
   |----|------|-------------|------------|--------|
   ```
   - **Status is NOT in the task file** — it lives exclusively in the
     index (`tasks.md` or parent's Subtasks table). The `**Status:**
     in-progress` in the template is for display; the real status
     lives in the table.
   - **No phase link** — the Before section states relevant files and
     constraints directly, self-contained.
   - **Subtasks table** — optional; only present if the task has
     subtasks. Columns: id, name, description, depends on, status.
     Rows are id-ascending; new subtasks are appended at the end.
   - **Deviation recording** — same inline `## Deviations` subsection
     pattern as before (added later by whichever operation raises it).
6. **Output:** One task file per task drafted this invocation. Update
   `tasks.md` (scaffolded first if needed).

### Step 2 — Rewrite `implement-task`

Rewrite `LAAW/skills/implement-task/SKILL.md`:

1. **Frontmatter:** Update `description` — remove phase/orphan; single
   task model.
2. **What to read:** Remove phase-file reading. Read `workflow.md`,
   `.ai/info.md`, the task file (leaf or parent), only the files the
   task's Context section lists, and explore the codebase with
   `tree`/`find`/`grep`/`ls`.
3. **Procedure:**
   - Step 1: Read the task file's Steps section.
   - Step 2: Read the Context section and only the referenced files.
   - Step 3: Check the task's Status in `tasks.md` (or parent's
     Subtasks table). It should be `in-progress`. If `planned`,
     `task-review` hasn't passed — stop. Set Status to `in-progress`.
   - Step 4: Follow the task's Steps in order. Adjust freely only
     where the task file explicitly marked a detail flexible. Everything
     else that doesn't match gets raised as a deviation.
   - Step 5: If the plan turns out wrong — stop and raise a deviation.
   - Step 6: **Decisions are context rows, not ADRs.** If an
     architectural decision is made, record it as a note for
     `propagate-context` to promote later, or write it directly as a
     context row (`c-{ID}-{name}.md`) if the operation contract
     assigns it to this skill. No `.ai/decisions/` directory, no
     `adr{NN}` files.
4. **Finishing:**
   - Set Status to `done` (not `reviewing` — the new enum has no
     `reviewing` state; `done` = implementation complete +
     `task-completion-review` passed, but `implement-task` sets it to
     `done` to signal ready for validation).
   - Commit: modified/created project files, updated Status row.
   - Stop for `task-completion-review` → `validate-work`.
5. **Status enum:** `not-started` · `planned` · `in-progress` · `done`
   (+`blocked`). No `not-planned`, `awaiting-plan-review`, `reviewing`,
   or `complete`.

### Step 3 — Rewrite `validate-work`

Rewrite `LAAW/skills/validate-work/SKILL.md`:

1. **Frontmatter:** Update `description` — remove phase; task-only
   validation.
2. **When to use:** After implementation, before review — at task level
   only. No phase-level validation.
3. **Procedure — task validation only:**
   - Step 1: Set the task's Status to `done` (replacing `reviewing` —
     the new status for "ready for review").
   - Step 2: Read the task file's Steps section (requirements + plan).
   - Step 3: Execute the validation instructions.
   - Step 4: Report pass/fail. On failure, set Status back to
     `in-progress` and return the task to the implementation loop.
   - Step 5: Record any accepted exceptions explicitly.
   - Step 6: Commit the updated Status row; the message should say
     pass or fail and for which task.
4. **Remove:** All phase validation procedure, phase-file routing,
   `phase-validation` gate references.
5. **Status enum:** `not-started` · `planned` · `in-progress` · `done`
   (+`blocked`).

### Step 4 — Rewrite `review-work`

Rewrite `LAAW/skills/review-work/SKILL.md`:

1. **Frontmatter:** Update `description` — remove phase; task-only
   review.
2. **When to use:** After validation passes, before a task is marked
   `done` — at task level only.
3. **Procedure:**
   - Step 1: Read `.ai/info.md` fresh; set Status to `done` (replacing
     `reviewing` — the review is part of the `done` transition).
   - Step 2: Confirm the change matches its stated scope.
   - Step 3: Check for unnecessary complexity.
   - Step 4: Check consistency with existing architecture and relevant
     **context rows** from `context/` (not ADRs from `.ai/decisions/`).
   - Step 5: Check validation coverage.
   - Step 6: Check that context files still accurately describe the
     result.
   - Step 7: Check for undocumented decisions — flag back to whichever
     operation produced it.
   - Step 8: Report findings — approve or changes requested.
   - Step 9: Commit the Status change.
   - Step 10: Stop for `task-completion-review`. When approval comes
     back, report and explicitly ask whether to run `propagate-context`
     now.
4. **Remove:** All phase review procedure, phase-file routing,
   `phase-completion-review` gate references, ADR-reading from
   `.ai/decisions/`.
5. **Status enum:** `not-started` · `planned` · `in-progress` · `done`
   (+`blocked`).

### Step 5 — Delete `skills/define-phase/`

Delete the entire `LAAW/skills/define-phase/` directory and its
`SKILL.md` file. No phases exist in the new model.

## Dependencies

- `t037-1693-16386` (rewrite-workflow-md) — the workflow.md must be
  rewritten first so skills can reference the correct gate names,
  status values, and directory structure.

## Expected result

A clean set of four core skills:
- `define-task` — single task model, new layout, recursive folder rule.
- `implement-task` — single task model, no ADR-writing, updated status.
- `validate-work` — task-only validation, updated status.
- `review-work` — task-only review, context-row reading, updated status.
- `skills/define-phase/` — gone.

No references to phases, orphan tasks, ADRs, `.ai/decisions/`, or the
old status values remain in these four files.

## Automatic validations

- `grep -r 'phase' LAAW/skills/define-task/SKILL.md` → **no hits**
  (except the word "phase" in a cross-reference to the parent task's
  id, which is acceptable if it's a link to the parent task itself).
- `grep -r 'orphan' LAAW/skills/define-task/SKILL.md` → **no hits**.
- `grep -r 'awaiting-plan-review\|not-planned\|reviewing\b\|complete\b' LAAW/skills/define-task/SKILL.md` → **zero matches** for these old status values as status strings.
- `grep -r 'not-started\|planned\|in-progress\|done' LAAW/skills/define-task/SKILL.md` → **finds the new status values** (at least one occurrence of each).
- `grep -r 'phase' LAAW/skills/implement-task/SKILL.md` → **no hits**
  (except in cross-reference prose like "see parent task").
- `grep -r 'ADR\|adr\|decisions/' LAAW/skills/implement-task/SKILL.md` → **no hits** (decisions are context rows now, not ADR files).
- `grep -r 'phase' LAAW/skills/validate-work/SKILL.md` → **no hits**
  (except in cross-reference prose).
- `grep -r 'phase' LAAW/skills/review-work/SKILL.md` → **no hits**
  (except in cross-reference prose).
- `grep -r 'decisions/' LAAW/skills/review-work/SKILL.md` → **no hits** (reads context rows from `context/`, not ADRs).
- `ls LAAW/skills/define-phase/` → **directory does not exist**.
- `grep -r 'define-phase' LAAW/skills/` → **no hits** (no skill references the deleted skill).
- `grep -c 'task-review' LAAW/skills/define-task/SKILL.md` → **≥ 1** (the gate name should appear in the procedure).
- `grep -c 'task-completion-review' LAAW/skills/implement-task/SKILL.md` → **≥ 1**.

## Manual validations

- A fresh agent reading `workflow.md` + `context.md` of a freshly
  synced scratch project can understand the two-gate lifecycle from
  these four skills alone, without reading reference files.
- The recursive folder rule is clearly stated in `define-task` and
  consistent with `workflow.md` §3.
- The status enum is the same across all four skills and matches
  `workflow.md` §11.
