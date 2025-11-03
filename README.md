<h1 align="center">Super Codex Workbench 🚀</h1>
<h3 align="center">⚡A Supercharged Codex CLI Workspace, Batteries-Included🔋</h3>

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


## 🤔 Who Is This For?
- 📊 Analysts, PMs, and ops who are comfortable with tools — not code
- ⚡ Power users who want repeatable results without wiring everything manually
- 🔨 Pros who want to work fast with the latest toolset, auto‑updated

## 🥳 Supercharge Codex CLI With All the Tools You Need.
  > Requires ChatGPT Plus/Pro access — details in `AGENTS.md`.

Level up from chat-only answers to a local, executable workbench that ships real outputs.

### 💥 Why It Beats ChatGPT
- ✅ Repeatable projects — every run is versioned and reproducible.
- 🗂️ Real artifacts — files, datasets, HTML/PDF/Excel saved in your project.
- 🧪 Quality gates — Ruff, Mypy, and environment health checks baked in.
- 🤖 Autonomy with guardrails — multi‑step workflows, verification, and git checkpoints.
- 🔒 Local‑first privacy — your code/data/logs stay on your machine.
- 🔌 Extensible — add MCP integrations and Python deps with one prompt.

### 🚫 What ChatGPT Can’t (We Do)
- 🖥️ Execute commands and orchestrate builds/tests.
- ✍️ Write, run, and refactor real code across files.
- 📂 Read/write your project, env, and configs.
- 🗄️ Query local data/DBs and manage a warehouse.
- 🤖 Automate multi‑step, reliable workflows.
- 🔐 Keep secrets local; only enabled MCPs touch network.

### ⚡ Do More, Faster
- 🚣 Project‑centric flow — tidy, repeatable workspaces per project.
- 🧷 Automatic git checkpoints — easy rollbacks and recovery.
- 🌐 Web + docs context — Firecrawl + Context7 on tap when configured.
- 📝 Elegant reporting — HTML, PDF, and Excel exports.
- 🪟 Windows‑friendly — great on WSL2.

### 🚀 Quickstart
- Setup: `bash ./scripts/setup.sh -y -p demo`
- Verify: `uv run python main.py -v diagnose`
- First project: `uv run python main.py workflow first-project --name demo --with-mcp`

👉 Ready to go? See: [Get Started Now](#get-started-now)

### 🔌 Add Capabilities (MCP)
- MCP are proven “plugins” that add web/docs/search and service integrations.
- Comes with Firecrawl + Context7; browse more at https://mcp.so/
- Prompts you can use:
  - `"Find an MCP for <your need>"`
  - `"Install the <X> MCP server"`

### 🧠 Smart Installs (via uv)
- As you ask for features (PDFs, Excel, Parquet, charts), the right deps are added locally.
- Examples: `weasyprint`/`pdfkit` (PDF), `openpyxl` (Excel), `pyarrow` (Parquet), `plotly` (charts).

---

## 🥳 Supercharge Codex CLI With All the Tools You Need.
  > You'll need an existing ChatGPT Plus or Pro Subscription - Learn more: [`AGENTS.md`](AGENTS.md).

1. Create or resume a project — your work is foldered automatically.
   - `"Show my 2026 projections project and resume demo"`
   - `"Create a project named sales-2024"`

   - 🚀 **Agent‑first, prompt‑driven experience** — You ask; it builds fast

     [![Codex CLI](https://img.shields.io/badge/Codex_CLI-Prompts-1F6FEB?style=flat-square&logo=gnubash&logoColor=white)](AGENTS.md)

   - 🚣 **Project‑centric flow** — Keep everything tidy and repeatable

     [![Projects](https://img.shields.io/badge/Projects-Organized-4A5568?style=flat-square&logo=openproject&logoColor=white)](#supercharge-codex-cli-with-all-the-tools-you-need)

   - 🧷 **Automatic git checkpoints** — Rewind or recover any point in your work

     [![Git](https://img.shields.io/badge/Git-Sync-0366d6?style=flat-square&logo=github&logoColor=white)](scripts/git-push.sh)

   - 🧰 **Quality gates** — Keep things neat behind the scenes

     [![uv](https://img.shields.io/badge/uv-Dependencies-2D3748?style=flat-square&logo=python&logoColor=white)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/badge/Ruff-Lint-ff3860?style=flat-square&logo=python&logoColor=white)](https://github.com/astral-sh/ruff) [![Mypy](https://img.shields.io/badge/Mypy-Types-5383EC?style=flat-square&logo=python&logoColor=white)](https://github.com/python/mypy)

   - 🪟 **Windows‑friendly** — Works great on Windows (WSL2)

     [![WSL2](https://img.shields.io/badge/Windows-WSL2-00BCF2?style=flat-square&logo=windows&logoColor=white)](https://learn.microsoft.com/windows/wsl/) [![Windows Terminal](https://img.shields.io/badge/Windows_Terminal-Theme-4A4A4A?style=flat-square&logo=windowsterminal&logoColor=white)](https://github.com/microsoft/terminal)

2. Bring in data — or ask the agent to fetch it.
   - `"Ingest data/sales.csv as dataset sales (date=2024-10-01)"`
   - `"Crawl https://example.com/docs and save the top pages"`

   - 📦 **Built‑in data store (warehouse)** — Store data safely; query quickly

     [![DuckDB](https://img.shields.io/badge/DuckDB-SQL-FFCB05?style=flat-square&logo=duckdb&logoColor=white)](https://duckdb.org/) [![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

   - 🌐 **Web context built‑in** — Pull the right docs and pages

     [![Context7](https://img.shields.io/badge/Context7-Docs%2FCode-0EA5E9?style=flat-square&logo=readthedocs&logoColor=white)](https://context7.dev/) [![Firecrawl](https://img.shields.io/badge/Firecrawl-Web_Fetch-F97316?style=flat-square&logo=firefoxbrowser&logoColor=white)](https://firecrawl.dev/)

3. Ask for outputs — get HTML, PDF, or Excel.
   - `"Make a datatable on all Japanese car makes and models from 1991"`
   - `"Render a PDF report summarizing the top 10 makes with charts"`

   - 📝 **Elegant reporting** — Share clean, polished outputs

     [![Jinja2](https://img.shields.io/badge/Jinja2-Templates-000000?style=flat-square&logo=jinja&logoColor=white)](https://github.com/pallets/jinja) [![WeasyPrint](https://img.shields.io/badge/PDF-WeasyPrint-EE1F25?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://weasyprint.org/) [![Excel](https://img.shields.io/badge/Excel-OpenPyXL-217346?style=flat-square&logo=microsoftexcel&logoColor=white)](https://openpyxl.readthedocs.io/)

   - 🌈 **Great logs** — Skim progress; spot issues fast

     [![Rich](https://img.shields.io/badge/Rich-Logs-6E56CF?style=flat-square&logo=python&logoColor=white)](https://github.com/Textualize/rich) [![Loguru](https://img.shields.io/badge/Loguru-Logger-0B84F3?style=flat-square&logo=python&logoColor=white)](https://github.com/Delgan/loguru)

   - 🔌 **Extensible** — Add new integrations in minutes

     [![MCP](https://img.shields.io/badge/MCP-Plugins-0EA5E9?style=flat-square&logo=puzzle&logoColor=white)](https://mcp.so/)

## Add capabilities on demand via proven plugins (MCP)
- MCP are "plugins" for AI tools — connect to services in a click.

- 🔎 Browse MCP servers: https://mcp.so/ — pick one to add via Codex CLI.

- Comes with: [Firecrawl](https://github.com/firecrawl/firecrawl) and [Context7](https://github.com/upstash/context7)

- Prompts:
  - `"Find an MCP for <your need>"`
  - `"Will an MCP help us <your goal>?"`
  - `"Install the <X> MCP server"`

## Codex installs what’s needed behind the scenes
- 🧠 Smart installs — When you ask for something new (e.g., “export to Excel”, “render a PDF”, “save as Parquet”), Codex CLI installs the right Python packages automatically using `uv`.

- 🔒 Safe & local — Everything lives in the project’s virtual environment; no global `pip`. Dependencies are tracked in `pyproject.toml` + `uv.lock` for repeatability.

- 🧹 Clean by default — After adding deps, Codex runs project checks to keep things tidy.

- Examples:
  - “Render a PDF report” → adds `weasyprint` (or `pdfkit`) and configures the export.
  - “Export results to Excel” → adds `openpyxl` (or `xlsxwriter`).
  - “Save as data tables for querying” → adds `pyarrow` for fast columnar files.
  - “Plot a quick chart” → adds `plotly` (or `matplotlib`) when needed.
  - “Fetch and parse a page” → adds `httpx` + `beautifulsoup4` for lightweight scraping.

- You just ask; Codex brings the pieces together so you can focus on outcomes.

---

## Use Case Samples

- 📊 Sales insights app — Ingest weekly CSVs, run Python transforms, and generate an HTML+PDF dashboard with highlights.

  ![Sales Insights sample](docs/images/samples/sales-insights.svg)

- 🧾 Finance reconciler — Combine bank exports with invoices, flag mismatches, and email a PDF summary automatically.

  ![Finance Reconciler sample](docs/images/samples/finance-reconciler.svg)

- 🧠 Docs summarizer — Crawl product docs with MCP, extract key points, and publish a one‑pager brief.

  ![Docs Summarizer sample](docs/images/samples/docs-summarizer.svg)

- 🔍 Data quality bot — Validate new batches, raise issues with details, and export a fix‑list for teams.

  ![Data Quality sample](docs/images/samples/data-quality-bot.svg)



## Project Directory
No coding required — but you can peek under the hood anytime.

Want the technical bits? See [`AGENTS.md`](AGENTS.md).

- `apps/` — app‑specific logic (prefix dataset names to avoid collisions)

- `data/` — ad‑hoc inputs and scratch during tasks

- `reports/` — user‑facing outputs (HTML/PDF/Excel) and templates

- `warehouse/` — curated datasets managed by the Warehouse API

- `scripts/` — helper scripts for setup, checks, and git checkpoints

- `logs/` — structured logs for task runs

## Get Started Now

> First step for windows users only
- Windows (first‑time)
  - Download the `windows-setup.ps1` script from [**here**](scripts/windows-setup.ps1)
  - Open PowerShell as Administrator
  - Run: `./scripts/windows-setup.ps1 -ProvisionWSL -DefaultProfile Ubuntu`
  - Reboot if prompted, open Ubuntu (WSL), and work inside your Linux home (e.g., `~/`)

- Get the code
  - Clone: `git clone https://github.com/Sharper-Flow/super-codex-workbench.git`
  - Or fork on GitHub, then: `git clone https://github.com/<your‑username>/super-codex-workbench.git`
  - Enter the folder: `cd super-codex-workbench`

- Install Codex CLI
  - Ensure ChatGPT Plus/Pro access
  - Follow the [official Codex CLI install guide](https://platform.openai.com/docs/guides/tools/codex-cli) for your OS
  - Verify it launches and can open this repo workspace

- Launch Codex CLI and Run Setup
  - Open your terminal (or WSL2 Ubuntu on Windows)
  - Run: `codex`
  - Once Codex CLI is running, tell it:
    > "run the setup script"

## Real-Life Recipes 🎯

Concrete, runnable flows you can copy and adapt. All commands run inside the local virtualenv via `uv run` and respect the current project context.

### 🏠 Smart Home: Nightly Energy Snapshot
- What you get: a daily usage summary (CSV + HTML + optional PDF) to spot energy spikes.
- How to try it:
  - Create a project: `uv run python main.py projects create --name home-energy`
  - Register a dataset: `uv run python main.py warehouse register --name energy_readings --format csv --partitioning date,source`
  - Land a sample batch (stand‑in for your smart‑plug/API feed):
    - `uv run python main.py warehouse write-sample --name energy_readings --partition "date=2025-01-01,source=smartplug"`
  - Summarize usage (example query):
    - `uv run python main.py warehouse sql --query "select event as device, sum(value) as kwh from ds_energy_readings group by device order by device" --output projects/home-energy/artifacts/energy_summary.csv`
  - Render HTML: `uv run python main.py reports render-html --title "Home Energy Snapshot" --output projects/home-energy/reports/html/energy.html`
  - Export PDF: `uv run python main.py reports export-pdf --html projects/home-energy/reports/html/energy.html --output projects/home-energy/reports/pdf/energy.pdf`
- Next step: replace the sample write with your real fetch (create a DataFrame and use the Warehouse API to write it).

### 👩‍⚕️ Professional Appointments App: Weekly Summary
- What you get: a weekly roll‑up of sessions per client (CSV + HTML + optional PDF) for quick billing.
- How to try it:
  - Create a project: `uv run python main.py projects create --name appointments`
  - Register a dataset: `uv run python main.py warehouse register --name client_sessions --format csv --partitioning week`
  - Land a sample batch: `uv run python main.py warehouse write-sample --name client_sessions --partition "week=2025-W01"`
  - Summarize the week:
    - `uv run python main.py warehouse sql --query "select event as client, count(*) as sessions, sum(value) as hours from ds_client_sessions group by client order by client" --output projects/appointments/artifacts/weekly_summary.csv`
  - Report HTML → PDF:
    - `uv run python main.py reports render-html --title "Weekly Appointments Summary" --output projects/appointments/reports/html/weekly.html`
    - `uv run python main.py reports export-pdf --html projects/appointments/reports/html/weekly.html --output projects/appointments/reports/pdf/weekly.pdf`
- Next step: add a custom template under `projects/appointments/templates/` to include your logo/fields.

### 🔁 Vendor Policy Update Brief (MCP)
- What you get: a concise brief of recent policy pages (HTML + optional PDF) so your team stays informed.
- Requires: Firecrawl MCP configured (`.env` with `FIRECRAWL_API_KEY`) and `mcp.config.json` present.
- How to try it:
  - Create a project: `uv run python main.py projects create --name policy-briefs`
  - Verify MCP: `uv run python main.py mcp info`
  - Crawl and generate report:
    - `uv run python main.py workflow mcp-web --url https://example.com/policy --limit 5`
  - Output: HTML at `projects/policy-briefs/reports/html/mcp_report.html` and a PDF if a backend is installed.
- Tip: add `--c7-query "your keywords"` to blend Context7 search results into the same report.

## Contributing
- License: MIT — see `LICENSE`.
- Contributing: Issues and PRs welcome. Keep diffs minimal, avoid secrets, and follow all instructions in [`AGENTS.md`](AGENTS.md).

### Bonus Fun
### Windows Terminal Theme (CodexDarkGrey) + Nerd Font Included in Windows Setup Script

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)
