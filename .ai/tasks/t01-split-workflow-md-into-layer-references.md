# T01 — Split `workflow.md`'s per-layer detail into `reference/` files

## Context

Backlog item surfaced during P06 validation (P06-T06): `workflow.md`
grew ~19% (1206 → 1432 words) instead of shrinking, because the
optional-layer/orphan-task rules needed real explanation somewhere —
see [`../phases/p06-redesign-laaw-modular-workflow.md`](../phases/p06-redesign-laaw-modular-workflow.md)'s
Deviations section for the exact numbers; not repeated here.

Goal: get back to "measurably lighter" — not by cutting real content,
but by moving detail that only applies to *one* layer's own
configuration into `reference/` files a skill reads only when that
layer is actually in play. A minimal (tasks-only) project's required
reading should shrink even though the document covers more ground
overall.

**No phase.** Deliberately scoped as a standalone orphan task, not
tied to any phase in this repo's roadmap — the first task to use
ADR03's orphan-task convention in this repo. The actual file changes
still happen and commit in `Full-Local-Model-Agent-Workflow/`'s own
checkout, same location discipline as every other content task in
this project (see `mission.md` Boundaries) — this file only tracks the
work item.

## Implementation

### Objective

Reduce `workflow.md`'s own required-reading size back toward (or
below) its pre-P06 baseline by extracting layer-specific detail into
`reference/` files, read only by the skills that actually need them.

### In scope

- Identify which parts of `workflow.md`'s current (post-P06) content
  are specific to one optional layer (e.g. orphan-task rules, per-layer
  scaffold conventions) versus genuinely universal.
- Move layer-specific detail into new or existing `reference/` files;
  leave a short pointer in `workflow.md` instead of the full
  explanation.
- Re-run the same word-count check P06-T06 used; confirm `workflow.md`
  itself is at or below its pre-P06 baseline (1206 words).

### Out of scope

- Changing any rule or decision from ADR03/P06 — presentation only, not
  a redesign.
- This outer meta-repo's own `.ai/` — stays on its pre-redesign schema,
  untouched.

### Files to modify

- `Full-Local-Model-Agent-Workflow/workflow.md`
- Relevant `Full-Local-Model-Agent-Workflow/reference/*.md` files
  (existing or new — exact split TBD during implementation)

### Files to create

TBD during implementation — likely one new `reference/` file for
orphan-task detail and/or per-layer presence rules.

### Steps

1. Re-read the current `workflow.md` post-P06 and mark every paragraph
   specific to one optional layer rather than universal.
2. For each marked block, decide: move into an existing `reference/`
   file, or a new one — group by topic, not by size.
3. Replace each moved block in `workflow.md` with a one-to-two-sentence
   pointer.
4. Re-run `wc -w workflow.md`; confirm it's at or below the pre-P06
   baseline (1206 words).
5. Spot-check that no skill lost access to detail it actually needs —
   a skill that owns a layer should still know to read that layer's
   reference file.

### Dependencies

None — orphan, no phase, no other task blocks it. Logically follows
P06 (can't split what P06 hadn't yet written), but P06 is already
complete.

### Expected result

`workflow.md` reads at or below its pre-P06 word count; per-layer
detail lives in `reference/`, read only by the skills that need it.

### Automatic validations

- `wc -w Full-Local-Model-Agent-Workflow/workflow.md` ≤ 1206.
- `git -C Full-Local-Model-Agent-Workflow log --oneline -1` shows a
  commit for this change.

### Manual validations

- Read `workflow.md` end to end — confirm it still reads as coherent
  and complete, not just short because content got orphaned into
  unreferenced files.
