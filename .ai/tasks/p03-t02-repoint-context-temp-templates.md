# P03-T02 — Repoint `context-temp-template.md`/`context-build-plan-template.md` to `.ai/workbench/`

## Context

See the owning phase file,
[`../phases/p03-workbench-context-temp-lifecycle.md`](../phases/p03-workbench-context-temp-lifecycle.md)
— this task is its Plan step 2.

**Same location rule as every other task in this phase: these are
`full`'s actual source files, edited in
`LAAW/`'s own checkout and committed to
*its own* git history — never this repo's `.ai/workflow/` copy.** See
P03-T01's Context for why this matters.

Relevant existing files (read in full before editing):
- `LAAW/templates/context-temp-template.md`
  — states its own copy target in a sentence near the top: "Copy
  target: `.ai/context/context.temp.md`."
- `LAAW/templates/context-build-plan-template.md`
  — same pattern: "Copy target: `.ai/context/build-plan.md`."

Neither template's own content changes otherwise — this task only
changes where each says it gets copied *to*. `build-context-full/SKILL.md`
itself (which does the actual copying) is P03-T03, not this task —
T02 exists so the templates' own stated destination is already correct
before T03 updates the skill that reads them, per this phase's
Depends-on ordering (T03 depends on T01 and T02).

## Implementation

### Objective

Both templates declare `.ai/workbench/` as their copy target instead
of `.ai/context/`, so P03-T03 (updating the skill that actually copies
them) has a consistent destination to point at.

### In scope

- The one "Copy target: ..." sentence in each of the two template
  files.

### Out of scope

- `build-context-full/SKILL.md` itself — P03-T03.
- `context-temp-template.md`'s reference to `.ai/context/*.md` as
  where *reconciled* content eventually lands (line 11: "`build-context.iterate`
  reconciles this into real `.ai/context/*.md` content") — that's a
  different, correct statement about the permanent destination of
  reconciled context, not this temp file's own copy target. Leave it
  untouched.

### Files to modify

- `LAAW/templates/context-temp-template.md`
- `LAAW/templates/context-build-plan-template.md`

### Files to create

None.

### Steps

1. In `context-temp-template.md`, change "Copy target:
   `.ai/context/context.temp.md`." to "Copy target:
   `.ai/workbench/context.temp.md`." — that single sentence only;
   leave the rest of the file (including its `.ai/context/*.md`
   reference further down) untouched.
2. In `context-build-plan-template.md`, change "Copy target:
   `.ai/context/build-plan.md`." to "Copy target:
   `.ai/workbench/build-plan.md`." — same, single-sentence change.

### Dependencies

None — independent of every other task in this phase (T03 depends on
this one, not the reverse).

### Expected result

Both templates state `.ai/workbench/...` as their copy target;
nothing else in either file changes. Committed inside
`LAAW/`'s own git history.

### Automatic validations

- `grep -n "Copy target" LAAW/templates/context-temp-template.md`
  shows `.ai/workbench/context.temp.md`.
- `grep -n "Copy target" LAAW/templates/context-build-plan-template.md`
  shows `.ai/workbench/build-plan.md`.
- `grep -n "\.ai/context/context\.temp\.md\|\.ai/context/build-plan\.md" LAAW/templates/`
  returns nothing.
- `git -C LAAW log --oneline -1` shows a
  commit for this change.

### Manual validations

- Diff each template against its pre-change version and confirm only
  the one "Copy target" line changed — no incidental edits to the
  `[ASSUMPTION]`/`[QUESTION]` example content or the `batch_size`
  comment.
