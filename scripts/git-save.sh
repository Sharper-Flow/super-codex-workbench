#!/usr/bin/env bash
set -euo pipefail

# Save a local git checkpoint with a concise message.
# Usage: ./scripts/git-save.sh "feat: add warehouse sql command"

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
cd "$ROOT_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[git-save] Not a git repository: $ROOT_DIR" >&2
  exit 1
fi

MSG="${1:-}"
if [[ -z "${MSG}" ]]; then
  TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MSG="chore: checkpoint at ${TS}"
fi

# Stage all changes and commit if there is anything to commit.
git add -A
if git diff --cached --quiet; then
  echo "[git-save] No changes to commit."
  exit 0
fi

git commit -m "$MSG"
echo "[git-save] Committed: $MSG"

