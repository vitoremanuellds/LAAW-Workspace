# ADR03 — Replace per-profile repos with one modular workflow

## Decision

Retire the "one independently-versioned repo per profile" model
entirely. There is one workflow going forward — its content lives in
`LAAW/`'s own checkout — built around three
independent axes instead of fixed named profiles:

- **Presence** — every layer except tasks is optional and inferred
  from what exists on disk, not declared in a config file:
  `.ai/constitution/` (mission, techstack), `.ai/context/`,
  `.ai/decisions/`, `.ai/phases/`. No directory means that layer is
  off for this project. Tasks are the one mandatory layer.
- **Granularity** — a task opts into a phase parent or not,
  independently of whether the project uses phases at all. A
  phases-using project can still have standalone ("orphan") tasks.
  Convention: `.ai/tasks/p{NN}-t{NN}-{name}.md` for phase-linked (as
  today), `.ai/tasks/t{NN}-{name}.md` for orphan, both flat in
  `.ai/tasks/`, distinguished by filename shape alone, each with its
  own independent sequential counter. `.ai/tasks/tasks.md` is the
  index/permanent-record table for orphan tasks only — phase-linked
  tasks stay indexed solely in their phase file's own task table, same
  "one authoritative table per item" rule the phase/roadmap split
  already followed.
- **Locality** — one `.ai/` tree, always in-repo. A consuming project
  gitignores whichever layer(s) it doesn't want committed; there is no
  separate external-path storage mechanism to design or maintain.
  Commit discipline (`workflow.md` §12) follows suit: "commit each
  draft immediately" applies only to files that aren't gitignored — a
  gitignored layer is exempt from commit discipline by definition, not
  a special case of it. This generalizes to every layer, workbench
  included, which **supersedes ADR02's specific "no gitignore
  carve-out" stance for `.ai/workbench/`** — that stance existed so a
  teammate or `sync-context` could see workbench content, but locality
  is now the consuming project's own choice regardless of layer, and a
  solo user with neither has no reason to keep it tracked. The rest of
  ADR02 (workbench exists, is disposable, isn't schema-tracked) stands.

`.ai/info.md` drops its Status section entirely — no more separate
"fast pointer" to keep in sync. `phases.md`/`tasks.md`/a phase's own
task table are now always the authoritative record whenever phases or
tasks exist at all (true post-this-ADR in a way it wasn't before:
orphan tasks previously had no top-level index, so `info.md`'s pointer
was the only cheap way to find "what's active" without opening every
phase file). `info.md` narrows to Policy only — gate authority, not
status.

Structural consequence inside `.ai/phases/`: the phase-level permanent
record (today's `.ai/constitution/roadmap.md`) moves into
`.ai/phases/phases.md` and is renamed — phases are groupings of related
tasks, not a project roadmap, and belong next to the tasks they group
rather than inside the constitution. `.ai/constitution/` narrows to
just `mission.md` + `techstack.md`.

Task files never record where their description originated (no
`Source`/ticket-link field) — whether the assignment came from the
codebase, a ticket tracker, or a conversation is irrelevant to the
file's own structure; the task file still authors its own
Context/Requirements/Plan/Validations locally, same rigor as today.

`Light-Local-Model-Agent-Workflow/` is retired as a separately
maintained repo — its whole reason to exist (fewer layers, no team
review) is now just one configuration of the single workflow, not a
variant worth its own repo, skills, and templates to keep in sync.
Whether its submodule entry gets deregistered or left in place marked
deprecated is a separate, deliberately deferred decision — not part of
this ADR.

## Context

`mission.md`'s original "Why" recorded that `full` used to ship
`medium`/`lite`/`minimal` profiles inline, and dropped them because
maintaining several profiles in one repo made every workflow change
multiply across all of them. This project's original premise was that
moving each lighter variant into its own independently-versioned repo
would solve that. It doesn't — it only relocates the multiplication:
a core-mechanics change (the `.ai/workbench/` convention, `sync-context`,
concurrency-safe planning — this project's own third mission goal)
still has to be manually ported into every variant's own repo and
history by hand. P01's own working notes
([`.ai/workbench/p01-profile-planning.md`](../workbench/p01-profile-planning.md),
now superseded) already flagged this tension when scoping `Light`:
"inherit P03–P05's mechanics... rather than forking from pre-P03
`full`" was already an attempt to avoid divergence between two
separately-maintained repos, not a solved problem.

The user proposed the alternative captured here directly: rather than
maintaining N variants of the same workflow, maintain one workflow
whose weight is a function of which optional layers a consuming
project turns on. `full` and `Light` (and any future named variant)
collapse into presets of the same underlying design rather than
separately-versioned document sets.

## Alternatives Considered

- **Keep the status quo** (one repo per profile, this repo's original
  premise) — rejected: doesn't solve "every workflow change
  multiplies," it just moves where the multiplication happens, from
  "profiles in one repo" to "profiles across repos with no shared
  source of truth."
- **Explicit config-file-driven layer selection** (an `info.md` flag
  list of active layers) — rejected: presence-on-disk is simpler,
  needs no schema to describe the schema, and keeps with the existing
  minimal-files philosophy (a project that doesn't use phases just has
  no `phases/` directory, nothing to declare).
- **Per-layer external storage location** (each layer independently
  choosing in-repo vs. some outside-repo path) — rejected per the
  user's own call: one `.ai/` convention with `.gitignore` for privacy
  is enough, and avoids building/maintaining an external-path bootstrap
  mechanism nobody asked for.

## Consequences

- The actual redesign — `LAAW/`'s
  `workflow.md`, skills, templates, and reference files rebuilt around
  these three axes — is content work done in *its own* checkout and
  git history, never in this repo's `.ai/workflow/` copy (frozen
  bootstrap snapshot per ADR01) and never absorbed into this outer
  repo's commits. It is scoped as a new phase, planned separately
  (successor to P01, not a reuse of its ID).
- P01 ("Design the `Light` workflow profile") is superseded by this
  ADR — its own file is marked as such, not deleted, and its
  `roadmap.md` row's Status reflects that. No `Light`-specific content
  work proceeds under it.
- `mission.md`'s Goals and `techstack.md`'s Versioning section both
  described a "one repo per variant" world; both need rewriting to
  match this decision (done alongside this ADR).
- This repo's own `.ai/` stays on its currently-bootstrapped (pre-this-
  redesign) structure — `roadmap.md` stays where it is, the orphan-task
  convention isn't introduced here — until a real re-bootstrap/re-sync
  mechanism (P02) lets it pull in the redesigned workflow. Until then,
  this repo's own phase/task files keep using the old schema for
  anything drafted here.
- Naming: the workflow repo (formerly `Full-Local-Model-Agent-Workflow/`)
  no longer described "the heaviest of several variants" once it's the
  only workflow. Renamed on GitHub to `LAAW` (Local AI Agents Workflow)
  on 2026-08-29; `.gitmodules`' URL updated same-day. The local
  submodule directory path and this repo's own prose references were
  renamed to match on 2026-08-30 — no longer deferred (see `mission.md`'s
  2026-08-30 note). `Light-Local-Model-Agent-Workflow/`'s submodule,
  left registered as an open question above, is likewise resolved as of
  2026-08-30: fully deregistered, not deprecated-in-place.
