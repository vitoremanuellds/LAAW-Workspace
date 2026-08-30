# P02-T04 — Update this repo's mission/techstack/ADR01

## Context

See the owning phase file,
[`../phases/p02-non-submodule-bootstrap-mechanism.md`](../phases/p02-non-submodule-bootstrap-mechanism.md).
This is Plan step 4. Three places in *this* repo (not
`LAAW/`) currently describe the bootstrap mechanism as
future work rather than something that exists:

- `mission.md`'s Why section: "This repo's own `.ai/workflow/` was
  bootstrapped today as a plain copy instead — proof of the mechanism
  this project exists to generalize."
- `mission.md`'s Goals: "Design and ship a copy-based bootstrap
  mechanism any project can use to install the workflow into
  `.ai/workflow/`" (phrased as a goal still to do).
- `techstack.md`'s Bootstrap mechanism note: "The bootstrap mechanism
  this project builds generalizes that pattern" (future tense).
- [ADR01](../decisions/adr01-plain-copy-bootstrap.md)'s Consequences:
  "re-running the (not yet built) bootstrap script... Designing that
  re-sync story is in scope for P02" and "open question for P02 to
  resolve" (version traceability).

Depends on P02-T02 and P02-T03: this task references the script's real
name and the updated README by name, so it should land after both
exist.

## Implementation

### Objective

`mission.md`, `techstack.md`, and ADR01 describe the bootstrap
mechanism as shipped, pointing at `LAAW/sync-workflow.sh`
and this phase, instead of describing it as future work.

### In scope

- `mission.md`'s Why paragraph and Goals list.
- `techstack.md`'s Bootstrap mechanism note.
- ADR01's Consequences section (its two "not yet built" /
  "open question for P02" bullets).
- A dated note in `mission.md`'s running log (matching the existing
  style of its `**2026-08-2X:**` entries) recording that P02 shipped.

### Out of scope

- `LAAW/README.md` itself — P02-T03.
- Rewriting ADR01's Decision/Context/Alternatives sections — only
  Consequences changes; the decision it recorded (plain copy over
  submodule) is unaffected by this phase actually building the
  mechanism.
- Touching `phases.md`'s own Status column for P02 — that's
  `implement-task`'s/this task-table's own bookkeeping per
  `workflow.md`, not something a task's *content* edits.

### Files to modify

- `.ai/constitution/mission.md`
- `.ai/constitution/techstack.md`
- `.ai/decisions/adr01-plain-copy-bootstrap.md`

### Steps

1. In `mission.md`'s Why section, change "was bootstrapped today as a
   plain copy instead — proof of the mechanism this project exists to
   generalize" to reflect that the generalized mechanism now exists
   (name it, `LAAW/sync-workflow.sh`), referencing P02.
2. In `mission.md`'s Goals, reword the bootstrap-mechanism goal from a
   forward-looking "design and ship" to reflect it's done, or move its
   substance into a dated log entry the way other resolved
   goals/decisions in this file already are (flexible: exact
   phrasing/placement, as long as a reader can tell it's complete
   without cross-referencing `phases.md`).
3. Add a dated note (today's date) to `mission.md`'s running log,
   mirroring the existing `**2026-08-2X:**` entries' style, stating P02
   shipped the copy-based bootstrap/re-sync mechanism and pointing at
   the phase file.
4. In `techstack.md`'s Bootstrap mechanism note, change "The bootstrap
   mechanism this project builds generalizes that pattern" to past
   tense, naming `sync-workflow.sh` directly.
5. In ADR01's Consequences, update the two bullets that call the
   script "not yet built" / flag open questions "for P02 to resolve" —
   state what P02 actually decided (pointing at P02-T01's ADR for the
   version-stamp specifics rather than duplicating it).

### Dependencies

P02-T02, P02-T03.

### Expected result

Reading `mission.md`, `techstack.md`, and ADR01 without also reading
`phases.md` or the phase file, a reader correctly concludes the
bootstrap mechanism exists and where to find it.

### Automatic validations

- `grep -n "not yet built" .ai/decisions/adr01-plain-copy-bootstrap.md`
  returns nothing.
- `grep -rn "sync-workflow.sh" .ai/constitution/ .ai/decisions/adr01-plain-copy-bootstrap.md`
  finds at least one hit in each of `mission.md`, `techstack.md`, and
  ADR01.

### Manual validations

- Review that the Goals/Why rewording doesn't overstate what shipped
  (e.g. doesn't claim tagged releases or migration tooling this phase
  explicitly left out of scope).
