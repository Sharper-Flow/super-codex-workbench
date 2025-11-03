**Purpose**
- Adaptation of integration notes for this repository’s MCP setup and Codex CLI workflows.
- Replaces project‑specific references with safe, repo‑aligned guidance.

**Scope**
- Firecrawl and Context7 MCP servers configured via `.env` + `mcp.config.json`.
- Usage via the existing CLI (`main.py`) and workflows defined in `AGENTS.md`.

**Repo-Specific Overrides** ✅
- Primary: follow `AGENTS.md` for setup, MCP, and reporting.
- Environment: run everything with `uv run <cmd>`; never use system Python/pip.
- Checks: run `./scripts/check.sh` after changes; fix Ruff/Mypy issues.
- Git: checkpoint with `./scripts/git-save.sh "chore: checkpoint"` or appropriate type.

**Configuration** 🔧
- Required env vars in `.env` (see `.env.example`):
  - `FIRECRAWL_API_KEY`, `FIRECRAWL_MCP_URL`
  - `CONTEXT7_API_KEY` (optional), `CONTEXT7_MCP_URL`
- Verify status:
  - `uv run python main.py mcp info`
  - `uv run python main.py check-mcp`

**Common Workflows** 🚀
- Web context and summarization:
  - `uv run python main.py workflow mcp-web --url <URL> [--c7-query <q>] --limit 5`
- First project (guided):
  - `uv run python main.py workflow first-project --name <NAME> [--with-mcp]`

**Data Handling** 📦
- Use Warehouse API only; do not write under `warehouse/` directly.
- Query with DuckDB via CLI; prefer Parquet for larger outputs.

**Reporting** 📝
- Render: `uv run python main.py reports render-html --template <tpl>`
- Export PDF: `uv run python main.py reports export-pdf [--html ...]`
- If HTML→PDF fails, install backend: `weasyprint` or `pdfkit` + `wkhtmltopdf`.

**Troubleshooting** 🛠️
- Missing keys: add to `.env`, rerun `uv sync` if deps change, then re‑verify MCP.
- Network/API errors: confirm endpoints in `mcp.config.json` and env var values.

This document intentionally avoids project‑specific assumptions and aligns with this repo’s rules and tooling.
