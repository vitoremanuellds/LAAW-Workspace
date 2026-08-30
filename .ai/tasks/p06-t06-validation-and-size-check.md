# P06-T06 — Cross-file validation and size check

## Context

See [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md).
Last task in the phase — depends on every other P06 task being done.

## Implementation

### Objective

Confirm the redesigned workflow is internally consistent and hasn't
grown heavier than before, then close out P06's bookkeeping in this
outer meta-repo.

### In scope

- Run every Automatic validation listed in P06-T01 through T05 again,
  together, against the final state (some may have been satisfied
  mid-way but regressed by a later task).
- Word-count comparison: `wc -w workflow.md` before vs. after (use
  `git -C LAAW show <pre-P06-commit>:workflow.md | wc -w`
  for the "before" baseline) — confirm it didn't grow to cover all the
  new flexibility prose; per-operation reading load (a skill file +
  workflow.md) should be flat or lighter than before for any given
  layer combination.
- Full-repo grep sweep across `LAAW/` for
  `roadmap.md`, `-full` skill-name suffixes, and any task-file `Source`
  field — zero hits expected anywhere, not just the files earlier
  tasks touched directly.
- Manual walkthroughs (P06's own Manual validations): tasks-only;
  constitution+tasks, no phases; full stack with one orphan task
  alongside phase-linked ones.
- Update this outer meta-repo's `.ai/phases/p06-*.md` task table
  (mark T01–T06 complete) and `.ai/constitution/roadmap.md`'s P06 row
  Status to `complete`; clear `info.md`'s `Active phase` back to `—`
  (this repo's own bookkeeping, per its still-current pre-P06 schema —
  not the redesigned one).

### Out of scope

- Any further content change to LAAW itself — if this step finds a
  real gap, that's a deviation on the specific earlier task, not new
  scope added here.

### Files to modify

- `.ai/phases/p06-redesign-laaw-modular-workflow.md` (this repo)
- `.ai/constitution/roadmap.md` (this repo)
- `.ai/info.md` (this repo)

### Files to create

None.

### Steps

1. Re-run every earlier task's Automatic validations against the final
   tree state.
2. Run the full-repo grep sweep described above.
3. Run the word-count comparison; record the before/after numbers in
   this task's own file (append a short `### Result` note) so the
   comparison is visible without re-deriving it.
4. Walk each of the three manual scenarios by hand.
5. Update this outer repo's phase file task table, roadmap row, and
   `info.md`'s Active phase — commit in *this* repo (not LAAW's), since
   this is this repo's own bookkeeping.

### Dependencies

P06-T01, P06-T02, P06-T03, P06-T04, P06-T05.

### Expected result

P06 fully implemented and internally consistent; this outer repo's own
phase/roadmap/info bookkeeping reflects completion.

### Automatic validations

- All greps above return zero unexpected hits.
- Word count is flat or lower than the pre-P06 baseline.

### Manual validations

- All three configuration walkthroughs complete without reaching for a
  layer that isn't present in that configuration.
