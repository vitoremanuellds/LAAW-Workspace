# P08-T09: Document the epoch definition

## Context

[Phase P08: Feedback Implementation Improvements](../phases/p08-feedback-improvements/phase.md)

## Implementation

### Objective

Create a constants file defining the custom epoch start date used for the minutes-elapsed calculation, so all agents compute IDs consistently. This satisfies R01's requirement for a well-defined epoch.

### In scope

- Create `LAAW/tools/constants.py` with the epoch, width, and random component constants.
- Update `LAAW/tools/generate_id.py` to import from this constants file (it already does — just verify the import works).

### Out of scope

- Changing the ID generation algorithm itself.
- Updating skills or workflow documents to reference the constants file (that's covered by other tasks).

### Files to create

- `LAAW/tools/constants.py` — Define the epoch, timestamp width, and random component constants.

### Files to modify

- `LAAW/tools/generate_id.py` — Verify the import from `constants` works correctly; update if the constants file path differs.

### Steps

1. Create `LAAW/tools/constants.py` with the following content:

```python
"""Constants for LAAW ID generation.

Defines the epoch, timestamp width, and random component parameters
used by generate_id.py to produce collision-safe identifiers.

ID format: {prefix}{minutes:07d}{random:05d}
Example: p00525960123456-name

The epoch is set so the minutes-elapsed counter starts near zero
and never resets during the project lifetime.
"""

from datetime import datetime, timezone

# Epoch: 2025-01-01 00:00:00 UTC
# Chosen so that minutes elapsed starts at a reasonable value
# (~525,600 minutes = ~1 year) and won't reset during the
# project's lifetime. 7 digits covers ~19 years (9,999,999 minutes).
EPOCH = datetime(2025, 1, 1, tzinfo=timezone.utc)

# Timestamp width in digits (zero-padded)
# 7 digits = max 9,999,999 minutes ≈ 19 years
MIN_WIDTH = 7

# Random component: number of combinations (10^5 = 100,000)
# Collision probability for 10 concurrent requests per minute:
# ~0.045% (~1 in 2,223)
RANDOM_MAX = 100_000
```

2. Verify `LAAW/tools/generate_id.py` imports these constants correctly. The existing import is:
   ```python
   from constants import EPOCH, MIN_WIDTH, RANDOM_MAX
   ```
   This uses `sys.path.insert(0, ...)` to add the parent directory to the path. Verify this works by running:
   ```bash
   cd /home/vitor/Projects/personal/LAAW-Workspace/LAAW/tools && python generate_id.py
   ```
3. Run `python generate_id.py 10` and verify all 10 IDs are unique, properly formatted (7-digit minutes + 5-digit random), and sorted ascending.
4. Run `python generate_id.py --count 100` and verify no collisions occur.

### Automatic validations

- Run `cd /home/vitor/Projects/personal/LAAW-Workspace/LAAW/tools && python generate_id.py` and verify it outputs a valid ID.
- Run `cd /home/vitor/Projects/personal/LAAW-Workspace/LAAW/tools && python generate_id.py --count 100` and verify all 100 IDs are unique.
- Run `cd /home/vitor/Projects/personal/LAAW-Workspace/LAAW/tools && python generate_id.py --count 1000` and verify no collisions (expected — collision risk is ~0.045% per minute for 10 concurrent requests).
- Confirm `constants.py` exports `EPOCH`, `MIN_WIDTH`, and `RANDOM_MAX`.

### Manual validations

- Is the epoch date (2025-01-01) reasonable for the project's lifetime?
- Does the constants file clearly document the rationale for each value?
- Is the random component width (5 digits = 100,000 combinations) sufficient for the expected concurrency level?
