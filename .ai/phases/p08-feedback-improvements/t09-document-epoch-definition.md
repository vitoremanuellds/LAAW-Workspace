# T09: Document the epoch definition

## Context

[Phase P08: Feedback Implementation Improvements](phase.md)

## Implementation

### Objective

Verify that `LAAW/constants.py` properly documents the epoch definition and all ID generation constants, so all agents compute IDs consistently. This satisfies R01's requirement for a well-defined epoch.

### In scope

- Review `LAAW/constants.py` for completeness and correctness.
- Add any missing documentation or clarifying comments to the constants file.

### Out of scope

- Creating the constants file (it already exists at `LAAW/constants.py`).
- Changing the epoch or format parameters (those are design decisions already made).

### Files to modify

- `LAAW/constants.py` — Add clarifying comments where needed to document the rationale for each constant value.

### Steps

1. Read `LAAW/constants.py`. It currently defines:
   - `EPOCH = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)`
   - `MIN_WIDTH = 7`, `RANDOM_WIDTH = 5`
   - `MIN_MAX = 10 ** MIN_WIDTH`, `RANDOM_MAX = 10 ** RANDOM_WIDTH`
   - `FORMAT_STRING = "{prefix}{minutes:07d}{random:05d}-{name}"`
   - `PREFIX_MAP = {"phase": "p", "task": "t", "decision": "d"}`
2. Verify each constant has a clear comment explaining:
   - **What** the value represents
   - **Why** this specific value was chosen (e.g., why 7 digits, why 2020-01-01 as epoch)
   - **What the implications are** (e.g., 7 digits ≈ 19 years, 5 random digits = 100,000 combinations ≈ 0.045% collision risk for 10 concurrent requests)
3. Add or improve comments where documentation is missing or unclear. Specifically:
   - The epoch comment should explain why 2020-01-01 was chosen and how long the 7-digit format covers from that epoch.
   - The random width should note the collision probability for typical concurrency scenarios.
   - The format string should include an example ID.
   - The prefix map should note which prefixes are used for each entity type.
4. Verify `LAAW/tools/generate_id.py` imports and uses these constants correctly.
5. Run `cd LAAW/tools && python generate_id.py --count 10` and verify all 10 IDs are unique, properly formatted (7-digit minutes + 5-digit random), and sorted ascending.

### Automatic validations

- Run `cd /home/vitor/Projects/personal/LAAW-Workspace/LAAW/tools && python generate_id.py` and verify it outputs a valid ID.
- Run `cd /home/vitor/Projects/personal/LAAW-Workspace/LAAW/tools && python generate_id.py --count 100` and verify all 100 IDs are unique.
- Verify `constants.py` exports `EPOCH`, `MIN_WIDTH`, `RANDOM_WIDTH`, `MIN_MAX`, `RANDOM_MAX`, `FORMAT_STRING`, and `PREFIX_MAP`.

### Manual validations

- Is the epoch date (2020-01-01) reasonable for the project's lifetime?
- Does the constants file clearly document the rationale for each value?
- Is the random component width (5 digits = 100,000 combinations) sufficient for the expected concurrency level?
