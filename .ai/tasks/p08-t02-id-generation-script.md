# P08-T02: Implement the ID generation script

## Context

See [../phases/p08-feedback-improvements.md](../phases/p08-feedback-improvements.md)
for the phase context, requirements, and plan.

The ID generation script is a CLI tool that agents invoke to obtain
ordered, collision-safe IDs for phases, tasks, and decisions. It
consumes `LAAW/constants.py` (P08-T01) to compute the timestamp and
random components.

## Implementation

### Objective

Create a Python script that generates one or N ordered IDs, accepting
only a count parameter and returning IDs only (no names). This is the
primary interface agents use to obtain IDs during operation.

### In scope

- Create `LAAW/tools/` directory for Python utility scripts.
- Write `LAAW/tools/generate_id.py` — executable Python script.
- Use `LAAW/constants.py` for epoch and format constants.
- Output only the ID portion (`{minutes:07d}{random:05d}`), one per line,
  **sorted ascending**.
- Accept optional `--count` flag (default: 1 — generate one ID if omitted).
- **No prefix, no name**: the script outputs only the 12-digit ID component.
  The caller prepends the prefix (p/t/d) themselves.

### Out of scope

- Prefix handling (caller responsibility: p/t/d).
- Name suffixes (caller responsibility if needed).
- Updating workflow.md references (P08-T03).
- Restructuring task folders (P08-T04).

### Files to create

- `LAAW/tools/generate_id.py` — Executable Python script that outputs only
  the ID portion (`{minutes:07d}{random:05d}`), defaults to 1 ID if no
  count given. Caller prepends prefix (p/t/d).

### Files to modify

- None.

### Steps

1. **Create the `LAAW/tools/` directory** — `mkdir -p LAAW/tools`.

2. **Write `LAAW/tools/generate_id.py`** with:
   - Shebang: `#!/usr/bin/env python3`
   - Imports: `sys`, `random`, `argparse`, `os`, `datetime`
   - Add parent directory to `sys.path` for importing `constants`
   - Argument parsing: Accept optional `--count` flag (default: 1)
   - Logic:
     ```
     parse arguments (default count=1)
     now = datetime.now(timezone.utc)
     minutes_elapsed = int((now - EPOCH).total_seconds() // 60)
     ids = []
     for i from 0 to count-1:
       random_value = random.randint(0, RANDOM_MAX - 1)
       ids.append(f"{minutes_elapsed:07d}{random_value:05d}")
     ids.sort()
     for id in ids:
       print(id)
     ```
   - Guard: If `__name__ == "__main__"`, run the logic.

3. **Make it executable** — `chmod +x LAAW/tools/generate_id.py`.

4. **Verify default behavior** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py
   ```
   Verify output is exactly one 12-digit ID (`{minutes:07d}{random:05d}`).

5. **Verify sorted output** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py --count 5
   ```
   Verify output is 5 unique 12-digit IDs sorted ascending.

6. **Verify format** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py --count 3
   ```
   Verify each ID is exactly 12 digits (7 + 5).

7. **Verify uniqueness** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py --count 100 | sort -u | wc -l
   ```
   Verify output is 100 (all unique).

### Dependencies

- `LAAW/constants.py` must exist and be importable.

### Expected result

- An executable Python script that generates N ordered IDs.
- IDs follow the format `{prefix}{minutes:07d}{random:05d}` (no name).
- Output is lexicographically sorted.

### Automatic validations

- Run `cd LAAW && python3 tools/generate_id.py` and verify it prints exactly 1 ID of 12 digits.
- Run `cd LAAW && python3 tools/generate_id.py --count 5` and verify output is sorted ascending.
- Run `cd LAAW && python3 tools/generate_id.py --count 10` and verify it prints exactly 10 lines.
- Run `cd LAAW && python3 tools/generate_id.py 100 | sort -u | wc -l` and verify it prints 100 (all unique).
- Verify the script is executable (`test -x LAAW/tools/generate_id.py`).

### Manual validations

- Does the script interface feel natural for agents to invoke?
- Is the `--kind` flag sufficient, or do agents need other options?
- Is the script's error handling adequate (e.g., invalid N, missing constants)?
