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
- Output only IDs, one per line, in order.
- Accept optional `--count` flag (default: 1 — generate one ID if omitted).
- Accept optional `--kind` flag to specify prefix (default: `phase`).

### Out of scope

- Generating IDs with names (that's the constants.py `generate_id()`
  function; the script is for bulk ID-only output).
- Updating workflow.md references (P08-T03).
- Restructuring task folders (P08-T04).

### Files to create

- `LAAW/tools/generate_id.py` — Executable Python script for generating
  N ordered IDs (defaults to 1 if no count given).

### Files to modify

- None.

### Steps

1. **Create the script** — Write `LAAW/generate_id.py` with:
   - Shebang: `#!/usr/bin/env python3`
   - Imports: `sys`, `random`, and `constants` from the same directory
   - Argument parsing: Accept a single positional argument (N, integer)
     and an optional `--kind` flag (choices: `phase`, `task`, `decision`;
     default: `phase`)
   - Logic:
     ```
     parse arguments
     for i from 0 to N-1:
       generate_id with kind and random_seed=i
       print the ID
     ```
   - Guard: If `__name__ == "__main__"`, run the logic.

2. **Make it executable** — `chmod +x LAAW/generate_id.py`.

3. **Create the script** — Write `LAAW/tools/generate_id.py` with:
   - Shebang: `#!/usr/bin/env python3`
   - Imports: `sys`, `random`, and `constants` from the same directory
   - Argument parsing: Accept optional `--count N` (default: 1) and
     optional `--kind` flag (choices: `phase`, `task`, `decision`;
     default: `phase`)
   - Logic:
     ```
     parse arguments (default count=1, default kind=phase)
     for i from 0 to count-1:
       generate_id with kind and random_seed=i
       print the ID
     ```
   - Guard: If `__name__ == "__main__"`, run the logic.

4. **Make it executable** — `chmod +x LAAW/tools/generate_id.py`.

5. **Verify the script works** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py
   ```
   Verify output is exactly one ID in format `{prefix}{minutes:07d}{random:05d}`
   (no name suffix).

6. **Verify with --count flag** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py --count 5
   ```
   Verify output is 5 unique IDs.

7. **Verify with --kind flag** — Run:
   ```bash
   cd LAAW && python3 tools/generate_id.py --kind task
   cd LAAW && python3 tools/generate_id.py --kind decision
   ```
   Verify prefixes are `t` and `d` respectively.

5. **Verify ordered output** — Run:
   ```bash
   cd LAAW && python3 generate_id.py 10 > /tmp/ids.txt
   sort /tmp/ids.txt -c && echo "Sorted correctly"
   ```
   Verify the output is lexicographically sorted (chronological order).

### Dependencies

- `LAAW/constants.py` must exist and be importable.

### Expected result

- An executable Python script that generates N ordered IDs.
- IDs follow the format `{prefix}{minutes:07d}{random:05d}` (no name).
- Output is lexicographically sorted.

### Automatic validations

- Run `cd LAAW && python3 tools/generate_id.py` and verify it prints exactly 1 ID matching the pattern `{prefix}\d{7}\d{5}`.
- Run `cd LAAW && python3 tools/generate_id.py --count 10` and verify it prints exactly 10 lines.
- Run `cd LAAW && python3 tools/generate_id.py 5 --kind task` and verify all IDs start with `t`.
- Run `cd LAAW && python3 tools/generate_id.py 100` and verify all IDs are unique.
- Verify the script is executable (`test -x LAAW/tools/generate_id.py`).

### Manual validations

- Does the script interface feel natural for agents to invoke?
- Is the `--kind` flag sufficient, or do agents need other options?
- Is the script's error handling adequate (e.g., invalid N, missing constants)?
