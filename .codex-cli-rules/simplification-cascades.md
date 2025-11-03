## Brief overview
- Seek a single unifying insight that collapses complexity (e.g., “Everything is a special case of …”).
- Optimize for deletions: measure success by how many components, branches, and configs disappear.
- Prefer one powerful abstraction over many special-cased implementations.

## When to use
- The same concept is implemented multiple ways across the codebase.
- Special-case lists keep growing; complexity is spiraling.
- Rules have many exceptions; configuration options proliferate.
- You are maintaining parallel “old vs new” flows that feel similar.

## Core principle
- If X is true, we can eliminate Y, Z, and W (unify patterns to delete code).
- Generalize to the essence: treat variants as parameters/sources of a single abstraction.
- One abstraction > many hacks; prefer fewer concepts with clearer contracts.

## Quick reference (symptom → action)
- Multiple implementations of similar logic → Abstract common pattern behind a single API.
- Growing list of special cases → Identify the general case and encode it directly.
- Complex rules with exceptions → Find a rule with no exceptions; encode defaults.
- Many configuration options → Set sane defaults that work for 95%; make the rest optional.

## The pattern (what to look for)
- Duplicated flows handling “almost the same” data or behavior.
- Everywhere checks like “if A then … else if B … else if C …”.
- Boilerplate branching that only differs in source/transport/format.
- Parallel systems that could be unified behind a shared contract.

## Examples
- Stream abstraction
  - Before: Separate handlers for batch/real-time/file/network.
  - Insight: All inputs are streams with different sources.
  - After: One stream processor; sources plug in via adapters.
  - Deleted: 4 bespoke pipelines.
- Resource governance
  - Before: Separate modules for sessions, rate limiting, file validation, pooling.
  - Insight: All enforce per-entity resource limits.
  - After: One ResourceGovernor with resource types.
  - Deleted: 4 custom enforcement systems.
- Immutability
  - Before: Defensive copying, locking, cache invalidation.
  - Insight: Data as immutable values + pure transformations.
  - After: Functional patterns; simpler reasoning.
  - Deleted: Entire classes of synchronization code.

## Process
- List variations: enumerate duplicated or parallel implementations.
- Find the essence: identify what’s the same underneath.
- Extract the abstraction: a domain-independent interface or pattern.
- Fit the cases: ensure each current case maps cleanly with minimal adapters.
- Measure the cascade: count components, branches, and configs removed.

## Red flags you’re missing a cascade
- “We just need to add one more case” keeps repeating.
- “These are all similar but different” without clear invariants.
- Refactors feel like whack-a-mole; changes break siblings elsewhere.
- Config files grow; more flags instead of fewer concepts.
- “Don’t touch that, it’s complicated” masks unify-able patterns.

## Success criteria
- Fewer concepts and files; parallel implementations removed.
- Reduced branching and special-case code paths.
- Smaller configuration surface with strong defaults.
- Simpler interfaces; clearer contracts and invariants.
- Measurable deletion: net negative LOC while increasing clarity.

## Integration with existing rules
- Quality-first engineering: prefer repo-wide codemods to consolidate patterns; remove obsolete paths in the same change where feasible.
- Systematic debugging: after 3 failed fix attempts across variants, reassess architecture for a unifying abstraction.

## Enforcement
- PRs that add complexity must justify why unification isn’t feasible now and include a concrete consolidation plan.
- Include a “deletion metric” (files/branches/configs removed or planned) when proposing an abstraction.
- Avoid indefinite “old + new”: plan and execute migration; remove the old path during rollout.
