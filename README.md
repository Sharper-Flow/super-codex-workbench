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


## 💡 Skip The Browser: Use Codex CLI
- If you have a ChatGPT Plus or Pro subscription, you already have access to Codex CLI — a terminal workspace that supercharges ChatGPT with real tooling.
- Why it’s a big upgrade over the browser:
  - 🧰 Executes commands and edits files locally
  - 🔌 Uses MCP integrations (e.g., Firecrawl, Context7) for web/docs context
  - 🧪 Adds quality gates (Ruff, Mypy) and reproducible workflows
  - 🧾 Produces real artifacts (datasets, HTML/PDF/Excel) in tidy project folders
  - 🔒 Keeps your code/data local by default
  - 🌐 Crawls and scrapes websites/docs at scale; parse, extract, and save structured data
  - 🧵 Automates multi‑step flows across git, Docker, SQL, Make, and shell tools
  - 🗄️ Reads/writes databases and files; transforms large datasets; schedules recurring jobs
  - 🔐 Works with private repos/SSH keys; searches, patches, and refactors codebases safely
  - 🧠 Persists long context with projects, logs, datasets, and caches (reproducible runs)
  - 🛡️ Enforces approvals/network controls; can run fully local/offline if you choose
  - 🧩 Extends on demand with new CLIs, Python packages, MCP servers, and API clients
  - 📈 Generates dashboards/reports/PDFs; exports CSV/Parquet/Excel to your project folders
  - 🕸️ Orchestrates headless browsers for scraping and form automation (when configured)
- Think of this as what any capable local AI agent can do — Codex CLI just makes it seamless for ChatGPT Plus/Pro users.
- This repo is your quickstart: a batteries‑included workspace tailored for Codex CLI so you can go from “chat” to real, repeatable outputs in minutes.
- Install Codex CLI via the official guide (see link below), open this repo in Codex, and run the setup to get moving fast.


## 🤔 Who Is This For?
- 📊 Analysts, PMs, and ops who are comfortable with tools — not code
- ⚡ Power users who want repeatable results without wiring everything manually
- 🔨 Pros who want to work fast with the latest toolset, auto‑updated

## 🥳 Supercharge Codex CLI With All the Tools You Need.
  > Requires ChatGPT Plus/Pro access — details in `AGENTS.md`.

Level up from chat-only answers to a local, executable workbench that ships real outputs.

👉 Ready to go? See: [Get Started Now](#get-started-now)

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

Concrete, runnable flows you can copy and adapt. Use these natural language prompts in Codex CLI.

### 🏠 Smart Home: Nightly Energy Snapshot
- What you get: a daily usage summary (CSV + HTML + optional PDF) to spot energy spikes.
- Try with prompts:
  - "Create a project named home-energy and set it current."
  - "Register a dataset energy_readings as CSV partitioned by date and source."
  - "Write a sample batch to energy_readings for date=2025-01-01, source=smartplug."
  - "Summarize total kWh by device from ds_energy_readings and save the CSV as energy_summary in the project."
  - "Render an HTML report titled Home Energy Snapshot, then export it to PDF."
- Next step: swap the sample batch for your real smart‑plug/API feed.

### 👩‍⚕️ Appointments: Weekly Summary
- What you get: a weekly roll‑up of sessions per client (CSV + HTML + optional PDF) for quick billing.
- Try with prompts:
  - "Create a project called appointments and select it."
  - "Register a dataset client_sessions as CSV partitioned by week."
  - "Write a sample batch to client_sessions for week=2025-W01."
  - "Summarize sessions and hours by client from ds_client_sessions and save as weekly_summary CSV."
  - "Render an HTML report titled Weekly Appointments Summary and also export a PDF."
- Next step: add a custom template under the project’s templates folder to include your logo/fields.

### 🔁 Vendor Policy Update Brief (MCP)
- What you get: a concise brief of recent policy pages (HTML + optional PDF) so your team stays informed.
- Requires: Firecrawl MCP configured (`.env` with `FIRECRAWL_API_KEY`) and `mcp.config.json` present.
- Try with prompts:
  - "Create a project named policy-briefs and select it."
  - "Check MCP status and confirm Firecrawl is configured."
  - "Crawl https://example.com/policy (limit 5) and generate an HTML report under the project."
  - "If a PDF backend is available, also export the report to PDF."
- Tip: "Blend Context7 results using the query: your keywords."

## Contributing
- License: MIT — see `LICENSE`.
- Contributing: Issues and PRs welcome. Keep diffs minimal, avoid secrets, and follow all instructions in [`AGENTS.md`](AGENTS.md).

### Bonus Fun
### Windows Terminal Theme (CodexDarkGrey) + Nerd Font Included in Windows Setup Script

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)
