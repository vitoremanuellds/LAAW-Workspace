# LAAW Workspace

The meta-project where **LAAW** (Local AI Agents Workflow) is
designed, planned, and developed. LAAW itself — the actual workflow
content (`workflow.md`, skills, templates, reference) — lives in its
own repo, [`LAAW/`](LAAW/), mounted here as a git submodule. This repo
is the workspace around it: the mission, decisions, and project-
management trail behind LAAW's design, not LAAW's own content.

See [`LAAW/README.md`](LAAW/README.md) for what LAAW actually is and
how to bootstrap it into a project. This README is about the
workspace, not the workflow.

## What LAAW is, briefly

A file-based agent workflow built around the hardest constraint —
small local models with tight context windows — so the same discipline
holds up (with more slack) on frontier models too. One workflow, not a
family of separately-maintained variants: how much of it a given
project uses scales through three independent axes — which optional
layers exist (constitution, context, decisions, phases; only tasks are
mandatory), whether a given task links to a phase or stands alone, and
which layers a project chooses to keep out of git. See
[`.ai/decisions/adr03-single-modular-workflow.md`](.ai/decisions/adr03-single-modular-workflow.md)
for the design decision behind that shape, and
[`.ai/constitution/mission.md`](.ai/constitution/mission.md) for the
full why/goals/boundaries.

This project used to take a different approach — separately-versioned
`full`/`medium`/`lite`/`minimal` profiles, then `full` plus a planned
`Light` — before ADR03 replaced that with the single modular design
above. That history is kept, not erased: superseded phases and
decisions stay in `.ai/`, marked as such, rather than deleted.

## How this repo is organized

```
README.md          ← this file
AGENTS.md           ← agent entry point: read .ai/workflow/workflow.md first, every session
LAAW/               ← submodule: LAAW's actual source, its own repo/history
.ai/                ← this workspace's own project management (dogfoods an older,
                       pre-redesign copy of the workflow — see note below)
├── workflow/          ← frozen bootstrap snapshot, never edited here (see ADR01)
├── info.md             ← policy: who's authorized for each gate
├── constitution/        ← mission.md, techstack.md, roadmap.md
├── context/              ← survey of this workspace's own structure
├── decisions/             ← ADRs — the actual decision trail behind LAAW's design
├── phases/                 ← feature-sized slices of work on LAAW (P01–P06 so far)
├── tasks/                   ← task breakdown per phase, plus orphan tasks (no phase parent)
└── workbench/                ← freeform scratch, gitignored, disposable
```

**Note on `.ai/workflow/`:** this workspace bootstrapped its own copy
of the workflow before the ADR03 redesign existed, and — per that
same redesign's own rules — never hand-edits it; a real re-bootstrap
mechanism to pull in the redesigned version is its own planned phase
(P02). So this repo's *own* `.ai/` still follows the older, pre-ADR03
schema (a `roadmap.md` instead of `phases.md`, no orphan-task
convention until it was retrofitted by hand for `T01`) even though the
workflow it's busy designing — in `LAAW/` — has already moved past
that schema. That's expected, not a bug: this workspace is a consumer
of an old bootstrap, same as any other project would be until it
re-bootstraps.

## Where things actually get built

Everything under `.ai/` in this repo is planning and decision-making
*about* LAAW — phases, tasks, ADRs. The actual content changes
(`workflow.md`, skills, templates, reference files) are always made
and committed inside [`LAAW/`](LAAW/)'s own checkout and git history,
never here — see `mission.md`'s Boundaries section for why, and
[`.ai/decisions/`](.ai/decisions/) for the ADR trail of decisions that
shape it.

## Getting started (as a human, not an agent)

- Want to know why LAAW looks the way it does? Start at
  [`.ai/constitution/mission.md`](.ai/constitution/mission.md), then
  the ADRs in [`.ai/decisions/`](.ai/decisions/) in order.
- Want to see what's actively being worked on? Check
  [`.ai/constitution/roadmap.md`](.ai/constitution/roadmap.md) for
  phases, [`.ai/tasks/tasks.md`](.ai/tasks/tasks.md) for orphan tasks.
- Want to use LAAW in your own project? You don't need any of this
  repo — go straight to [`LAAW/README.md`](LAAW/README.md).
