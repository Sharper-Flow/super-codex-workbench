## Brief overview
- Global guideline enabling continuous improvement of `.clinerules` from real interactions.
- Triggered before finalizing complex tasks or those involving user feedback.
- Focuses on proposing concise, actionable rule updates aligned with explicit user preferences.

## When to trigger reflection
- Trigger if any of the following are true during the current task:
  - The user provided feedback at any point (corrections, preferences, constraints, style guidance).
  - The task involved multiple non-trivial steps (e.g., several file edits, cross-module changes, complex logic).
- Do not trigger if:
  - No `.clinerules` were active for the workspace.
  - The task was trivial and involved no feedback (e.g., a single small edit or a quick answer).

## Reflection workflow
- Ask once, verbatim: “Before I complete the task, would you like me to reflect on our interaction and suggest potential improvements to the active `.clinerules`?”
- If the user declines or does not affirmatively respond, proceed directly to completion.
- If the user confirms:
  - Review interaction history for explicit feedback, patterns, and preferences.
  - Identify which global and workspace `.clinerules` files were active (by filename).
  - Propose precise, minimal improvements targeted at the relevant files.
  - Ask for approval to apply the changes now; if approved, apply updates, then proceed to completion.

## How to analyze feedback
- Extract only explicit preferences and corrective feedback (avoid inferring tastes without evidence).
- Map each piece of feedback to: naming, style, architecture, workflow, testing, UI/UX, or tool usage.
- Prefer converting recurring directives into short, concrete rules rather than narrative explanations.

## Proposing rule changes
- Prioritize suggestions that directly address the user’s feedback for this workspace.
- Keep rules:
  - Concise, non-redundant, and scoped to the behavior being clarified.
  - Formatted as headings with bullet points (consistent with `.clinerules` style).
  - Free of conversation recap; capture stable guidance, not history.
- When practical, propose a `replace_in_file` diff block for targeted edits; otherwise, clearly specify new content to add under specific headings.

## Identifying active rules
- List the specific rule files in play (e.g., global defaults and any workspace `.clinerules/*.md`).
- Read them to avoid duplication, ensure consistency, and place updates in the most appropriate file (or propose a new file if introducing a new concept).

## Applying changes
- Only modify files after explicit user approval.
- Use the appropriate edit method:
  - `replace_in_file` for targeted changes with diff blocks.
  - Create a new `.md` file when introducing a new concept; use hyphenated filenames and succinct names.
- Maintain Markdown heading structure and bullet formatting consistent with existing rules.

## Edge cases
- If `.clinerules` do not exist or are inactive: skip reflection and proceed to completion.
- If feedback conflicts with existing rules: flag the conflict and propose a minimal, consistent resolution path.
- Avoid including sensitive or user-specific data; codify the principle behind it instead.

## Communication style during reflection
- Be direct and technical; keep proposals concise and scannable.
- Offer improvements once per task (avoid repeated prompts).
- Use the exact one-line question for reflection offer; avoid additional qualifiers or softeners.

## Success criteria
- Proposed changes are specific, minimal, and clearly improve alignment with the user’s demonstrated preferences.
- Rules remain concise, easy to maintain, and actionable in future tasks without restating conversation history.
