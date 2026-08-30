# ADR04 — Record the installed workflow version as a sibling stamp file

## Decision

The copy-based install/re-sync script (P02-T02) writes a plain-text
metadata file at `.ai/workflow-version` — a sibling of `.ai/workflow/`,
not inside it — on every run, fresh install and re-sync alike:

```
source=<path or URL of the LAAW checkout copied from>
commit=<full commit SHA of that checkout at copy time>
date=<ISO 8601 date of this run>
```

It is written only by the script, never hand-edited or merged — the
same "generated, not authored" status `.ai/workflow/` itself already
has, just placed one level up so `.ai/workflow/` stays a byte-for-byte
mirror of the source checkout with nothing appended to it.

## Context

[ADR01](adr01-plain-copy-bootstrap.md)'s Consequences flagged that a
plain copy loses the "pinned to a commit, verifiable via `git -C
.ai/workflow log`" traceability a submodule gives for free, and left
resolving that as an open question for
[P02](../phases/p02-non-submodule-bootstrap-mechanism.md). This is
P02-T01, called for by the phase file's own Plan step 1. Two
constraints from that phase file bound the design:

- `workflow.md` §3 already treats `.ai/workflow/` as "submodule, never
  written to" — a human/agent editing convention this stamp shouldn't
  strain even though it's the install mechanism, not a person, writing
  something related to that directory.
- It has to work without `.ai/workflow/` being a git checkout in the
  target project — the entire point of not using a submodule — so the
  record has to be a plain file the script itself writes, not
  something derived from `git log` inside `.ai/workflow/`.

## Alternatives Considered

- A stamp file inside `.ai/workflow/` itself (e.g.
  `.ai/workflow/VERSION`) — rejected: it would still read as install
  metadata rather than workflow content, but it breaks the property
  that `.ai/workflow/`'s tree is byte-identical to the source
  checkout. That property is worth keeping — P02-T02's own planned
  automatic validation compares the two with `diff -r` and expects it
  clean; a stamp living inside would force that comparison (and any
  future one) to special-case one file forever.
- Recording it inside `.ai/info.md` — rejected: ADR03 already narrowed
  `info.md` to Policy-only, explicitly removing its prior role as a
  status pointer. Putting install provenance back in would partially
  reverse that and mix two unrelated concerns — gate authority and
  install metadata — in one file.
- A JSON or YAML metadata file — rejected: this project's techstack is
  Markdown/shell only, no build tooling or parsers in play
  (`techstack.md`). Plain `key=value` lines read exactly as easily for
  a human and are trivial for the bash script itself to write and
  later re-read, with no parsing dependency to add.
- Deriving install provenance from the target project's own git
  history (e.g. blame on `.ai/workflow/` files) — rejected: that's
  exactly the traceability a plain copy doesn't have, which is the
  problem this ADR exists to solve. Nothing in the target's own
  history says where the files came from unless something writes it
  down explicitly.

## Consequences

- P02-T02's script must write `.ai/workflow-version` on every run
  (fresh install and re-sync alike), populating `commit` via `git -C
  <source> rev-parse HEAD` — falling back to `unknown` with a warning,
  rather than failing the whole copy, if the source isn't itself a git
  checkout (e.g. a tarball extraction).
- `.ai/workflow/` stays a pure mirror of the source checkout — no
  file-level exclusions needed when comparing the two.
- A target project can tell which `LAAW` commit is
  installed by reading one small file, without `.ai/workflow/` needing
  to be its own git repository — the traceability ADR01 noted a
  submodule gives for free.
- If `.ai/workflow-version` is deleted or gitignored, the record is
  lost until the next re-sync. Acceptable: it's regenerable by
  re-running the script, the same disposable, script-owned status
  `.ai/workflow/`'s own content already has.
