# P06-T02 — Narrow the constitution skill; add the `bootstrap` skill

## Context

See [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md)
and [ADR03](../decisions/adr03-single-modular-workflow.md). Depends on
P06-T01's `reference/scaffold-on-first-use.md` and renamed operation
table existing first.

**LAAW's actual source files, edited in
`LAAW/`'s own checkout, committed to *its
own* git history.**

## Implementation

### Objective

`create-constitution-full` becomes `create-constitution`, narrowed to
mission/techstack content only. A new `bootstrap` skill lets a user
choose which optional layers to turn on now, delegating to each
layer's own scaffold step.

### In scope

- `git mv skills/create-constitution-full skills/create-constitution-full`
  → rename directory to `skills/create-constitution`; update its
  `SKILL.md` frontmatter `name:`.
- Remove its roadmap-writing step (old step 6) entirely — phases are no
  longer part of the constitution.
- Remove its first-run side-effect bootstrapping of `info.md`/
  `context.md`/`decisions.md`/workbench-README (old step 2) — each of
  those becomes its owning skill's own scaffold-on-first-use
  responsibility (per T01's reference doc), not the constitution
  skill's job. `info.md` bootstrapping specifically has no other clear
  owner since it's not a layer — keep exactly that one piece
  (`info.md` bootstrap, Policy only, no Status section) in
  `create-constitution` as the "always runs first" step, since a
  project without a constitution still needs gate authority. Every
  other bootstrapped file's ownership moves.
- New `skills/bootstrap/SKILL.md`: Can — ask which optional layers
  (constitution / context / decisions / phases / workbench) to enable
  now, trigger each chosen layer's own scaffold step (calling into
  `create-constitution`, phase-planning, task-planning [only if the
  user explicitly wants an empty `tasks.md` seeded early], context,
  decisions, workbench conventions as appropriate). Must — never
  overwrite an existing layer; safely re-runnable to add a layer not
  chosen initially. Cannot — author actual mission/techstack/phase/task
  content itself (that's each owning skill's job once invoked for real
  work).

### Out of scope

- Any other skill's own scaffold step — T03, T04.
- Templates/reference files beyond what `bootstrap`/`create-constitution`
  directly need — T05.

### Files to modify

- `LAAW/skills/create-constitution-full/SKILL.md`
  (moved to `create-constitution/SKILL.md`)

### Files to create

- `LAAW/skills/bootstrap/SKILL.md`

### Steps

1. `git mv skills/create-constitution-full skills/create-constitution`.
2. Rewrite its `SKILL.md`: update frontmatter `name`/`description`;
   remove the roadmap-writing step and the file-bootstrapping side
   effects other than `info.md` itself; keep mission/techstack
   interview steps as-is; update its Output section to list only
   `mission.md`, `techstack.md`, and (first run only) `info.md`.
3. Write `skills/bootstrap/SKILL.md`: frontmatter, Can/Must/Cannot,
   When to use, Inputs, Procedure (ask layer menu → for each chosen
   layer, invoke that layer's scaffold step per
   `reference/scaffold-on-first-use.md` → commit), Output.
4. Update `workflow.md` §2's `bootstrap` row (added in T01) to link to
   this skill file.

### Dependencies

P06-T01.

### Expected result

`skills/create-constitution/SKILL.md` exists (old path gone), narrowed
to mission/techstack + `info.md`-first-run only.
`skills/bootstrap/SKILL.md` exists with the exact layer menu from
ADR03.

### Automatic validations

- `test -f LAAW/skills/create-constitution/SKILL.md`
- `test ! -d LAAW/skills/create-constitution-full`
- `test -f LAAW/skills/bootstrap/SKILL.md`
- `grep -n roadmap.md LAAW/skills/create-constitution/SKILL.md`
  — no hits.

### Manual validations

- Read both skill files together — confirm no overlapping
  responsibility (bootstrap never authors content, constitution never
  scaffolds layers other than itself + `info.md`).
