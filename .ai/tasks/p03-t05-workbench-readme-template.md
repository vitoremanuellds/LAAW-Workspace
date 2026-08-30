# P03-T05 — Add `workbench-readme-template.md`, wire into `create-constitution-full`'s bootstrap

## Context

See the owning phase file,
[`../phases/p03-workbench-context-temp-lifecycle.md`](../phases/p03-workbench-context-temp-lifecycle.md)
— this task is its Plan step 5, appended 2026-08-29 at the user's
suggestion (not present in P03's original draft).

**Same location rule as every other task in this phase: these are
`full`'s actual source files, edited in
`LAAW/`'s own checkout and committed to
*its own* git history — never this repo's `.ai/workflow/` copy.** See
P03-T01's Context for why this matters (it was gotten wrong once
there and corrected).

Relevant existing files/pattern to match:
- `LAAW/templates/context-template.md` —
  the style to mirror: short, entry-point prose, no filler.
- `LAAW/skills/create-constitution-full/SKILL.md`
  step 2 ("First run only") — currently copies `info-template.md` →
  `.ai/info.md`, `context-template.md` → `.ai/context/context.md`,
  `decisions-template.md` → `.ai/decisions/decisions.md`, each only if
  the destination doesn't already exist. This task adds a fourth,
  identical copy.

## Implementation

### Objective

A newly bootstrapped project gets `.ai/workbench/README.md`
automatically on first run, the same way it already gets
`.ai/info.md`/`.ai/context/context.md`/`.ai/decisions/decisions.md` —
via a new template file and one more copy step in
`create-constitution-full`.

### In scope

- New template file: `templates/workbench-readme-template.md`.
- `create-constitution-full/SKILL.md`'s step 2: one more first-run,
  don't-overwrite-if-exists copy.
- `create-constitution-full/SKILL.md`'s Inputs and Output sections:
  list the new template/destination alongside the existing three.

### Out of scope

- Creating `.ai/workbench/README.md` in any specific project (this
  repo included) — that only happens via an actual
  `create-constitution-full` first run, not as a side effect of this
  task.
- Anything about `context.temp.md`/`build-plan.md` or
  `build-context-full` — P03-T02/T03/T04.

### Files to modify

- `LAAW/skills/create-constitution-full/SKILL.md`
  — step 2, Inputs, Output.

### Files to create

- `LAAW/templates/workbench-readme-template.md`

### Steps

1. Create `LAAW/templates/workbench-readme-template.md`
   with this content (flexible: exact wording, as long as it states
   the directory is freeform/disposable and not part of the permanent
   record):
   ```
   # Workbench

   Freeform scratch space for the human and agent working together —
   planning notes, scratch questions and answers, prompt drafts,
   anything disposable. Nothing here is part of the permanent record:
   no fixed schema, no `info.md`/roadmap pointer into it, and no skill
   treats its content as an input it depends on.
   ```
2. In `create-constitution-full/SKILL.md` step 2, after the existing
   `decisions-template.md` copy sentence, add: "If
   `.ai/workbench/README.md` doesn't exist, copy
   `.ai/workflow/templates/workbench-readme-template.md` there
   unedited." (flexible: exact phrasing, must preserve the
   don't-overwrite-if-exists rule already stated for the other three.)
3. In that same skill file's `## Inputs` section, add
   `.ai/workflow/templates/workbench-readme-template.md` to the list
   of templates "only read/used if the destinations don't exist yet."
4. In that same skill file's `## Output` section, add
   `.ai/workbench/README.md` to the "first run only" list alongside
   `.ai/info.md`, `.ai/context/context.md`, `.ai/decisions/decisions.md`.

### Dependencies

None.

### Expected result

`LAAW/templates/workbench-readme-template.md`
exists; `create-constitution-full/SKILL.md` copies it to
`.ai/workbench/README.md` on a project's first run, same
don't-overwrite guarantee as the other three templates. Committed
inside `LAAW/`'s own git history.

### Automatic validations

- `test -f LAAW/templates/workbench-readme-template.md`
- `grep -n "workbench-readme-template" LAAW/skills/create-constitution-full/SKILL.md`
  — matches in step 2, Inputs, and Output.
- `git -C LAAW log --oneline -1` shows a
  commit for this change.

### Manual validations

- Read the updated step 2 and confirm the new copy sentence reads as
  the same pattern as the other three, not as a bolted-on exception.
