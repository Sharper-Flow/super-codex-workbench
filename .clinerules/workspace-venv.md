## Brief overview
- Project-specific rule: always use the workspace `.venv` virtual environment for all local Python development and package operations.
- Purpose: ensure reproducible development environments, consistent dependency management, and predictable CI/local parity.
**Workspace + Venv Discipline**

**Principles** ✅
- Work from the repo root; default outputs under `projects/<current>/...`.
- Use `uv run <cmd>` so the local `.venv` is always used.
- Never write directly to `warehouse/`; use the Warehouse API.

**Project Context** 📂
- Check: `uv run python main.py projects context --json`
- Resume: `uv run python main.py projects resume --name <NAME>`
- Create: `uv run python main.py projects create --name <NAME>`

**Quality Gates** 🛡️
- After changes: `./scripts/check.sh` (Ruff + Mypy)
- Save progress: `./scripts/git-save.sh "chore: checkpoint"`

**Tips** 💡
- Avoid system Python; avoid ad hoc virtualenvs.
- Prefer `uv run` over manual activation for consistency.
## Virtual environment rule
- Always activate and use the repository-root `.venv` for any Python commands, running tests, or installing packages.
- Do not create or use virtual environments outside of the workspace `.venv` (no per-feature venvs, global envs, or ad-hoc venvs).
- If `.venv` is intentionally absent, obtain explicit confirmation from the project owner before creating a new venv.

## Activation & common commands
- POSIX (macOS / Linux / zsh / bash):
  - Activate: `source .venv/bin/activate`
  - Deactivate: `deactivate`
- Windows (PowerShell / cmd) — mention only as cross-platform note:
  - PowerShell: `.venv\Scripts\Activate.ps1`
  - cmd: `.venv\Scripts\activate.bat`
- Run Python inside the venv explicitly if needed: `.venv/bin/python <script>` (POSIX) to avoid ambiguous interpreter selection.

## Package management
- Use the workspace's approved package manager wrapper for all installs/updates/removals (follow the project's existing rule: use `uv` for package operations).
  - Example: `uv pip install <package>` rather than calling `pip install` directly.
- Do not run `pip` or other global package managers outside the `.venv` unless a maintainer instructs otherwise.
- When adding or upgrading packages:
  - Activate `.venv` first.
  - Update lockfiles or dependency manifests per project practice (e.g., update pyproject / poetry / requirements as applicable).

## CI, automation, and scripts
- Local scripts and automation should assume `.venv` exists and is used during local development.
- CI systems may create isolated environments; ensure CI scripts use reproducible dependency definitions exported from the workspace environment (lockfiles, pyproject, etc.).
- Document any deviation in the project's docs; do not silently rely on developer-local global packages.

## Exceptions & troubleshooting
- If `.venv` is missing:
  - Ask the project owner/maintainer before creating it.
  - If approved, create the venv using a minimal, explicit command (e.g., `python -m venv .venv`) and then install dependencies via the approved package flow.
- If activation fails, report the exact error and system shell (e.g., "zsh on Linux") so the issue can be diagnosed.
- Temporary use of alternative tools (containers, remote interpreters) is allowed only with explicit agreement and documented in the repository.

## Enforcement & checks
- During reviews and onboarding, verify contributors use `.venv` locally (spot-check activation commands in dev instructions or PR notes).
- Prefer small, clear documentation in README or docs/ showing how to activate `.venv` for new contributors.

## Examples
- Correct: `source .venv/bin/activate` → `uv pip install requests`
- Incorrect: `pip install requests --user` (installs to user environment, not `.venv`)
