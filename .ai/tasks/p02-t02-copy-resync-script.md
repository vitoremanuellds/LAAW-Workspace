# P02-T02 — Draft the copy/re-sync script

## Context

See the owning phase file,
[`../phases/p02-non-submodule-bootstrap-mechanism.md`](../phases/p02-non-submodule-bootstrap-mechanism.md).
This is Plan step 2: the actual install/update mechanism ADR01 decided
on but never built. `LAAW/sync-skills.sh` is the
closest existing precedent — same repo, same self-locating pattern,
same "copy, don't link, and warn the user to re-run after an update"
philosophy — but it only mirrors `skills/` into `.agents/skills/`; this
script generalizes that to the whole workflow content landing in
`.ai/workflow/`.

Depends on P02-T01: the version-stamp file/format this script writes
is decided there, not here.

**Task-level deviation, discovered and fixed during P02-T05's dogfood
run, after this task was already marked complete:** the script's copy
list below originally omitted `sync-skills.sh`. `LAAW/README.md`'s own "Optional: sync skills to
`.agents/skills/`" step documents running `.ai/workflow/sync-skills.sh`
from inside a bootstrapped project — that file has to actually land in
`.ai/workflow/` for that documented step to work, the same as the five
items already listed. Fixed by adding it to the copy list in this
task's own Steps/Files below and in the shipped script; no plan/scope
change beyond correcting this omission.

## Implementation

### Objective

A bash script, `LAAW/sync-workflow.sh`, that installs or re-syncs
`LAAW`'s workflow content into a target project's
`.ai/workflow/`, replacing `git submodule add` as the install step and
`git submodule update --remote` as the update step.

### In scope

- First-time install: target has no `.ai/workflow/` yet.
- Re-sync: target already has a `.ai/workflow/` from a prior run of
  this same script — wholesale-replace its content with the source's
  current state.
- Writing the version-stamp file per P02-T01's ADR, every run.
- A source path argument (defaults to the script's own checkout, same
  as `sync-skills.sh`) and a target project root argument (defaults to
  the current directory).
- Copying `sync-skills.sh` itself into `.ai/workflow/` alongside the
  other five items (added per the deviation note above) — it has to
  land there for `LAAW/README.md`'s own documented
  `.ai/workflow/sync-skills.sh` step to work in a bootstrapped project.

### Out of scope

- Any variant/profile selection menu — superseded by ADR03, per the
  phase file's Context; always copies the one workflow, wholesale.
- Migrating a target project's own `.ai/` content (constitution,
  phases, tasks, decisions) — this script never touches anything under
  a target's `.ai/` besides `.ai/workflow/` itself.
- Updating `LAAW/README.md` or this repo's own docs to
  reference the script — P02-T03/P02-T04.
- Conflict/merge handling for local edits inside a target's
  `.ai/workflow/` — not applicable; nothing is ever supposed to
  hand-edit it (`workflow.md` §3).

### Files to modify

None in this outer repo — this task's own output lives entirely in
`LAAW/`'s checkout, per the phase file's Context
note on where this phase's work happens (its own commit, its own
history, never absorbed into this outer repo's commits).

### Files to create

- `LAAW/sync-workflow.sh` — the script itself.

### Steps

1. Resolve the source directory: default to the script's own directory
   (`$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)`, same as
   `sync-skills.sh`'s `SCRIPT_DIR` pattern), overridable by a first
   positional argument.
2. Resolve the target project root: default to the current working
   directory, overridable by a second positional argument.
3. Validate the source actually looks like a `LAAW`
   checkout (`workflow.md` exists at its root) — fail with a clear
   message otherwise, same defensiveness `sync-skills.sh` applies to
   its own `skills/` source check.
4. Compute the destination: `<target>/.ai/workflow/`.
5. If the destination already exists, remove it first (wholesale
   replace — no partial-merge logic, matching the phase file's
   Requirements: re-sync "replaces `.ai/workflow/`'s content with the
   source's current state").
6. Create the destination and copy `workflow.md`, `skills/`,
   `templates/`, `reference/`, `README.md`, and `sync-skills.sh` from
   source into it.
7. Write the version-stamp file per P02-T01's ADR (path/format as
   decided there) — recording at minimum the source repo and the
   commit SHA the copy was taken from (`git -C <source> rev-parse
   HEAD`, falling back gracefully with a warning if the source isn't
   itself a git checkout — e.g. a tarball extraction — rather than
   hard-failing the whole copy over a metadata nicety).
8. Print a summary: whether this was a fresh install or a re-sync
   (destination existed beforehand or not), and the commit SHA now
   stamped.
9. Make the script executable (`chmod +x`) as part of creating it, same
   as `sync-skills.sh` ships.

### Pseudocode

```
source_dir = arg1 or this script's own directory
target_root = arg2 or current directory
assert workflow.md exists under source_dir, else fail with message

dest = target_root/.ai/workflow
was_existing = dest already exists

if was_existing: remove dest entirely
create dest
copy workflow.md, skills/, templates/, reference/, README.md, sync-skills.sh from source_dir into dest

sha = `git -C source_dir rev-parse HEAD`, or "unknown" with a warning if source_dir isn't a git checkout
write version-stamp file (path/format per P02-T01's ADR) with source repo + sha (+ date)

print "installed" or "re-synced", and the stamped sha
```

### Dependencies

P02-T01 (version-stamp path/format).

### Expected result

Running `LAAW/sync-workflow.sh` with no arguments from
inside a project whose current directory is the project root, pointed
at a `LAAW` checkout, produces a complete
`.ai/workflow/` (or replaces an existing one) plus the version-stamp
file, with no other part of the target's `.ai/` touched.

### Automatic validations

- `LAAW/sync-workflow.sh` exists and is executable.
- Running it against a scratch empty target directory produces
  `.ai/workflow/{workflow.md, skills/, templates/, reference/,
  README.md, sync-skills.sh}` matching the source checkout's content
  (`diff -r`, `.git` excluded, clean) — the phase file's own automatic
  validation.
- Running it a second time against the same scratch target exits `0`
  and the target still matches the source (re-sync path exercised).
- The version-stamp file exists after a run at the path P02-T01's ADR
  specifies, and its recorded SHA matches `git -C <source> rev-parse
  HEAD`.
- Running it against a source directory two different commits apart
  (checkout commit A, run, checkout commit B, run again) produces two
  different stamped SHAs matching each checkout.

### Manual validations

- Review that the script never writes anywhere under the target's
  `.ai/` besides `.ai/workflow/` itself and the version-stamp file's
  own location.
- Review the script's failure messaging for a source that isn't a
  `LAAW` checkout at all — clear enough that a first-time
  user isn't left guessing.
