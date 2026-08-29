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
  phase/task planning. Designed and proven out here, in this repo's
  own `.ai/workflow/` copy, for variants (including a future `full`
  update, made independently in its own repo per the Boundaries below)
  to adopt.

## Boundaries

- Does not modify `Full-Local-Model-Agent-Workflow`'s own content or
  history — it stays its own repo, developed independently.
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
