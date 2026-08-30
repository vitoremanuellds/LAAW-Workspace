# Mission

## What

This repo (`Local-Model-Agent-Workflow`) is the meta-project for the
Local Model Agent Workflow family. It develops **one modular
workflow** — its content lives in
[`LAAW`](../../LAAW/)'s
own checkout — whose weight scales via optional layers rather than via
separately-maintained variants, and a mechanism for bootstrapping it
into a target project's `.ai/workflow/` without a git submodule. See
[`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md)
for the full design.

## Why

`LAAW` used to ship `medium`/`lite`/`minimal`
profiles alongside `full` inline, then dropped to `full`-only —
maintaining several profiles inside one repo made every workflow change
multiply across all of them. This project's original premise was that
moving each lighter variant into its own independently-versioned repo
would fix that. It didn't — it only relocated the multiplication: a
core-mechanics change still has to be manually ported into every
variant's own repo and history by hand, one at a time. ADR03 replaces
that with a single workflow built on three independent axes:
**presence** (every layer but tasks is optional, inferred from what
exists on disk — no config to declare it), **granularity** (a task
opts into a phase parent or not, independently of whether the project
uses phases at all), and **locality** (one `.ai/` tree, always in-repo;
a consuming project gitignores whatever layer it doesn't want
committed). `full` and `Light` collapse into presets of this one
design rather than separately-versioned document sets.

Submodules were `full`'s original bootstrap mechanism, but carry real
cost: `git submodule update --remote` against a dirty submodule ranges
from refusing to run to silently discarding uncommitted project work,
the repo doesn't publish tagged releases yet so every update is a
potential breaking change, and every consuming project needs its own
submodule literacy just to get the files onto disk. This repo's own
`.ai/workflow/` was bootstrapped today as a plain copy instead — proof
of the mechanism this project exists to generalize (see
[`adr01-plain-copy-bootstrap.md`](../decisions/adr01-plain-copy-bootstrap.md)).

## Who

The repo owner — solo maintenance for now.

## Goals

- Redesign `LAAW/`'s own content
  (`workflow.md`, skills, templates, reference) around the three axes
  in [`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md) —
  developed directly in its own checkout, committed to that repo's own
  history — see Boundaries below.
- Design and ship a copy-based bootstrap mechanism any project can use
  to install the workflow into `.ai/workflow/`.
- Evolve core workflow mechanics that aren't specific to any one
  layer's weight — a freeform temp/scratch workspace, context-build
  cleanup, git-history-driven context sync, and concurrency-safe
  phase/task planning. Developed directly in
  `LAAW/`'s own checkout, committed to that
  repo's own history — see Boundaries below.

## Boundaries

- Changes to `full`'s actual content (`workflow.md`, `skills/`,
  `templates/`, `reference/`) are made in
  `LAAW/`'s own checkout and committed to
  *its own* git history — never absorbed into this outer repo's
  commits, and never hand-edited via this repo's `.ai/workflow/` copy.
  `.ai/workflow/` here stays a frozen bootstrap snapshot (per ADR01,
  literally "submodule, never written to" per its own §3) until a real
  re-bootstrap/re-sync mechanism exists (P02) — this repo's own
  planning work reads it, never edits it.
- Not responsible for a project's actual `.ai/` content (constitution,
  phases, tasks, decisions) once bootstrapped — that's the consuming
  project's own, per `workflow.md`'s repo-boundary rules.

---

**[ASSUMPTION]** Split into exactly two goals/phases (design the
lighter variant(s); design the bootstrap mechanism) based on how the
request was phrased. If these should be one combined phase, or there's
a third piece of scope (e.g. which specific profile(s) to bring back —
`lite`? `minimal`? something new?), flag it at review.

**2026-08-28:** Added a third goal (workflow-mechanics evolution) and
three phases (P03–P05) for it, confirmed with the user as a separate
goal from "lighter variant design" rather than folded into P01 —
these mechanics (workbench dir, context-build cleanup, sync-context,
concurrency-safe planning) aren't about weight, they're improvements
any variant should eventually inherit.

**2026-08-29:** Resolved the `[ASSUMPTION]` above: one profile, named
`Light`, designed fresh rather than reviving `medium`/`lite`/`minimal`.
Its repo (`Light-Local-Model-Agent-Workflow/`) already existed and is
now registered as a proper submodule of this meta-repo. See
[`p01-design-light-profile.md`](../phases/p01-design-light-profile.md)
for the full scope.

**2026-08-29:** Corrected a task-level deviation: P03-T01 was first
implemented by hand-editing this repo's own `.ai/workflow/` copy
instead of `LAAW/`'s actual checkout. Fixed
by reverting the `.ai/workflow/` edits and redoing them in
`LAAW/` (its own commit). Rewrote the third
Goal and Boundaries above, which had the wrong location baked in, so
P03-T02 through T04 and P04/P05 don't repeat it.

**2026-08-29:** Project-level pivot, superseding the same-day note
above about `Light`: rather than maintaining `full` and `Light` as
separately-versioned repos, this project now builds **one** modular
workflow whose weight is a function of which optional layers a
consuming project turns on. See
[`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md).
P01 is superseded — no `Light`-specific content work proceeds under it.
`Light-Local-Model-Agent-Workflow/`'s submodule is left registered for
now; whether to deregister it or mark it deprecated in place is a
separate, still-open decision. What/Why/Goals above were rewritten to
match; Boundaries' rules on where content work happens are unchanged.

**2026-08-30:** Resolved the two open naming/registration items from
the note above. `Light-Local-Model-Agent-Workflow`'s submodule is
deregistered entirely (`git submodule deinit` + `git rm` +
`.gitmodules` cleanup) — not left in place deprecated; there is no
remaining trace of it in this repo beyond Git history. The remaining
workflow repo's local submodule path is renamed from
`Full-Local-Model-Agent-Workflow/` to `LAAW/` (matching its GitHub
rename from the same day), and every path reference across this
repo's own `.ai/` and `AGENTS.md` updated to match — the "deferred
cleanup" both ADR03 and P06 mentioned is done.
