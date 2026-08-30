# P06 — Redesign LAAW as a single modular workflow

## Context

Successor to P01 (superseded), scoped directly from
[`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md)
and its amendment (gitignore-aware commit discipline, `info.md` Status
removal, ADR02 partial supersession) — read both in full before
planning tasks, this phase doesn't repeat their reasoning.
[`.ai/workbench/idea.md`](../workbench/idea.md) has the original framing
that started this, while it still exists (now gitignored per the
user's own `.gitignore` — disposable, not load-bearing; everything it
says that matters is already folded into ADR03).

Unlike P01, this phase does not stand up a new repo — it redesigns
`Full-Local-Model-Agent-Workflow/`'s own existing `workflow.md`,
skills, templates, and reference files **in place**. That repo was
renamed on GitHub to `LAAW` (`.gitmodules` and its own `origin` remote
already repointed); its local submodule directory path and this outer
repo's prose still say `Full-Local-Model-Agent-Workflow/` for now —
deferred cleanup, not this phase's concern (ADR03 Consequences).

**Same location discipline established the hard way in P03-T01, and
carried by P01 before being superseded:** everything this phase's Plan
produces is written in `Full-Local-Model-Agent-Workflow/`'s own
checkout and committed to *its own* git history — never this repo's
`.ai/` tree, and never `.ai/workflow/` (a frozen bootstrap snapshot of
the *pre*-this-redesign workflow, per ADR01 — this repo's own planning
work reads it, never edits it, until a re-bootstrap mechanism exists,
P02).

## In scope

- New `bootstrap` skill: asks which optional layers
  (constitution / context / decisions / phases / workbench) to enable
  now — tasks excluded, always implicit — then triggers each chosen
  layer's own scaffold step. Re-runnable later to add a layer not
  chosen the first time.
- A shared "scaffold on first use" convention, documented once and
  wired into every skill that owns an optional layer (constitution,
  phase-planning, task-planning, context-survey, decisions, workbench),
  so calling that skill directly — without ever running `bootstrap` —
  still creates its own directory + starter file the first time it's
  needed.
- Narrowing the constitution skill to mission/techstack content only —
  drop its roadmap-writing step and its first-run
  side-effect-bootstrapping of `info.md`/`context.md`/`decisions.md`/
  workbench-README (moved to `bootstrap` + each owning skill's own
  scaffold step).
- Phase-level permanent record moves from `.ai/constitution/roadmap.md`
  to `.ai/phases/phases.md`, scaffolded on first use like any other
  optional layer.
- Orphan-task convention: `.ai/tasks/tasks.md` as the index/permanent
  record for orphan tasks only, `.ai/tasks/t{NN}-{name}.md` naming
  (own sequential counter, distinguished from phase-linked
  `p{NN}-t{NN}-{name}.md` by filename shape alone). No `Source`/
  ticket-link field on any task file.
- Dropping `info.md`'s Status section — `phases.md`/`tasks.md`/a
  phase's own task table are the sole permanent record, no separate
  pointer to keep in sync.
- Commit discipline (`workflow.md` current §12) updated: applies only
  to files that aren't gitignored.
- Rewriting `workflow.md` itself throughout — directory structure,
  artifact hierarchy, lifecycle/gates framing, Deviations/ADR
  references to `roadmap.md` — to describe one modular workflow with
  optional layers, not a "full" profile among several.
- Confirming and applying any skill/file renames implied by there no
  longer being a "full" profile to distinguish from (e.g. whether
  `create-constitution-full`, `define-task-full`, `implement-task-full`,
  etc. drop their `-full` suffix) — decided as this phase's first Plan
  step, not assumed here.

## Out of scope

- The actual non-submodule bootstrap *installer* mechanism that copies
  `.ai/workflow/` into a consuming project's disk — that's P02,
  unrelated content, still `not-planned`.
- Retiring or deregistering the `Light-Local-Model-Agent-Workflow`
  submodule — separate, deliberately deferred decision (ADR03
  Consequences).
- Renaming this outer meta-repo's own local submodule directory path
  or its own prose references away from
  `Full-Local-Model-Agent-Workflow/` — deferred cleanup, not part of
  this phase.
- This outer meta-repo's own `.ai/` adopting any of the new schema
  (`phases.md`, `tasks.md`, orphan tasks, no `info.md` Status) — it
  stays on its currently-bootstrapped structure until a real
  re-bootstrap/re-sync mechanism (P02) exists, per ADR03's own
  Consequences. Nothing in this phase touches this repo's own
  `.ai/constitution/roadmap.md`, `.ai/info.md`, etc. beyond the
  Status/Depends-on bookkeeping every phase does for itself.
- P04 (context sync from git history) and P05 (concurrency-safe
  planning) mechanics — independently scoped, already separately
  planned, untouched by this phase.

## Requirements

- `workflow.md` documents all three ADR03 axes (presence, granularity,
  locality) explicitly; no remaining "profile" framing.
- A working `bootstrap` skill exists with the exact layer menu from
  ADR03.
- Every skill that owns an optional layer has its own scaffold-on-
  first-use step, referencing one shared documented convention rather
  than repeating diverging prose per skill.
- The constitution skill writes mission/techstack content only; no
  roadmap-writing step remains anywhere in it.
- `.ai/tasks/tasks.md` + `.ai/tasks/t{NN}-{name}.md` (orphan) and the
  existing `.ai/tasks/p{NN}-t{NN}-{name}.md` (phase-linked) conventions
  are both documented, with no `Source` field on either.
- `.ai/phases/phases.md` fully replaces `.ai/constitution/roadmap.md`
  in every reference across `workflow.md`, skills, templates, and
  reference files.
- No `info.md` template section remains describing a Status/fast-
  pointer pattern.
- Commit discipline explicitly states gitignored files are exempt.
- Every file this phase produces is written and committed in
  `Full-Local-Model-Agent-Workflow/`'s own checkout/history — never
  this outer repo's `.ai/workflow/` copy, never absorbed into this
  outer repo's own commits.

## Plan

1. Confirm the exact skill inventory and naming for the redesigned
   workflow — which existing `*-full` skills get renamed, merged, or
   split, and the new `bootstrap` skill's exact name. Every later step
   references files by name, so this comes first.
2. Design and document the shared "scaffold on first use" convention
   once (a `reference/` file), then wire each owning skill to it
   instead of repeating the logic per skill.
3. Write the new `bootstrap` skill: layer menu, delegation to each
   layer's own scaffold step, safe to re-run later to add a layer not
   chosen initially.
4. Narrow the constitution skill to mission/techstack content only;
   remove its roadmap-writing and first-run side-effect-bootstrapping
   steps.
5. Update the phase-planning skill: `.ai/phases/phases.md` as the
   index table (replacing `roadmap.md`), scaffolded on first use.
6. Update the task-planning skill: orphan-task convention
   (`t{NN}-{name}.md`, `.ai/tasks/tasks.md` index), phase-linked
   convention unchanged, no `Source` field.
7. Rewrite `workflow.md`: directory structure, artifact hierarchy,
   lifecycle/gates framing (confirm no changes needed beyond "layers
   are optional"), remove the Status-pointer section, update commit
   discipline for gitignore-awareness, update Deviations/ADR-section
   references to `roadmap.md`.
8. Check the fully redesigned `workflow.md` (+ whatever each operation
   reads) against its own prior size — confirm the added flexibility
   didn't grow what a single operation has to read, since that defeats
   the point.

## Automatic validations

- `Full-Local-Model-Agent-Workflow/skills/bootstrap/SKILL.md` (or
  whatever this phase's Plan step 1 settles on as its final name)
  exists.
- `grep -rl roadmap.md Full-Local-Model-Agent-Workflow/` returns
  nothing (no lingering references to the retired file).
- `grep -rl 'Source' Full-Local-Model-Agent-Workflow/skills/*/SKILL.md`
  shows no task-file `Source`/ticket-link field.
- `git -C Full-Local-Model-Agent-Workflow log --oneline` shows this
  phase's commits, separate from this outer repo's own.

## Manual validations

- Walk through three configurations by hand using only the redesigned
  workflow's own docs: (a) tasks-only, no other layer; (b)
  constitution + tasks, no phases; (c) full stack with an orphan task
  alongside phase-linked ones — confirm each works without reaching
  for a layer that isn't present.
- Confirm `bootstrap` and each owning skill's own scaffold-on-first-use
  step don't disagree or duplicate work, whichever path (bootstrap
  first, or lazy-only) gets exercised.
- Review that `workflow.md`'s own size stayed flat or shrank relative
  to before this phase — the new flexibility shouldn't cost more
  required reading per operation than the old fixed-profile version
  did.

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
| P06-T01 | Scaffold convention + `workflow.md` rewrite | Shared scaffold-on-first-use doc; rewrite directory structure, artifact hierarchy, Status/permanent-record framing, commit discipline | — | plan-approved |
| P06-T02 | Constitution + `bootstrap` skills | Narrow `create-constitution-full`→`create-constitution`; add new `bootstrap` skill | P06-T01 | plan-approved |
| P06-T03 | Phase + task planning skills | `define-phase` uses `phases.md`; `define-task-full`→`define-task` gains orphan-task convention | P06-T01 | plan-approved |
| P06-T04 | Remaining skill renames + `propagate-context` | Drop remaining `-full` suffixes; scaffold-on-first-use for context/decisions/workbench; fix `propagate-context` | P06-T01 | plan-approved |
| P06-T05 | Templates + `reference/` updates | `info-template.md`, `directory-and-links.md`, `status-and-info.md`, remaining reference files | P06-T01, P06-T02, P06-T03, P06-T04 | plan-approved |
| P06-T06 | Validation + size check | Cross-file grep sweep, word-count comparison, manual walkthroughs, close out this repo's own bookkeeping | P06-T01, P06-T02, P06-T03, P06-T04, P06-T05 | plan-approved |
