# P03-T04 — Automate `build-context.iterate`'s workbench-file cleanup

## Context

See the owning phase file,
[`../phases/p03-workbench-context-temp-lifecycle.md`](../phases/p03-workbench-context-temp-lifecycle.md)
— this task is its Plan step 4, decided in
[ADR02](../decisions/adr02-workbench-directory.md). Depends on
[P03-T03](p03-t03-repoint-build-context-full-skill.md) (complete) —
`build-context.iterate` now reads/writes `.ai/workbench/context.temp.md`
and `.ai/workbench/build-plan.md`, which this task's deletion targets.

**Same location rule as every other task in this phase: this is
`full`'s actual source file, edited in
`LAAW/`'s own checkout and committed to
*its own* git history — never this repo's `.ai/workflow/` copy.**

Current behavior (`build-context-full/SKILL.md`, `build-context.iterate`
step 6, "queue is now empty" branch): "report completion, and ask
whether `context.temp.md` should be archived or deleted now that its
assumptions have been reconciled into real `context/` content — never
delete it unilaterally." Per ADR02, this caution existed to protect
the *permanent record* from unilateral deletion — `.ai/workbench/`
content isn't part of that record, so the same caution doesn't apply
once these two files live there (T01–T03 already moved them).

## Implementation

### Objective

Once `build-context.iterate` empties its read queue, it deletes
`.ai/workbench/context.temp.md` and `.ai/workbench/build-plan.md`
itself and commits the deletion — no "ask the human first" step.

### In scope

- `build-context.iterate` step 6's "queue is now empty" branch only.
- The `## Output` section's one-line note for `build-context.iterate`,
  so it reflects the new completion behavior.

### Out of scope

- Step 6's "queue still has rows" branch (stop-and-report-progress) —
  unchanged.
- Anything about `.assess`/`.plan`, or about `context.temp.md`'s own
  `[ASSUMPTION]`/`[QUESTION]`-line deletion rule (that's a different
  protection — individual lines inside the file while it's still in
  use — and stays exactly as-is; this task only ever deletes the whole
  file, and only after the queue is fully empty).

### Files to modify

- `LAAW/skills/build-context-full/SKILL.md`

### Files to create

None.

### Steps

1. In `build-context.iterate` step 6, replace the "If the queue is now
   empty" sentence — currently "report completion, and ask whether
   `context.temp.md` should be archived or deleted now that its
   assumptions have been reconciled into real `context/` content —
   never delete it unilaterally" — with: delete
   `.ai/workbench/context.temp.md` and `.ai/workbench/build-plan.md`
   (their assumptions are now reconciled into real `context/` content,
   and nothing under `.ai/workbench/` is part of the permanent
   record); commit that deletion (cross-reference `workflow.md` §12,
   same as every other commit instruction in this skill file); then
   report completion. (flexible: exact sentence structure, as long as
   it (a) deletes both files without asking first, (b) explicitly
   commits the deletion, (c) still reports completion to the human.)
2. In the `## Output` section's `build-context.iterate` line, add a
   clause noting that the final call (queue empty) also deletes
   `.ai/workbench/context.temp.md` and `.ai/workbench/build-plan.md`.

### Dependencies

P03-T03 (complete).

### Expected result

`build-context.iterate`'s finished-queue branch deletes both workbench
files and commits that deletion without a human-confirmation step; the
`## Output` section documents it. Committed inside
`LAAW/`'s own git history.

### Automatic validations

- `grep -n "ask whether" LAAW/skills/build-context-full/SKILL.md`
  returns nothing (the old ask-first phrasing is gone).
- `grep -n "delete" LAAW/skills/build-context-full/SKILL.md`
  shows the new step 6 language.
- `git -C LAAW log --oneline -1` shows a
  commit for this change.

### Manual validations

- Read step 6 end to end (both branches) and confirm the "queue still
  has rows" branch reads unchanged, and the "queue empty" branch reads
  as a complete, unambiguous instruction (delete → commit → report),
  not a sentence fragment.
