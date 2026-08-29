# P01 planning notes — which lighter profile(s)?

Scratch space for working out P01 ("Design lighter workflow
profile(s)") before drafting the actual phase file via `define-phase`.
Disposable — delete or fold into the phase file once this converges.

## Known constraints (from mission.md / techstack.md)

- `full` used to ship `medium`/`lite`/`minimal` alongside `full`, then
  dropped to `full`-only because maintaining several profiles in one
  repo made every workflow change multiply across all of them.
- This project's whole point is developing lighter variants as their
  own independently-scoped repos/copies instead.
- Target constraint carried over from `full`: every variant's
  `workflow.md` (+ whatever it reads per operation) must fit inside a
  small local model's context window (7B–35B, 48k–64k) — a lighter
  variant should need *less* of that budget than `full`, not the same
  amount reorganized.
- mission.md's own `[ASSUMPTION]` note flags this as unresolved: "which
  specific profile(s) to bring back — lite? minimal? something new?"

## [QUESTION] How many profiles, and named what?

Options as I see them:
- Revive the old names (`medium`, `lite`, `minimal`) as-is.
- Design one new profile from scratch, informed by what actually made
  `full` heavy, rather than assuming the old three-tier split still
  makes sense.
- Something in between — e.g. one lighter profile now, more later if
  actually needed.

## [QUESTION] What actually makes a profile "lighter"?

Candidate levers, not mutually exclusive:
- Fewer distinct skills/operations (e.g. merge phase+task planning
  into one skill for small projects).
- Fewer gates (e.g. skip phase-review, keep only constitution- and
  task-review).
- No separate task files — inline task detail directly in the phase
  file.
- Shorter `workflow.md` itself (less prose, fewer cross-references).
- Drop artifact types entirely (e.g. no ADRs, no `context/` survey
  step) for projects too small to need them.

## [QUESTION] Does the lighter profile inherit P03/P04/P05, or fork from pre-P03 full?

If it forks from `full`'s current state, it inherits `.ai/workbench/`,
and (once built) `sync-context` and concurrency-safe planning too. If
those are judged "full-only" complexity, the lighter profile might
deliberately omit some of them.

## [QUESTION] Where does the new profile's source content live?

`full` lives in its own repo (`Full-Local-Model-Agent-Workflow/`,
submodule of this one). Does the lighter profile get the same
treatment (own repo, own submodule), or does it start life inside this
meta-repo directly and get extracted once it stabilizes?
