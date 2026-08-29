# P03-T03 — Update `build-context-full/SKILL.md` to read/write `.ai/workbench/`

## Context

See the owning phase file,
[`../phases/p03-workbench-context-temp-lifecycle.md`](../phases/p03-workbench-context-temp-lifecycle.md)
— this task is its Plan step 3. Depends on
[P03-T01](p03-t01-document-workbench-directory.md) (the directory is
documented) and [P03-T02](p03-t02-repoint-context-temp-templates.md)
(the templates already declare `.ai/workbench/` as their own copy
target) — both complete.

**Same location rule as every other task in this phase: this is
`full`'s actual source file, edited in
`Full-Local-Model-Agent-Workflow/`'s own checkout and committed to
*its own* git history — never this repo's `.ai/workflow/` copy.**

Read `Full-Local-Model-Agent-Workflow/skills/build-context-full/SKILL.md`
in full before editing — every `.ai/context/context.temp.md` and
`.ai/context/build-plan.md` reference across its three sub-operations
(`.assess`, `.plan`, `.iterate`) needs to become `.ai/workbench/...`.
Its references to `.ai/context/*.md` (the *real*, reconciled context
files `.iterate` writes) are a different thing and stay unchanged —
only the two temp files' own path moves.

## Implementation

### Objective

`build-context-full` reads and writes `context.temp.md`/`build-plan.md`
under `.ai/workbench/` throughout `.assess`, `.plan`, and `.iterate`,
matching what the templates (T02) and the directory documentation
(T01) already say.

### In scope

- Every literal `.ai/context/context.temp.md` and
  `.ai/context/build-plan.md` path in `build-context-full/SKILL.md`
  (`.assess` steps 2–3, `.plan`'s precondition and steps 1 and 4–5,
  `.iterate`'s precondition, and the `## Output` section).

### Out of scope

- `.iterate`'s "queue empty" step (its current "ask whether to
  archive or delete" behavior) — that's P03-T04, a behavior change,
  not a path change. Leave its wording alone in this task even though
  it's adjacent.
- Any `.ai/context/*.md` reference that means the *real* reconciled
  context output (`.iterate` step 3, and the `## Output` section's
  "updated `.ai/context/*.md` files" line) — those are correct as-is
  and must not change.
- The two template files themselves — already done, P03-T02.

### Files to modify

- `Full-Local-Model-Agent-Workflow/skills/build-context-full/SKILL.md`

### Files to create

None.

### Steps

1. In `build-context.assess` step 2, change `.ai/context/context.temp.md`
   to `.ai/workbench/context.temp.md` (the file `.assess` writes).
2. In `build-context.assess` step 3 (commit instruction), change
   "stage `.ai/context/context.temp.md`" to "stage
   `.ai/workbench/context.temp.md`".
3. In `build-context.plan`'s precondition sentence, change
   `.ai/context/context.temp.md` to `.ai/workbench/context.temp.md`.
4. In `build-context.plan` step 1, change "Read
   `.ai/context/context.temp.md` in full" to "Read
   `.ai/workbench/context.temp.md` in full".
5. In `build-context.plan` step 4, change the write target
   `.ai/context/build-plan.md` to `.ai/workbench/build-plan.md`.
6. In `build-context.plan` step 5 (commit instruction), change "stage
   `.ai/context/build-plan.md`" to "stage `.ai/workbench/build-plan.md`".
7. In `build-context.iterate`'s precondition sentence, change
   `.ai/context/build-plan.md` to `.ai/workbench/build-plan.md`.
8. In the `## Output` section, change the `build-context.assess` and
   `build-context.plan` lines' paths (`.ai/context/context.temp.md`,
   `.ai/context/build-plan.md`) to `.ai/workbench/...`. Leave the
   `build-context.iterate` line ("updated `.ai/context/*.md` files and
   `context.md`'s table, plus `build-plan.md`'s Status column")
   unchanged — it already correctly refers to real context output plus
   the (now-workbench-rooted, but path-unqualified there) build plan.

### Dependencies

P03-T01, P03-T02 (both complete).

### Expected result

No occurrence of `.ai/context/context.temp.md` or
`.ai/context/build-plan.md` remains anywhere in
`build-context-full/SKILL.md`; every reference to either file now
reads `.ai/workbench/...`. Every reference to genuine reconciled
`.ai/context/*.md` content is untouched. Committed inside
`Full-Local-Model-Agent-Workflow/`'s own git history.

### Automatic validations

- `grep -n "\.ai/context/context\.temp\.md\|\.ai/context/build-plan\.md" Full-Local-Model-Agent-Workflow/skills/build-context-full/SKILL.md`
  returns nothing.
- `grep -cn "\.ai/workbench/context\.temp\.md\|\.ai/workbench/build-plan\.md" Full-Local-Model-Agent-Workflow/skills/build-context-full/SKILL.md`
  returns at least 6 (one per occurrence listed in Steps 1–8, some
  steps touch the same filename more than once across sub-operations).
- `grep -n "\.ai/context/\*\.md" Full-Local-Model-Agent-Workflow/skills/build-context-full/SKILL.md`
  still returns its existing matches (unchanged) — confirms the
  real-context references weren't accidentally touched.
- `git -C Full-Local-Model-Agent-Workflow log --oneline -1` shows a
  commit for this change.

### Manual validations

- Read all three sub-operations end to end after the edit and confirm
  each still reads coherently as one flow (`.assess` writes to
  `.ai/workbench/`, `.plan` reads/writes there, `.iterate` reads its
  precondition from there) — not just correct greps in isolation.
