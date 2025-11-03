<h1 align="center">Super Codex Workbench 🚀</h1>
<h3 align="center">Turn AI chat into real, local outputs</h3>

<p align="center"><em>Made with ❤️ by <strong>Sharper Flow LLC</strong></em></p>

---

## Why It Exists 💡

You talk; it ships. With Codex CLI + this repo, a plain English request becomes
repeatable, local work: datasets, SQL, and polished HTML/PDF/Excel — all under a
project folder with logs and git checkpoints.

This is for people who want results, not glue work:

- ✅ Project-scoped workflows that stay tidy and reproducible
- ✅ Web/docs context via MCP (Firecrawl, Context7) when available
- ✅ Data + SQL + reporting out of the box (DuckDB, Pandas)
- ✅ Quality gates (Ruff/Mypy) and environment health checks
- ✅ Git checkpoints so every run is reversible
- ✅ Windows-friendly (WSL2) and local-first privacy

---

## What It’s Best At 🎯

- Turning a vague prompt into a concrete artifact (HTML/PDF/CSV/Parquet)
- Orchestrating multi-step flows across shell, SQL, Python, and MCP
- Keeping everything inside a clean project directory you can trust
- Making “do it again next week” a single command, not a rebuild

When to use it:

- Use when you want repeatable, file-backed outputs with light automation
- Use when web/docs context matters (MCP) and you need a brief/report
- Skip when pure chat is enough or you need heavy backend services

---

## The Story: From Ask → Artifact 📦

- You: “Summarize the latest competitor pricing and produce a one‑page brief.”
- Workbench: checks environment, creates/selects a project, and sets guardrails.
- MCP: fetches relevant pages (Firecrawl) and optional docs context (Context7).
- Data: writes a dataset, registers it as `ds_*`, and runs SQL via DuckDB.
- Report: renders an HTML brief and (if configured) exports a PDF.
- Safety: saves a git checkpoint so you can diff or roll back anytime.

Result: a tidy `projects/<name>/...` folder with datasets, HTML/PDF, and logs.

---

## Try It In 3 Minutes ⚡

- Clone and enter the repo:
  - `git clone https://github.com/Sharper-Flow/super-codex-workbench.git`
  - `cd super-codex-workbench`
- Launch Codex CLI and run setup:
  - `codex` → say: “run the setup script”
  - The script ensures `uv`, venv, dependencies, and `.env` scaffolding
- Run the guided first-project workflow:
  - `uv run python main.py workflow first-project --name demo`
- Open your outputs under:
  - `projects/demo/reports` and `projects/demo/...`

Windows first-time? Use `./scripts/windows-setup.ps1 -ProvisionWSL -DefaultProfile Ubuntu`
then work inside Ubuntu under `~/`.

---

## Minimal Commands 🧭

- Diagnose environment: `uv run python main.py -v diagnose`
- List or resume a project:
  - `uv run python main.py projects list`
  - `uv run python main.py projects resume --name demo`
- Web context + brief (MCP):
  - `uv run python main.py workflow mcp-web --url https://example.com --limit 5`
- Render a report:
  - `uv run python main.py reports render-html --template sample.html`
  - `uv run python main.py reports export-pdf --html sample.html`

More quick commands live in AGENTS.md.

---

## Configure MCP 🔌

- Firecrawl requires `FIRECRAWL_API_KEY`; Context7 is optional.
- Copy `.env.example` → `.env` and set keys if you have them.
- Verify MCP:
  - `uv run python main.py mcp info`
  - `uv run python main.py check-mcp`

No keys? You can still run local data + reporting flows.

---

## Where Things Go 🗂️

- `projects/<name>/...` — all outputs by default (datasets, reports, logs)
- `reports/` — shared templates; project-specific live under `projects/<name>/templates`
- `warehouse/` — curated datasets (managed by the Warehouse API)

Deeper details and rules are in `AGENTS.md`.

---

## Contributing 🤝

- License: MIT (see `LICENSE`)
- Issues and PRs welcome — keep diffs small and follow `AGENTS.md`

