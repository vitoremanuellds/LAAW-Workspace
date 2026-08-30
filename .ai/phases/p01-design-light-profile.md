# P01 — Design the `Light` workflow profile

**Superseded 2026-08-29 by
[ADR03](../decisions/adr03-single-modular-workflow.md):** `Light` as a
separately-versioned repo/profile is retired in favor of one modular
workflow with optional layers. No further work proceeds under this
phase. Its successor (redesigning `LAAW/`'s
content around ADR03) is planned under a new phase ID — this file is
kept for history, not reused.

## Context

First of the mission's original two goals (see
[`mission.md`](../constitution/mission.md#goals)) — `mission.md`'s own
`[ASSUMPTION]` note flagged "which specific profile(s) to bring back"
as unresolved; that's now answered (see `mission.md`'s 2026-08-29
note and the working notes this phase grew out of,
[`.ai/workbench/p01-profile-planning.md`](../workbench/p01-profile-planning.md)
while it still exists — freeform, disposable, safe to delete once this
phase file is reviewed).

**Resolved scope, from the user directly:**
- One profile, designed fresh (not reviving `medium`/`lite`/`minimal`) —
  named **`Light`**. Its repo already exists and is registered as a
  submodule of this meta-repo: `Light-Local-Model-Agent-Workflow/`
  (currently just a `README.md`).
- Target user: **a solo developer**, not a team. Core loop, in the
  user's own words: "a way of gathering context from the application,
  plan the tasks he was assigned, and implement it" — plus a
  workbench. Tasks are *assigned* to this dev externally (a ticket, a
  request), not self-authored from a roadmap.
- **The defining constraint:** Light's own working artifacts do not go
  into git — "it only serves him," no team needs the audit trail
  `full`'s commit-per-gate discipline exists for. This isn't a smaller
  version of `full`'s artifact hierarchy; it's a different premise —
  §1's Plan step 1 has to resolve exactly what that means in practice.
- Inherits `full`'s current mechanics as a starting point (P03's
  workbench convention now, `sync-context`/concurrency later once
  P04/P05 land) rather than forking from a pre-P03 baseline — but see
  Out of scope below on what that does and doesn't commit this phase
  to right now.

**Same location discipline as every phase touching a variant's actual
content (established the hard way in P03-T01 — see `mission.md`'s
Boundaries): everything this phase's Plan produces is written in
`Light-Local-Model-Agent-Workflow/`'s own checkout and committed to
*its own* git history — never this repo's `.ai/` tree, and never
`.ai/workflow/` (that's `full`'s frozen copy, unrelated to `Light`).**
`LAAW/` is this phase's reference pattern
(shape to adapt, not to copy) for what a variant's `workflow.md` +
`skills/` + `templates/` + `reference/` looks like — read it for
structure, don't reuse its ceremony wholesale.

Context-window target carried over from `techstack.md`: `full`'s own
`workflow.md` (+ whatever each operation reads) targets 7B–35B models,
48k–64k context. `Light` should need measurably *less* of that budget,
not the same amount reorganized.

## In scope

- Resolving how (or whether) `Light`'s own working artifacts are
  stored: git-tracked-but-local, gitignored, or not file-based as
  versioned records at all.
- Designing `Light`'s reduced operation set — gather context, plan an
  assigned task, implement it — as its own skills, with a workbench
  convention adapted from P03.
- Designing `Light`'s gate policy (expected to be minimal-to-none: one
  person is both author and approver).
- Writing `Light-Local-Model-Agent-Workflow/`'s actual content:
  `workflow.md`, `skills/*/SKILL.md`, `templates/`, `reference/` as
  needed — sized for the reduced operation set, not a trimmed copy of
  `full`'s files.

## Out of scope

- Any second or third profile (`medium`/`lite`/`minimal` or otherwise)
  — deliberately one profile for this phase; a future phase if the
  need for another actually materializes.
- The copy-based bootstrap mechanism that installs a variant into a
  consuming project's `.ai/workflow/` — P02 (not yet planned).
- Backporting any of `Light`'s design choices into `full` — `full`
  stays independently maintained
  ([`mission.md`](../constitution/mission.md#boundaries)).
- Actually building `Light`'s `sync-context`/concurrency equivalents —
  those land in `full` via P04/P05 first; this phase doesn't block on
  either landing, and doesn't need to design `Light`'s version of them
  yet. Revisit once P04/P05 ship.
- Team-oriented features generally — `Light` is explicitly a
  single-user tool; P05's concurrency work targets `full`, not `Light`.

## Requirements

- A single, explicit, ADR-recorded answer for how `Light`'s working
  artifacts are stored — no longer an open question.
- `Light` has a documented operation set covering gather-context,
  plan-assigned-task, and implement, each with real procedure detail
  (not just names) — same rigor as a `full` skill file, far less
  ceremony.
- `Light`'s gate policy is explicit, even if "none" — not left
  implicit.
- `Light-Local-Model-Agent-Workflow/workflow.md` (+ whatever each
  operation reads) is measurably lighter than `full`'s own, per
  `techstack.md`'s carried-over context-window target.
- Every file this phase produces lives in
  `Light-Local-Model-Agent-Workflow/`'s own checkout, committed to its
  own git history.

## Plan

1. Design (ADR) how `Light`'s own working artifacts are stored —
   resolve git-tracked-but-local vs. gitignored vs. not
   versioned-as-files at all. This decision shapes every later step,
   so it comes first.
2. Design `Light`'s operation set and gate policy: confirm the exact
   boundary between gather-context / plan-task / implement (three
   skills, or does gather-context fold into plan-task?), whether a
   workbench-equivalent directory is part of it, and what if any
   review checkpoint exists between them.
3. Scaffold `Light-Local-Model-Agent-Workflow/`'s file layout —
   `workflow.md`, `skills/`, and `templates/`/`reference/` only where
   the reduced operation set actually needs them (don't create empty
   ceremony directories `full` has that `Light` doesn't need).
4. Write `Light-Local-Model-Agent-Workflow/workflow.md`: artifact
   storage convention (step 1), the operation set and gate policy
   (step 2), commit discipline (or the lack thereof, if step 1 lands
   on not-versioned).
5. Write each skill file under
   `Light-Local-Model-Agent-Workflow/skills/`.
6. Check `Light`'s `workflow.md` (+ per-operation reads) against
   `full`'s own size as a baseline — confirm it's measurably lighter,
   not just reorganized.

## Automatic validations

- `Light-Local-Model-Agent-Workflow/workflow.md` exists.
- Every skill named in Plan step 2 has a matching
  `Light-Local-Model-Agent-Workflow/skills/*/SKILL.md`.
- `wc -w Light-Local-Model-Agent-Workflow/workflow.md` is meaningfully
  lower than `wc -w LAAW/workflow.md`.
- `git -C Light-Local-Model-Agent-Workflow log --oneline` shows this
  phase's commits, separate from this outer repo's and from `full`'s.

## Manual validations

- Walk through the solo-dev loop by hand using only `Light`'s own
  docs — gather context on a small fixture, plan a made-up assigned
  task, implement it — without reaching for any of `full`'s heavier
  machinery to fill a gap.
- Review that the ADR from Plan step 1 actually delivers "doesn't go
  into the git repo, as it only serves him," not just a smaller
  version of `full`'s commit-every-draft discipline.

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
