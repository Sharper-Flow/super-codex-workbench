# Codex Workbench · Batteries‑Included for Codex CLI 🚀

<!-- Badges -->
<p align="center">
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

Turn ideas into data, reports, and APIs — fast. This workspace is purpose‑built for
Codex CLI users who want an agent‑first, fully provisioned environment with clear rules,
great logging, warehouse patterns, and out‑of‑the-box workflows.

## What Is It?
- A ready‑to‑use workspace where Codex CLI can gather data, store it safely, and turn it into
  clean reports. Think: “one folder where everything just works.”
- Comes prewired with a data warehouse (CSV/JSONL/Parquet), SQL via DuckDB, HTML→PDF, Excel,
  strict Python tooling, and optional MCP‑backed web context (Firecrawl + Context7).

## Why This Instead of Starting From Scratch?
- 🧰 Everything you need is included and consistent — no yak shaving.
- 🧱 Safe, simple patterns for storing data and outputs (per‑project folders).
- 🌈 Great logs by default, so debugging is friendly and human.
- 🪟 Windows‑friendly onboarding (Terminal, Nerd Font, WSL2 Ubuntu) with one script.
- 🧪 Quality gates on every change (ruff + mypy) keep things reliable as you grow.

## Who Is This For?
- New to programming and want a guided, safe place to explore data + reports.
- Power users who want a structured, repeatable environment for day‑to‑day work.
- Teams who plan to standardize how agents (Codex CLI) interact with a local workspace.

## How It Works (In 60 Seconds)
1) Pick a project: `projects create` or `projects resume`. Everything you do lives under that name.
2) Ingest data: write datasets via the Warehouse API (CSV/JSONL/Parquet, partitioned by date/source).
3) Query: use DuckDB SQL against auto-registered views (`ds_<dataset>`).
4) Report: render HTML with Jinja2 and export to PDF/Excel. Outputs land under `projects/<current>/reports`.

## Actions at a Glance
- 🔧 Setup once: `bash scripts/setup.sh -y -p demo -s`
- 🗂️ Resume or create a project: `uv run python main.py projects list`
- 🏗️ Land sample data + report (guided): `uv run python main.py workflow first-project --name demo`
- 🧠 Query warehouse: `uv run python main.py warehouse sql --query "select * from ds_events_demo limit 5"`
- 🌐 Pull web context: `uv run python main.py workflow mcp-web --url https://example.com --limit 5`
- 📦 Package check: `cd codex && ./scripts/check.sh`

## Operate With Codex CLI
- All work in this repo should be driven via the Codex CLI assistant.
- Codex CLI is authorized to:
  - Install Python packages with `uv` as needed to complete tasks.
  - Use configured MCP servers (Context7, Firecrawl) via `mcp.config.json` and env vars in `.env`.
  - Scaffold files/folders, generate reports, and organize outputs while preserving the structure below.
- Conventions to preserve:
  - Always use `.venv` (`uv run ...`) and record dependencies in `pyproject.toml` + `uv.lock`.
  - Persist canonical data via the Warehouse API under `warehouse/`.
  - Place app-specific logic under `apps/`, and reports under `reports/`.
  - Manage named work contexts under `projects/` and keep `projects/manifest.json` current. Codex CLI should:
    - Ask whether to resume an existing project at session start.
    - Offer names from `projects context --json` and set current via `projects resume --name <NAME>`.
    - Create new projects with `projects create --name <NAME> [--desc ...]` when starting fresh.
  - For big data tasks, Codex CLI may install `pyarrow` and `duckdb` to enable Parquet IO and SQL over datasets.
  - For HTML→PDF, Codex CLI may install `weasyprint` or `pdfkit` (plus `wkhtmltopdf`).
  - For MCP‑backed web data, set `FIRECRAWL_API_KEY` (and optional `FIRECRAWL_BASE_URL`),
    `CONTEXT7_API_KEY` (optional; free tier usually works) and `CONTEXT7_BASE_URL` if needed.
    - Verify: `uv run python main.py mcp info` and `uv run python main.py check-mcp`.
  - Response style in this repo: concise headers, tight bullets, and tasteful emoji for clarity.

## Contents
- `AGENTS.md` — guidance for agents and contributors working in `codex-workbench/`.
- `.editorconfig` — consistent editor settings (LF, UTF-8, indentation).
- `.gitignore` — generic ignores for common toolchains.
- `warehouse/` — canonical datasets managed via the Warehouse API.
- `apps/` — app-specific code that uses the Warehouse API.
- `projects/` — named work contexts (resumable), manifest and current pointer.

## Showcase
- Windows Terminal theme (CodexDarkGrey) + Nerd Font

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)

- Sample HTML report preview

  ![Sample report preview](docs/images/report-preview.svg)

## Getting Started (WSL2 Ubuntu)
- Prefer working inside Linux home (e.g., `/home/<user>/...`) for performance.
- Ensure LF endings in editors; avoid CRLF.
- To open Windows Explorer here: `explorer.exe .`
- To open a file in Windows default app: `wslview <file>` (install with `sudo apt install wslu` if missing).
- On Windows (optional): Run `scripts/windows-setup.ps1` as Administrator to install Windows Terminal, CaskaydiaCove Nerd Font, Starship, enable WSL2, install Ubuntu LTS, and apply a dark grey theme. Example:
  - Open PowerShell (Admin) and run: `Set-ExecutionPolicy Bypass -Scope Process -Force; cd <repo>\codex\scripts; .\windows-setup.ps1 -ProvisionWSL -DefaultProfile Ubuntu`
  - With `-ProvisionWSL`, the script also configures zsh (Oh My Zsh, autosuggestions, syntax highlighting), fzf keybindings, Starship prompt, and attempts to set zsh as default.

## Quickstart
- Run initial setup:
  - `bash scripts/setup.sh` (or `bash scripts/setup.sh -y -p demo -s` for non-interactive + sample)
- Create a virtual env and install deps (managed by `uv`):
  - `uv run python -V` (uses `.venv` created automatically)
  - `uv sync` (re-sync deps if `pyproject.toml` changes)
- Run the app (Typer CLI):
  - `uv run python main.py hello --name Alice`
  - `uv run python main.py check-mcp` (check MCP vars)
  - Increase verbosity with `-v` or `-vv` to show rich-formatted logs.
  - Initialize folders: `uv run python main.py init`
  - Sample outputs:
    - Excel: `uv run python main.py make-excel`
    - PDF: `uv run python main.py make-pdf`
  - Warehouse:
    - List: `uv run python main.py warehouse list`
    - Register: `uv run python main.py warehouse register --name events --format csv --partitioning date`
    - Write sample: `uv run python main.py warehouse write-sample --name events --partition date=$(date -u +%F)`
    - Show: `uv run python main.py warehouse show --name events --limit 5`
    - SQL (DuckDB): `uv run python main.py warehouse sql --query "select * from ds_events limit 5"`
    - Save result: add `--output reports/excel/query.csv` or `.parquet`
  - Projects:
    - Create: `uv run python main.py projects create --name myproj --desc "Short description"`
    - List: `uv run python main.py projects list` (shows `*` next to current)
    - Resume: `uv run python main.py projects resume --name myproj`
    - Context JSON (for Codex CLI): `uv run python main.py projects context --json`
  - Workflow (end-to-end demo):
    - `uv run python main.py projects create --name demo --desc "Demo project"`
    - `uv run python main.py workflow first-project --name demo`
    - Outputs are written under `projects/<current>/` when a current project is set:
      - Aggregation CSV: `projects/<current>/artifacts/agg.csv`
      - HTML report: `projects/<current>/reports/html/workflow.html`
      - PDF report: `projects/<current>/reports/pdf/workflow.pdf` (if PDF backend installed)
  - Reports:
    - Render HTML from template: `uv run python main.py reports render-html --template sample.html.j2 --output reports/html/sample.html`
    - Export HTML to PDF: `uv run python main.py reports export-pdf --html reports/html/sample.html --output reports/pdf/from_html.pdf`
      - If backend missing, Codex CLI may install `weasyprint` or `pdfkit` and `wkhtmltopdf`.
  - MCP helpers:
    - Show configured MCP servers and env presence: `uv run python main.py mcp info`
  - MCP workflow (web-backed):
    - Firecrawl crawl with optional Context7 search, then render a combined report:
      - `uv run python main.py workflow mcp-web --url https://example.com --c7-query "keyword" --limit 5`
    - Outputs land under the current project (if set). Otherwise, falls back to top-level `reports/`.
  - Diagnostics:
    - Quick snapshot: `uv run python main.py diagnose`
    - JSON output (for Codex CLI ingestion): `uv run python main.py diagnose --json`

## Example Session (Transcript)
```bash
# 1) Initial setup (Linux/WSL)
bash scripts/setup.sh -y -p demo

# 2) Verify environment
uv run python main.py -v diagnose

# 3) Create/select a project (if not already via setup)
uv run python main.py projects create --name demo --desc "First project"
uv run python main.py projects list

# 4) Land sample data and produce outputs (guided)
uv run python main.py workflow first-project --name demo

# 5) Query the warehouse
uv run python main.py warehouse sql --query "select * from ds_events_demo limit 5"

# 6) Render a custom report from a template
uv run python main.py reports render-html --template sample.html.j2 --output reports/html/sample.html
uv run python main.py reports export-pdf --html reports/html/sample.html --output reports/pdf/sample.pdf
```
- Environment:
  - Copy `.env.example` to `.env` and set keys.
  - Load `.env` in your code using `python-dotenv` as needed.

## Suggested Workflow
- Keep tasks small and documented as you go.
- For scripts, add a one-line usage comment and `chmod +x`.
- If you add dependencies, document install steps for Ubuntu.
  - Prefer Parquet for large datasets (`uv add pyarrow`) and use Warehouse API.

## Python Tooling (required)
- Data models: use Pydantic v2+ strict models (inherit from `workbench.models.StrictBaseModel`).
- Lint/format: Ruff; static typing: Mypy.
- After EVERY code change, run checks and fix issues:
  - `cd codex && ./scripts/check.sh`
  - This runs: `ruff format`, `ruff check --fix`, and `mypy` with `mypy.ini`.

What you get out‑of‑the‑box
- ✅ Strict Python project with `uv` dependency management
- 📦 Warehouse API (CSV/JSONL/Parquet) + DuckDB SQL views (`ds_<dataset>`)
- 🧱 Project contexts with resumable manifests under `projects/`
- 📝 Jinja2 templates + HTML→PDF (WeasyPrint/pdfkit)
- 📊 Excel generation via Pandas + openpyxl
- 🧭 MCP‑ready hooks for Context7 + Firecrawl
- 🌈 Rich+Loguru logging with `-v`/`-vv` verbosity

## MCP Configuration
- Edit `mcp.config.json` with URLs and keys for Context7 and Firecrawl.
- Set environment variables in `.env` or your shell: `CONTEXT7_API_KEY`, `CONTEXT7_MCP_URL`, `FIRECRAWL_API_KEY`, `FIRECRAWL_MCP_URL`.
 - Setup state is tracked in `setup-requirements.json`. Codex CLI should ensure required items are true and run `bash scripts/setup.sh -y` if not.

Policy & safety
- 🛡️ Codex CLI must read `setup-requirements.json`; if required items are missing/false, assume
  fresh setup and run `scripts/setup.sh -y`.
- 🔑 Firecrawl requires an API key; Context7 is optional (free tier assumed).
- 🧹 Keep outputs organized under the current project; default to top‑level when none is set.

## Notes
- This workspace is intentionally lightweight. Add subfolders (`notes/`, `scripts/`, `docs/`) as needs emerge.
 - Logging uses Loguru with Rich formatting and tracebacks. Prefer `logger.info/debug/...` for diagnostics.

Next steps
- 💡 Create a project: `uv run python main.py projects create --name research`
- 🔎 Pull web context: `uv run python main.py workflow mcp-web --url https://example.com --limit 5`
- 🧪 Add a dataset and query it: register, write sample, then run `warehouse sql`
