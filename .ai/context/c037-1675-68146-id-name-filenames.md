# Filenames are `{id}-{name}`

**ID:** c037-1675-68146
**Name:** id-name-filenames
**Relation:** c037-1650-68133, c037-1693-91765
**Superseded by:** —

Every id'd file in the new model is named `<id>-<name>` — the
globally-unique id followed by the file's kebab-case name, never the
bare id:

- Leaf task: `tasks/t{ID}-{name}.md`
- Task with subtasks: folder `tasks/t{ID}-{name}/` whose parent file
  is `t{ID}-{name}.md` (same stem as the folder); subtask files
  follow the same rule recursively
- Context item: `context/c{ID}-{name}.md`

Set by the user on 2026-09-17 during task-review of
t002-7178-26058, amending the revamp design's bare-id folder rule
(`t{ID}/t{ID}.md`) before implementation starts. Consequences:

- `name` is the file's name column in its index (`tasks.md`,
  `context.md`, or a parent's Subtasks table), kebab-case. Index
  files (`tasks.md`, `context.md`, `index-*.md`) and `workbench/`
  remain id-exempt, as before.
- The id keeps its fixed shape (`t`/`c` + 3-4-5 digit groups), so it
  is an unambiguous filename prefix: a minted id is *taken* if any
  sibling entry's name starts with `{id}-`. Collision checks in
  `tools/generate-id.py --dir` use this rule.
- The workspace's pilot files were renamed in place to the new shape
  (`t002-7178-75813-revamp-laaw-repo/` + parent file,
  `t002-7178-26058-new-id-system.md`,
  `c037-1650-68133-revamp-open-decisions.md`). Legacy pre-id
  context files (`purpose.md`, `architecture.md`,
  `full-directory-structure.md`) — `purpose.md` deleted as
  redundant with context.md; `architecture.md` and
  `full-directory-structure.md` re-id'd to
  `c037-2477-14840-architecture.md` and
  `c037-2477-58211-full-directory-structure.md`.

Relation: c037-1650-68133 — the pilot-scope decision whose folder
shape this amends; nothing here touches its epoch/router/template
settled items.
