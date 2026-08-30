# P06-T04 — Rename remaining `-full` skills; update `propagate-context`

## Context

See [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md)
and [ADR03](../decisions/adr03-single-modular-workflow.md). Depends on
P06-T01.

**LAAW's actual source files, edited in
`LAAW/`'s own checkout, committed to *its
own* git history.**

## Implementation

### Objective

Finish the `-full` suffix rename across the remaining skills, and
update `propagate-context` (and `build-context`'s own scaffold step)
for the removed `info.md` Status section and `phases.md` rename.

### In scope

- `git mv` for: `implement-task-full`→`implement-task`,
  `review-work-full`→`review-work`, `validate-work-full`→
  `validate-work`, `build-context-full`→`build-context`. Update each
  `SKILL.md`'s frontmatter `name`; update any internal cross-references
  to other skills by their new names (e.g. `implement-task-full` might
  reference `define-task-full` — fix both directions).
- `build-context/SKILL.md`: add a scaffold-on-first-use step for
  `.ai/context/` + `context.md`, per `reference/scaffold-on-first-use.md`
  (matches what `create-constitution` used to do as a side effect,
  now owned here instead).
- `propagate-context/SKILL.md`: replace any `roadmap.md` reference with
  `phases.md`; remove any step that reads/clears `info.md`'s Status
  section (it no longer exists) — `phases.md`/`tasks.md`/phase task
  tables are the permanent record now, nothing to clear.
- Decisions-writing (wherever an ADR gets authored, e.g. inside
  `implement-task`): add a scaffold-on-first-use step for
  `.ai/decisions/` + `decisions.md` if a project's first-ever ADR is
  being written and the directory doesn't exist.
- Workbench: confirm whichever skill first writes into
  `.ai/workbench/` (today, `build-context`'s temp files) scaffolds it
  + copies `workbench-readme-template.md` on first use, replacing the
  side effect `create-constitution` used to own.

### Out of scope

- `define-phase`/`define-task` — T03. `create-constitution`/`bootstrap`
  — T02.

### Files to modify

- `LAAW/skills/implement-task-full/SKILL.md`
  (moved)
- `LAAW/skills/review-work-full/SKILL.md`
  (moved)
- `LAAW/skills/validate-work-full/SKILL.md`
  (moved)
- `LAAW/skills/build-context-full/SKILL.md`
  (moved)
- `LAAW/skills/propagate-context/SKILL.md`

### Files to create

None.

### Steps

1. `git mv` each of the four skill directories to drop `-full`; update
   each file's frontmatter `name`.
2. Grep all skill files for the old `-full` names and fix any
   cross-references.
3. Add the context scaffold-on-first-use step to `build-context`.
4. Add the decisions scaffold-on-first-use step wherever ADRs get
   authored.
5. Confirm/add the workbench scaffold-on-first-use step wherever it's
   currently missing.
6. Rewrite `propagate-context`: `roadmap.md`→`phases.md`, remove the
   `info.md` Status-clearing step.

### Dependencies

P06-T01.

### Expected result

No skill directory or frontmatter still carries a `-full` suffix
except where genuinely renamed already in T02/T03; every layer has an
owning skill with its own scaffold-on-first-use step;
`propagate-context` has no remaining `info.md` Status or `roadmap.md`
references.

### Automatic validations

- `grep -rl "\-full" LAAW/skills/*/SKILL.md`
  — no hits.
- `grep -n roadmap.md LAAW/skills/propagate-context/SKILL.md`
  — no hits.
- `grep -n "Active phase\|Active task" LAAW/skills/propagate-context/SKILL.md`
  — no hits.

### Manual validations

- Confirm each of the six optional/mandatory layers (constitution,
  context, decisions, phases, tasks, workbench) has exactly one skill
  responsible for scaffolding it on first use — no gaps, no
  duplicates.
