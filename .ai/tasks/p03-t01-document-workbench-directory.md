# P03-T01 — Document `.ai/workbench/` in workflow.md and directory-and-links.md

## Context

See the owning phase file,
[`../phases/p03-workbench-context-temp-lifecycle.md`](../phases/p03-workbench-context-temp-lifecycle.md),
for the full rationale — not repeated here. The concrete decision this
task documents was already made in
[ADR02](../decisions/adr02-workbench-directory.md): `.ai/workbench/`
is freeform, disposable, git-tracked, and outside the permanent-record
hierarchy — no skill treats its content as an input dependency.

**These are `full`'s actual source files, edited in
`LAAW/`'s own checkout and committed to
*its own* git history — not this repo's `.ai/workflow/` copy.** (This
task was first implemented against `.ai/workflow/` by mistake, then
corrected — see `mission.md`'s 2026-08-29 note.)

Relevant existing files:
- `LAAW/workflow.md` §3 (Directory
  structure) — the code block listing every `.ai/` subdirectory with a
  one-line role each, plus a short prose paragraph right after it.
- `LAAW/reference/directory-and-links.md` —
  detail/reasoning file for §3's rules; each existing section explains
  the "why" behind one directory/link convention.

## Implementation

### Objective

Make `.ai/workbench/` a real, documented directory in `full`'s own
source: listed in `workflow.md` §3 alongside every other `.ai/`
subdirectory, and explained in `reference/directory-and-links.md`.

### In scope

- One new line in `workflow.md` §3's directory-structure code block.
- One short addition to §3's existing prose, cross-linking
  `reference/directory-and-links.md` for detail.
- One new section in `reference/directory-and-links.md`.

### Out of scope

- Changing `build-context-full`, its templates, or anything about
  `context.temp.md`/`build-plan.md` — that's P03-T02/T03/T04.
- Instantiating `.ai/workbench/` as an actual directory anywhere — `full`'s
  own repo has no `.ai/` of its own to instantiate it in; a real
  consuming project's `.ai/workbench/` comes into existence the first
  time something is actually written there (P03-T03/T04, or an ad hoc
  human/agent file), not from this documentation-only task.

### Files to modify

- `LAAW/workflow.md` — add `.ai/workbench/`
  to §3's directory block; add one sentence to §3's prose noting it's
  the one exception to "part of the permanent record."
- `LAAW/reference/directory-and-links.md` —
  add a new section explaining why `.ai/workbench/` exists and isn't
  read as a dependency.

### Files to create

None.

### Steps

1. In `LAAW/workflow.md` §3's
   directory-structure code block, add a line for `.ai/workbench/`
   after the existing `.ai/tasks/` line, matching the block's existing
   column-alignment style: `.ai/workbench/     freeform scratch —
   planning notes, Q&A, prompt drafts; disposable, not part of the
   permanent record` (flexible: exact wording of the description, as
   long as "freeform" and "disposable"/"not part of the permanent
   record" both appear).
2. Immediately after that code block, in §3's existing prose (the
   paragraph starting "Flat by design..."), add one sentence:
   `.ai/workbench/` is the one exception — nothing in it is part of
   the permanent record, and no skill reads it as an input dependency
   (see `reference/directory-and-links.md`). (flexible: exact
   phrasing, as long as it cross-links `reference/directory-and-links.md`.)
3. In `LAAW/reference/directory-and-links.md`,
   add a new section (heading level `##`, e.g. `## Why .ai/workbench/
   isn't part of the permanent record`) after the existing sections.
   Content: freeform/disposable/git-tracked (not gitignored), and
   state explicitly that "read only what the current task needs"
   (`workflow.md` §1) never includes `.ai/workbench/` content unless a
   human explicitly points an agent at a specific file in it. Do not
   link to this repo's ADR02 from here — `full` is its own repo,
   distributed independently; that ADR isn't reachable from a
   consuming project.

### Dependencies

None — first task in this phase.

### Expected result

`.ai/workbench/` is listed in `LAAW/workflow.md`
§3's directory block, has a short cross-linking note in §3's prose,
and has its own explanatory section in
`LAAW/reference/directory-and-links.md`.
Committed inside `LAAW/`'s own git history.

### Automatic validations

- `grep -n "workbench" LAAW/workflow.md` —
  at least one match inside §3's code block, at least one in its
  prose.
- `grep -n "workbench" LAAW/reference/directory-and-links.md`
  — at least one match, inside its own new section.
- `git -C LAAW log --oneline -1` shows a
  commit for this change, separate from this outer repo's own commits.

### Manual validations

- Read `workflow.md` §3 and the new `directory-and-links.md` section
  together and confirm the tone/placement is consistent with the rest
  of both files — reads as a real convention, not a note tacked on
  after the fact.
