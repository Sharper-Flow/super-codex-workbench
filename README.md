<h1 align="center">Super Codex Workbench 🚀</h1>
<h3 align="center">Turn AI chat into real, local outputs</h3>

<p align="center"><em>Made with ❤️ by <strong>Sharper Flow LLC</strong></em></p>

<p align="center"><strong>Requires ChatGPT Plus/Pro</strong> for Codex CLI</p>

---

## You Found Your Workbench 🎉

- For non‑coders who don’t want “vibe coding.”
- A strict workbench for Codex CLI that keeps projects tidy, manages context step‑by‑step, and produces real files you can share.
- Get ~70% of a full coding environment’s power at ~30% of the effort and knowledge.

### Why this is a great find ✨
- Ask in plain English. Get fast, reliable results — not loose notes.
- Pivot between topics without losing your place; each project keeps its own context.
- Turn research into shareable briefs and simple apps in minutes, not days.
- Fast tables for large lists and quick lookups; no tech jargon required.
- Automatic safety nets: logs and git checkpoints after meaningful steps.

### What is Codex CLI?
- Codex CLI turns your ChatGPT into a local operator that can run commands, edit files, manage projects, and integrate tools (MCP servers like Firecrawl/Context7).
- You speak in plain English; Codex performs actions on your machine with logs and checkpoints.

### What this Workbench adds (beyond a chatbot)
- Tight structure: project‑scoped runs, reproducible outputs, and automatic checkpoints.
- Managed context: datasets, views, and reports that build on each other as you go.
- Real artifacts: HTML/PDF/Excel/CSV/Parquet in `projects/<name>/...` you can share immediately.

## Why It Exists 💡

You talk; it ships. With Codex CLI + this repo, a plain English request becomes
repeatable, local work: datasets, fast tables and analysis, and polished HTML/PDF/Excel — all
under a project folder with logs and git checkpoints.

This is for people who want results, not glue work:

- ✅ Project‑scoped workflows that stay tidy and reproducible
- ✅ Web/docs context via MCP (Firecrawl, Context7) when available
- ✅ Data steps + reporting out of the box (no jargon, just outputs)
- ✅ Health checks to keep things working as you go
- ✅ Git checkpoints so every run is reversible
- ✅ Windows‑friendly (WSL2) and local‑first privacy

---

## What It’s Best At 🎯

- Turning a vague prompt into a concrete artifact (HTML/PDF/CSV/Parquet)
- Orchestrating multi‑step flows across shell, data steps, and web context
- Keeping everything inside a clean project directory you can trust
- Making “do it again next week” a single command, not a rebuild

When to use it:

- Use when you want repeatable, file‑backed outputs with light automation
- Use when web/docs context matters and you need a brief/report
- Skip when pure chat is enough or you need heavy backend services

---

## The Story: From Ask → Artifact 📦

- You: “Summarize the latest competitor pricing and produce a one‑page brief.”
- Workbench: checks environment, creates/selects a project, and sets guardrails.
- MCP: fetches relevant pages (Firecrawl) and optional docs context (Context7).
- Data: builds a dataset, registers a view, and lets you run quick summaries.
- Report: renders an HTML brief and (if configured) exports a PDF.
- Safety: saves a git checkpoint so you can diff or roll back anytime.

Result: a tidy `projects/<name>/...` folder with datasets, HTML/PDF, and logs.

---

## What You Can Build 🧩

- 📈 Price Check Researcher — Scrape marketplaces (e.g., eBay), compare pricing, and produce a clean brief with highlights.
  ![Sales Insights sample](docs/images/samples/sales-insights.svg)
- 🧾 Office Automation Hero — Pull exports from different tools, clean them up, and generate reports that replace tedious data entry.
  ![Finance Reconciler sample](docs/images/samples/finance-reconciler.svg)
- 🧠 Curious → App Builder — Ask questions, pivot to a new project, then combine both into a lightweight “mini‑app” with shareable outputs.
  ![Docs Summarizer sample](docs/images/samples/docs-summarizer.svg)

Why it matters: your ideas don’t stall at “cool” — they convert into usable files you can send to a teammate or client.

---

## Prompt Snippets 🎮

Say these in Codex CLI. They create/choose a project, do the work, and save real outputs.

- 🏀 NBA Player Glow‑Up
  - “Create a project `nba-research` and set it current. Find recent game logs for [PLAYER NAME] and [TEAM] from trusted public sources. Build a fast table of games with points, rebounds, assists, and efficiency. Highlight trends week‑over‑week. Render an HTML brief and export a PDF under the project.”

- 🏚️ Closed Business Detective
  - “Create a project `business-check` and select it. Crawl the web for information on whether ‘[BUSINESS NAME]’ is closed, when it closed, last known address, and any successor company. Summarize findings with dates and source links. Produce an HTML one‑pager and a CSV of sources.”

- 💸 eBay Price Pulse
  - “Create `price-pulse` and set it current. Collect recent sold listings for ‘[PRODUCT]’ from marketplaces. Clean titles, remove outliers, and estimate typical price ranges (low/median/high). Generate a pricing brief with a simple visual and export CSV + PDF.”

- 🧾 Office Automation Hero
  - “Resume `ops-automation`. Combine the latest CRM export and invoicing export. Match by customer and month, flag mismatches, and prepare a ‘fix list’ CSV. Draft a short summary I can paste into Slack with counts and top issues. Render an HTML report too.”

- 🧠 Curious → Pivot → Mini‑App
  - “Create `topic-pivot`. Research ‘[TOPIC A]’ and summarize three key insights with sources. Now pivot: research ‘[TOPIC B]’ the same way. Build a small helper that lets me pick insights from both and outputs a merged brief as HTML + PDF.”

- 🗺️ Venue Shortlist in a Flash
  - “Create `event-venues`. Gather venues in [CITY] that fit 80–150 guests, budget under $[X], and available within [DATES]. Build a shortlist table with capacity, location, notes, and links. Export to Excel and render a one‑page summary.”

Tip: Replace bracketed fields like [PLAYER NAME], [PRODUCT], and [CITY] with your specifics.

---

## Try It In 3 Minutes ⚡

- Clone and enter the repo:
  - `git clone https://github.com/Sharper-Flow/super-codex-workbench.git`
  - `cd super-codex-workbench`
- Launch Codex CLI and run setup:
  - `codex` → say: “run the setup script”
  - The script prepares your environment, installs dependencies, and scaffolds `.env`
- Run the guided first‑project workflow:
  - In Codex, say: “Run the first‑project workflow for a project named ‘demo’.”
- Open your outputs under:
  - `projects/demo/reports` and `projects/demo/...`

Windows first-time? Use `./scripts/windows-setup.ps1 -ProvisionWSL -DefaultProfile Ubuntu`
then work inside Ubuntu under `~/`.

---

## Minimal Prompts 🧭

- “Diagnose the environment and show details.”
- “List all projects.”
- “Resume the project named ‘demo’.”
- “Use the MCP web workflow to summarize https://example.com, limit to 5 pages, and create a brief under the current project.”
- “Render an HTML report using the sample template, then export that HTML to a PDF.”

More quick prompts live in AGENTS.md.

---

## Configure MCP 🔌

- Firecrawl requires `FIRECRAWL_API_KEY`; Context7 is optional.
- Copy `.env.example` → `.env` and set keys if you have them.
- Verify MCP:
  - In Codex, say: “Show MCP info.”
  - Then: “Check MCP status.”

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
