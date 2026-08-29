# P05 — Concurrency-safe phase/task planning

## Context

Part of the mission's third goal (workflow-mechanics evolution — see
[`mission.md`](../constitution/mission.md#goals)).

**Every file this phase's Plan touches is `full`'s actual source
content, edited in `Full-Local-Model-Agent-Workflow/`'s own checkout
and committed to *its own* git history — never this repo's
`.ai/workflow/` copy, which stays a frozen bootstrap snapshot (see
`mission.md`'s Boundaries; P03-T01 got this wrong once and was
corrected — don't repeat it here).** Below, `workflow.md`,
`reference/status-and-info.md`, `info-template.md`, and every skill
named all mean the copies under `Full-Local-Model-Agent-Workflow/`.

Two things about the current workflow assume a single worker at a
time. First, `workflow.md` §11: `.ai/info.md`'s Status section tracks
exactly one `Active phase` and one `Active task` — a single global
fast pointer, cleared and reset by `propagate-context`. A team means
multiple humans/agents may each have a different phase or task
genuinely in flight at once, each needing their own "what am I on"
pointer without overwriting anyone else's. Second, ID assignment
(`P{NN}`, `P{NN}-T{NN}`) is sequential and never reused (`workflow.md`
§3, §11): two contributors independently running
`define-phase`/`define-task-full` around the same time could each pick
the same next ID before either commits, a collision that only shows up
at merge/push time.

The Depends-on graph already exists and is already the documented
mechanism for "what can run in parallel" (§11) — this phase doesn't
invent that concept, it makes the rest of the workflow actually able
to act on it with more than one worker present: a way to claim an
unblocked item before starting it, and a mechanical way to resolve an
ID collision when two contributors' branches both claim the same
next ID.

## In scope

- A redesigned `.ai/info.md` Status schema that can represent more
  than one simultaneously active phase/task, attributed to whoever
  (which human or agent identity) claimed each.
- A claim/release convention: how a contributor marks a Depends-on-clear
  phase/task as theirs before starting it, and clears that when done
  or abandoned.
- An ID-collision resolution convention: what happens when two
  branches each independently assigned the same next ID, discovered
  at merge time (which one renumbers, and how that renumbering is
  tracked so nothing silently points at a stale ID).
- Updating `workflow.md` §5, §11, `reference/status-and-info.md`, and
  `info-template.md` to the new schema and conventions.
- Updating every skill that reads/writes `.ai/info.md`'s Status
  section (`define-phase`, `define-task-full`, `implement-task-full`,
  `propagate-context`, and `create-constitution-full`'s bootstrap
  step) to the new schema — none left writing the old single-pointer
  shape.

## Out of scope

- Any git-hosting or PR-workflow-specific integration (branch-per-task
  conventions, CI checks) — stays a plain Markdown/commit-based
  convention, not tied to GitHub/GitLab specifics.
- Real-time locking or a server component — no new runtime dependency;
  consistent with the project's Markdown-only, no-build-system
  techstack ([`techstack.md`](../constitution/techstack.md)).
- `sync-context` itself — [P04](p04-context-sync-from-git-history.md)
  is what reconciles a given agent's view of the repo; P05 only makes
  concurrent state representable in the first place.

## Requirements

- `.ai/info.md` can represent multiple concurrently active phases/tasks,
  each attributable to who claimed it.
- Two contributors working the roadmap/a phase file at the same time
  can each tell, from Depends-on + Status alone, which items are safe
  to claim without colliding with the other's in-flight work.
- The next-ID assignment convention has a documented, mechanical
  resolution path for a collision discovered at merge time — always
  renumbering the later-merged item, never the earlier one.
- Every skill that touches `.ai/info.md`'s Status section is updated
  to the new schema — verified by grep, not left to drift.

## Plan

1. Design (ADR) the multi-pointer `.ai/info.md` schema and the
   claim/release convention.
2. Design (same ADR, or a second one if the two decisions turn out
   independent enough to version separately) the ID-collision
   resolution convention.
3. Update `workflow.md` §5 (Lifecycle & gates) and §11 (Status) for
   the new schema and conventions.
4. Update `reference/status-and-info.md` with a worked example of two
   contributors claiming different items concurrently, and a worked
   example of the collision-resolution path.
5. Update `info-template.md` to the new Status section shape.
6. Update `define-phase`, `define-task-full`, `implement-task-full`,
   `propagate-context`, and `create-constitution-full`'s bootstrap
   step — every place that reads or writes the old single `Active
   phase`/`Active task` pointer — to the new schema.

## Automatic validations

- `grep -rn "Active phase\|Active task" Full-Local-Model-Agent-Workflow/`
  (run from this repo's root) — every remaining match uses the new
  schema's field names; none of the old singular-pointer shape
  survives outside historical ADR text.
- `info-template.md` reflects the new Status section shape.

## Manual validations

- Walk through a 2-contributor scenario by hand — two phases claimed
  concurrently, one task claimed under each — and confirm nothing in
  the new schema forces serializing the two.
- Review that the collision-resolution convention is mechanical enough
  to follow without a judgment call beyond "which one renumbers."

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
