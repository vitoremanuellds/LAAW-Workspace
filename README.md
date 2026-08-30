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
.ai/                ← this workspace's own project management, bootstrapped from LAAW itself
├── workflow/          ← plain-copy snapshot of LAAW, never edited here (see ADR01)
├── info.md             ← policy only: who's authorized for each gate
├── constitution/        ← mission.md, techstack.md — optional
├── context/              ← survey of this workspace's own structure — optional
├── decisions/             ← ADRs — the actual decision trail behind LAAW's design
├── phases/                 ← phases.md (index) + one file per phase (P01–P06 so far) — optional
├── tasks/                   ← tasks.md (orphan index) + one file per task, phase-linked or orphan
└── workbench/                ← freeform scratch, gitignored, disposable — optional
```

**Note on `.ai/workflow/`:** this workspace re-bootstrapped its copy
from `LAAW/`'s current content once the ADR03 redesign landed (P06) —
a manual, one-off application of what P02 (still unplanned) means to
eventually automate as a reusable mechanism. Per the workflow's own
rule, it's never hand-edited here; a structural change to it always
happens in `LAAW/`'s own checkout first, then gets pulled in by
re-running the same copy.

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
  [`.ai/phases/phases.md`](.ai/phases/phases.md) for phases,
  [`.ai/tasks/tasks.md`](.ai/tasks/tasks.md) for orphan tasks.
- Want to use LAAW in your own project? You don't need any of this
  repo — go straight to [`LAAW/README.md`](LAAW/README.md).
