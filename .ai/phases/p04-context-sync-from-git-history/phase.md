# P04 — Context sync from git history

## Context

Part of the mission's third goal (workflow-mechanics evolution — see
[`mission.md`](../constitution/mission.md#goals)).

**Every file this phase's Plan touches is `full`'s actual source
content, edited in `LAAW/`'s own checkout
and committed to *its own* git history — never this repo's
`.ai/workflow/` copy, which stays a frozen bootstrap snapshot (see
`mission.md`'s Boundaries; P03-T01 got this wrong once and was
corrected — don't repeat it here).** Below, `workflow.md`, its skills,
and `reference/` all mean the copies under
`LAAW/`.

The workflow already has two context sub-operations (`workflow.md`
§9): `build-context` (survey an existing codebase from scratch)
and `propagate-context` (promote what a just-completed task/phase
learned). Neither covers a third case: an agent picking work back up
after the repo moved on without it going through either of those
paths — a human edited files directly, a teammate merged their own
work, or another agent/session made commits — and needing to know what
changed before trusting its own view of `.ai/context/` or the active
phase file's Context section.

Answering "what changed since I last looked" requires knowing which
commit *this agent* last made, which nothing in the workflow currently
records — `workflow.md` §12 (commit discipline) says only that each
skill's own commit step states what to stage, with no agent-identity
convention at all. This phase has to design that convention before the
skill itself can work.

## In scope

- A commit convention that tags a commit as made by a given agent
  identity (e.g. a trailer such as `Agent: <name-or-id>`), extending
  `workflow.md` §12 — decided via ADR, since it changes something
  every commit-writing skill touches.
- A new skill, `sync-context`: given `.ai/info.md`'s current Active
  phase/task, locate the last commit carrying this agent's identity
  trailer, diff it against HEAD, and reconcile anything relevant into
  the correct artifact level (phase file's Context, or `.ai/context/`)
  — following the exact same promotion rule `propagate-context`
  already uses, never skipping past it.
- The "no prior commit from this agent identity" case (first run, or a
  new agent joining an existing repo).
- Adding `sync-context` to `workflow.md` §2's operation table.

## Out of scope

- Resolving conflicts between concurrent edits, or any locking/claim
  mechanism — that's [P05](p05-concurrency-safe-phase-task-planning.md)'s
  job; this phase only detects and reports drift, using existing
  human/agent judgment to reconcile it once found.
- Real-time or background watching — `sync-context` is invoked
  on-demand (e.g. at the start of a session, or after a merge), not a
  daemon.
- Changing what `build-context` or `propagate-context` themselves
  do — `sync-context` is a third, additive sub-operation invoked
  between them when drift is suspected, not a replacement for either.

## Requirements

- A commit made by an agent following this workflow is identifiable as
  such, without changing the format of a human-authored commit.
- Given the current `.ai/info.md` Active phase/task, `sync-context`
  can enumerate everything that changed since the last commit *this*
  agent identity made — scoped to the whole repo if no phase/task is
  active, narrower otherwise.
- Drift that matters gets reconciled into the correct level (phase
  Context vs. `.ai/context/`), per `workflow.md` §9 — never written to
  `.ai/context/` directly by this skill for a
  phase-scoped fact, same restriction `propagate-context.task` already
  has.
- `sync-context/SKILL.md` exists with the same Can/Must/Cannot
  frontmatter shape as every other skill.

## Plan

1. Design and record (ADR) the agent-identifier commit convention:
   where the identity string comes from (e.g. a field the human sets
   once in `.ai/info.md`, vs. a fixed per-agent-tool default), and
   exactly what marks a commit as this agent's own (trailer key,
   placement) — must not require changing every other skill's own
   commit-step wording beyond a one-line reference.
2. Update `workflow.md` §12 (Commit discipline) to reference the new
   convention from step 1.
3. Draft `LAAW/skills/sync-context/SKILL.md`:
   inputs (`.ai/info.md`, `git log`), procedure (locate this agent's
   last commit → diff to HEAD → scope by Active phase/task → reconcile
   per §9), Can/Must/Cannot contract, output — same shape as every
   other skill file in `LAAW/skills/`.
4. Add a `sync-context` row to `workflow.md` §2's operation table.
5. If the "locate last commit by this agent, per scope" logic needs a
   worked example beyond what fits in the skill file itself, add one
   to `reference/`.

## Automatic validations

- `LAAW/skills/sync-context/SKILL.md`
  exists; its frontmatter has `name` and `description` fields matching
  the shape of every sibling skill file.
- `LAAW/workflow.md` §2's table includes a
  `sync-context` row.
- Against a fixture repo with a synthetic agent-tagged commit history:
  running the skill's commit-location logic correctly identifies the
  last commit carrying the test agent's identity trailer and lists the
  correct diff set since it.

## Manual validations

- Review that `sync-context`'s reconciliation step routes through the
  same promotion rule as `propagate-context`, rather than introducing
  a second, inconsistent path to `.ai/context/`.
- Review the ADR's identifier convention against the case where a
  human commits under the same author identity the agent tooling
  itself would use — does the convention still distinguish them?

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
