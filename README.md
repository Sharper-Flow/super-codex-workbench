# Super Codex Workbench

Batteries‑included workbench for Codex CLI. 🚀

<p align="center">
  <img src="docs/images/repo-banner.svg" alt="Super Codex Workbench banner" width="720" />
</p>

<p align="center">
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge"></a>
  <a href="https://astral.sh/uv/"><img alt="uv" src="https://img.shields.io/badge/deps-managed%20by%20uv-2D3748?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/badge/lint-Ruff-ff3860?style=for-the-badge"></a>
  <a href="https://github.com/python/mypy"><img alt="Mypy" src="https://img.shields.io/badge/types-Mypy-5383EC?style=for-the-badge"></a>
  <a href="https://pandas.pydata.org/"><img alt="Pandas" src="https://img.shields.io/badge/data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"></a>
  <a href="https://duckdb.org/"><img alt="DuckDB" src="https://img.shields.io/badge/sql-DuckDB-FFCB05?style=for-the-badge"></a>
  <a href="https://firecrawl.dev/"><img alt="Firecrawl" src="https://img.shields.io/badge/web-Firecrawl-F97316?style=for-the-badge"></a>
  <a href="https://context7.dev/"><img alt="Context7" src="https://img.shields.io/badge/context-Context7-0EA5E9?style=for-the-badge"></a>
</p>

<p align="center"><em>Made with ❤️ for friends by <strong>Sharper Flow LLC</strong></em></p>

Turn ideas into data, reports, and APIs — fast. An agent‑first, prompt‑driven workspace for Codex CLI.

## Feature Highlights

- 🚀 Agent‑first, prompt‑driven experience
  - User Benefit — Faster from prompt to outputs
  - What & How — Build from prompts in Codex CLI
- 🚣 Project‑centric flow
  - User Benefit — Organized, reproducible work
  - What & How — Everything lands under your active project
- 📦 Reliable warehouse
  - User Benefit — Trustworthy storage with fast SQL
  - What & How — CSV/JSONL/Parquet with instant DuckDB views
- 📝 Elegant reporting
  - User Benefit — Share clear, polished outputs
  - What & How — Jinja2 HTML → PDF and Excel export
- 🌐 Web context built‑in
  - User Benefit — Pull relevant docs and pages fast
  - What & How — Context7 (docs/code) + Firecrawl (crawl/summarize)
- 🌈 Great logs
  - User Benefit — Understand progress and issues quickly
  - What & How — Rich + Loguru for readable diagnostics
- 🛣️ Guided workflows
  - User Benefit — Onboard and deliver quickly
  - What & How — First‑project setup and MCP web report flow
- 🧰 Quality gates
  - User Benefit — Keep code clean and typed
  - What & How — uv‑managed deps, Ruff lint, Mypy typing
- 🪟 Windows‑friendly
  - User Benefit — Smooth setup on Windows/WSL2
  - What & How — One‑shot provisioning (Terminal, Nerd Font, WSL2, zsh)
- 🔌 Extensible
  - User Benefit — Add new services easily
  - What & How — Configure MCP servers/APIs; scaffold clients

## Who Is This For?
- 🙋‍♂️ Newcomers who want a safe, guided path to build data + reports
- ⚡ Power users who value structure, repeatability, and speed
- 🤝 Teams who want a standard way for agents to work locally

## How It Works (In 60 Seconds)
1) Choose a project (resume or create). Everything lands under that name.
2) Ingest data via the Warehouse API (CSV/JSONL/Parquet; partition by date/source).
3) Query with DuckDB SQL on auto‑registered views (`ds_<dataset>`).
4) Report with Jinja2 HTML → export to PDF/Excel under `projects/<current>/reports`.

## Try MCP
- 🔎 Explore servers: https://mcp.so/
- Try prompts:
  - "Find an MCP for <your need> on mcp.so"
  - "Will an MCP help us <your goal>?"
  - "Install the <X> MCP server"

## Actions at a Glance (Prompts)
- 🔧 “Set up the workspace with a demo project and run the guided first‑project workflow.”
- 🗂️ “Show my projects and resume ‘demo’ (or create it if missing).”
- 🧠 “Preview the latest rows for the events dataset using DuckDB SQL.”
- 🌐 “Crawl https://example.com, summarize the top pages, and generate a quick report.”
- 📦 “Run the repository checks and fix any formatting or typing issues.”

## Example Prompt Script
- “Set up the workspace with a demo project and run the guided first‑project workflow.”
- “Resume the ‘demo’ project and show me recent outputs.”
- “Preview the events dataset using a simple SQL query.”
- “Render a sample HTML report and export it to PDF under the current project.”

## Showcase
- Windows Terminal theme (CodexDarkGrey) + Nerd Font

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)

- Sample HTML report preview

  ![Sample report preview](docs/images/report-preview.svg)

## Notes
Talk to the agent — we’ve done the heavy lifting.
Agents and contributors: see `AGENTS.md` for setup, MCP usage, coding rules, and git checkpoints.

## Project Structure
- `apps/` — app‑specific logic (prefix dataset names to avoid collisions)
- `data/` — ad‑hoc inputs and scratch during tasks
- `reports/` — user‑facing outputs (HTML/PDF/Excel) and templates
- `warehouse/` — curated datasets managed by the Warehouse API
- `scripts/` — helper scripts for setup, checks, and git checkpoints
- `logs/` — structured logs for task runs

## License & Contributing
- License: MIT — see `LICENSE`.
- Contributing: Issues and PRs welcome. Keep diffs minimal, avoid secrets, and follow the style in `AGENTS.md`.
