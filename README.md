# Super Codex Workbench · Batteries‑Included for Codex CLI 🚀

<!-- Banner -->
<p align="center">
  <img src="docs/images/repo-banner.svg" alt="Super Codex Workbench banner" width="720" />
<br/>
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge"></a>
  <a href="https://astral.sh/uv/"><img alt="uv" src="https://img.shields.io/badge/deps-managed%20by%20uv-2D3748?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/badge/lint-Ruff-ff3860?style=for-the-badge&logo=ruff&logoColor=white"></a>
  <a href="https://github.com/python/mypy"><img alt="Mypy" src="https://img.shields.io/badge/types-Mypy-5383EC?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://pandas.pydata.org/"><img alt="Pandas" src="https://img.shields.io/badge/data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"></a>
  <a href="https://duckdb.org/"><img alt="DuckDB" src="https://img.shields.io/badge/sql-DuckDB-FFCB05?style=for-the-badge&logo=duckdb&logoColor=black"></a>
  <a href="https://firecrawl.dev/"><img alt="Firecrawl" src="https://img.shields.io/badge/web-Firecrawl-F97316?style=for-the-badge"></a>
  <a href="https://context7.dev/"><img alt="Context7" src="https://img.shields.io/badge/context-Context7-0EA5E9?style=for-the-badge"></a>
</p>

<p align="center"><em>Made with ❤️ for friends by <strong>Sharper Flow LLC</strong></em></p>

Turn ideas into data, reports, and APIs — fast. This repo is an agent‑first workbench for
Codex CLI: strict tooling, clean patterns, and ready‑made workflows with optional MCP context.

## Highlights
- ✅ Batteries‑included: uv deps, Ruff + Mypy, Pandas/DuckDB, Jinja2, HTML→PDF.
- 🗂️ Project‑aware: all outputs under `projects/<name>/...` with easy resume.
- 📦 Warehouse API: CSV/JSONL/Parquet with DuckDB SQL views (`ds_<dataset>`).
- 🌐 MCP‑ready: Firecrawl + Context7 helpers and a crawl→report workflow.
- 🧪 Friendly dev rig: logs, checks, and sample flows that “just work”.

## Quick Start
- Prereqs: install `uv` and ensure it’s on PATH.
- One‑time setup (creates venv, syncs deps, initializes folders):

```bash
bash ./scripts/setup.sh -y -p demo
uv run python main.py -v diagnose
```

- Guided first project (lands data, runs SQL, renders HTML/PDF):

```bash
uv run python main.py workflow first-project --name demo
```

## Usage

### Projects
- Create and set current:
  ```bash
  uv run python main.py projects create --name demo --desc "Demo project"
  uv run python main.py projects context --json
  ```
- Resume later:
  ```bash
  uv run python main.py projects resume --name demo
  uv run python main.py projects list
  ```

### Warehouse (data)
- Register a dataset with partitions and write a sample batch:
  ```bash
  uv run python main.py warehouse register --name events_demo --format csv --partitioning date,source
  uv run python main.py warehouse write-sample --name events_demo --partition date=2025-01-01,source=seed
  uv run python main.py warehouse show --name events_demo --limit 5
  ```
- Run SQL via DuckDB over auto‑views (`ds_<dataset>`); save to CSV/Parquet:
  ```bash
  uv run python main.py warehouse sql --query "select event, count(*) as n from ds_events_demo group by event" --limit 10 --output projects/demo/artifacts/events_agg.csv
  # Parquet requires pyarrow
  uv add pyarrow
  uv run python main.py warehouse sql --query "select * from ds_events_demo" --limit 1000 --output projects/demo/artifacts/events.parquet
  ```

### Reports
- Render HTML with Jinja2 (project templates override global ones):
  ```bash
  uv run python main.py reports render-html --template sample.html.j2 --title "My Report" --output projects/demo/reports/html/sample.html
  ```
- Export HTML→PDF (tries WeasyPrint, then pdfkit if available):
  ```bash
  uv run python main.py reports export-pdf --html projects/demo/reports/html/sample.html --output projects/demo/reports/pdf/sample.pdf
  # If no backend installed, pick one:
  uv add weasyprint    # or: uv add pdfkit  (and install system wkhtmltopdf)
  ```

### Workflows
- End‑to‑end demo (lands data → SQL → HTML → PDF under current project):
  ```bash
  uv run python main.py workflow sample
  ```
- First‑project guide (creates/selects project and runs the demo):
  ```bash
  uv run python main.py workflow first-project --name demo [--with-mcp]
  ```

### MCP (optional, recommended)
- Set env vars in `.env` (see `.env.example`) then verify:
  ```bash
  uv run python main.py mcp info
  uv run python main.py check-mcp
  ```
- Crawl the web with Firecrawl and generate a report:
  ```bash
  # Requires FIRECRAWL_API_KEY in .env
  uv run python main.py workflow mcp-web --url https://example.com --limit 5
  ```
- Add an MCP server entry (helper script):
  ```bash
  ./scripts/mcp-add.sh firecrawl https://your-firecrawl-sse-endpoint FIRECRAWL_API_KEY
  ```

## Examples

### 1) Project → Warehouse → Report
- Initialize, create project, land data, run SQL, export outputs:
  ```bash
  bash ./scripts/setup.sh -y -p demo
  uv run python main.py projects resume --name demo
  uv run python main.py warehouse write-sample --name events_demo --partition date=2025-01-01,source=seed
  uv run python main.py warehouse sql --query "select event, count(*) n from ds_events_demo group by event" --output projects/demo/artifacts/agg.csv
  uv run python main.py reports render-html --template sample.html.j2 --output projects/demo/reports/html/agg.html --title "Events Aggregation"
  uv run python main.py reports export-pdf --html projects/demo/reports/html/agg.html --output projects/demo/reports/pdf/agg.pdf
  ```

### 2) MCP Crawl → HTML/PDF Report
- With Firecrawl configured, crawl and render a site summary:
  ```bash
  uv run python main.py workflow mcp-web --url https://example.com --limit 5 --c7-query "site:example.com key topics"
  ```

### 3) HTML→PDF Backends
- If HTML→PDF fails, install a backend:
  ```bash
  # Option A: WeasyPrint (may need system deps)
  uv add weasyprint
  # Option B: pdfkit + wkhtmltopdf
  uv add pdfkit && sudo apt-get install -y wkhtmltopdf
  ```

## Troubleshooting
- ⚠️ `uv` not found: install via `curl -LsSf https://astral.sh/uv/install.sh | sh` and ensure `~/.local/bin` on PATH.
- ⚠️ Parquet write fails: `uv add pyarrow` to enable `DataFrame.to_parquet`.
- ⚠️ HTML→PDF fails: install `weasyprint` or `pdfkit` + system `wkhtmltopdf` (see above).
- ⚠️ No current project: create/resume with `projects create` or `projects resume`.
- ⚠️ MCP not configured: set `FIRECRAWL_API_KEY` and optionally `CONTEXT7_API_KEY` in `.env`, then `uv run python main.py mcp info`.

## Dev Workflow
- Run checks (format, lint, types):
  ```bash
  ./scripts/check.sh
  ```
- Make local git checkpoints (conventional commits encouraged):
  ```bash
  ./scripts/git-save.sh "docs: refresh README with detailed usage"
  # optional: ./scripts/git-push.sh
  ```

## Showcase
- Windows Terminal theme (CodexDarkGrey) + Nerd Font

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)

- Sample HTML report preview

  ![Sample report preview](docs/images/report-preview.svg)

## Reference
- Full agent/operator guidance lives in `AGENTS.md` (strongly recommended for Codex CLI usage).
- Quick commands (from repo root):
  - Setup once: `bash ./scripts/setup.sh -y -p demo`
  - Diagnose: `uv run python main.py -v diagnose`
  - First project: `uv run python main.py workflow first-project --name demo`
  - MCP crawl: `uv run python main.py workflow mcp-web --url https://example.com --limit 5`
  - Checks: `./scripts/check.sh`

## License
MIT — see `LICENSE`.
