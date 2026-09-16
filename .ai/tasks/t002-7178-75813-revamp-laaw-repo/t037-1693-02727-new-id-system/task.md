# New id system

**ID:** t037-1693-02727       **Status:** done

## Description

Rewrite LAAW's id generator (`LAAW/tools/generate-id.py`) to the
revamped design's id format — dash-separated 7-digit
minutes-since-epoch (split 3+4) plus 5 random digits, `t`/`c` prefix,
the shipped epoch moved to `2026-01-01T00:00:00Z`, and a collision
check against a target directory when minting filenames. First
subtask of the revamp; no other subtask precedes it.

## TL;DR

Replace the base-36 8-char format with `<prefix>{xxx-yyyy-zzzzz}`
(e.g. `t005-4321-48213`), point `LAAW/tools/.epoch` at
`2026-01-01T00:00:00Z`, keep `--count`/`--epoch`, and make minting
safe against duplicates in a batch and against an existing target
directory; a batch of N ids is emitted sorted ascending (smallest to
biggest).

## Context

### Before

- Parent task [t002-7178-75813](../task.md) — the LAAW revamp.
  This subtask has no depends-on; the `workflow.md` rewrite
  (t037-1693-16386) and the sync scripts (t037-1693-73540) depend on
  it.
- Current generator (`LAAW/tools/generate-id.py`): base-36, 5-char
  timestamp + 3-char random, **no prefix**, options `--count` and
  `--epoch`, default epoch read from `LAAW/tools/.epoch`
  (`2026-08-28 01:27:20 -0300`, no trailing newline).
- Format authority: the [revamp design](../../workbench/revamp-design.md)
  "IDs" section and the parent task's validation regex
  `^t\d{3}-\d{4}-\d{5}$` (same shape for `c`). The design's "Full
  form" line renders a dash after the prefix, but every minted
  example in the design, in this workspace, and the parent's regex
  have **no** dash between prefix and timestamp — the regex is the
  binding shape.
- Decision [c037-1650-68133](../../context/c037-1650-68133-revamp-open-decisions.md) settles
  the shipped epoch (`2026-01-01T00:00:00Z`, superseding the old
  default) and requires no migration of already-minted ids.
- Filename convention (binds the `--dir` check): every id'd file is
  `{id}-{name}` — tasks (leaf files, folders, parent files) and
  context alike; the id is a fixed-shape prefix and is never reused.
  Settled as [c037-1675-68146](../../context/c037-1675-68146-id-name-filenames.md).
- IDs are ordered by table position
  ([c037-1693-91765](../../context/c037-1693-91765-ids-ordered-by-table.md)):
  since a batch of N ids gets appended to a table in one go, a
  `--count N` batch must be emitted sorted ascending — smallest id
  first, biggest last — so the appended rows are already in order.
- The 7-digit minute counter caps at 9,999,999 min (≈ 19 years from
  2026): overflow must be an explicit error, never silent truncation
  or wrap.

### After

- `tools/generate-id.py` now mints `<prefix>{mmm-dddd-rrrrr}` (e.g. `t037-1719-95251`) — prefix `t`/`c`, 7-digit zero-padded minutes since epoch split 3+4, 5 random decimal digits; no dash between prefix and timestamp. All four CLI capabilities landed with the flexible-marker names: `--count`, `--epoch`, `--prefix`, `--dir`.
- Shipped default epoch is `2026-01-01T00:00:00Z` (per c037-1650-68133); epoch parsing accepts ISO 8601 with `Z`/offset or bare `YYYY-MM-DD HH:MM:SS` (UTC). Negative or ≥ 10,000,000 minute counts are hard errors, never truncated or wrapped.
- `--dir` collision check keys on entries whose name starts with `{id}-` (files *and* directories — so a subtask folder `t{ID}-{name}/` blocks re-minting its id, matching the never-reused-id rule from c037-1675-68146).
- Batches of N share one minute part, are deduped (within batch and against the directory), and emit sorted ascending — matching the ids-ordered-by-table rule (c037-1693-91765).
- LAAW commit `3497c49` on `main`; workspace pointer advanced. Unblocks t037-1693-16386 and t037-1693-73540.

## In scope

- `LAAW/tools/generate-id.py` — rewritten to the new format.
- `LAAW/tools/.epoch` — new shipped epoch value.
- Nothing else in LAAW: docs/skills/templates that mention the id
  format in prose belong to their own subtasks.

## Out of scope

- Migrating or staying compatible with old base-36 ids — none
  required.
- Wiring the generator into workflow docs, skills, or templates —
  later subtasks.
- Moving `tools/` or changing the sync scripts — subtask
  t037-1693-73540.
- "Done" concretely: the mechanical validations below pass from a
  clean checkout and the emitted shape matches the parent's regex
  byte-for-byte.

## Steps

1. Set `LAAW/tools/.epoch` to exactly `2026-01-01T00:00:00Z`
   (ISO 8601, UTC). (flexible: trailing newline present or absent)
2. Rewrite `LAAW/tools/generate-id.py` with these four CLI
   capabilities:
   - `--count N` (default 1) — mint N ids in the same minute.
   - `--epoch STRING` (default: read `tools/.epoch` next to the
     script, as today) — override the epoch.
   - `--prefix` with choices `t` | `c`, default `t`.
   - `--dir PATH` (default: off) — collision check against an
     existing directory of task/context files.
   (flexible: exact flag names for `--prefix`/`--dir`; the four
   capabilities are binding and must each be reachable from the CLI.)
3. Epoch handling: accept ISO 8601 with `Z` or an explicit offset; a
   bare `YYYY-MM-DD HH:MM:SS` or date-time without offset is UTC
   (same tolerance as the current tool). Unparseable ⇒ error to
   stderr, non-zero exit.
4. Minute counter: `minutes = floor((now_utc - epoch) / 60)`.
   `minutes < 0` or `minutes >= 10_000_000` ⇒ error to stderr,
   non-zero exit.
5. Id shape: `prefix + mmm-dddd-rrrrr` — the 7-digit zero-padded
   minute count split 3+4, then `-`, then 5 random decimal digits.
   Emit one id per line on stdout, as today.
6. Batch safety and order (`--count N`): all N share the same minute
   part; re-draw the random part on any within-batch duplicate so the
   batch always yields N unique ids; emit the N ids sorted ascending
   (smallest first, biggest last) — never in mint order.
7. Directory safety (`--dir PATH`): PATH must exist (error if not);
   after minting, if the id is already used in PATH — any file or
   directory whose name starts with `{id}-` (filenames are
   `{id}-{name}.md`, ids are never reused) — re-draw its random part
   and re-check; combine with the within-batch rule so batch +
   directory are both clean.
8. Mint loop, as guidance (not a script):

   ```
   for each of the N requested ids:
     loop:
       candidate = prefix + minutes_part(split 3+4) + "-" + random5()
       if candidate is already in this batch: re-draw random part
       if --dir given and any entry in dir starts with candidate + '-': re-draw
     accept candidate
   sort the accepted ids ascending (smallest first); emit one per line
   ```

9. Run every check in Validations from `LAAW/`.

## Validations

Mechanical (run from `LAAW/`):

- `python3 tools/generate-id.py` → one line matching
  `^t[0-9]{3}-[0-9]{4}-[0-9]{5}$`
- `python3 tools/generate-id.py --prefix c` → matches
  `^c[0-9]{3}-[0-9]{4}-[0-9]{5}$`
- `python3 tools/generate-id.py --count 5` → 5 lines, all sharing the
  same 3+4 minute part, all 5 ids unique, sorted ascending (smallest
  to biggest)
- `python3 tools/generate-id.py --epoch 2020-01-01T00:00:00Z` runs
  and still matches the shape (larger minute count)
- Minute part is correct: independently recompute minutes since
  `2026-01-01T00:00:00Z` (e.g. via `date -u`) and compare against the
  emitted `xxx-yyyy`
- `--dir` collision: in a scratch dir, touch a file named
  `t{just-minted-id}-probe.md`, re-run with `--dir` at it, and
  confirm the returned id is not the existing one's prefix
- `python3 -m py_compile tools/generate-id.py`
- `grep -rin base36 tools/` → no hits

Judgment:

- Emitted ids look byte-identical in structure to already-minted
  workspace ids (`t037-1693-02727`, `c037-1650-68133`) — in
  particular: no dash between prefix and timestamp.
