# P03-T01 — Document `.ai/workbench/` in workflow.md and directory-and-links.md

## Context

See the owning phase file,
[`../phases/p03-workbench-context-temp-lifecycle.md`](../phases/p03-workbench-context-temp-lifecycle.md),
for the full rationale — not repeated here. The concrete decision this
task documents was already made in
[ADR02](../decisions/adr02-workbench-directory.md): `.ai/workbench/`
is freeform, disposable, git-tracked, and outside the permanent-record
hierarchy — no skill treats its content as an input dependency.

Relevant existing files:
- `.ai/workflow/workflow.md` §3 (Directory structure) — the code block
  listing every `.ai/` subdirectory with a one-line role each, plus a
  short prose paragraph right after it.
- `.ai/workflow/reference/directory-and-links.md` — detail/reasoning
  file for §3's rules; each existing section explains the "why" behind
  one directory/link convention.

## Implementation

### Objective

Make `.ai/workbench/` a real, documented directory: listed in
`workflow.md` §3 alongside every other `.ai/` subdirectory, explained
in `reference/directory-and-links.md`, and instantiated on disk (via a
short `README.md`, since git doesn't track empty directories) — so
later tasks in this phase have a real, documented location to point
`build-context-full` at.

### In scope

- One new line in `workflow.md` §3's directory-structure code block.
- One short addition to §3's existing prose, cross-linking
  `reference/directory-and-links.md` for detail.
- One new section in `reference/directory-and-links.md`.
- `.ai/workbench/README.md`, short, mirroring `context.md`'s
  entry-point style.

### Out of scope

- Changing `build-context-full`, its templates, or anything about
  `context.temp.md`/`build-plan.md` — that's P03-T02/T03/T04.
- Any other content inside `.ai/workbench/` beyond the `README.md` —
  this task only establishes the directory and its convention.

### Files to modify

- `.ai/workflow/workflow.md` — add `.ai/workbench/` to §3's directory
  block; add one sentence to §3's prose noting it's the one exception
  to "part of the permanent record."
- `.ai/workflow/reference/directory-and-links.md` — add a new section
  explaining why `.ai/workbench/` exists and isn't read as a
  dependency.

### Files to create

- `.ai/workbench/README.md` — short freeform-convention explainer;
  also what makes the otherwise-empty directory exist in git.

### Steps

1. In `.ai/workflow/workflow.md` §3's directory-structure code block,
   add a line for `.ai/workbench/` after the existing `.ai/tasks/`
   line, matching the block's existing column-alignment style:
   `.ai/workbench/     freeform scratch — planning notes, Q&A, prompt
   drafts; disposable, not part of the permanent record` (flexible:
   exact wording of the description, as long as "freeform" and
   "disposable"/"not part of the permanent record" both appear).
2. Immediately after that code block, in §3's existing prose (the
   paragraph starting "Flat by design..."), add one sentence: `.ai/workbench/`
   is the one exception — nothing in it is part of the permanent
   record, and no skill reads it as an input dependency (see
   `reference/directory-and-links.md`). (flexible: exact phrasing, as
   long as it cross-links `reference/directory-and-links.md`.)
3. In `.ai/workflow/reference/directory-and-links.md`, add a new
   section (heading level `##`, e.g. `## Why .ai/workbench/ isn't part
   of the permanent record`) after the existing sections. Content:
   freeform/disposable/git-tracked (not gitignored), reference
   [ADR02](../../decisions/adr02-workbench-directory.md) for the
   decision, and state explicitly that "read only what the current
   task needs" (`workflow.md` §1) never includes `.ai/workbench/`
   content unless a human explicitly points an agent at a specific
   file in it.
4. Create `.ai/workbench/README.md`: one or two sentences — this
   directory is freeform scratch space for the human and agent
   (planning notes, Q&A, prompt drafts, anything disposable); nothing
   here is part of the permanent record; see
   [ADR02](../decisions/adr02-workbench-directory.md).

### Dependencies

None — first task in this phase.

### Expected result

`.ai/workbench/` exists on disk (via `README.md`), is listed in
`workflow.md` §3's directory block, has a short cross-linking note in
§3's prose, and has its own explanatory section in
`reference/directory-and-links.md`.

### Automatic validations

- `test -f .ai/workbench/README.md`
- `grep -n "workbench" .ai/workflow/workflow.md` — at least one match
  inside §3's code block, at least one in its prose.
- `grep -n "workbench" .ai/workflow/reference/directory-and-links.md`
  — at least one match, inside its own new section.

### Manual validations

- Read `workflow.md` §3 and the new `directory-and-links.md` section
  together and confirm the tone/placement is consistent with the rest
  of both files — reads as a real convention, not a note tacked on
  after the fact.
