## Brief overview
- Global guideline: prioritize production-grade quality, avoid shortcuts, and keep the codebase free of technical debt by default.
- Refactors are completed immediately; legacy code and placeholder hacks are not carried forward.

## Principles
- No shortcuts or hacks
  - Implement the correct solution rather than expedient workarounds.
  - Disallow commented-out code, dead code, or unused files in main.
- Strategy-bound placeholders only
  - Temporary mocks/scaffolds are allowed only as an explicitly approved strategy (e.g., tests, staged rollout).
  - Must be narrowly scoped, documented in the PR, and removed in the same change by default (or tracked with owner and deadline).
- Immediate refactor and migration
  - When touching related code, complete renames, migrate all usages, and delete obsolete paths in the same change set.
  - Do not defer cleanup to a later phase.
- Zero technical debt by default
  - No TODOs without a linked issue and near-term deadline.
  - Remove stale feature flags and deprecated patterns when encountered.
- Legacy prevention
  - Avoid maintaining parallel “old + new” indefinitely.
  - Complete end-to-end migration promptly and remove the old path as part of rollout.
  - Prefer codemods/bulk updates to eliminate deprecated patterns repo-wide once touched.

## Development workflow
- Plan changes to fully finish refactors within the change boundary.
- Keep observability signals (logs/metrics) clean and actionable; remove noisy or redundant output during refactor.

## Definition of Done
- Tests updated/added (unit/integration/e2e as appropriate) and passing.
- Linters/formatters pass; no new warnings introduced.
- Documentation updated (README/ADRs/internal notes/migration steps when applicable).
- No temporary placeholders left (unless explicitly approved strategy with owner/deadline).
- No unused symbols/imports/files; no commented-out code.
- Refactors/migrations completed and obsolete paths removed.

## Exceptions (strictly limited)
- Emergency hotfixes may defer cleanup only with:
  - A tracked follow-up issue, named owner, and short deadline.
  - Clear rationale documented in the PR.
  - Commitment to bring code fully up to standard immediately after stabilization.
