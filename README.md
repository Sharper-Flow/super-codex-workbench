# Super Codex Workbench 🚀
## Batteries‑Included for Codex CLI


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

|  Feature Highlights| | |
| --- | --- | --- |
| 🚀 Agent‑first, prompt‑driven experience | Faster from prompt to outputs | Build and scaffold directly from prompts in Codex CLI |
| 🚣 Project‑centric flow | Keep work organized and reproducible | Everything lands under the active project |
| 📦 Reliable warehouse | Trustworthy storage with fast SQL | CSV/JSONL/Parquet with instant DuckDB views |
| 📝 Elegant reporting | Share clear, polished outputs | Jinja2 HTML → PDF and Excel export |
| 🌐 Web context built‑in | Pull relevant docs and pages fast | Context7 (docs/code) + Firecrawl (crawl/summarize) |
| 🌈 Great logs | Understand progress and issues quickly | Rich + Loguru for readable diagnostics |
| 🛣️ Guided workflows | Onboard and deliver quickly | First‑project setup and MCP web report flow |
| 🧰 Quality gates | Maintain clean, typed code | uv‑managed deps, Ruff lint, Mypy typing |
| 🪟 Windows‑friendly | Smooth setup on Windows/WSL2 | One‑shot provisioning (Terminal, Nerd Font, WSL2, zsh) |
| 🔌 Extensible | Add new services easily | Configure MCP servers/APIs and scaffold clients |

## Who Is This For?
- 🙋‍♂️ Newcomers who want a safe, guided path to build data + reports
- ⚡ Power users who value structure, repeatability, and speed
- 🤝 Teams who want a standard way for agents to work locally

## How It Works (In 60 Seconds)
1) Choose a project (resume or create). Everything lands under that name.
2) Ingest data via the Warehouse API (CSV/JSONL/Parquet; partition by date/source).
3) Query with DuckDB SQL on auto‑registered views (`ds_<dataset>`).
4) Report with Jinja2 HTML → export to PDF/Excel under `projects/<current>/reports`.

## Actions at a Glance (Prompts)
- 🔧 “Set up the workspace with a demo project and run the guided first‑project workflow.”
- 🗂️ “Show my projects and resume ‘demo’ (or create it if missing).”
- 🗃️ “Show me recent outputs for the ‘demo’ project.”
- 🧠 “Preview the events dataset using a simple SQL query.”
- 🌐 “Crawl https://example.com, summarize the top pages, and generate a quick report.”
- 📝 “Render a sample HTML report and export it to PDF under the current project.”
- 📦 “Run the repository checks and fix any formatting or typing issues.”

## Showcase
- Windows Terminal theme (CodexDarkGrey) + Nerd Font

  ![Windows Terminal dark grey theme](docs/images/windows-terminal-theme.svg)

- Sample HTML report preview

  ![Sample report preview](docs/images/report-preview.svg)

## Notes
Talk to the agent — we’ve done the heavy lifting. Technical details (setup, MCP, coding rules, git checkpoints) live in `AGENTS.md`.
