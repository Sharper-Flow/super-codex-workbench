## Brief overview
- Project-specific guidelines for Python development environment and package management in this workspace.
- Ensures consistent tooling across all Python-related tasks.
**Python Environment (Repo-Specific)**

**Principles** ✅
- Use `uv` with the local `.venv` at the repo root.
- Never use system `python`/`pip` for this project.
- Prefer `uv run <cmd>` over activating the venv directly.

**Setup** 🔧
- Ensure `uv` is installed and on PATH.
- Sync deps: `uv sync`
- Diagnose: `uv run python main.py -v diagnose`

**Everyday Commands** 🚀
- Run CLI: `uv run python main.py <command>`
- Checks (format + lint + types): `./scripts/check.sh`
- MCP status: `uv run python main.py mcp info`

**Adding/Removing Deps** 📦
- Add: `uv add <package>`
- Remove: `uv remove <package>`
- Commit changes to `pyproject.toml` and `uv.lock`.

**Conventions** 🧩
- Do not introduce alternative environment tools.
- Keep changes minimal and reversible; follow `AGENTS.md`.
## Virtual environment
- Always use the workspace `.venv` directory for Python virtual environments.
- Activate `.venv` before running Python commands or installing packages.
- Do not create virtual environments in other locations.

## Package management
- Use `uv` for all package operations (install, update, remove).
- Do not use `pip` for package management.
- Example: `uv pip install <package>` instead of `pip install <package>`.
