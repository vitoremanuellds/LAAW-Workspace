# IDs are ordered by table position

**ID:** c037-1693-91765
**Status:** decided 2026-09-17, during task-review of t037-1693-02727
**Relation:** c037-1650-68133, c037-1675-68146



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Decision](#decision)
  - [Consequences](#consequences)
  - [Consequence (2026-09-17)](#consequence-2026-09-17)

</details>
## Decision

Every task table — `tasks.md` and each parent task's `Subtasks`
table — is sorted by id ascending: a row that appears first has a
smaller id than every row appearing after it. Because filenames are
`{id}-{name}`, the files in `tasks/` sort in the same order as their
tables.

## Consequences

- New tasks/subtasks are **appended at the end** of their table with
  a freshly minted (current, therefore largest) id.
- Inserting a row mid-table requires renumbering every later row and
  renaming the affected files — a deliberate, recorded exception to
  "ids are minted once and never renumbered". Prefer appending.
- The 5-digit random part still serves same-minute disambiguation; it
  no longer carries a "no ordering guarantee" disclaimer.

## Consequence (2026-09-17)

The pilot renumbered the nine subtasks of
[t002-7178-75813](../tasks/t002-7178-75813-revamp-laaw-repo/t002-7178-75813-revamp-laaw-repo.md)
in table order:

| old id | new id | name |
|--------|--------|------|
| t002-7178-26058 | t037-1693-02727 | new-id-system |
| t002-7178-76890 | t037-1693-16386 | rewrite-workflow-md |
| t002-7178-97526 | t037-1693-17315 | rewrite-core-skills |
| t002-7178-47657 | t037-1693-28735 | rewrite-context-skills |
| t002-7178-08279 | t037-1693-50470 | add-router-skill |
| t002-7178-70147 | t037-1693-59324 | update-reference-docs |
| t002-7178-80074 | t037-1693-63951 | update-templates |
| t002-7178-69484 | t037-1693-66263 | update-readme |
| t002-7190-44432 | t037-1693-73540 | crossplatform-python-sync-scripts |

The parent task keeps its own id — it was minted before the
subtasks, so it is already smaller than all of them, which the rule
requires.
