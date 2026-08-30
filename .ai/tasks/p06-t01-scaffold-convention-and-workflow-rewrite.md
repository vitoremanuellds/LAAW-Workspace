# P06-T01 — Shared scaffold-on-first-use convention + `workflow.md` rewrite

## Context

See [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md)
for full rationale; not repeated here. Decisions this task implements
come from [ADR03](../decisions/adr03-single-modular-workflow.md) and
its amendment. First task in the phase — every later P06 task
references the convention doc and `workflow.md` sections this one
establishes.

**LAAW's actual source files, edited in
`LAAW/`'s own checkout and committed to
*its own* git history — never this repo's `.ai/workflow/` copy.**

## Implementation

### Objective

Document the "scaffold on first use" convention once, and rewrite
`workflow.md` to describe one modular workflow (presence/granularity/
locality) instead of a fixed profile.

### In scope

- New `reference/scaffold-on-first-use.md`: the shared convention every
  layer-owning skill follows — check whether its directory exists;
  if not, create it plus a starter index file (a table with the same
  columns `roadmap.md` used: `| ID | Title | ... | Status |`, adapted
  per layer) before doing anything else; never overwrite existing
  content.
- `workflow.md` §3 (directory structure): `.ai/constitution/` narrows
  to mission/techstack; `.ai/phases/` gains `phases.md` as its index
  (replacing `.ai/constitution/roadmap.md`); `.ai/tasks/` gains
  `tasks.md` (orphan-task index only) and the `t{NN}-{name}.md` naming
  alongside existing `p{NN}-t{NN}-{name}.md`; every layer except
  `.ai/tasks/` marked optional, presence inferred from existence.
- `workflow.md` §4 (artifact hierarchy): note phases/context/decisions/
  constitution are optional; a task may skip its phase link (orphan).
- `workflow.md` §11-equivalent (Status/permanent record section):
  remove the "fast pointer" framing entirely — `phases.md`/`tasks.md`/
  a phase's own task table are the sole permanent record now, no
  separate `info.md` pointer to keep in sync.
- `workflow.md` §12 (commit discipline): add that it applies only to
  files that aren't gitignored.
- `workflow.md` §6/§7 (Deviations/ADRs) and anywhere else in the file:
  update any reference from `roadmap.md` to `phases.md`.
- Rename decision applied here and assumed by later tasks: drop the
  `-full` suffix from every skill name (no other profile exists to
  distinguish from) — `create-constitution-full`→`create-constitution`,
  `define-task-full`→`define-task`, `implement-task-full`→
  `implement-task`, `review-work-full`→`review-work`,
  `validate-work-full`→`validate-work`, `build-context-full`→
  `build-context`. `define-phase` and `propagate-context` keep their
  names (never had the suffix). New skill: `bootstrap`. Update every
  skill-name reference inside `workflow.md`'s own operation table (§2)
  to the new names — actually renaming the skill directories/files
  themselves happens in the tasks that own each skill (T02–T04), not
  here; this task only updates `workflow.md`'s references.

### Out of scope

- Actually renaming/rewriting individual skill files — T02, T03, T04.
- Templates and `reference/` files other than the new
  `scaffold-on-first-use.md` — T05.
- This outer meta-repo's own `.ai/` — untouched, stays on its current
  bootstrapped structure (P06's own Out-of-scope).

### Files to modify

- `LAAW/workflow.md`

### Files to create

- `LAAW/reference/scaffold-on-first-use.md`

### Steps

1. Write `reference/scaffold-on-first-use.md`: state the convention
   once (check-exists → create dir + starter index file → never
   overwrite), and list which skill owns which layer's scaffold step
   (constitution, phases, tasks, context, decisions, workbench) —
   forward-reference the skills by their new (post-rename) names.
2. In `workflow.md` §2's operation table, rename every `*-full` skill
   to its new name; add a `bootstrap` row for "layer setup."
3. In `workflow.md` §3, rewrite the directory-structure block per the
   In-scope bullets above; rewrite the prose immediately after it to
   state presence-by-existence and tasks-as-the-only-mandatory-layer.
4. In `workflow.md` §4, add the one-paragraph note on optional layers
   and orphan tasks.
5. Find and rewrite the Status/fast-pointer section (currently §11):
   remove the pointer framing, state `phases.md`/`tasks.md`/phase task
   tables as the sole permanent record.
6. In §12 (commit discipline), add the gitignore-exemption sentence.
7. Grep the whole file for `roadmap.md` and replace every hit with
   `phases.md`, adjusting surrounding prose where the sentence assumed
   `roadmap.md` lived in `constitution/`.

### Dependencies

None — first task in this phase.

### Expected result

`workflow.md` fully describes the modular workflow; a new
`reference/scaffold-on-first-use.md` exists and is the single source
every later task's skill points back to.

### Automatic validations

- `grep -n roadmap.md LAAW/workflow.md` — no
  hits.
- `grep -n "\-full" LAAW/workflow.md` — no
  hits (all skill references renamed).
- `LAAW/reference/scaffold-on-first-use.md`
  exists.

### Manual validations

- Read `workflow.md` end to end — confirm it reads as one coherent
  document, not a patchwork of edits (no leftover "profile" language).
