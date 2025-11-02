#!/usr/bin/env bash
set -euo pipefail

# Codex Workbench setup script (WSL2 Ubuntu friendly)
# - Ensures uv/venv, installs dependencies, prepares env, verifies CLI
# - Optionally creates a project and runs a sample workflow

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

REQ_FILE="${REPO_ROOT}/setup-requirements.json"

YES="false"
PROJECT_NAME=""

usage() {
  cat <<EOF
Usage: bash scripts/setup.sh [options]

Options:
  -y, --yes            Non-interactive; accept defaults and skip prompts
  -p, --project NAME   Create and select a project named NAME
  -s, --sample         Run guided first-project workflow after setup
  -h, --help           Show this help

This script will:
  - Check for uv and provide install guidance if missing
  - Create/refresh the local virtualenv and sync dependencies (uv sync)
  - Copy .env.example -> .env if missing and remind to set MCP keys
  - Initialize standard folders (data/, reports/, templates/, logs/)
  - Optionally create/select a project and run a sample workflow
  - Run diagnostics to verify setup
EOF
}

log() { printf "\033[1;34m[setup]\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m[warn]\033[0m  %s\n" "$*"; }
err() { printf "\033[1;31m[err]\033[0m   %s\n" "$*"; }
ok() { printf "\033[1;32m[ok]\033[0m    %s\n" "$*"; }

json_set() {
  local key="$1"; shift
  local val="$1"; shift
  python3 - "$REQ_FILE" "$key" "$val" << 'PY'
import json, sys, os
path, key, val = sys.argv[1:4]
val_bool = (val.lower() == 'true')
data = {}
if os.path.exists(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        data = {}
data[key] = val_bool
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
PY
}

ensure_requirements() {
  if [[ ! -f "$REQ_FILE" ]]; then
    cp "$REPO_ROOT/setup-requirements.json" "$REQ_FILE" 2>/dev/null || cat >"$REQ_FILE" <<'JSON'
{
  "uv_installed": false,
  "venv_ready": false,
  "deps_synced": false,
  "env_file_present": false,
  "folders_initialized": false,
  "mcp_firecrawl_configured": false,
  "mcp_context7_optional": true,
  "mcp_context7_configured": false,
  "project_created": false,
  "ran_diagnostics": false,
  "ran_sample_workflow": false
}
JSON
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -y|--yes) YES="true"; shift ;;
    -p|--project) PROJECT_NAME="${2:-}"; shift 2 ;;
    -s|--sample) RUN_SAMPLE="true"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) err "Unknown option: $1"; usage; exit 1 ;;
  esac
done

# 1) Environment checks
ensure_requirements
if grep -qi microsoft /proc/version 2>/dev/null; then
  log "Detected WSL/Microsoft kernel (ok)."
fi

if ! command -v uv >/dev/null 2>&1; then
  warn "uv not found. Please install uv before continuing:"
  echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
  echo "Then ensure ~/.local/bin is on your PATH (echo 'export PATH=\"$HOME/.local/bin:$PATH\"' >> ~/.bashrc)"
  if [[ "$YES" != "true" ]]; then
    read -r -p "Continue without uv? (y/N) " ans
    if [[ ! "$ans" =~ ^[Yy]$ ]]; then
      exit 1
    fi
  fi
  json_set uv_installed false
else
  json_set uv_installed true
fi

# 2) Prepare env file
if [[ ! -f .env ]]; then
  if [[ -f .env.example ]]; then
    cp .env.example .env
    log "Created .env from .env.example. Please edit .env to set MCP keys."
  else
    warn ".env.example not found; skipping .env creation."
  fi
fi
if [[ -f .env ]]; then
  json_set env_file_present true
else
  json_set env_file_present false
fi

# 3) Sync dependencies and create venv
if command -v uv >/dev/null 2>&1; then
  log "Syncing dependencies with uv..."
  uv sync
  if [[ -d .venv ]]; then
    json_set venv_ready true
  fi
  json_set deps_synced true
else
  warn "uv missing; attempting to proceed with existing environment."
  if [[ -d .venv ]]; then
    json_set venv_ready true
  fi
fi

# 4) Initialize folders
log "Ensuring standard folders exist..."
if command -v uv >/dev/null 2>&1; then
  uv run python main.py init || true
else
  python3 main.py init || true
fi
json_set folders_initialized true

# 5) Project selection/creation
if [[ -z "$PROJECT_NAME" && "$YES" != "true" ]]; then
  read -r -p "Create/select a project now? (y/N) " ans
  if [[ "$ans" =~ ^[Yy]$ ]]; then
    read -r -p "Project name: " PROJECT_NAME
  fi
fi

if [[ -n "$PROJECT_NAME" ]]; then
  log "Creating/selecting project: $PROJECT_NAME"
  if command -v uv >/dev/null 2>&1; then
    uv run python main.py projects create --name "$PROJECT_NAME" --desc "User project" || true
  else
    python3 main.py projects create --name "$PROJECT_NAME" --desc "User project" || true
  fi
  json_set project_created true
fi

# 6) Diagnostics
log "Running diagnostics..."
if command -v uv >/dev/null 2>&1; then
  uv run python main.py -v diagnose || true
  uv run python main.py mcp info || true
else
  python3 main.py -v diagnose || true
  python3 main.py mcp info || true
fi
json_set ran_diagnostics true

# 6b) MCP requirements assessment
# Firecrawl requires API key; Context7 is optional (free tier acceptable)
if grep -Eq '^FIRECRAWL_API_KEY=.+$' .env 2>/dev/null || [[ -n "${FIRECRAWL_API_KEY:-}" ]]; then
  json_set mcp_firecrawl_configured true
else
  json_set mcp_firecrawl_configured false
  warn "FIRECRAWL_API_KEY not found. Firecrawl MCP is required — ask the user to obtain an API key and update .env, then re-run setup."
fi

if grep -Eq '^CONTEXT7_API_KEY=.+$' .env 2>/dev/null || [[ -n "${CONTEXT7_API_KEY:-}" ]]; then
  json_set mcp_context7_configured true
else
  json_set mcp_context7_configured false
  warn "CONTEXT7_API_KEY not found. Context7 MCP is required — ask the user to obtain an API key and update .env, then re-run setup."
fi

# 7) Optional guided first-project workflow
if [[ "${RUN_SAMPLE:-false}" == "true" ]]; then
  log "Running guided first-project workflow..."
  if command -v uv >/dev/null 2>&1; then
    uv run python main.py workflow first-project --name "${PROJECT_NAME:-demo}" || true
  else
    python3 main.py workflow first-project --name "${PROJECT_NAME:-demo}" || true
  fi
  json_set ran_first_project_workflow true
fi
ok "Setup complete. Next steps:"
echo "- Edit .env and set MCP keys (CONTEXT7_*, FIRECRAWL_*)"
echo "- (Optional) MCP web workflow: uv run python main.py workflow mcp-web --url https://example.com --c7-query 'keyword'"
echo "- To re-run checks after changes: ./scripts/check.sh"
echo "- Setup requirements recorded in: $REQ_FILE"
