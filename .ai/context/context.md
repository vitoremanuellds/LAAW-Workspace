# Context

## Mission

### What

This repo (`LAAW-Workspace`, renamed from `Local-Model-Agent-Workflow`)
is the meta-project where **LAAW** (Local AI Agents Workflow) is
designed, planned, and developed. It develops **one modular
workflow** — its content lives in
[`LAAW`](../../LAAW/)'s
own checkout — whose weight scales via optional layers rather than via
separately-maintained variants, and a mechanism for bootstrapping it
into a target project's `.ai/workflow/` without a git submodule. See
[`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md)
for the full design.

### Why

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
`.ai/workflow/` was first bootstrapped as a plain copy proving the
mechanism was possible (see
[`adr01-plain-copy-bootstrap.md`](../decisions/adr01-plain-copy-bootstrap.md));
[P02](../phases/p02-non-submodule-bootstrap-mechanism.md) generalized
that into `LAAW/sync-workflow.sh`, the actual
install/re-sync script any project can run instead of `git submodule
add`.

### Who

The repo owner — solo maintenance for now.

### Goals

- Redesign `LAAW/`'s own content
  (`workflow.md`, skills, templates, reference) around the three axes
  in [`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md) —
  developed directly in its own checkout, committed to that repo's own
  history — see Boundaries below.
- A copy-based bootstrap mechanism any project can use to install the
  workflow into `.ai/workflow/` — shipped as
  `LAAW/sync-workflow.sh` (see
  [P02](../phases/p02-non-submodule-bootstrap-mechanism.md)).
- Evolve core workflow mechanics that aren't specific to any one
  layer's weight — a freeform temp/scratch workspace, context-build
  cleanup, git-history-driven context sync, and concurrency-safe
  phase/task planning. Developed directly in
  `LAAW/`'s own checkout, committed to that
  repo's own history — see Boundaries below.

### Boundaries

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

**2026-08-30:** This outer meta-repo itself renamed on GitHub, from
`Local-Model-Agent-Workflow` to `LAAW-Workspace`. Local `origin` remote
repointed to match; the local directory path
(`/home/vitor/Projects/personal/Local-Model-Agent-Workflow`) is
untouched — not requested, and lower-stakes than the submodule
renames above since nothing else references this repo's own directory
name by path the way `LAAW/` is referenced throughout `.ai/`.

**2026-08-30:** [P02](../phases/p02-non-submodule-bootstrap-mechanism.md)
shipped the copy-based bootstrap/re-sync mechanism this project's
second Goal called for: `LAAW/sync-workflow.sh`
installs/re-syncs the workflow into a target project's
`.ai/workflow/`, replacing `git submodule add`/`git submodule update
--remote` as the install/update step, plus a version-stamp file
([ADR04](../decisions/adr04-workflow-version-stamp.md)) restoring the
"which commit is installed" traceability a submodule gave for free.
Variant selection (the "chosen variant" language ADR01 originally used)
doesn't apply — ADR03 already collapsed that into one workflow, so the
script always installs it wholesale. See the phase file for what's
still explicitly out of scope (tagged releases, migrating a consuming
project's own `.ai/` content).

## Techstack

**Content format:** Markdown only — workflow specs, skill definitions
(YAML frontmatter + Markdown body), reference docs, templates. No code
runtime, no build system, no package manager — same convention as
`LAAW`.

**Bootstrap mechanism:** Shell (bash). `LAAW/sync-skills.sh`
was the closest existing precedent — it copies `skills/` to
`.agents/skills/` inside a consuming project.
[P02](../phases/p02-non-submodule-bootstrap-mechanism.md) generalized
that pattern into `LAAW/sync-workflow.sh`: it copies
the workflow's content (`workflow.md`, `skills/`, `templates/`,
`reference/`, `README.md`) wholesale into a target project's
`.ai/workflow/`, replacing `git submodule add`/`git submodule update
--remote` as the install/update step. There's no "chosen variant" to
select — ADR03 already collapsed that into one workflow, so the
script always installs it wholesale. Every run also writes a version-stamp
file beside `.ai/workflow/` (see
[ADR04](../decisions/adr04-workflow-version-stamp.md)).

**Versioning:** Git, one repo for the workflow itself —
`LAAW/` (kept as a git submodule of this
one, since it's this project's actual development checkout, not a
bootstrapped consumer copy) holds the single modular workflow's actual
content, per
[`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md).
There is no per-variant repo to keep in sync anymore — weight is a
function of which optional layers a consuming project turns on, not of
which repo it bootstrapped from. This repo's own `.ai/workflow/`,
bootstrapped today, is itself a plain copy — proof of the target
mechanism, not a submodule.

**Target constraint carried over from `full`:** every variant's own
`workflow.md` (and whatever it reads per operation) must stay usable
inside a small local model's context window (7B–35B, 48k–64k, per
`full`'s own design target) — a "lighter" variant should need *less*
of that budget than `full`, not the same amount reorganized.

## Index

| File | Description | Status | Relations |
|---|---|---|---|
| [full-directory-structure.md](full-directory-structure.md) | Snapshot of LAAW's `.ai/` directory structure, current as of the ADR03/P06 redesign and this workspace's own re-bootstrap | active | related: [c037-2384-22173-workbench-directory.md](c037-2384-22173-workbench-directory.md), [c037-2384-01677-single-modular-workflow.md](c037-2384-01677-single-modular-workflow.md) |
| [purpose.md](purpose.md) | Project purpose, mission, goals, and history — LAAW = Local AI Agents Workflow | active | |
| [architecture.md](architecture.md) | Project architecture: directory layout, key relationships, tech stack, LAAW workflow structure, skills overview | active | related: [purpose.md](purpose.md) |
| [c037-1650-68133-revamp-open-decisions.md](c037-1650-68133-revamp-open-decisions.md) | Decision: revamp open items settled — shipped epoch `2026-01-01T00:00:00Z`, router skill `route`, final template set, no Owner field, workspace new-model pilot | active | related: [architecture.md](architecture.md), c037-1675-68146 |
| [c037-1675-68146-id-name-filenames.md](c037-1675-68146-id-name-filenames.md) | Decision: id'd files are named `{id}-{name}` — task leaf files, folders + parent files, and context files; amends the revamp design's bare-id folder rule | active | related: [c037-1650-68133-revamp-open-decisions.md](c037-1650-68133-revamp-open-decisions.md), c037-1693-91765 |
| [c037-1693-91765-ids-ordered-by-table.md](c037-1693-91765-ids-ordered-by-table.md) | Decision: ids are ordered by table position — tables sorted id-ascending, new rows appended at the end with a fresh id, mid-table insertion renumbers later rows; pilot subtasks renumbered 2026-09-17 | active | related: [c037-1650-68133-revamp-open-decisions.md](c037-1650-68133-revamp-open-decisions.md), [c037-1675-68146-id-name-filenames.md](c037-1693-91765) |
| [c037-2384-96156-plain-copy-bootstrap.md](c037-2384-96156-plain-copy-bootstrap.md) | Decision: bootstrap workflow via copy script, not git submodule — resolves submodule pain; resolved by c037-2384-76968 for version traceability | active | related: [c037-2384-76968-workflow-version-stamp.md](c037-2384-76968-workflow-version-stamp.md) |
| [c037-2384-22173-workbench-directory.md](c037-2384-22173-workbench-directory.md) | Decision: add `.ai/workbench/` as freeform disposable directory; partially superseded by c037-2384-01677 (workbench gitignore carve-out no longer holds) | active | related: [c037-2384-01677-single-modular-workflow.md](c037-2384-01677-single-modular-workflow.md) |
| [c037-2384-01677-single-modular-workflow.md](c037-2384-01677-single-modular-workflow.md) | Decision: replace per-profile repos with one modular workflow (presence/granularity/locality axes); supersedes P01, partially supersedes c037-2384-22173 | active | related: [c037-2384-22173-workbench-directory.md](c037-2384-22173-workbench-directory.md) |
| [c037-2384-76968-workflow-version-stamp.md](c037-2384-76968-workflow-version-stamp.md) | Decision: record installed workflow version as sibling stamp file; resolves c037-2384-96156's version-traceability open question | active | related: [c037-2384-96156-plain-copy-bootstrap.md](c037-2384-96156-plain-copy-bootstrap.md) |
| [c037-2384-72444-id-format.md](c037-2384-72444-id-format.md) | Decision: collision-safe ID format with timestamp + random component for phases, tasks, decisions | active | — |

**Status** is `active` or `superseded`. When an architecture changes,
don't delete the old file — mark it superseded and point to what
replaced it, same as an ADR. Whoever writes or updates a context file
updates its row here in the same step.
