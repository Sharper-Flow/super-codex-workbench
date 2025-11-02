#!/usr/bin/env bash
set -euo pipefail

# Create and switch to a new branch from main (or current HEAD if main missing)
# Usage: ./scripts/git-start.sh feature/add-reporting

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
cd "$ROOT_DIR"

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <branch-name>" >&2
  exit 1
fi

BR="$1"
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[git-start] Not a git repository: $ROOT_DIR" >&2
  exit 1
fi

BASE="main"
if ! git show-ref --verify --quiet refs/heads/main; then
  BASE="HEAD"
fi

git checkout -B "$BR" "$BASE"
echo "[git-start] Switched to new branch: $BR (base: $BASE)"

