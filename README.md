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

## Quick Start (Users)
- Target audience: first‑time Codex CLI users. You won’t run Python commands — you will prompt Codex CLI and it will operate this repo for you.

### Windows (Recommended)
- 1) Prepare Windows + WSL2 (Admin PowerShell):
  ```powershell
  # From the repo folder on Windows
  powershell -ExecutionPolicy Bypass -File .\scripts\windows-setup.ps1 -ProvisionWSL -DefaultProfile Ubuntu
  ```
  - Installs Windows Terminal, Nerd Font, WSL2 + Ubuntu, and applies a clean theme.
  - If prompted to create a UNIX user in Ubuntu, complete that step.

- 2) Copy this repo into Ubuntu (WSL2):
  - Option A (Explorer): open `\\wsl$\Ubuntu\home\<your-username>\` and drag‑drop this repo folder (e.g., `codex`).
  - Option B (Git in Ubuntu): open an Ubuntu tab, then:
    ```bash
    cd ~ && git clone <your-repo-url> codex && cd codex
    ```

- 3) Install Codex CLI (in Ubuntu)
  - Follow Codex CLI’s official installation instructions, then verify `codex` runs in Ubuntu.
  - Open Ubuntu in Windows Terminal, `cd ~/codex`.

- 4) Launch Codex CLI from the repo
  - Start Codex CLI in this folder and interact using prompts (see “Try These Prompts”).

### Linux/macOS
- Ensure a modern terminal, Git, and Codex CLI are installed.
- Clone this repo locally and start Codex CLI in the repo folder, then use the prompts below.

## Try These Prompts
- Setup (one‑time, fully guided):
  - “Set up the workspace with a demo project and run the guided first‑project workflow.”
  - “Run diagnostics and verify MCP configuration.”

- Project context:
  - “List available projects and resume ‘demo’ (or create it if missing).”
  - “Show the current project and recent projects.”

- Data + SQL:
  - “Register a dataset named ‘events_demo’, land a small sample batch, and preview the first rows.”
  - “Run a DuckDB query that counts events by type and save the result to my project artifacts.”

- Reports:
  - “Render a sample HTML report titled ‘My Report’ under the current project.”
  - “Export that HTML report to PDF; if missing, install a PDF backend and try again.”

- MCP (optional):
  - “Crawl https://example.com (limit 5) and generate a quick HTML summary report.”
  - “Also run a Context7 search for ‘site:example.com key topics’ and include results.”

## What The Agent Does
- Creates a local Python env with `uv` inside this repo when needed.
- Initializes project folders and selects a current project for outputs.
- Writes datasets into the warehouse and exposes DuckDB SQL views.
- Renders HTML and exports PDF/Excel into your project’s `reports/`.
- Uses MCP (if configured) to crawl the web or fetch context, then compiles a report.

## Troubleshooting
- ⚠️ Codex CLI not installed: follow its official install guide for Linux/macOS or run it inside Ubuntu (WSL2) on Windows.
- ⚠️ PDF export fails: ask Codex CLI to install a PDF backend (WeasyPrint or pdfkit + wkhtmltopdf) and re‑run the export step.
- ⚠️ MCP missing: add `FIRECRAWL_API_KEY` to `.env` (Context7 is optional), then ask Codex CLI to verify MCP.

## For Contributors
- Agent/coder instructions live in `AGENTS.md` (environment discipline, checks, MCP, and tooling). Keep user‑facing README prompt‑oriented.

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
