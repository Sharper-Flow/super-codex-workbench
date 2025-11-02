# Super Codex Workbench 🚀

Use plain-English prompts to turn ideas into data and reports. No coding required to start.


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

Use plain-English prompts to turn ideas into data and reports. No coding required to start.

## Feature Highlights

- 🚀 Agent‑first, prompt‑driven experience
  - User Benefit — You ask; it builds fast
  - What & How — Build from prompts in Codex CLI
- 🚣 Project‑centric flow
  - User Benefit — Keep everything tidy and repeatable
  - What & How — Everything stays under your active project
- 📦 Built‑in data store (warehouse)
  - User Benefit — Store data safely; query quickly
  - What & How — Load CSV/JSON; get ready‑to‑query views
- 📝 Elegant reporting
  - User Benefit — Share clean, polished outputs
  - What & How — Make HTML reports; export to PDF and Excel
- 🌐 Web context built‑in
  - User Benefit — Pull the right docs and pages
  - What & How — Finds docs/code and crawls sites for you
- 🌈 Great logs
  - User Benefit — Skim progress; spot issues fast
  - What & How — Readable progress messages and summaries
- 🛣️ Guided workflows
  - User Benefit — Get results with guided steps
  - What & How — Guided flows for setup and web reports
- 🧰 Quality gates
  - User Benefit — Keep things neat behind the scenes
  - What & How — Manage dependencies and check code quality
- 🪟 Windows‑friendly
  - User Benefit — Works great on Windows (WSL2)
  - What & How — One‑shot setup with sensible defaults
- 🔌 Extensible
  - User Benefit — Add new integrations in minutes
  - What & How — Plug in services via MCP plugins

## Who Is This For?
- Analysts, PMs, ops — comfortable with tools, not code
- Power users who want repeatable results without wiring everything
- Teams that want a simple, standard way to work locally

## How It Works (In 60 Seconds)
1) Pick a project. Everything you do lives there.
2) Bring in data (or let the agent fetch it).
3) Ask for a report; get HTML, PDF, or Excel.

## What You Can Build
- 📊 Sales insights app — Ingest weekly CSVs, run Python transforms, and generate an HTML+PDF dashboard with highlights.
- 🧾 Finance reconciler — Combine bank exports with invoices, flag mismatches, and email a PDF summary automatically.
- 🧠 Docs summarizer — Crawl product docs with MCP, extract key points, and publish a one‑pager brief.
- 📈 KPI tracker — Append telemetry to the warehouse daily, run DuckDB SQL, and render a monthly report.
- 🔍 Data quality bot — Validate new batches, raise issues with details, and export a fix‑list for teams.
- 🧪 Experiment notebook — Join datasets, run simple Python analyses, and export a shareable report for stakeholders.

## Try MCP (Plugins)
- MCP are "plugins" for AI tools — connect to services in a click.
- 🔎 Browse MCP servers: https://mcp.so/ — pick one to add via Codex CLI.
- Prompts:
  - Find an MCP for <your need>
  - Will an MCP help us <your goal>?
  - Install the <X> MCP server

## Actions at a Glance (Prompts)
- 🔧 Set up a demo and run the guided first-project workflow
- 🗂️ Show my projects and resume demo (or create it)
- 🗃️ Show recent outputs for the demo project
- 🧠 Preview the events dataset with a simple SQL
- 🌐 Crawl a website, summarize top pages, and generate a report
- 📝 Render a sample HTML report and export to PDF
- 📦 Run checks and fix formatting/typing issues

---

## Showcase
- Windows Terminal theme (CodexDarkGrey) + Nerd Font

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)
  Windows Terminal dark theme with Nerd Font

- Sample HTML report preview

  ![Sample report preview](docs/images/report-preview.svg)
  Sample HTML report preview

## Notes
No coding required — but you can peek under the hood anytime.
Want the technical bits? See `AGENTS.md`.

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
