# Codex CLI Rule Bank

This folder contains a curated set of agent rules originally authored for another project, adapted for this repository and Codex CLI. Treat these as secondary guidance that complements (and never overrides) the primary rules in `AGENTS.md`.

Repo-Specific Overrides (Read First) ✅
- Primary source: `AGENTS.md` (takes precedence over anything here).
- Environment: use `uv` + local `.venv` only; run commands via `uv run <cmd>`.
- Checks: after any code/deps change, run `./scripts/check.sh` (Ruff format+lint, Mypy) and fix issues.
- Git: checkpoint work with `./scripts/git-save.sh "<type>: <summary>"`; push with `./scripts/git-push.sh`.
- Project context: set/resume with `uv run python main.py projects context|resume|create`.
- Data: use the Warehouse API only; never write directly under `warehouse/`.
- MCP: Firecrawl/Context7 via `.env` + `mcp.config.json`; verify with `uv run python main.py mcp info`.
- Reports: render via CLI (`reports render-html`, `reports export-pdf`).
- Response style: short headers, tight bullets, and tasteful emoji (see `AGENTS.md`).

Included Documents 💼
- Decision clarity: `decision-clarification.md`
- Quality mindset: `quality-first-engineering.md`
- Reflection and simplification: `self-improving-reflection.md`, `simplification-cascades.md`
- Debugging workflow: `systematic-debugging.md`
- Python/runtime discipline: `python-environment.md`, `workspace-venv.md`
- MCP/Integrations: `mcp-integrations.md` (adapted)
- Speckit workflows: `workflows/speckit.*.md`

How To Use 🚀
- Start with `AGENTS.md` for repository rules and workflows.
- Consult these files for decision frameworks and execution checklists.
- Always apply the repo’s environment discipline (uv, checks, MCP, projects) when following any guidance here.
