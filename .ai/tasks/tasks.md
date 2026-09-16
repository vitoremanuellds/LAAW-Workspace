# Tasks

Index/permanent record for root-level tasks. Subtask statuses live in
their parent task file's Subtasks table, never duplicated here.

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
| [t002-7178-75813](t002-7178-75813-revamp-laaw-repo/t002-7178-75813-revamp-laaw-repo.md) | revamp-laaw-repo | Rewrite LAAW's workflow.md, skills, reference/, templates/, id tool, README, and sync scripts to the revamped single-process design | — | done |
| [t037-2374-78689](t037-2374-78689-migrate-workspace-to-new-model/t037-2374-78689-migrate-workspace-to-new-model.md) | migrate-workspace-to-new-model | Migrate LAAW-Workspace's own .ai/ tree to the revamped single-process design (merge constitution/decisions/phases into context, flatten phases→tasks, update info.md, re-sync workflow) | t002-7178-75813 | done |
| [t037-2386-13289](t037-2386-13289-non-submodule-bootstrap/t037-2386-13289-non-submodule-bootstrap.md) | non-submodule-bootstrap | Converted from P02 — shipped copy-based bootstrap/re-sync mechanism (sync-workflow.sh + version stamp) | — | done |
| [t037-2386-79357](t037-2386-79357-workbench-context-temp-lifecycle/t037-2386-79357-workbench-context-temp-lifecycle.md) | workbench-context-temp-lifecycle | Converted from P03 — established .ai/workbench/, relocated build-context temp files, added workbench-readme-template | — | done |
| [t037-2386-24191](t037-2386-24191-redesign-laaw-modular-workflow/t037-2386-24191-redesign-laaw-modular-workflow.md) | redesign-laaw-modular-workflow | Converted from P06 — one modular workflow with optional layers (presence/granularity/locality) | — | done |
| [t037-2386-43783](t037-2386-43783-feedback-implementation-improvements/t037-2386-43783-feedback-implementation-improvements.md) | feedback-implementation-improvements | Converted from P07 — gitignore discipline, define-task single-task default, status sequence | — | done |
| [t037-2386-49264](t037-2386-49264-feedback-improvements/t037-2386-49264-feedback-improvements.md) | feedback-improvements | Converted from P08 — collision-safe ID format, task folder organization, .gitignore discipline | — | in-progress |
| [t037-2389-20360](t037-2389-20360-split-workflow-md-into-layer-references/t037-2389-20360-split-workflow-md-into-layer-references.md) | split-workflow-md-into-layer-references | Extract layer-specific detail from workflow.md into reference/ files | t002-7178-75813 | not-started |
| [t037-2389-40026](t037-2389-40026-fix-laaw-submodule-mislabel/t037-2389-40026-fix-laaw-submodule-mislabel.md) | fix-laaw-submodule-mislabel | Replace remaining "submodule" references in LAAW/ with "plain copy" | t037-2389-20360 | not-started |
| [t037-2390-59511](t037-2390-59511-explicit-gate-skip-for-missing-layers/t037-2390-59511-explicit-gate-skip-for-missing-layers.md) | explicit-gate-skip-for-missing-layers | Add explicit gate-skip statement to LAAW/README.md and workflow.md §5 | t037-2389-20360 | not-started |
| [t037-2426-52295](t037-2426-52295-convert-feedback-tasks/task.md) | convert-feedback-tasks | Convert all tasks to task.md naming, fix define-task description bug, review context ID pattern, add generate-id instruction to skills | — | planned |
