# Context

Entry point for `context/` — everything about the actual codebase:
architecture, conventions, terminology, and however many additional
files make sense for this project's actual moving parts. No fixed
subfolder convention — name and organize additional files by whatever
groups the project naturally: an architectural layer, a feature-level
concept, a domain area. "Module" here means a conceptual group of
moving parts that make up a feature, not a coding-language module or a
folder of classes.

| File | Description | Status | Relations |
|---|---|---|---|
<!-- auth-module.md | Auth flow, session handling, token lifecycle | active | related: score-engine.md -->
| [full-directory-structure.md](full-directory-structure.md) | Snapshot of LAAW's `.ai/` directory structure, current as of the ADR03/P06 redesign and this workspace's own re-bootstrap | active | related: [ADR02](../decisions/adr02-workbench-directory.md), [ADR03](../decisions/adr03-single-modular-workflow.md) |
| [purpose.md](purpose.md) | Project purpose, mission, goals, and history — LAAW = Local AI Agents Workflow | active | |
| [architecture.md](architecture.md) | Project architecture: directory layout, key relationships, tech stack, LAAW workflow structure | active | related: [purpose.md](purpose.md) |

**Status** is `active` or `superseded`. When an architecture changes,
don't delete the old file — mark it superseded and point to what
replaced it, same as an ADR. Whoever writes or updates a context file
updates its row here in the same step.
