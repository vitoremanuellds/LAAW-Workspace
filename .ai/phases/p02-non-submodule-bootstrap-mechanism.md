# P02 — Non-submodule bootstrap mechanism

## Context

Part of the mission's second goal (bootstrap mechanism — see
[`mission.md`](../constitution/mission.md#goals)).

**The script and doc updates this phase's Plan produces are `LAAW`'s
own content, edited in `LAAW/`'s own checkout and
committed to *its own* git history — never this repo's `.ai/workflow/`
copy, which stays a frozen bootstrap snapshot (see `mission.md`'s
Boundaries; P03-T01 got this wrong once and was corrected — don't
repeat it here).** Below, `workflow.md`, `skills/`, `templates/`,
`reference/`, and `README.md` all mean the copies under `LAAW/`.

[ADR01](../decisions/adr01-plain-copy-bootstrap.md) already decided
*that* bootstrapping happens by plain copy instead of `git submodule
add`, and this repo's own `.ai/workflow/` (most recently re-copied by
hand in the commit that redid it post-P06) is proof the copy itself
works. What doesn't exist yet is the actual mechanism — ADR01's
Consequences flagged three things explicitly left for this phase:

- The copy script itself. `LAAW/sync-skills.sh`
  is the closest existing precedent (per
  [`techstack.md`](../constitution/techstack.md)) but only mirrors
  `skills/` into `.agents/skills/` — this phase generalizes that
  pattern to the whole workflow (`workflow.md`, `skills/`,
  `templates/`, `reference/`, `README.md`) landing in a target
  project's `.ai/workflow/`.
- A re-sync story — today, pulling in a newer version means hand-
  redoing what the commit above did manually. There's no `git
  submodule update --remote` equivalent.
- A way to tell which version is installed — a plain copy loses the
  "pinned to a commit, verifiable via `git -C .ai/workflow log`"
  traceability a submodule gives for free.

`LAAW/README.md`'s own "Bootstrapping into a
project" section still literally instructs `git submodule add` today
— it hasn't been updated since ADR01, and does the opposite of what
this project now recommends.

The version-traceability question above is resolved by
[ADR04](../decisions/adr04-workflow-version-stamp.md) (P02-T01): a
plain-text stamp file, `.ai/workflow-version`, written by the script
itself beside `.ai/workflow/` on every bootstrap and re-sync.

**P02-T02 shipped the script as `LAAW/sync-workflow.sh`, taking two
*independent* optional positional arguments — `[source-dir]
[target-root]`, not `sync-skills.sh`'s single-arg convention (which is
always the destination, source always implicit).** Both default
sensibly: source defaults to the script's own directory, target to the
current working directory. The natural invocation from inside a
project you want to bootstrap/re-sync is therefore **zero arguments**,
run via the script's path inside a `LAAW` checkout —
e.g. `cd your-project && ../LAAW/sync-workflow.sh` — not "run the
script's own single argument as the target," which is what P02-T03's
task file drafted before this task actually shipped. P02-T03 should
document the real two-independent-args shape and the zero-arg common
case, not the single-arg assumption its own draft prose used.

One thing has simplified since ADR01's Consequences were written:
[ADR03](../decisions/adr03-single-modular-workflow.md) collapsed the
"per-profile repos" model into one workflow with optional layers.
ADR01's own wording ("copy a chosen variant's entire workflow
content") predates that collapse — there is no variant to choose
between anymore, so this phase's script has no selection menu to
design; it always installs the one workflow, wholesale. (Choosing
which of *this project's own* optional `.ai/` layers —
constitution/context/decisions/phases/workbench — to scaffold is a
separate, already-solved concern: the existing
[`bootstrap` skill](../workflow/skills/bootstrap/SKILL.md), which
this phase's script doesn't touch or duplicate.)

## In scope

- A bash script in `LAAW/`'s own checkout
  (parallel to `sync-skills.sh`) that copies `workflow.md`, `skills/`,
  `templates/`, `reference/`, and `README.md` from a `LAAW` checkout
  into a target project's `.ai/workflow/` — the first-time install
  path, replacing `git submodule add`.
- The same script's re-sync path: re-running it against an
  already-bootstrapped `.ai/workflow/` replaces its content wholesale
  with the source's current state. Safe by construction — `.ai/`'s own
  directory structure (`workflow.md` §3) already treats
  `.ai/workflow/` as never hand-edited, so there's no local-edit case
  to merge or preserve.
- A version-stamp convention recording which `LAAW` commit is
  currently installed, restoring the traceability ADR01 noted a
  submodule gives for free.
- Updating `LAAW/README.md`'s "Bootstrapping into
  a project" and "Updating the workflow" sections to document the
  script as the install/update step, in place of `git submodule add`.
- Updating this repo's own `mission.md` (Why/Goals),
  `techstack.md` (Bootstrap mechanism note), and ADR01's Consequences
  to reflect the mechanism as shipped rather than "not yet built."

## Out of scope

- Choosing which of a project's own optional `.ai/` layers
  (constitution/context/decisions/phases/workbench) to scaffold —
  already owned by the existing
  [`bootstrap` skill](../workflow/skills/bootstrap/SKILL.md); this
  phase's script only ever touches `.ai/workflow/` itself.
- Any variant-selection menu (`full` vs. `Light` vs. anything else) —
  superseded by ADR03; the script always installs the one workflow.
- Publishing tagged/semver releases of `LAAW` —
  version-stamping records a commit identifier, not a release
  process; ADR01's "no tagged releases yet" pain point stands as a
  separate, still-open concern this phase doesn't resolve.
- Migrating a consuming project's own `.ai/` content (constitution,
  phases, tasks, decisions) to match schema changes a newer `LAAW`
  version introduces — stays a manual, case-by-case job, same as this
  repo's own most recent re-bootstrap was. This phase's script is
  scoped to `.ai/workflow/` only, never a project's own content
  layers.
- Conflict resolution or merge logic for local edits inside
  `.ai/workflow/` — not applicable, since nothing is ever supposed to
  hand-edit it in the first place.

## Requirements

- A project with no `.ai/workflow/` yet ends up with a complete one
  (`workflow.md` + `skills/` + `templates/` + `reference/` +
  `README.md`) by running one script against a `LAAW`
  checkout — no `git submodule add` step involved.
- Re-running that script later against an already-bootstrapped project
  updates `.ai/workflow/` to match the source's current state, without
  touching anything else under that project's `.ai/`.
- After bootstrapping or re-syncing, it's possible to determine which
  `LAAW` commit is currently installed without
  `.ai/workflow/` itself being a git repository.
- `LAAW/README.md`'s "Bootstrapping into a project"
  and "Updating the workflow" sections describe the script — not `git
  submodule add` — as the install/update path.
- This repo's `mission.md`, `techstack.md`, and ADR01 describe the
  mechanism as shipped, referencing this phase.

## Plan

1. Design and record (ADR) the version-stamp convention: what gets
   recorded (source, commit SHA, date), and where it lives relative to
   `.ai/workflow/`'s "never written to" contract (`workflow.md` §3) —
   e.g. a marker written by the script itself only, never hand-edited,
   whether that lives inside `.ai/workflow/` or just outside it as a
   sibling. Written on both first bootstrap and every re-sync.
2. Draft the script in `LAAW/`'s checkout (name
   and exact location decided during drafting, parallel to
   `sync-skills.sh`): given a source `LAAW` checkout path (default:
   the script's own directory, same self-locating pattern
   `sync-skills.sh` already uses) and a target project root (default:
   current directory), copy `workflow.md`, `skills/`, `templates/`,
   `reference/`, `README.md` into `<target>/.ai/workflow/`,
   wholesale-replacing existing content on rerun, then write the
   version stamp from step 1.
3. Update `LAAW/README.md`'s "Bootstrapping into
   a project" and "Updating the workflow" sections to document the
   script as the install/update step, removing the `git submodule
   add` instruction.
4. Update this repo's own `mission.md` (Why/Goals),
   `techstack.md` (Bootstrap mechanism note), and ADR01's Consequences
   to reflect the mechanism as shipped, referencing this phase.
5. Dogfood: run the new script against this repo's own project root
   (source = the already-checked-out
   `LAAW/` submodule) and confirm it
   reproduces `.ai/workflow/`'s current content unchanged — proof
   against a real target that was, until now, only ever bootstrapped
   by hand.

## Automatic validations

- The script exists in `LAAW/`'s checkout, is
  executable, and running it with no arguments against a scratch
  target directory produces `.ai/workflow/{workflow.md, skills/,
  templates/, reference/, README.md}` matching the source checkout's
  content (`diff -r`, `.git` excluded, clean).
- Running it a second time against the same target (re-sync) exits
  successfully and the target still matches the source.
- A version-stamp marker exists after a run, and its recorded value
  changes between two runs when the source checkout's HEAD commit
  changes in between.
- Running it against this repo's own project root reproduces the
  current `.ai/workflow/` tree with no diff (the Plan step 5 dogfood
  check).

## Manual validations

- Review that the script never writes anywhere under a target
  project's `.ai/` besides `.ai/workflow/` itself.
- Review the version-stamp convention against `workflow.md` §3's
  "submodule, never written to" wording for `.ai/workflow/` — confirm
  the stamp reads as the script's own install metadata rather than a
  violation of that rule, or place it outside `.ai/workflow/` if that
  reads cleaner.
- Review `LAAW/README.md`'s updated bootstrapping
  section for a newcomer's first read — does it still hold together
  with no submodule step at all?

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
| P02-T01 | Design and record the version-stamp convention | Restore traceability of which `LAAW` commit is installed, without `.ai/workflow/` being a git repo | — | complete |
| P02-T02 | Draft the copy/re-sync script | The actual install/update mechanism, generalizing `sync-skills.sh` | P02-T01 | complete |
| P02-T03 | Update `LAAW/README.md`'s bootstrapping/updating sections | Document the script as the install/update path, replacing `git submodule add` | P02-T02 | complete |
| P02-T04 | Update this repo's mission/techstack/ADR01 | Reflect the mechanism as shipped rather than "not yet built" | P02-T02, P02-T03 | awaiting-plan-review |
| P02-T05 | Dogfood the script against this repo's own project root | Prove the mechanism against a real, previously hand-bootstrapped target | P02-T02 | awaiting-plan-review |
