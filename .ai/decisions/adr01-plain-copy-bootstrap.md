# ADR01 — Bootstrap workflow variants via plain copy, not git submodule

## Decision

Bootstrap a workflow variant into a project's `.ai/workflow/` by
copying its files, not by `git submodule add`. This repo's own
`.ai/workflow/` (containing `full`'s content) was bootstrapped this
way today, as the first proof of the mechanism.

## Context

`Full-Local-Model-Agent-Workflow`'s README documents real submodule
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
  re-running the (not yet built) bootstrap script is how a project
  pulls in a newer variant version; there's no `git submodule update
  --remote` equivalent yet. Designing that re-sync story is in scope
  for P02.
- Loses the "pinned to an exact commit, verifiable via `git -C
  .ai/workflow log`" traceability a submodule gives for free — a
  copy-based bootstrap needs its own way to record which variant and
  version was installed; open question for P02 to resolve.
- `Full-Local-Model-Agent-Workflow/` stays a git submodule of this
  repo, unaffected by this decision — it's this project's actual
  development checkout for the `full` variant, not a bootstrapped
  consumer copy.
