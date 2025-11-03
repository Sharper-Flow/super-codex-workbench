## Brief overview
- Always identify and verify the root cause before attempting any fix.
- Follow a four-phase framework: Root Cause Investigation → Pattern Analysis → Hypothesis & Testing → Implementation.
- Minimize changes; test one variable at a time; verify outcomes before proceeding.
- If multiple fix attempts fail, question the architecture rather than stacking more changes.

## When to use
- Any technical issue: test failures, production bugs, unexpected behavior, performance problems, build failures, integrations.
- Especially under time pressure or when a "quick fix" seems obvious.
- After multiple failed attempts or when the issue is not fully understood.

## Core principle
- Iron Law: No fixes without root cause investigation first.
- Symptom fixes are considered failures; focus on the source of truth for the defect.

## Phase 1: Root cause investigation
- Read error messages and stack traces carefully (note file paths, line numbers, error codes).
- Reproduce the issue consistently; if not reproducible, gather more data first.
- Check recent changes (commits, dependency/config updates, environment differences).
- Multi-component systems: instrument at boundaries (log inputs/outputs, verify environment/config propagation, inspect state at each layer) to pinpoint the failing component.
- Trace data flow back to the origin of the bad value and fix at the source.
- **File editing failures**: If `replace_in_file` fails, immediately re-read the target file to ensure you have the current state before attempting another fix.
- **Edit verification**: Always confirm the exact file state (including auto-formatting) before crafting SEARCH blocks for subsequent edits.

## Phase 2: Pattern analysis
- Find working examples in the codebase; compare against reference implementations.
- Identify all differences (even minor ones) between working and broken paths.
- Understand dependencies, assumptions, and configuration required by the pattern.

## Phase 3: Hypothesis and testing
- Form a single, specific hypothesis: "X is the root cause because Y."
- Test minimally: change one variable at a time with the smallest possible modification.
- Verify results before continuing; if wrong, form a new hypothesis rather than stacking changes.
- If uncertain, acknowledge knowledge gaps and research or request help.

## Phase 4: Implementation
- Create the simplest failing test or reproduction script first (automated where possible).
- Implement a single fix that addresses the identified root cause.
- Verify the fix: failing test now passes, broader tests remain green, behavior confirmed resolved.
- If the fix fails: stop and return to Phase 1 with new evidence. After 3 failed attempts, question the architecture.
- **Edit fallback strategy**: If `replace_in_file` fails multiple times, use `write_to_file` as a fallback, but only after re-reading the file to ensure you have the complete current content.

## Red flags (stop and return to Phase 1)
- "Quick fix for now, investigate later" or "just try changing X."
- Bundling multiple fixes at once or skipping tests.
- Proposing solutions before tracing data flow or reading errors fully.
- "One more fix attempt" after 2+ failures, or each fix reveals new problems elsewhere.

## Partner signals (course-correct immediately)
- "Is that not happening?" indicates an unverified assumption.
- "Will it show us…?" signals missing evidence gathering.
- "Stop guessing" or "Ultrathink this" signals need to return to systematic analysis.

## Quick reference
- Phase 1: Read errors, reproduce, inspect changes, instrument boundaries → understand what/why.
- Phase 2: Compare to working patterns → list differences and dependencies.
- Phase 3: One hypothesis → smallest testable change → verify or revise.
- Phase 4: Test-first, implement single fix, verify globally → if repeated failure, reassess architecture.

## Edge cases and environment-driven issues
- If a thorough investigation shows a truly external or timing-dependent cause:
  - Document what was investigated and why it's external.
  - Implement appropriate handling (retries, timeouts, clearer errors).
  - Add monitoring/logging for future diagnostics.
- Note: most "no root cause" outcomes reflect incomplete investigation.

## Integration with other skills
- Root-cause tracing: use for deep call stacks and cross-layer data flow.
- Test-driven development: required for writing failing tests before fixes.
- Complementary patterns: defense-in-depth validation; condition-based waiting instead of arbitrary timeouts; verification-before-completion.

## Enforcement
- Any proposed fix must include: the identified root cause, the focused change to address it, and the verification method (failing test, check, or reproduction) that proves it.
- Bug-fix PRs must include:
  - Link to the failing test or exact reproduction steps
  - Evidence from Phase 1 (errors, stacks, logs, diffs) summarized in the PR
  - One-hypothesis summary and the minimal-change test performed
- After 3 failed fix attempts, pause implementation and schedule an architectural review before proceeding.

## Success criteria
- Root cause identified and documented.
- Minimal change implemented that addresses the source, not the symptom.
- Automated test or reproducible check passes; broader test suite remains green.
- If cause is external/timing-dependent, mitigations added and monitoring/logging in place.
