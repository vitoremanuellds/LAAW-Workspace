# Cross-platform Python sync scripts

**ID:** t037-1693-73540       **Status:** done

## Description

Replace the two bash sync scripts (`LAAW/sync-workflow.sh`,
`LAAW/sync-skills.sh`) with cross-platform Python equivalents in
`LAAW/tools/`: `sync-workflow.py` and `sync-skills.py`. The scripts
move into `tools/` alongside `generate-id.py`, ship the entire `tools/`
folder (including `.epoch`), use `pathlib`/`shutil` only (no bash, no
POSIX-only calls), resolve paths the same way on Windows/macOS/Linux,
and preserve the same behavior (wholesale install/re-sync, version
stamp, skills mirror). The old `.sh` files are deleted.

## TL;DR

- Replace `sync-workflow.sh` → `tools/sync-workflow.py`.
- Replace `sync-skills.sh` → `tools/sync-skills.py`.
- Both move into `tools/` next to `generate-id.py`.
- Cross-platform: `pathlib`/`shutil` only, no bash, no POSIX-only calls.
- Ship `tools/` (incl. `.epoch`) — the bash scripts never shipped
  `tools/`.
- Delete the old `.sh` files.
- Depends on t037-1693-02727 (new id system, done) — the scripts ship
  `generate-id.py` and `.epoch`.

## Context

### Before

- Parent task [t002-7178-75813](t002-7178-75813-revamp-laaw-repo.md) — the LAAW revamp.
  Depends on t037-1693-02727 (new id system, done) and
  t037-1693-16386 (workflow.md rewrite, done — the README and
  workflow.md already reference `sync-workflow.py`).
- Current scripts:
  - `LAAW/sync-workflow.sh` (2610 bytes): copies `workflow.md`,
    `skills/`, `templates/`, `reference/`, `README.md`,
    `sync-skills.sh` into `.ai/workflow/`; writes version stamp to
    `.ai/workflow-version`. Uses bash: `set -euo pipefail`,
    `$(...)`, `BASH_SOURCE`, `dirname`, `rm -rf`, `cp -r`, `git`,
    `date`.
  - `LAAW/sync-skills.sh` (1742 bytes): mirrors `skills/` into
    `.agents/skills/`; uses bash: `set -euo pipefail`, `$(...)`,
    `BASH_SOURCE`, `dirname`, `rm -rf`, `cp -r`.
- **Key gap:** `sync-workflow.sh` does NOT copy `tools/` or `.epoch`
  — projects can't mint ids after install. This must be fixed.
- The revamp design says: cross-platform Python, `pathlib`/`shutil`
  only, same behavior, ships `tools/` (incl. `.epoch`), git invoked
  only via `subprocess` for version stamp (tolerate absent git).

### After

<!-- Filled in by implement-task after implementation -->

## In scope

- **`LAAW/tools/sync-workflow.py`** — Python equivalent of
  `sync-workflow.sh`:
  - Arguments: `[source_dir] [target_root]` — same as the bash script.
    Defaults: source = script's own checkout, target = current dir.
  - Validates `source_dir` has `workflow.md` (error if not).
  - Dest: `<target_root>/.ai/workflow/` (wholesale replace).
  - Copies: `workflow.md`, `skills/`, `templates/`, `reference/`,
    `README.md`, `tools/` — **now includes `tools/`** (the bash
    script never did).
  - Writes version stamp to `<target_root>/.ai/workflow-version`
    (sibling of `.ai/workflow/`, never inside it).
  - Version stamp format: `source=<label>`, `commit=<SHA>`,
    `date=<UTC date>` — same as bash, but using Python's `datetime`.
  - Git invocation: `subprocess.run(['git', '-C', source, 'rev-parse',
    'HEAD'], ...)` — tolerate absent git (set SHA to "unknown").
  - No bash, no `os.fork`, no hardcoded `/` paths — use `pathlib` for
    all path operations.
  - Entry point: `if __name__ == '__main__':` — resolvable on Windows
    (`py -3 tools/sync-workflow.py`), macOS, Linux.

- **`LAAW/tools/sync-skills.py`** — Python equivalent of
  `sync-skills.sh`:
  - Arguments: `[destination]` — optional, defaults to
    `<project_root>/.agents/skills/` (where project root is derived
    from the script location: two levels up from `.ai/workflow/`).
  - Source: `.ai/workflow/skills/` (standard mount point).
  - For each skill dir: add if new, update if existing (rm + cp).
  - Prints: `added N, updated M. Synced to <dest>`.
  - No bash, no POSIX-only calls — `pathlib`/`shutil` only.

- **Delete `LAAW/sync-workflow.sh`** — replaced by the Python version.
- **Delete `LAAW/sync-skills.sh`** — replaced by the Python version.

## Out of scope

- Changes to `workflow.md` — already done by t037-1693-16386.
- Changes to skill files — covered by steps 3–5.
- Changes to reference docs — covered by step 6.
- Changes to templates — covered by step 7.
- Changes to the README — covered by step 8.
- Changes to `generate-id.py` — already done by t037-1693-02727.

## Steps

1. Create `LAAW/tools/sync-workflow.py`:
   - Parse optional arguments (source_dir, target_root).
   - Validate source_dir has `workflow.md`.
   - Wholesale replace `.ai/workflow/`: rm + mkdir + copy
     (workflow.md, skills/, templates/, reference/, README.md, tools/).
   - Git version stamp via subprocess (tolerate absent git).
   - Write version stamp file (sibling of `.ai/workflow/`).
   - Print success message (installed vs re-synced).
2. Create `LAAW/tools/sync-skills.py`:
   - Parse optional destination argument.
   - Default destination: `<project_root>/.agents/skills/`.
   - Mirror skills/ directory (rm + cp each skill).
   - Print added/updated counts.
3. Delete `LAAW/sync-workflow.sh`.
4. Delete `LAAW/sync-skills.sh`.
5. Verify `tools/` contains: `generate-id.py`, `.epoch`,
   `sync-workflow.py`, `sync-skills.py`.
6. Verify no remaining `.sh` files in `LAAW/`.
7. Verify both Python scripts compile:
   `python3 -m py_compile tools/sync-workflow.py tools/sync-skills.py`.
8. Test: run `sync-workflow.py` into a scratch dir → verify `.ai/
   workflow/` contains all expected files (including `tools/` with
   `generate-id.py`, `.epoch`, `sync-workflow.py`, `sync-skills.py`).
9. Verify no POSIX-only constructs in Python (no `os.fork`, no
   hardcoded `/` paths, `shutil`-level only).

## Validations

- `tools/sync-workflow.py` and `tools/sync-skills.py` exist in `tools/`.
- Both scripts compile: `python3 -m py_compile` succeeds for both.
- `sync-workflow.py` copies `tools/` (including `generate-id.py` and
  `.epoch`) — the bash script never did.
- Old `.sh` files are deleted (not kept alongside).
- `sync-workflow.py` into a scratch dir → `.ai/workflow/tools/`
  contains `sync-workflow.py`, `sync-skills.py`, `generate-id.py`,
  `.epoch`.
- `generate-id.py` runs from the installed copy.
- No POSIX-only constructs: no `os.fork`, no hardcoded `/` paths.
- Entry points resolvable on Windows (`py -3 tools/sync-workflow.py`),
  macOS, Linux.
- Grep `LAAW/` for `sync-workflow.sh` or `sync-skills.sh` — all gone
  (the README update in step 8 will reference the Python versions).
