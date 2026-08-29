# ADR02 — Add `.ai/workbench/` as a freeform, disposable directory

## Decision

Add `.ai/workbench/` as a new top-level directory under `.ai/`: no
fixed file schema, no `info.md`/`roadmap.md` pointer into it, not part
of the permanent record. Human and agent can create/edit ad hoc
Markdown files there freely — planning notes, scratch Q&A, prompt
drafts, tool notes — same way a table gets covered in loose papers.

`build-context-full`'s two ephemeral outputs (`context.temp.md`,
`build-plan.md`) move from `.ai/context/` into `.ai/workbench/`. Once
`build-context.iterate` empties its read queue, those two files are
deleted by default — no per-run human confirmation — since the whole
point of `.ai/workbench/` is that nothing in it is load-bearing once
its content has been reconciled elsewhere. Workbench files stay
git-tracked (committed, then later deleted in a follow-up commit),
consistent with everything else under `.ai/` — no gitignore carve-out.

## Context

Two of the user's requests, both about the same missing piece: (1) a
place for informal working files that today have nowhere sanctioned to
live — every existing `.ai/` subdirectory (`context/`, `phases/`,
`tasks/`, `decisions/`) is part of the permanent record, with its own
schema and Status tracking; (2) `build-context-full`'s temp files
currently live inside `.ai/context/` itself, alongside real content,
and today's cleanup step ("ask the human whether to archive or
delete") adds a manual step to every context-build run for files
nobody actually wants to keep.

## Alternatives Considered

- Keep `context.temp.md`/`build-plan.md` inside `.ai/context/`, just
  rename them more clearly as temp — rejected: doesn't solve request
  (1) at all, and still mixes disposable and permanent content in one
  directory.
- Gitignore `.ai/workbench/` instead of committing it — rejected: the
  user's own framing ("a table where I can place a lot of papers and
  tools") implies this is meant to be visible to and shared with a
  teammate or a later session, not purely local scratch; an
  uncommitted file is invisible to anyone else and to `sync-context`
  (P04), which reads git history.
- Keep the "ask before deleting" step for `build-context-full`'s temp
  files even after the move — rejected: that step exists in
  `workflow.md` §9 to protect the *permanent record* from unilateral
  deletion; once these files live in a directory whose entire purpose
  is disposability, the same caution no longer applies.

## Consequences

- `build-context-full/SKILL.md`, `context-temp-template.md`, and
  `context-build-plan-template.md` all need their copy-target paths
  updated from `.ai/context/` to `.ai/workbench/` — P03's Plan step 3.
- `workflow.md` §3 and `reference/directory-and-links.md` need to
  document `.ai/workbench/` as a directory no skill reads as an input
  requirement — an agent doing "read only what the current task needs"
  (§1) should never treat `.ai/workbench/` content as authoritative.
- Any *other* skill that later grows its own temp output can reuse
  `.ai/workbench/` without a new ADR — this decision establishes the
  convention, not a `build-context-full`-specific exception.
