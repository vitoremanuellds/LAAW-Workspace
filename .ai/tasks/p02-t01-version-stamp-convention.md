# P02-T01 — Design and record the version-stamp convention

## Context

See the owning phase file,
[`../phases/p02-non-submodule-bootstrap-mechanism.md`](../phases/p02-non-submodule-bootstrap-mechanism.md),
for full background. This task is Plan step 1 there: a plain copy of
`LAAW`'s content loses the "pinned to a commit, verifiable via `git -C
.ai/workflow log`" traceability a submodule gives for free
([ADR01](../decisions/adr01-plain-copy-bootstrap.md)'s Consequences).
This task designs the replacement — a marker the eventual script
(P02-T02) writes on every bootstrap/re-sync — and records the decision
as an ADR, since it's a phase-level design call future work (and the
script itself) needs to know.

Two constraints from the phase file bound the design:

- `workflow.md` §3 already treats `.ai/workflow/` as "submodule, never
  written to" (a human/agent editing convention) — the stamp is
  written only by the install/re-sync script itself, never hand-edited,
  so it doesn't violate that in spirit even if it technically lives
  under `.ai/workflow/`.
- It must work without `.ai/workflow/` being a git checkout in the
  target project (the whole point of not using a submodule) — so the
  stamp has to be a plain file the script writes, not something that
  relies on `git log` inside `.ai/workflow/` itself.

## Implementation

### Objective

Decide what the version-stamp file records and exactly where it lives,
write the ADR, and leave the phase file (and this task) referencing it
— no code yet, that's P02-T02.

### In scope

- Choosing the stamp's file name/location (inside `.ai/workflow/` as
  the one exception to "never written to," since it's install
  metadata rather than workflow content — or, if that reads as too
  much of a stretch on review, a sibling path like
  `.ai/.workflow-version` just outside it).
- Choosing its content/format: at minimum the source repo and the
  commit SHA copied from; a human-readable date is a reasonable
  addition, since it costs nothing and helps a reader who doesn't want
  to resolve a SHA by hand.
- Writing the ADR itself.

### Out of scope

- Writing the script that produces the stamp — P02-T02.
- Any notion of semantic version numbers or tags — `LAAW`
  doesn't publish releases yet (per ADR01), so the stamp records a
  commit identifier, not a version string.

### Files to modify

- `.ai/decisions/decisions.md` — add this ADR's index row.

### Files to create

- `.ai/decisions/adr{NN}-{name}.md` (next sequential ADR number after
  the current highest in `decisions.md` — ADR03 is the latest as of
  this task's drafting, so this is very likely ADR04, but check
  `decisions.md` fresh rather than assuming) — using
  `.ai/workflow/templates/adr-template.md`'s shape. Decision: the
  stamp file's exact path, its field set, and that it's written
  unconditionally on every bootstrap and every re-sync (never
  hand-edited, never merged). Context: the two constraints above and
  ADR01's Consequences. Alternatives considered should include at
  least the "inside `.ai/workflow/`" vs. "sibling path outside it"
  choice, with a reasoned pick between them.

### Steps

1. Read `.ai/decisions/decisions.md` for the next available ADR
   number.
2. Decide the stamp's path and format per the two constraints above.
3. Write the ADR file and its `decisions.md` index row.
4. Add one sentence to this phase's own Context section in
   `.ai/phases/p02-non-submodule-bootstrap-mechanism.md` pointing at
   the new ADR, next to the existing ADR01/ADR03 links, so a later
   reader lands on the decision without re-deriving it.

### Dependencies

None — first task in the phase's dependency chain.

### Expected result

A committed ADR stating exactly what the version stamp records and
where it lives, ready for P02-T02 to implement against without making
its own design call mid-script.

### Automatic validations

- `.ai/decisions/decisions.md` has a new row for this ADR, Status
  `valid`.
- The new ADR file exists at `.ai/decisions/adr{NN}-{name}.md` and
  follows `adr-template.md`'s section shape (Decision, Context,
  Alternatives Considered, Consequences).

### Manual validations

- Review that the chosen stamp location and format are actually
  sufficient for P02-T02 to implement without further design
  decisions — no open question left dangling.
