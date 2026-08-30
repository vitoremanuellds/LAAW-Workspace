# P02-T05 — Dogfood the script against this repo's own project root

## Context

See the owning phase file,
[`../phases/p02-non-submodule-bootstrap-mechanism.md`](../phases/p02-non-submodule-bootstrap-mechanism.md).
This is Plan step 5, and the phase's own dogfood validation: this
repo's `.ai/workflow/` was, until now, only ever bootstrapped/re-synced
by hand (most recently in the commit that redid it post-P06). Running
the real script against this repo's own project root, with source =
the already-checked-out `LAAW/` submodule, is the proof
that the mechanism actually reproduces what hand-editing did.

Depends on P02-T02 (the script must exist).

## Implementation

### Objective

Run `LAAW/sync-workflow.sh` against this repo's own
project root and confirm `.ai/workflow/` ends up identical to its
current (hand-bootstrapped) content, plus the new version-stamp file.

### In scope

- Running the script for real, once, against this repo.
- Verifying the resulting `.ai/workflow/` matches what's already
  there (no unexpected diff — the whole point is this repo's copy is
  already current, so a re-sync should be a no-op on content).
- Committing the version-stamp file this run produces (the one
  genuinely new artifact) as this repo's own regular tracked content
  under `.ai/workflow/`, if P02-T01's ADR places it there — or wherever
  the ADR placed it if outside `.ai/workflow/`.

### Out of scope

- Any content changes to `.ai/workflow/` itself — if the script
  produces a diff against what's currently checked out, that's a bug
  in P02-T02 to fix, not something this task papers over or accepts.
- Re-running this after every future `LAAW` change — this
  is a one-time proof for this phase, not a new standing habit
  (whether to adopt the script as this repo's own regular update path
  going forward is a separate, later call, not part of this task).

### Files to modify

None directly by hand — whatever the script itself writes
(`.ai/workflow/`'s content, unchanged if the dogfood succeeds; the new
version-stamp file, genuinely new).

### Steps

1. From this repo's project root, run
   `LAAW/sync-workflow.sh` `.` (or
   `LAAW/sync-workflow.sh` with no target argument, if
   P02-T02 defaults the target to the current directory) — source
   defaults to the script's own directory, which is exactly the
   checked-out `LAAW/` submodule already sitting in this
   repo.
2. Run `git status` and `git diff` scoped to `.ai/workflow/` — expect
   no content diff (this repo's copy is already current post the last
   manual re-bootstrap), only the new version-stamp file appearing as
   untracked/added.
3. If any unexpected diff shows up, treat it as a P02-T02 bug (fix the
   script, don't hand-patch the output) rather than closing this task.
4. Stage and commit the version-stamp file (and nothing else, unless
   step 3 required a genuine content fix) with a message noting this
   is the phase's dogfood run.

### Dependencies

P02-T02.

### Expected result

`.ai/workflow/` is byte-identical to its pre-run state; the only new
file is the version stamp, committed.

### Automatic validations

- `git diff --stat .ai/workflow/` (excluding the new stamp file) shows
  no changes after running the script.
- The version-stamp file exists at the path P02-T01's ADR specifies and
  its recorded SHA matches `git -C LAAW rev-parse HEAD`.

### Manual validations

- Confirm the run's console output correctly reported this as a
  re-sync (destination already existed), not a fresh install, per
  P02-T02's own summary output.
