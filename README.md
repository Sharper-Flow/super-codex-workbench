# Super Codex Workbench · Batteries‑Included for Codex CLI 🚀

<!-- Banner -->
<p align="center">
  <img src="docs/images/repo-banner.svg" alt="Super Codex Workbench banner" width="720" />
</p>

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
- 🌈 Great logs by default, so debugging is friendly.
- 🪟 Windows‑friendly onboarding with one script.

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
- 🔧 Setup once (prompt): “Set up the workspace for me with a demo project and run the guided first‑project workflow.”
- 🗂️ Project context (prompt): “Show my projects and resume ‘demo’ (or create it if missing).”
- 🧠 Query warehouse (prompt): “Preview the latest rows for the events dataset using DuckDB SQL.”
- 🌐 MCP web context (prompt): “Crawl https://example.com, summarize the top pages, and generate a quick report.”
- 📦 Code quality (prompt): “Run the repository checks and fix any formatting or typing issues.”

## Operate With Codex CLI
- Use the agent‑first flow documented in `AGENTS.md` (setup, project context, warehouse, reporting, MCP).
- Talk to Codex CLI with clear prompts (examples above) — no need to run Python commands directly.

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

## Get Started (Talk to Codex CLI)
Ask Codex CLI:
- “Run the setup and create a project named ‘demo’. Then verify the environment.”
- “Run the first‑project workflow for ‘demo’ and place outputs under that project.”
- “Show me diagnostics and confirm MCP configuration status.”

- ## Example Prompt Script
- “Set up the workspace with a demo project and run the guided first‑project workflow.”
- “Resume the ‘demo’ project and show me recent outputs.”
- “Preview the events dataset using a simple SQL query.”
- “Render a sample HTML report and export it to PDF under the current project.”
- Environment:
  - Copy `.env.example` to `.env` and set keys.
  - Load `.env` in your code using `python-dotenv` as needed.

## Suggested Workflow
- Keep tasks small and documented as you go.
- For scripts, add a one-line usage comment and `chmod +x`.
- If you add dependencies, document install steps for Ubuntu.
  - Prefer Parquet for large datasets (`uv add pyarrow`) and use Warehouse API.

## Python Tooling
- Ask Codex CLI to “Run the repository checks and fix issues (Ruff + Mypy).”

What you get out‑of‑the‑box
- ✅ Strict Python project with `uv` dependency management
- 📦 Warehouse API (CSV/JSONL/Parquet) + DuckDB SQL views (`ds_<dataset>`)
- 🧱 Project contexts with resumable manifests under `projects/`
- 📝 Jinja2 templates + HTML→PDF (WeasyPrint/pdfkit)
- 📊 Excel generation via Pandas + openpyxl
- 🧭 MCP‑ready hooks for Context7 + Firecrawl
- 🌈 Rich+Loguru logging with `-v`/`-vv` verbosity

## MCP Configuration
- Edit `mcp.config.json` and set `.env` if you plan to use Firecrawl/Context7 (see `AGENTS.md` for agent rules).

## Notes
- This workspace is intentionally lightweight. Add subfolders (`notes/`, `scripts/`, `docs/`) as needs emerge.
 - Logging uses Loguru with Rich formatting and tracebacks. Prefer `logger.info/debug/...` for diagnostics.

Next steps
- 💡 “Create a new project named ‘research’ and get it ready for reporting.”
- 🔎 “Pull web context for https://example.com and summarize top pages into a report.”
- 🧪 “Register a dataset, write a small sample, and run a quick SQL preview.”
