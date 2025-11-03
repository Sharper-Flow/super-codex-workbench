<h1 align="center">Super Codex Workbench 🚀</h1>
<h3 align="center">A Codex CLI Workspace with Batteries Included🔋</h3>

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


## Who Is This For?
- 📊 Analysts, PMs, and ops who are comfortable with tools — not code
- ⚡ Power users who want repeatable results without wiring everything manually
- 🤝 Teams that want a simple, standard way to work locally

## ⚡ Supercharge Codex CLI With All the Tools You Need.
  > You'll need an existing ChatGPT Plus or Pro Subscription - Learn more: [Codex CLI](AGENTS.md).

1) Create or resume a project — your work is foldered automatically.
     - `"Show my 2026 projections project and resume demo"`
     - `"Create a project named sales-2024"`
2) Bring in data — or ask the agent to fetch it.
     - `"Ingest data/sales.csv as dataset sales (date=2024-10-01)"`
     - `"Crawl https://example.com/docs and save the top pages"`
3) Ask for outputs — get HTML, PDF, or Excel.
     - `"Make a datatable on all Japanese car makes and models from 1991"`
     - `"Render a PDF report summarizing the top 10 makes with charts"`



## Feature Highlights

- 🚀 Agent‑first, prompt‑driven experience
  - 👩‍💻 — You ask; it builds fast
  - What & How — [![Codex CLI](https://img.shields.io/badge/Codex_CLI-Prompts-1F6FEB?style=flat-square&logo=gnubash&logoColor=white)](AGENTS.md)
- 🚣 Project‑centric flow
  - 👮‍♂️ — Keep everything tidy and repeatable
  - What & How — [![Projects](https://img.shields.io/badge/Projects-Organized-4A5568?style=flat-square&logo=openproject&logoColor=white)](#how-it-works-in-60-seconds)
- 📦 Built‑in data store (warehouse)
  - 👩‍🔬 — Store data safely; query quickly
  - What & How — [![DuckDB](https://img.shields.io/badge/DuckDB-SQL-FFCB05?style=flat-square&logo=duckdb&logoColor=white)](https://duckdb.org/) [![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
- 📝 Elegant reporting
  - 👩‍🎨 — Share clean, polished outputs
  - What & How — [![Jinja2](https://img.shields.io/badge/Jinja2-Templates-000000?style=flat-square&logo=jinja&logoColor=white)](https://github.com/pallets/jinja) [![WeasyPrint](https://img.shields.io/badge/PDF-WeasyPrint-EE1F25?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://weasyprint.org/) [![Excel](https://img.shields.io/badge/Excel-OpenPyXL-217346?style=flat-square&logo=microsoftexcel&logoColor=white)](https://openpyxl.readthedocs.io/)
- 🌐 Web context built‑in
  - 🕵️‍♂️ — Pull the right docs and pages
  - What & How — [![Context7](https://img.shields.io/badge/Context7-Docs%2FCode-0EA5E9?style=flat-square&logo=readthedocs&logoColor=white)](https://context7.dev/) [![Firecrawl](https://img.shields.io/badge/Firecrawl-Web_Fetch-F97316?style=flat-square&logo=firefoxbrowser&logoColor=white)](https://firecrawl.dev/)
- 🌈 Great logs
  - 👩‍🏫 — Skim progress; spot issues fast
  - What & How — [![Rich](https://img.shields.io/badge/Rich-Logs-6E56CF?style=flat-square&logo=python&logoColor=white)](https://github.com/Textualize/rich) [![Loguru](https://img.shields.io/badge/Loguru-Logger-0B84F3?style=flat-square&logo=python&logoColor=white)](https://github.com/Delgan/loguru)
- 🛣️ Guided workflows
  - 👩‍🚒 — Get results with guided steps
  - What & How — [![Workflows](https://img.shields.io/badge/Workflows-Guided-2563EB?style=flat-square&logo=githubactions&logoColor=white)](#actions-at-a-glance-prompts)
- 🧰 Quality gates
  - 🧑‍🏭 — Keep things neat behind the scenes
  - What & How — [![uv](https://img.shields.io/badge/uv-Dependencies-2D3748?style=flat-square&logo=python&logoColor=white)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/badge/Ruff-Lint-ff3860?style=flat-square&logo=python&logoColor=white)](https://github.com/astral-sh/ruff) [![Mypy](https://img.shields.io/badge/Mypy-Types-5383EC?style=flat-square&logo=python&logoColor=white)](https://github.com/python/mypy)
- 🪟 Windows‑friendly
  - 👷 — Works great on Windows (WSL2)
  - What & How — [![WSL2](https://img.shields.io/badge/Windows-WSL2-00BCF2?style=flat-square&logo=windows&logoColor=white)](https://learn.microsoft.com/windows/wsl/) [![Windows Terminal](https://img.shields.io/badge/Windows_Terminal-Theme-4A4A4A?style=flat-square&logo=windowsterminal&logoColor=white)](https://github.com/microsoft/terminal)
- 🔌 Extensible
  - 👨‍🚀 — Add new integrations in minutes
  - What & How — [![MCP](https://img.shields.io/badge/MCP-Plugins-0EA5E9?style=flat-square&logo=puzzle&logoColor=white)](https://mcp.so/)

## Extend Codex CLI's Reach with MCP Servers
- MCP are "plugins" for AI tools — connect to services in a click.
- 🔎 Browse MCP servers: https://mcp.so/ — pick one to add via Codex CLI.
- Prompts:
  - `"Find an MCP for <your need>"`
  - `"Will an MCP help us <your goal>?"`
  - `"Install the <X> MCP server"`

## Intelligent Auto‑Adding of Relevant Features
- 🧠 Smart installs — When you ask for something new (e.g., “export to Excel”, “render a PDF”, “save as Parquet”), Codex CLI installs the right Python packages automatically using `uv`.
- 🔒 Safe & local — Everything lives in the project’s virtual environment; no global `pip`. Dependencies are tracked in `pyproject.toml` + `uv.lock` for repeatability.
- 🧹 Clean by default — After adding deps, Codex runs project checks to keep things tidy.

- Examples:
  - “Render a PDF report” → adds `weasyprint` (or `pdfkit`) and configures the export.
  - “Export results to Excel” → adds `openpyxl` (or `xlsxwriter`).
  - “Save tables as Parquet” → adds `pyarrow` for fast columnar files.
  - “Plot a quick chart” → adds `plotly` (or `matplotlib`) when needed.
  - “Fetch and parse a page” → adds `httpx` + `beautifulsoup4` for lightweight scraping.

- You just ask; Codex brings the pieces together so you can focus on outcomes.

## Actions at a Glance (Prompts)
- 🔧 `"Set up a demo and run the guided first-project workflow"`
- 🗂️ `"Show my projects and resume demo (or create it)"`
- 🗃️ `"Show recent outputs for the demo project"`
- 🧠 `"Preview the events dataset with a simple SQL"`
- 🌐 `"Crawl a website, summarize top pages, and generate a report"`
- 📝 `"Render a sample HTML report and export to PDF"`
- 📦 `"Run checks and fix formatting/typing issues"`

---

## Showcase
  ### Windows Terminal theme (CodexDarkGrey) + Nerd Font

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)


### Use Case Samples (What You Can Build)

- 📊 Sales insights app — Ingest weekly CSVs, run Python transforms, and generate an HTML+PDF dashboard with highlights.

  ![Sales Insights sample](docs/images/samples/sales-insights.svg)

- 🧾 Finance reconciler — Combine bank exports with invoices, flag mismatches, and email a PDF summary automatically.

  ![Finance Reconciler sample](docs/images/samples/finance-reconciler.svg)

- 🧠 Docs summarizer — Crawl product docs with MCP, extract key points, and publish a one‑pager brief.

  ![Docs Summarizer sample](docs/images/samples/docs-summarizer.svg)

- 📈 KPI tracker — Append telemetry to the warehouse daily, run DuckDB SQL, and render a monthly report.

  ![KPI Tracker sample](docs/images/samples/kpi-tracker.svg)

- 🔍 Data quality bot — Validate new batches, raise issues with details, and export a fix‑list for teams.

  ![Data Quality sample](docs/images/samples/data-quality-bot.svg)

- 🧪 Experiment notebook — Join datasets, run simple Python analyses, and export a shareable report for stakeholders.

  ![Experiment Notebook sample](docs/images/samples/experiment-notebook.svg)

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
