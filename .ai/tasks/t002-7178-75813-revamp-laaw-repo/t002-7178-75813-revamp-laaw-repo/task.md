# Revamp the LAAW repo to the simplified design

**ID:** t002-7178-75813       **Status:** done

## Description

Rewrite the LAAW repository (the workflow source, currently at
`LAAW/` in this workspace — remote `vitoremanuellds/LAAW`) so it
implements the simplified design in
[revamp-design.md](../../workbench/revamp-design.md): one context
folder instead of three, tasks-with-subtasks instead of phases, two
gates, the new status list, the new dash-separated timestamp+random
ids, and a router skill in front of the per-operation skills.
Everything this task touches is the *workflow definition* — no
project files. The LAAW-Workspace's own `.ai/` tree is **not**
migrated here; that is a follow-up task that consumes this one's
output.

## TL;DR

Replace LAAW's workflow.md, all 9 skills, 5 reference files, 7
templates, the id tool, README, and both sync scripts with the
revamped single-process design; validate by syncing into a scratch
project and grepping for stale concepts.

## Context

### Before

- Current LAAW checkout (clean `main`, commit `e9e4485`): `workflow.md`
  (269 lines), `skills/` (9 skills: bootstrap, build-context,
  create-constitution, define-phase, define-task, implement-task,
  propagate-context, review-work, validate-work), `reference/` (5
  files), `templates/` (7 files), `tools/` (`generate-id.py`, `.epoch`),
  `sync-workflow.sh`, `sync-skills.sh`, `README.md`.
- **ID format is currently in flux:** `tools/generate-id.py` implements
  the *old* base-36 8-char format (ADR05-era), while the workspace's
  ADR08 and the revamp design both specify the *new* format: 7-digit
  zero-padded minutes since a fixed epoch, split 3+4, dash-separated,
  plus 5 random digits, prefix `t`/`c` — full form `t{xxx-yyyy-zzzzz}`.
  The revamp design supersedes both; this task implements the design
  format and records the superseding decision.
- `tools/.epoch` = `2026-08-28 01:27:20 -0300` (= `2026-08-28
  04:27:20 UTC`). The revamp design says the epoch is a *project*
  constant recorded once in the project's `context.md`; for LAAW
  itself, `tools/.epoch` remains the shipped default the generator
  reads.
- `sync-workflow.sh` copies `workflow.md`, `skills/`, `templates/`,
  `reference/`, `README.md`, `sync-skills.sh` — it does **not** copy
  `tools/` or `.epoch`, so projects can't mint ids after install.
  Must be fixed.
- Both sync scripts are **bash** — POSIX-only (shebangs, `set -euo
  pipefail`, `$(...)`, `dirname`); they don't run on stock Windows.
  The revamp makes them cross-platform by rewriting them in Python
  (the repo already ships a Python tool in `tools/`).
- The revamp design left a few things deliberately open (epoch value
  for LAAW's own minting, router skill name, exact template set).
  **Resolved 2026-09-16 at step 0** — recorded as a decision in this
  project's `context/` (new model, per the decision itself):
  [c037-1650-68133](../../context/c037-1650-68133-revamp-open-decisions.md).
- **Filenames amended 2026-09-17** (during task-review of
  t037-1693-02727): every id'd file is named `{id}-{name}` — the
  unique id plus the file's kebab-case name — for task leaf files,
  folders with parent files, and context files alike; the design
  doc's bare-`t{ID}` folder rule is amended, not restated. Settled
  as [c037-1675-68146](../../context/c037-1675-68146-id-name-filenames.md).
- **IDs are ordered by table position** (settled 2026-09-17): every
  task table sorts id-ascending; new rows are appended at the end
  with a freshly minted (largest) id; mid-table insertion requires
  renumbering later rows (a recorded exception to "minted once, never
  renumbered"). This pilot's nine subtasks were renumbered in table
  order accordingly —
  [c037-1693-91765](../../context/c037-1693-91765-ids-ordered-by-table.md).

### After

*(filled in at completion — what implementation established that
wasn't obvious before, candidate for promotion to context/)*

## In scope

Only the LAAW repo (`LAAW/`). Files/areas touched:

- `tools/generate-id.py`, `tools/.epoch` — new id format.
- `workflow.md` — full rewrite to the revamped process.
- `skills/` — rewrite 7, add 1 (router), remove 1 (`define-phase`).
- `reference/` — rewrite all 5 files to the new model.
- `templates/` — rewrite/replace to the settled set of 7 (step 7).
- `sync-workflow.sh` → `tools/sync-workflow.py`, `sync-skills.sh` →
  `tools/sync-skills.py` — rewritten in Python and moved into `tools/`
  alongside the id generator, cross-platform (Windows, macOS,
  Linux), shipping the whole `tools/` folder (incl. `.epoch`), new
  skill set, no bash dependency.
- `README.md` — rewrite to the new design.

## Out of scope

- Migrating LAAW-Workspace's own `.ai/` tree (phases→tasks,
  context merge, etc.) — follow-up task consuming this one.
- Updating this workspace's `AGENTS.md` / `.ai/info.md` — they will
  reference stale paths and are updated by the migration task.
- Any change to LAAW's git history, remotes, or release/publishing.
- Backward compatibility with old ids/statuses/layers — none required.
- Changes to `.gitignore` beyond what the layout needs.
- "Done" concretely means: a fresh project synced from the new LAAW
  has a coherent, self-consistent workflow (no phase/constitution/
  three-gate residue), mints ids per the new format, and every skill
  maps to the two-gate lifecycle.

## Steps

0. **Settle the open design decisions** — *resolved 2026-09-16*,
   recorded in [c037-1650-68133](../../context/c037-1650-68133-revamp-open-decisions.md):
   (a) shipped default epoch `2026-01-01T00:00:00Z`; (b) router skill
   named `route`; (c) final template set per step 7. All subtasks may
   proceed.
1. **New id system** (t037-1693-02727): rewrite `generate-id.py` to
   emit `<prefix>{xxx-yyyy-zzzzz}` (prefix `t`|`c`, 7-digit minutes
   since epoch split 3+4, dash-separated, 5-digit random; `--count N`
   mints N ids in the same minute, same-minute namespace); keep
   `--epoch` override; `.epoch` as default source, now
   `2026-01-01T00:00:00Z`; add a collision check against the target
   directory when minting filenames.
2. **Rewrite `workflow.md`** (t037-1693-16386): new §3 structure
   (`context/`, `tasks/` with the recursive folder rule, `workbench/`);
   two gates (`task-review`, `task-completion-review`) replacing the
   five; status list `not-started → planned → in-progress → done`
   (+`blocked`); ids per the design (globally unique, minted once,
   index/workbench exempt); deviations recorded *as decisions*;
   context flows into the single `context/`; teams: file-overlap rule
   and git-as-sync (**no Owner field**); drop all phase language,
   constitution-review, context-update gate.
3. **Rewrite core skills** (t037-1693-17315): `define-task` (new task
   file layout exactly as the design; recursive folder rule — leaf =
   `tasks/t{ID}-{name}.md`, has-subtasks = `tasks/t{ID}-{name}/` with
   parent file `t{ID}-{name}.md` (per c037-1675-68146); subtask table
   columns id/name/description/depends
   on/status; no phase link, no orphan concept), `implement-task`,
   `validate-work`, `review-work` (each re-anchored to the two
   gates). Delete `skills/define-phase/`.
4. **Rewrite context skills** (t037-1693-28735): `create-constitution`
   (scaffolds `info.md` + `context/context.md` with inline
   mission/techstack core + index table), `build-context` (fills
   `c-{ID}.md` items), `propagate-context` (single-folder
   promote/finalize; no phase-file routing), `bootstrap` (new layer
   menu).
5. **Add the router skill** (t037-1693-50470): `skills/route/` —
   plain-language request → points to the operation skill; routing
   only, does no operation work.
6. **Update `reference/`** (t037-1693-59324): `status-and-info.md`
   (new statuses, one-place rule), `directory-and-links.md` (new
   structure + folder rule), `scaffold-on-first-use.md` (context.md /
   tasks.md / workbench), `starting-without-a-plan.md` (tasks instead
   of phases), `reread-skill-discipline.md` (router-aware).
7. **Update `templates/`** (t037-1693-63951) to the settled set of 7:
   new `task-template.md` (exact design layout) and new
   `context-item-template.md` (`c-{ID}` shape, incl. decision shape
   with relation/superseded-by); update `context-template.md` (now the
   `context.md` index: mission + techstack inline + index table),
   `info-template.md`, `workbench-readme-template.md`,
   `context-build-plan-template.md`; rename
   `context-temp-template.md` → `assumptions-template.md` (the
   assumptions file for ground-up context building); remove
   `adr-template.md` and `decisions-template.md` (decisions are
   context rows now).
8. **README** (t037-1693-66263): rewritten to the new design (one
   context layer, tasks+subtasks, two gates, router).
9. **Cross-platform Python sync scripts** (t037-1693-73540): replace
   `sync-workflow.sh` and `sync-skills.sh` with
   `tools/sync-workflow.py` / `tools/sync-skills.py` (moved into
   `tools/` next to `generate-id.py`; installed projects get them at
   `.ai/workflow/tools/`) — same behavior (wholesale install/re-sync
   into `.ai/workflow/`, version stamp, skills mirror into
   `.agents/skills/`), plus: ships `tools/` (incl. `.epoch`); uses
   `pathlib`/`shutil` only, no bash, no POSIX-only calls; resolves
   source/target paths the same way on Windows, macOS, and Linux;
   git invoked only via `subprocess` for the version stamp (tolerate
   absent git, as today); the two old `.sh` files are deleted, not
   kept alongside.
10. **Validate** (see Validations) — mechanical pass first, then
    judgment review at the completion gate. Commit each subtask's
    result to `LAAW/` `main` locally (one commit per subtask); never
    push, don't touch remotes or publishing.

## Validations

Mechanical:
- `python3 tools/generate-id.py` emits `t{xxx-yyyy-zzzzz}` matching
  `^t\d{3}-\d{4}-\d{5}$` (and `c` prefix); `--count 5` returns 5
  unique ids in the same minute; `--epoch` override works.
- `python3 -m py_compile tools/sync-workflow.py tools/sync-skills.py tools/generate-id.py`;
  run `python3 tools/sync-workflow.py` into a scratch dir →
  `.ai/workflow/tools/` contains `sync-workflow.py`, `sync-skills.py`,
  `generate-id.py`, and `.epoch`, and `generate-id.py` runs from the
  *installed* copy. No POSIX-only constructs in the Python (no
  `os.fork`, hardcoded `/` paths, `shutil`-level only); entry points
  resolvable on Windows (`py -3 tools/sync-workflow.py` /
  `python tools/sync-workflow.py` without a shell), macOS, and Linux.
- Grep the whole LAAW tree for stale concepts — all hits explained or
  gone: `phase` (as a layer), `constitution` (as a folder),
  `awaiting-plan-review|reviewing|complete` (old statuses),
  `adr{NN}|decisions.md` (as a standalone index), base-36/8-char id
  references.
- Every skill named in `workflow.md`'s operation table exists in
  `skills/` and vice versa; `define-phase` is gone; router exists.

Judgment (at `task-completion-review`):
- A fresh agent reading only `workflow.md` + `context.md` of a
  freshly synced scratch project can say what's active, what its gate
  is, and what "done" means — without reading `skills/`.
- The two-gate lifecycle is expressible for the minimal case
  (one leaf task, no subtasks) with zero optional layers.

## Subtasks

| id | name | description | depends on | status |
|----|------|-------------|------------|--------|
| t037-1693-02727 | new-id-system | Rewrite generate-id.py to the dash-separated timestamp+random format; epoch handling | — | done |
| t037-1693-16386 | rewrite-workflow-md | Full rewrite of workflow.md to the two-gate, no-phase, single-context process | t037-1693-02727 | done |
| t037-1693-17315 | rewrite-core-skills | define-task / implement-task / validate-work / review-work; delete define-phase | t037-1693-16386 | done |
| t037-1693-28735 | rewrite-context-skills | create-constitution / build-context / propagate-context / bootstrap for the single context folder | t037-1693-16386 | done |
| t037-1693-50470 | add-router-skill | New router skill: plain-language request → correct operation skill | t037-1693-16386 | done |
| t037-1693-59324 | update-reference-docs | Rewrite all five reference/ files to the new model | t037-1693-16386 | done |
| t037-1693-63951 | update-templates | New task/context templates; drop decisions/adr templates | t037-1693-16386 | done |
| t037-1693-66263 | update-readme | README rewrite to the new design | t037-1693-16386 | done |
| t037-1693-73540 | crossplatform-python-sync-scripts | Move + rewrite sync-workflow/sync-skills as tools/sync-workflow.py / tools/sync-skills.py — cross-platform Python (Windows/macOS/Linux), shipping the whole tools/ incl. .epoch | t037-1693-02727 | done |

*(Subtask files are drafted as `t037-1693-02727-new-id-system.md` etc.
under this parent's folder when implementation starts — filename is
`{id}-{name}` per c037-1675-68146 — this table is the index;
substance goes in the subtask files.)*
