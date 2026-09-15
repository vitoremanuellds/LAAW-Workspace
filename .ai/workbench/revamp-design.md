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
│   ├── context.md          mission + techstack + index of the rest
│   ├── decisions.md        index of decisions
│   ├── adr-NN-*.md         one file per decision
│   └── *.md                architecture / invariants / whatever fits
├── tasks/
│   ├── tasks.md             index: every task, one row, status + owner
│   └── t-NN-*.md            task files (may define subtasks)
└── workbench/       freeform scratch (unchanged in spirit)
```

- `context.md` is a **small index + the mission/techstack core** — the
  first thing an agent reads; everything else is reached by link.
  Small files, links, lazy reading — no single big file.
- Presence rules collapse: `tasks/` is mandatory; `context/` is
  effectively mandatory (even one small file is enough); `workbench/`
  optional. No more five-axis presence matrix — the axes
  (presence/granularity/locality) survive as: *what you keep in git is
  up to the project* and *a task opts into subtasks or not*.

## Task model

A **task** is one mechanical unit of work, written small enough that
its spec fits comfortably in a context window.

Task file, compressed:

```markdown
# t-NN-name
**Status:** in-progress
**Owner:** (who/which agent, if a team)
**Spec:**            ← narrow, precise (anti-hallucination)
  - touches exactly these files/areas
  - inputs, expected output, done-when (acceptance)
  - out of scope
**Subtasks:**        ← optional; none = task is its own subtask
  | # | what | status |
  |---|------|--------|
  | 1 | ...  | done   |
**Handoff:**        ← last session's state, ≤ few lines
  last: <what's done, what's next, gotchas>
```

- **Subtasks** are table rows in the task file — like the old
  phase-task table, but owned by the task. A subtask that outgrows a
  row gets its own file linked from the row. Task ≈ old phase file;
  subtask ≈ old task file. Nothing else changes conceptually.
- **Narrow specs are the anti-hallucination mechanism.** A task file
  must name the files it touches, what "done" concretely looks like,
  and what is out of scope. An agent that needs more information than
  the file + its links holds should stop and ask, not invent.
- **Handoff section is the session-persistence mechanism.** When a
  session ends mid-task, the agent leaves ≤ a few lines: what's done,
  what's next, gotchas. A new session starts by reading the task file —
  enough to resume without replaying history. (Optional: a single
  shared `workbench/session.md` for cross-task session notes.)

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

- **Assignment is the coordination unit:** `Owner` field in the task
  row. Rule: one owner per task at a time; work on the same file set
  should not overlap across two `in-progress` tasks — the "touches
  these files" spec line makes conflicts visible before they happen.
- **Parallelism comes from subtasks:** a task can be approved as a
  whole while subtasks are picked up by different people/agents.
- **Git is the sync layer:** commit each draft/step; review happens via
  diff, as before. No locks beyond the Owner field.
- **Handoff lines matter more in a team:** they are what the next
  person (human or agent) reads before touching the task.

## What each principle buys

| Concern | Mechanism |
|---|---|
| Limited context window | small files + index `context.md` + links + "read only this file" rule; handoff lines instead of session history |
| Hallucination | narrow task specs (files, done-when, out-of-scope); ask-don't-invent rule |
| Teams | owner per task, file-overlap visibility, subtask parallelism, git diff review |
| Not source of truth | task files are guidance; acceptance is checked against the code/behavior, not the doc |
| Not PM tool | no roadmap, no progress metrics, no dependency graph — only what an agent needs to do its assigned task |
| Compressed info | everything small by design; anything long gets split + linked |
| Lazy reading | index files (`context.md`, `tasks.md`) hold only pointers + status |

## Open questions

1. **Subtask files:** worth allowing subtasks to become their own files,
   or keep subtasks strictly as table rows (force the task to be split
   into two tasks instead)?
2. **`context.md` contents:** mission + techstack + index inline (as
   proposed), or mission/techstack as their own files linked from
   `context.md`? (Inline keeps it to one read; linked keeps the file
   smaller. Tension between two of our own rules.)
3. **Decisions index:** keep a `decisions.md` index, or list decisions
   in `context.md`'s index section too (one index to rule them all)?
4. **Orphan tasks vs. tasks:** with phases gone, every task is flat in
   `tasks.md`. Does "planning scope" (the old phase plan) need *any*
   artifact, or is it just a task with a coarse spec and no subtasks
   yet?
5. **Handoff location:** inside the task file (one per task) vs. a
   single shared session file (one per project)?
6. **Bootstrap/skills:** do we keep the skill-per-operation shape, or
   collapse to fewer skills (e.g. plan / implement / review /
   context)?
7. **Deviations:** with no phase layer, where does "work diverged from
   plan" land? Simplest: replan the task file + note in handoff;
   ADR only if architecturally significant. Confirm.
