# Phases

Index/permanent record for phases — moved here from
`.ai/constitution/roadmap.md` when this repo re-bootstrapped from
LAAW's redesigned workflow (P06); same table, same rows, new location
and name per [ADR03](../decisions/adr03-single-modular-workflow.md).

Starting without a full plan up front, per `workflow.md`'s "starting
without a plan" mode: P02 is still stubbed title-only. It gets its own
Context/In-scope/Out-of-scope/Requirements/Plan/Validations drafted
later via `define-phase`.

P01 is superseded by
[ADR03](../decisions/adr03-single-modular-workflow.md) — see its own
file for what replaces it. P06 is its successor, redesigning
`LAAW/`'s content around ADR03's three axes,
under a new ID rather than reusing P01's.

P03–P05 cover the third mission goal (workflow-mechanics evolution)
and are already fully drafted — see each phase's own file. They're
deliberately independent of each other (no Depends-on between them) so
they can be planned and implemented concurrently by different
contributors, which also doubles as this project's first real exercise
of the concurrency model P05 itself defines.

| ID | Title | Depends on | Status |
|---|---|---|---|
| P01 | Design the `Light` workflow profile | — | superseded (ADR03) |
| P02 | Non-submodule bootstrap mechanism | — | not-planned |
| P03 | Workbench directory & context-build temp-file lifecycle | — | complete |
| P04 | Context sync from git history | — | awaiting-plan-review |
| P05 | Concurrency-safe phase/task planning | — | awaiting-plan-review |
| P06 | Redesign LAAW as a single modular workflow | — | complete |
