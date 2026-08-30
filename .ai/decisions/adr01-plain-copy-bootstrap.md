# ADR01 — Bootstrap workflow variants via plain copy, not git submodule

## Decision

Bootstrap a workflow variant into a project's `.ai/workflow/` by
copying its files, not by `git submodule add`. This repo's own
`.ai/workflow/` (containing `full`'s content) was bootstrapped this
way today, as the first proof of the mechanism.

## Context

`LAAW`'s README documents real submodule
pain: `git submodule update --remote` against a dirty submodule ranges
from refusing to run to silently discarding uncommitted project work;
the repo doesn't publish tagged releases yet, so every update is a
potential breaking change that has to be reviewed and pinned by hand;
and every consuming project needs its own submodule literacy just to
get the workflow files onto disk. This project exists to build lighter
variants aimed at simpler setups — carrying that same submodule
friction forward would work against that goal.

## Alternatives Considered

- Keep `git submodule add` (the status quo for `full`) — rejected: the
  exact failure modes above are what this project is meant to get
  away from.
- A package-manager-style versioned fetch (npm/pip-style dependency) —
  rejected: no existing precedent in this workflow family, and it
  would add a runtime/toolchain dependency this project's techstack
  explicitly avoids (Markdown-only, no build system).

## Consequences

- A bootstrapped copy doesn't automatically track upstream changes —
  [P02](../phases/p02-non-submodule-bootstrap-mechanism.md) built the
  re-sync story: re-running
  `LAAW/sync-workflow.sh` against an
  already-bootstrapped project wholesale-replaces `.ai/workflow/` with
  the source checkout's current state, the copy-based equivalent of
  `git submodule update --remote`.
- Loses the "pinned to an exact commit, verifiable via `git -C
  .ai/workflow log`" traceability a submodule gives for free —
  resolved by
  [ADR04](adr04-workflow-version-stamp.md) (P02-T01):
  `sync-workflow.sh` writes a version-stamp file,
  `.ai/workflow-version`, as a sibling of `.ai/workflow/` on every run,
  recording the source and commit copied from.
- `LAAW/` stays a git submodule of this
  repo, unaffected by this decision — it's this project's actual
  development checkout for the `full` variant, not a bootstrapped
  consumer copy.
