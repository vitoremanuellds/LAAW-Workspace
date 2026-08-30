# P02-T03 — Update `LAAW/README.md`'s bootstrapping/updating sections

## Context

See the owning phase file,
[`../phases/p02-non-submodule-bootstrap-mechanism.md`](../phases/p02-non-submodule-bootstrap-mechanism.md).
This is Plan step 3. `LAAW/README.md` currently
documents `git submodule add` as the install step ("Bootstrapping into
a project") and `git submodule update`/checkout-and-pin as the update
step ("Updating the workflow") — both now superseded by P02-T02's
script. Depends on P02-T02 existing so this task can describe the
script's real name, arguments, and behavior rather than a placeholder.

This task also touches two sections that describe *why* a submodule
was used (`## This repo is only the fixed half`) and the file-manifest
table/tree (`## What's in this repo vs. what's in your project`,
`## This repo's own structure`) — both need the new script added or
reworded so the README stays internally consistent, not just the two
headline sections.

## Implementation

### Objective

`LAAW/README.md` documents `sync-workflow.sh` as the
install and update path; no remaining instruction to run `git
submodule add` against this repo.

### In scope

- Rewriting "## Bootstrapping into a project"'s install step.
- Rewriting "## Updating the workflow" to describe re-running the
  script instead of pinning/resetting a submodule.
- Adding `sync-workflow.sh` to the "## What's in this repo vs. what's
  in your project" table and the "## This repo's own structure" tree,
  alongside the existing `sync-skills.sh` entries.
- Adjusting "## This repo is only the fixed half"'s submodule-specific
  rationale (dirty-submodule risk, `git submodule update --remote`
  behavior) so it still reads correctly once submodule installation is
  no longer the documented path — reframe around why `.ai/workflow/`
  stays untouched by agents, not around submodule mechanics
  specifically, since that reasoning still holds independent of how
  the files got there.

### Out of scope

- Changing anything about `sync-skills.sh` itself or its own section
  of the README (step 3 of "Bootstrapping into a project") — orthogonal
  to this task, still valid as-is.
- This outer repo's own docs (`mission.md`, `techstack.md`, ADR01) —
  P02-T04.
- Removing the `.gitmodules`-based install as an option entirely from
  history/discussion — the README can still mention it existed
  previously if useful context, just not as the recommended path
  going forward. (flexible: whether to keep a one-line historical
  mention at all, or drop it entirely)

### Files to modify

- `LAAW/README.md`

### Steps

1. In "## Bootstrapping into a project," replace the `git submodule
   add <this-repo-url> .ai/workflow` code block with instructions to
   run `sync-workflow.sh` against a local checkout (clone this repo
   somewhere, then run `path/to/LAAW/sync-workflow.sh
   /path/to/your-project`, or `cd` into the checkout and run it with
   the target as an argument) — keep the numbered steps after it
   (AGENTS.md wiring, bootstrapping info.md) unchanged, since those
   don't depend on how the files arrived.
2. In "## Updating the workflow," replace the pin-to-a-commit
   `git -C .ai/workflow checkout <sha>` flow and the "if a submodule
   update leaves things broken" `git submodule deinit`/`add` flow with:
   re-running `sync-workflow.sh` against the same target re-syncs it to
   the source checkout's current `HEAD`; if you want to review changes
   before adopting them, check them out at a specific commit in your
   own separate `LAAW` clone first (`git -C
   /path/to/LAAW-clone log`/`checkout <sha>`), then point
   `sync-workflow.sh` at that clone. Keep the "this repo doesn't
   publish tagged releases yet, review before adopting" caution — it
   still applies, just phrased against a script re-run instead of a
   submodule pin.
3. Add a `sync-workflow.sh` row/line next to the existing
   `sync-skills.sh` ones in "## What's in this repo vs. what's in your
   project" and "## This repo's own structure."
4. Reread "## This repo is only the fixed half" and reword only the
   parts that assert the submodule mechanism specifically (the
   dirty-submodule and `--remote` failure modes) — keep the part
   explaining *why* `.ai/workflow/` must stay agent-write-free, since
   that reasoning is independent of install mechanism.
5. Read the whole README once more front-to-back after editing —
   confirm no other section still assumes a submodule install (e.g.
   "How it works, briefly" or elsewhere) went unnoticed.

### Dependencies

P02-T02 (script's real name/arguments/behavior to describe accurately).

### Expected result

A newcomer following `LAAW/README.md` top to bottom
ends up running `sync-workflow.sh`, never `git submodule add`, and the
rest of the README (manifest table, structure tree, rationale section)
stays consistent with that.

### Automatic validations

- `grep -n "git submodule add" LAAW/README.md` returns
  nothing.
- `grep -n "sync-workflow.sh" LAAW/README.md` finds it in
  at least the bootstrapping section, the updating section, the
  manifest table, and the structure tree (4+ occurrences).

### Manual validations

- Review "## This repo is only the fixed half" reads coherently after
  the reword — does it still make the case for why `.ai/workflow/`
  isn't hand-edited, without leaning on submodule-specific mechanics
  that no longer apply to the recommended path?
- Read the updated "Bootstrapping into a project" section as if seeing
  it for the first time — is it actually clear what to run and where,
  without assuming the reader already has this repo cloned somewhere
  specific?
