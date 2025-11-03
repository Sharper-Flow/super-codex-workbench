---
description: Execute the fix workflow to clear lint, formatting, and type-check issues reported by IDE tooling.
---

## User Input

```text
$ARGUMENTS
```

The `/fix` command does not accept free-form arguments. If any input is provided, acknowledge it but proceed with the standard workflow unless the user explicitly changes scope.

## Outline

1. **Run automated fix script**: From the repo root execute `.specify/scripts/bash/run-fix.sh`. The script applies Ruff and Black formatting, runs Ruff lint with fixes, then executes Ruff, mypy, and Pyright verification. It stops at the first failure.
2. **Resolve failures iteratively**:
   - For formatter or Ruff failures, edit the reported files to satisfy the rules (or rerun the script after manual adjustments).
   - For mypy/Pyright diagnostics, update the code or typing annotations to eliminate errors. Prefer targeted changes that align with the project constitution and Spec Kit artifacts.
   - Re-run the script after each fix to ensure earlier stages still pass.
3. **Document blockers**: If a diagnostic cannot be resolved without new guidance, annotate the response with up to three `[NEEDS CLARIFICATION: …]` items summarizing options and impacts.
4. **Finish**: Stop when the script completes all stages successfully and no tools report outstanding issues.

## Notes

- Pylance does not provide a standalone CLI. Pyright serves as the authoritative CLI check for Pylance parity. Surface any discrepancies if IDE diagnostics differ.
- Keep fixes tightly scoped to the reported problems; avoid opportunistic refactors.
- Capture essential command output in your response so the user understands what was fixed.
