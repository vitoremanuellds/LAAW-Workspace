# LAAW Revamp — Simplified Design (draft for planning)

Companion to [`revamp-context.md`](revamp-context.md) (the abstract ideas
this must keep). This draft proposes a concrete new design based on the
simplifications decided so far. Working draft — iterate freely.

## Guiding decisions (from the revamp discussion)

1. **No phases.** A phase was just a super-task with subtasks, so: only
   **tasks exist, and a task may have subtasks**.
2. **One context folder.** `constitution`, `context`, and `decisions`
   are all *context* — merge into a single folder. Decisions (ADRs) are
   context files too.
3. **Two gates only:** after *plan task*, after *implement task*.
4. **Simpler statuses**, following from #3.
5. **Guide, not truth.** Task files guide the agent through assigned
   work; they are **not** the source of truth (the code is) and not a
   project-management system. Explicitly *not* spec-driven development:
   a task file can be slightly stale or wrong — the point is direction,
   not contract.

## Proposed structure

```
.ai/
├── workflow/        installed workflow (read-only, synced wholesale)
├── info.md          policy only: mode + per-gate authority (unchanged in spirit)
├── context/         THE one context layer (merged)
│   ├── context.md          mission + techstack + the index table
│   ├── c-{ID}-{name}.md    one file per context item (code description,
│   │                       decision/ADR, architecture, invariants, ...)
│   └── index-*.md          (optional) sub-index tables, only when
│                           context.md's index would grow too big
│                           (exempt from ids — they are indexes)
├── tasks/
│   ├── tasks.md             root index: one row per top-level task
│   │                        (id, name, description, depends-on, status)
│   ├── t{ID}-{name}.md      a task with NO subtasks (a leaf)
│   └── t{ID}-{name}/        a task WITH subtasks (a folder)
│       ├── t{ID}-{name}.md  the parent task — same stem as the folder,
│       │                    same layout as a leaf
│       └── ...              each subtask is its own file, named the
│                            same way (its own id + name); a subtask
│                            with subtasks becomes a folder the same way
└── workbench/       freeform scratch (unchanged in spirit)
```

- `context.md` is a **small index + the mission/techstack core** — the
  first thing an agent reads; everything else is reached by link.
  Small files, links, lazy reading — no single big file. Its index is
  a table (see [Context index](#context-index)).
- **The task folder rule is recursive.** Every task id is a globally
  unique `t{ID}` (see [IDs](#ids)). A leaf task is a single file
  `tasks/t{ID}-{name}.md` — id plus the file's kebab-case name, never
  the bare id. The moment it has subtasks it *becomes a folder*
  `tasks/t{ID}-{name}/` whose `t{ID}-{name}.md` (named after the
  folder) is the
  parent task and whose other entries are its subtasks. A subtask is
  just a task with its own unique id, so it follows the same rule:
  leaf = file, has-subtasks = folder with its own `t{ID}-{name}.md`.
  Context files take the same treatment: `c{ID}-{name}.md`. There is
  no third shape.
- Presence rules collapse: `tasks/` is mandatory; `context/` is
  effectively mandatory (even one small file is enough); `workbench/`
  optional. No more five-axis presence matrix — the axes
  (presence/granularity/locality) survive as: *what you keep in git is
  up to the project* and *a task opts into subtasks or not*.

## IDs

Every **addressable file** — every task file and every context file —
gets a **globally unique id**, so references work without collisions and
without scoped or renumbered ids. **Exempt:** index files
(`context.md`, `tasks.md`, and `index-*.md` sub-indexes) and everything
under `workbench/` — those are not addressable units.

An id has **two components**, in this order:

1. **timestamp** — whole **minutes elapsed since a fixed project epoch**,
   zero-padded to **7 digits**.
2. **random** — **5 random digits** (`00000`–`99999`), to break ties
   between ids minted in the same minute.

- **Full form:** `<prefix>-xxx-yyyy-zzzzz` — dash-separated for
  readability: the 7-digit timestamp split as **3+4** (`xxx-yyyy`), then
  the 5-digit random (`zzzzz`). e.g. `t005-4321-48213` (task) or
  `c005-4321-48213` (context). The dashes are part of the id — use this
  exact shape everywhere.
- **Prefix:** `t` for tasks, `c` for context. Tasks and context draw
  from independent id spaces. Filenames are `{id}-{name}` — a task's
  folder and parent file share the full stem
  (`t{ID}-{name}/t{ID}-{name}.md`) and a context file is
  `c{ID}-{name}.md` (settled 2026-09-17, workspace context
  `c037-1675-68146`).
- **Ordered by table position.** Every table — `tasks.md` and each
  parent's `Subtasks` table — is sorted by id ascending: a row that
  appears first has a smaller id than every row after it, and since
  filenames are `{id}-{name}`, the files sort the same way. New tasks
  are appended at the end of their table with a freshly minted (and
  therefore largest) id; inserting a row mid-table requires
  renumbering every later row and renaming its files — allowed but
  costly, so append is the default. Settled 2026-09-17, workspace
  context `c037-1693-91765`.
- **Epoch:** a fixed project constant (e.g. `2025-01-01T00:00:00Z`).
  Record it once (in `context.md`) so any agent can compute the
  timestamp. With 7 digits the ceiling is 9,999,999 min ≈ **19 years**
  (2025 → ~2044); the id is minted once and never renumbered or
  re-scoped.
- **Collision math:** the random part is a *per-minute* namespace of 10⁵.
  Two files collide only if they are minted in the same minute *and*
  draw the same 5 digits. With 10–20 concurrent authors that is well
  under 1% per crowded minute, and only if many files land in the same
  minute — accepted, since this is **not** a PM tool and heavy concurrent
  minting is out of scope. One knob if it ever matters: widen the random
  part (6–7 digits → 10⁶+ ≈ never).

## Task model

A **task** is one mechanical unit of work, written small enough that
its spec fits comfortably in a context window.

A task file has this layout, in this order:

```markdown
# <name>
**ID:** t{ID}       **Status:** in-progress

## Description
<what this task is and why — the intent, one short paragraph>

## TL;DR
<the fastest possible orientation to the task — what it does, in a
 line or two, for an agent deciding whether to open the full file>

## Context
### Before
<the knowledge/situation the agent needs to START this task — state of
 the relevant code, constraints, assumptions. Not a work log.>
### After
<the context/understanding this task PRODUCES once implemented — what
 the agent now knows that wasn't obvious before. This is earned
 knowledge, not a record of effort. Propagated to context/ (c-{ID}) if
 it
 is useful beyond this task.>

## In scope
- <the changes this task makes; names the files/areas touched>

## Out of scope
- <what is explicitly NOT touched, and what "done" concretely means>

## Steps
1. <ordered step>
2. <ordered step>
   - <pseudocode here where it helps, otherwise plain prose>

## Validations
- <how to check done — the mechanical checks + the judgment checks>

## Subtasks            ← optional; omit for a leaf task
| id | name | description | depends on | status |
|----|------|-------------|------------|--------|
```

- **Subtasks are their own files, always** — never inline detail. The
  `Subtasks` table in the parent only *indexes* them (one row each);
  the substance lives in a subtask file following the folder rule above.
  The table columns are the task columns: **id, name, description,
  depends on, status.** Rows are id-ascending (see [IDs](#ids)); a
  new subtask is appended at the end of the table.
- **Narrow specs are the anti-hallucination mechanism.** In scope names
  the files touched; out of scope names what "done" concretely means
  and what is left alone. An agent that needs more information than the
  file + its links holds should stop and ask, not invent.
- **Context (Before/After) replaces "handoff."** It is *not* a labor
  log ("what I did / what's next"). It is the **context the task
  established**: Before is what you needed to start; After is what you
  now understand as a result. A resuming agent reads Before+After to
  pick up without replaying history, and After is the candidate for
  promotion into `context/` when it outlives the task. (Optional:
  a single shared `workbench/session.md` for transient cross-task
  session notes that are not yet durable context.)

## Task index (root task folder)

`tasks/tasks.md` is the index of the **root task folder** — one row per
*top-level* task, using the same column shape as a task's subtask table:

| id | name | description | depends on | status |
|----|------|-------------|------------|--------|
| t-01 | ...  | <short> | — | in-progress |

It points at the task's file or folder (`t{ID}-{name}.md` /
`t{ID}-{name}/`); it does
not duplicate their contents. Rows are id-ascending (see [IDs](#ids)). Subtasks are *not* listed here — each
lives only in its parent's subtask table (one status owner per fact).

## Context index

`context.md` opens with the **mission + techstack core inline**, then an
**index table** over the `c-{ID}` files. Mission and techstack are
themselves context — essential to understanding the project, and small
enough to keep inline in `context.md` rather than split out. Every
other context file has its own **id** (`c{ID}`):

| id | name | description | relation | superseded by |
|----|------|-------------|----------|---------------|
| c-{ID} | ... | <short> | c-{ID} | — |

- **Files:** each `c-{ID}-{name}.md` is one unit of context — either a
  general
  description/information about the code (architecture, invariants,
  conventions) or a **decision** (the reason it was made + the approach
  taken). No separate `decisions.md` — decisions are context rows too.
- **relation** names the *other* context file(s) whose information is
  related to this row's (by convention the link is bidirectional: if A
  relates to B, both point at each other).
- **superseded by** names the file that supersedes this one — a
  decision is never deleted, it is superseded by a later `c-{ID}`
  (keeps the supersede-not-delete rule).
- **Lazy reading / size:** the index can **point to another index**
  (`index-*.md`, exempt from ids) if it would grow too big, and always
  points out
  to the individual context files it indexes. Small files, links, no
  big blob.

## Gates & statuses

Gates collapse to two:

| Gate | After | Checks |
|---|---|---|
| `task-review` | plan task (draft) | spec is narrow, in-scope, doable |
| `task-completion-review` | implement task | validate (mech.) then review (judgment) — both kept |

Statuses (one list, tasks and subtasks share the shape):

```
not-started → planned → in-progress → done
(blocked from any active state)
```

- `planned` = draft exists, `task-review` gate pending/passed.
- `in-progress` = approved, implementation underway.
- `done` = implementation complete + `task-completion-review` passed.
- No separate `awaiting-plan-review` / `reviewing` / `blocked-review`
  states — the two gates are transitions, not states.
- **One status per fact, one place:** task rows live in `tasks.md`,
  subtask rows in the task file. `info.md` still holds policy only.

## Teams (many developers)

- **The file-overlap rule is the coordination unit:** work on the
  same file set should not overlap across two `in-progress` tasks —
  the "touches these files" spec line makes conflicts visible before
  they happen. (No owner/assignment field — settled 2026-09-16, see
  LAAW-Workspace context `c037-1650-68133`.)
- **Parallelism comes from subtasks:** a task can be approved as a
  whole while subtasks are picked up by different people/agents.
- **Git is the sync layer:** commit each draft/step; review happens via
  diff, as before. No locks beyond the Owner field.
- **Context (Before/After) matters more in a team:** it is what the
  next person (human or agent) reads before touching the task — and
  where a deviation from the plan gets recorded if it isn't a full
  replan.

## What each principle buys

| Concern | Mechanism |
|---|---|
| Limited context window | small files + index `context.md` + links + "read only this file" rule; Context Before/After instead of session history |
| Hallucination | narrow task specs (files, done-when, out-of-scope); ask-don't-invent rule |
| Teams | owner per task, file-overlap visibility, subtask parallelism, git diff review |
| Not source of truth | task files are guidance; acceptance is checked against the code/behavior, not the doc |
| Not PM tool | no roadmap, no progress metrics, no dependency graph — only what an agent needs to do its assigned task |
| Compressed info | everything small by design; anything long gets split + linked |
| Lazy reading | index files (`context.md`, `tasks.md`) hold only pointers + status |

## Resolved (from the revamp discussion)

- **Subtasks are always separate files**, indexed in the parent's table
  (see the folder rule above).
- **Decisions live in the single `context.md` index** as `c-{ID}` rows
  with `relation` / `superseded by`; there is no standalone
  `decisions.md`.
- **Context (Before/After) lives inside the task file** — the old
  handoff is reframed as earned context, not a labor log. A shared
  `workbench/session.md` remains an optional extra for transient notes
  only.
- **IDs are timestamp+random, globally unique, not scoped.** Every file
  is named `t{ID}-{name}`/`c{ID}-{name}`; a folder and its parent file
  share the full stem (`t{ID}-{name}/t{ID}-{name}.md`); tables are
  id-ascending with append-at-end as the default. No
  scoped/renumbered ids (see [IDs](#ids)).
- **Mission + techstack are context, kept inline** in `context.md` —
  they are essential to understanding the project and small enough not
  to warrant their own files.
- **Deviations create decisions.** Any deviation from an approved plan
  is recorded as a **decision** (`c-{ID}` ADR row) — the deviation
  itself is part of that decision (what changed, why, and the approach
  taken). Replan the task file to match, and the decision row is the
  durable trace. There is no separate "deviation" state or artifact.
- **No orphan-task concept / no planning artifact.** A task with no
  subtasks is just a task in `tasks/`; a *phase* is simply a task with
  subtasks. Planning scope is the parent task's `Steps` + subtask
  table — no extra artifact. **Breaking a prompt into a single task vs.
  task-with-subtasks is the agent's/human's judgment**, made when
  drafting (and revisited at the plan-review gate if the breakdown looks
  off).
- **Skills stay per-operation, with a router.** Keep one skill per
  operation (plan / implement / review / context, ...). In front of them
  sits a **router skill**: the user states what they want in plain
  terms, and the router points the agent to the correct operation skill
  — the user does **not** have to name a skill. This is routing, not a
  fourth skill doing the operation's work.
