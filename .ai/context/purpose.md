# Purpose / Mission

LAAW = **Local AI Agents Workflow**. This repo (`LAAW-Workspace`) is the
meta-project where LAAW is designed, planned, and developed. It develops
**one modular workflow** — its content lives in
[`LAAW`](../../LAAW/) (a git submodule) — whose weight scales via
optional layers rather than via separately-maintained variants, and a
mechanism for bootstrapping it into a target project's `.ai/workflow/`
without a git submodule.

**What LAAW is:** A file-based agent workflow built around the hardest
constraint — small local models with tight context windows — so the same
discipline holds up (with more slack) on frontier models too. One
workflow, not a family of separately-maintained variants: how much of it
a given project uses scales through three independent axes — which
optional layers exist (constitution, context, decisions, phases; only
tasks are mandatory), whether a given task links to a phase or stands
alone, and which layers a project chooses to keep out of git.

**Why:** `LAAW` used to ship `medium`/`lite`/`minimal` profiles alongside
`full` inline, then dropped to `full`-only — maintaining several profiles
inside one repo made every workflow change multiply across all of them.
ADR03 replaced that with a single workflow built on three independent
axes: **presence** (every layer but tasks is optional, inferred from what
exists on disk), **granularity** (a task opts into a phase parent or not,
independently of whether the project uses phases at all), and **locality**
(one `.ai/` tree, always in-repo; a consuming project gitignores whatever
layer it doesn't want committed).

**Who:** The repo owner — solo maintenance for now.

**Goals:**
- Redesign `LAAW/`'s own content (`workflow.md`, skills, templates,
  reference) around the three axes in [ADR03](../decisions/adr03-single-modular-workflow.md)
- A copy-based bootstrap mechanism any project can use to install the
  workflow into `.ai/workflow/` — shipped as `LAAW/sync-workflow.sh`
- Evolve core workflow mechanics (workbench dir, context-build cleanup,
  sync-context, concurrency-safe planning)

**Boundaries:** Changes to `LAAW/`'s actual content are made in `LAAW/`'s
own checkout and committed to *its own* git history — never absorbed into
this outer repo's commits, and never hand-edited via this repo's
`.ai/workflow/` copy. Not responsible for a project's actual `.ai/`
content once bootstrapped.

**Nature:** This is purely a workflow/framework development workspace —
all content is markdown files and bash scripts. No actual application code.

**History:** This project used to take a different approach —
separately-versioned `full`/`medium`/`lite`/`minimal` profiles, then
`full` plus a planned `Light` — before ADR03 replaced that with the
single modular design. Superseded phases and decisions stay in `.ai/`,
marked as such.
