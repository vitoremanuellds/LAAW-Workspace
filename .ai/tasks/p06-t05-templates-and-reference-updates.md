# P06-T05 — Update templates and `reference/` files

## Context

See [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md)
and [ADR03](../decisions/adr03-single-modular-workflow.md). Depends on
P06-T01–T04 (references the final skill names and layer conventions
those tasks establish).

**LAAW's actual source files, edited in
`LAAW/`'s own checkout, committed to *its
own* git history.**

## Implementation

### Objective

Bring `templates/` and `reference/` in line with the redesigned
workflow: no `info.md` Status section, no `roadmap.md`, skill names
updated, orphan-task convention documented where relevant.

### In scope

- `templates/info-template.md`: remove the Status section entirely;
  keep Policy only.
- `reference/directory-and-links.md`: update the directory list —
  `.ai/constitution/` narrowed, `.ai/phases/phases.md` replaces
  `.ai/constitution/roadmap.md`, `.ai/tasks/tasks.md` +
  `t{NN}-{name}.md` added alongside the existing phase-linked
  convention; every layer but `.ai/tasks/` marked optional.
- `reference/status-and-info.md`: this file was entirely about the
  `info.md` Status pointer, which no longer exists — rewrite it to
  instead explain how to find "what's active" by reading
  `phases.md`/`tasks.md`/a phase's own task table directly (or fold
  its still-relevant content, if any, into `workflow.md` itself and
  delete the file — decide based on how much survives).
- `reference/starting-without-a-plan.md` and
  `reference/reread-skill-discipline.md`: grep for old skill names
  (`-full` suffixes) and `roadmap.md`; fix any hits.

### Out of scope

- Any skill file itself — T01–T04 already covered those.

### Files to modify

- `LAAW/templates/info-template.md`
- `LAAW/reference/directory-and-links.md`
- `LAAW/reference/status-and-info.md`
  (rewritten, or removed if nothing survives — note the choice made)
- `LAAW/reference/starting-without-a-plan.md`
- `LAAW/reference/reread-skill-discipline.md`

### Files to create

None.

### Steps

1. Rewrite `templates/info-template.md`: drop the Status section and
   its surrounding prose; keep the Policy section as-is.
2. Rewrite `reference/directory-and-links.md`'s directory list and
   per-directory rationale to match T01's `workflow.md` §3.
3. Decide `status-and-info.md`'s fate (rewrite vs. delete) and execute;
   if deleted, remove its link from `workflow.md` §11-equivalent and
   anywhere else it's referenced.
4. Grep `starting-without-a-plan.md` and `reread-skill-discipline.md`
   for `-full` skill names and `roadmap.md`; fix all hits.

### Dependencies

P06-T01, P06-T02, P06-T03, P06-T04.

### Expected result

No template or reference file references a removed concept (`info.md`
Status, `roadmap.md`) or a renamed skill by its old name.

### Automatic validations

- `grep -n "Status" LAAW/templates/info-template.md`
  — no hits describing a pointer/fast-pointer section.
- `grep -rln roadmap.md LAAW/reference/`
  — no hits.
- `grep -rln "\-full" LAAW/reference/ LAAW/templates/`
  — no hits.

### Manual validations

- Read `directory-and-links.md` end to end against the final
  `workflow.md` §3 — confirm they agree exactly on which layers are
  optional and where each index file lives.
