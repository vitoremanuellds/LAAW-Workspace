# Mission

## What

This repo (`Local-Model-Agent-Workflow`) is the meta-project for the
Local Model Agent Workflow family. It develops workflow variants
lighter than [`Full-Local-Model-Agent-Workflow`](../../Full-Local-Model-Agent-Workflow/)
(the only variant that exists today, still its own repo), and a
mechanism for bootstrapping any variant into a target project's
`.ai/workflow/` without a git submodule.

## Why

`Full-Local-Model-Agent-Workflow` used to ship `medium`/`lite`/`minimal`
profiles alongside `full`, then dropped to `full`-only — maintaining
several profiles inside one repo made every workflow change multiply
across all of them. Developing lighter variants as their own
repos/copies from this meta-project instead avoids that: each variant
stays independently scoped, maintained, and versioned, the same way
`full` already is.

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

- Design and ship at least one workflow variant lighter than `full`.
- Design and ship a copy-based bootstrap mechanism any project can use
  to install a chosen variant into `.ai/workflow/`.
- Evolve core workflow mechanics that aren't specific to any one
  profile's weight — a freeform temp/scratch workspace, context-build
  cleanup, git-history-driven context sync, and concurrency-safe
  phase/task planning. Developed directly in
  `Full-Local-Model-Agent-Workflow/`'s own checkout, committed to that
  repo's own history — see Boundaries below.

## Boundaries

- Changes to `full`'s actual content (`workflow.md`, `skills/`,
  `templates/`, `reference/`) are made in
  `Full-Local-Model-Agent-Workflow/`'s own checkout and committed to
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
instead of `Full-Local-Model-Agent-Workflow/`'s actual checkout. Fixed
by reverting the `.ai/workflow/` edits and redoing them in
`Full-Local-Model-Agent-Workflow/` (its own commit). Rewrote the third
Goal and Boundaries above, which had the wrong location baked in, so
P03-T02 through T04 and P04/P05 don't repeat it.
