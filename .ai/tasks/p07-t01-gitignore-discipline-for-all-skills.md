# Task: P07-T01 — Add gitignore discipline to all skill commit steps

## Context

See [p07-feedback-implementation-improvements](../phases/p07-feedback-implementation-improvements.md).

Workflow §12 already states: "Applies only to non-gitignored files:
locality is a per-layer, per-project choice (§3), and a gitignored
layer simply has nothing to commit — not a violation of this
discipline." However, every skill's commit step explicitly asks for
commits without checking `.gitignore` first. This creates a gap: the
agent may try to commit gitignored files, or the reader may not
realize the discipline already excludes them.

Make the gitignore check **explicit** in every skill's commit step,
so the agent knows to skip gitignored files and the reader sees the
rule applied in practice.

## Implementation

### Objective

Add an explicit gitignore check to the commit step of every skill
that has a commit step. The check should:
1. Reference `.ai/workflow/workflow.md §12` (commit discipline).
2. State that gitignored files are skipped.
3. Be concise — one sentence in the commit step.

### In scope

- All skill files under `.ai/workflow/skills/` that have a commit
  step in their procedure.
- The workflow.md §12 text is already correct — no change needed there.

### Out of scope

- Changes to which files are actually gitignored.
- Changes to the `.gitignore` file itself.
- Changes to skills that don't have a commit step (none currently,
  but future skills should follow the pattern).

### Files to modify

- `.ai/workflow/skills/define-phase/SKILL.md` — step 8 commit step
- `.ai/workflow/skills/define-task/SKILL.md` — steps 8 (phase-linked)
  and 7 (orphan) commit steps
- `.ai/workflow/skills/implement-task/SKILL.md` — step 3 commit step
- `.ai/workflow/skills/validate-work/SKILL.md` — steps 6 (task) and
  5 (phase) commit steps
- `.ai/workflow/skills/review-work/SKILL.md` — step 9 commit step
- `.ai/workflow/skills/propagate-context/SKILL.md` — steps 4 (task)
  and 5 (phase) commit steps
- `.ai/workflow/skills/create-constitution/SKILL.md` — step 8 commit
  step
- `.ai/workflow/skills/bootstrap/SKILL.md` — step 4 commit step
- `.ai/workflow/skills/build-context/SKILL.md` — steps 4 (assess),
  5 (plan), 6/7 (iterate) commit steps

### Steps

1. Read the current `.ai/workflow/skills/define-phase/SKILL.md`
   step 8 commit text.
2. Add a sentence before "Stop for phase plan review" that says:
   "Commit the draft, **excluding any gitignored files** (see
   [.ai/workflow/workflow.md §12](.ai/workflow/workflow.md#12-commit-discipline)
   — gitignored layers simply have nothing to commit)."
3. Repeat the same pattern for every other skill's commit step,
   adapting the wording slightly to fit each skill's context but
   keeping the core phrase "excluding any gitignored files" and the
   §12 reference consistent.
4. Verify no skill's commit step remains without the gitignore note.

### Automatic validations

- `grep -r "gitignored" .ai/workflow/skills/` returns one match per
  skill file (9 skills total: define-phase, define-task,
  implement-task, validate-work, review-work, propagate-context,
  create-constitution, bootstrap, build-context).
- `git diff` shows no changes outside `.ai/workflow/skills/`.

### Manual validations

- Each skill's commit step reads naturally — the gitignore note
  doesn't feel tacked on.
- The wording is consistent across all skills (same core phrase,
  same §12 reference).
