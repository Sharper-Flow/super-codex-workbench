# AGENTS.md

Purpose: Guidance for AI agents and contributors working inside this repository (repo root).

Scope: Applies to the entire directory tree rooted at the repository's top‑level folder (whatever it's named on disk).

## Codex CLI Is The Operator
- All user interactions occur through Codex CLI. Treat this repo as an agent‑first workbench.
- Codex CLI may scaffold files, run commands, and reorganize as needed to satisfy user requests while following the rules here.
- Codex CLI may install additional Python packages via `uv` when tasks require new functionality, updating `pyproject.toml` and `uv.lock`.
- Codex CLI may use locally configured MCP servers (see `mcp.config.json`) with credentials from `.env`.

## Response Style (Repo‑Specific)
- In this repository, return responses with strong visual balance for the user — use clear section headers, concise bullet points, and tasteful emoji to guide attention and improve scannability.
- Keep within CLI constraints: plain text, short headers (1–3 words), bullets preferred, and no ANSI codes. Emoji are welcome when they add clarity (e.g., ✅, ⚠️, 💡, 🚀).
- Maintain brevity and substance: prioritize actionable steps, outcomes, and next actions; avoid decorative overload.
- Still follow the global CLI formatting rules (no tables by default, no heavy markup); combine them with emoji for emphasis.

## Agent Playbook (Do This Every Time)

1) Setup enforcement (repo‑name agnostic)
- From the repo root, read `setup-requirements.json`. If missing or any required item is false
  (`uv_installed`, `venv_ready`, `deps_synced`, `env_file_present`, `folders_initialized`), assume a fresh environment and run:
  - `bash ./scripts/setup.sh -y -p demo` (use a meaningful project name in place of `demo`).
- After setup, verify:
  - `uv run python main.py -v diagnose`
  - `uv run python main.py mcp info`

2) Environment discipline
- Always run inside `./.venv` using `uv run <cmd>`. Never use system `python`/`pip`.
- After changing code or deps, run `./scripts/check.sh` and fix all issues (Ruff + Mypy) before proceeding.

3) Project context first
- Prompt to resume or create a project at session start.
- Use:
  - `uv run python main.py projects context --json`
  - `uv run python main.py projects resume --name <NAME>` or `projects create --name <NAME>`
- Default all outputs to `projects/<current>/...`; only fall back to top‑level if no project is set.

4) Data handling
- Use the Warehouse API only; do not write files directly under `warehouse/`.
- Name datasets clearly; partitions should be meaningful (e.g., `date`, `source`).
- Query with DuckDB: views are auto‑registered as `ds_<dataset>`.
- Prefer Parquet for larger outputs; install `pyarrow` if needed.

5) Reporting
- Template search precedence: `projects/<current>/templates` then `templates/`.
- Render with:
  - `uv run python main.py reports render-html --template <tpl> [--output ...]`
  - `uv run python main.py reports export-pdf [--html ...] [--output ...]`
- If HTML→PDF fails, install a backend: `weasyprint` or `pdfkit` + `wkhtmltopdf`.

6) MCP usage
- Firecrawl requires `FIRECRAWL_API_KEY`; Context7 is optional (free tier assumed).
- Prefer the workflow command for web context:
  - `uv run python main.py workflow mcp-web --url <URL> [--c7-query <q>] --limit 5`

7) Guided first‑project workflow
- Kick‑start a new user’s project:
  - `uv run python main.py workflow first-project --name <NAME> [--with-mcp]`
- This ensures folders, creates/selects the project, lands sample data, runs SQL, and renders outputs.

8) Response style (always)
- Use short headers, tight bullets, and tasteful emoji (✅ ⚠️ 💡 🚀) for emphasis.
- Provide next steps; avoid excessive verbosity.

9) Git checkpoints (mandatory)
- After completing a task or a logical step, make a local checkpoint:
  - `./scripts/git-save.sh "<type>: <concise summary>"` (e.g., `feat: add mcp web workflow`)
- Push regularly if a remote is configured:
  - `./scripts/git-push.sh`
- For larger efforts, start a feature branch first:
  - `./scripts/git-start.sh feature/<slug>`
- Commit messages: use conventional types when possible (`feat`, `fix`, `docs`, `chore`, `refactor`).
- Never commit secrets (see `.gitignore`); keep diffs minimal and scoped.

## Quick Command Reference (from repo root)
- Setup once: `bash ./scripts/setup.sh -y -p demo`
- Diagnose: `uv run python main.py -v diagnose`
- Project list: `uv run python main.py projects list`
- First‑project workflow: `uv run python main.py workflow first-project --name demo`
- MCP web workflow: `uv run python main.py workflow mcp-web --url https://example.com --limit 5`
- Warehouse SQL: `uv run python main.py warehouse sql --query "select 1 as x"`
- Checks: `./scripts/check.sh`
- Save checkpoint: `./scripts/git-save.sh "chore: checkpoint"`
- Push branch: `./scripts/git-push.sh`
- New branch: `./scripts/git-start.sh feature/add-x`

## Setup Checklist (Do This First)
- Work under Linux home (e.g., `/home/<user>/codex`) for performance — avoid `/mnt/c`.
- Ensure `uv` is installed and on PATH.
- Use the venv for everything: prefer `uv run <cmd>` or `. .venv/bin/activate`.
- Copy `.env.example` to `.env` and set MCP vars: `CONTEXT7_API_KEY`, `CONTEXT7_MCP_URL`, `FIRECRAWL_API_KEY`, `FIRECRAWL_MCP_URL`.
- Verify MCP: `uv run python main.py check-mcp` and `uv run python main.py mcp info`.
- Sync deps: `uv sync`.
- Sanity check: `uv run python main.py -v diagnose`.

## Day‑to‑Day Codex CLI Workflow
- Project context first: list with `projects context --json`, then `projects resume --name <NAME>` or `projects create --name <NAME>`.
- Use the Warehouse API and CLI for data (never write directly to files under `warehouse/`).
- Use Reports CLI to render HTML/PDF. If PDF export fails, install a backend (`weasyprint` or `pdfkit` + `wkhtmltopdf`).
- For a demo end‑to‑end run (with a current project set): `uv run python main.py workflow sample`.
- For first‑time guided project setup (creates/selects project and produces outputs):
  `uv run python main.py workflow first-project --name <NAME> [--with-mcp]`.
- Increase verbosity with `-v`/`-vv` for rich logs.

### Setup Requirements Enforcement
- Codex CLI must read `setup-requirements.json` and ensure all required items are satisfied before executing tasks.
- If the file is missing or any required item is false (e.g., `uv_installed`, `venv_ready`, `deps_synced`, `env_file_present`, `folders_initialized`), assume a fresh environment and run `bash scripts/setup.sh -y`.
- Firecrawl requires an API key; if `mcp_firecrawl_configured` is false and a Firecrawl-backed action is requested, prompt the user to add `FIRECRAWL_API_KEY` to `.env`, then re-run setup.
- Context7 is optional (free tier assumed); lack of an API key should not block Context7-backed tasks.

## Principles
- Keep changes minimal, focused, and reversible.
- Prefer clarity over cleverness; avoid unnecessary abstractions.
- Fix root causes, not symptoms; don’t touch unrelated code.
- Match existing style and naming; keep diffs small and readable.

## Coding & Structure
- Line length target: ~100 chars.
- Use meaningful names; avoid single-letter identifiers except for trivial loops.
- Add only the files needed for the task at hand.
- When adding scripts, mark them executable (`chmod +x`) and include a one-line usage comment at top.
- Documentation lives next to code: place `README.md` or `NOTES.md` in the relevant folder if helpful.

## Edit & Patch Rules
- Use atomic patches; group related changes together.
- Do not add license headers unless explicitly requested.
- Prefer `.editorconfig` settings for formatting; do not introduce new formatters unless requested.
- For large edits, outline intent and verify success criteria before proceeding.

## File Conventions
- Markdown docs: wrap at ~100 chars; keep headings short; use ordered bullets only when sequence matters.
- Scripts: default to bash with `#!/usr/bin/env bash` and `set -euo pipefail`.
- Configuration: include minimal, well-commented defaults; provide `*.example` files when secrets/env vars are involved.

### Data Warehouse Pattern
- Canonical data lives under `warehouse/` managed by the Warehouse API (`workbench/warehouse.py`).
- Datasets are registered in `warehouse/manifest.json` and stored in `warehouse/datasets/<name>/`.
- Use Hive-style partitions (`key=value`) when needed.
- Apps should write via Warehouse API, not directly to files.

### Directory Responsibilities
- `apps/` — app-specific logic; each app should prefix dataset names to avoid collisions.
- `data/` — ad hoc inputs/scratch during tasks; not canonical.
- `reports/` — user-facing outputs (Excel/PDF) and templates.
- `warehouse/` — curated datasets; prefer append-only batches; compact on demand.
- `logs/` — structured logs for task runs.

## WSL2 (Ubuntu) Notes
- Work inside Linux filesystem (e.g., `/home/...`) for performance; avoid editing under `/mnt/c` for heavy workloads.
- Ensure LF line endings. If using Git, consider `git config core.autocrlf input`.
- Opening in Windows: `explorer.exe .` (from the directory) or `wslview <file>`.
- Scripts may need the executable bit set: `chmod +x script.sh`.
- Watch permissions when moving files between Windows and WSL; reapply `chmod` as needed.

## Tools & Tips
- Searching: prefer `rg` (ripgrep). Read files in chunks (<= 250 lines) when necessary.
- Keep environment assumptions explicit in READMEs.
- If adding dependencies, document install steps for Ubuntu (`apt`, `pip`, `npm`, etc.).

## Python Code Rules
- Data models: use Pydantic v2+ with strict validation and no extras.
  - Prefer inheriting from `workbench.models.StrictBaseModel` (strict=True, extra='forbid').
- Typing: new and modified Python code must be fully typed.
  - Add explicit return types (use `-> None` when appropriate).
  - Avoid `Any` unless absolutely necessary.
- Lint/format: use Ruff for format and lint; use Mypy for static checks.
  - After EVERY code change, run `./scripts/check.sh` (runs Ruff format, Ruff check --fix, Mypy) and fix all issues.
  - Keep `ruff.toml` and `mypy.ini` as the single sources of truth for style and typing.

## Dependency Policy (uv)
- Manage Python dependencies exclusively with `uv` inside `.venv`.
  - Add: `uv add <pkg>`
  - Remove: `uv remove <pkg>`
  - Sync: `uv sync`
- Never use global `pip`/`python` for this project.

## MCP Usage Policy
- MCP configuration lives in `mcp.config.json`; secrets in `.env` (see `.env.example`).
  - `CONTEXT7_API_KEY`, `CONTEXT7_MCP_URL`
  - `FIRECRAWL_API_KEY`, `FIRECRAWL_MCP_URL`
- Codex CLI may call MCP servers for documentation search, crawling, extraction, and summarization.
- Never commit real secrets; update `.env.example` when new vars are needed.

## Mandatory Environment Rule (Python)
- ALWAYS use the local virtualenv at the repo root (`./.venv`).
  - Interactive shells: run `. .venv/bin/activate` before any commands.
  - Scripts/commands: prefer `uv run <cmd ...>` to auto-use the venv.
- Do NOT use system `python`/`pip` in this project.
  - Add deps with `uv add <package>` and commit `pyproject.toml` + `uv.lock`.
  - Re-sync with `uv sync` if `pyproject.toml` changes.

## Review Checklist
- Change is minimal and scoped to the goal.
- Docs updated (if behavior or usage changes).
- Scripts are executable and have usage comments.
- No stray credentials or machine-specific paths.

## Approvals & Safety
- Request elevation/approval when the environment requires it for installs or networked tasks.
- Avoid destructive commands (e.g., `rm -rf`) unless explicitly asked and justified.
- Keep changes atomic and reversible; summarize intent for larger edits.
