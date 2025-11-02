#!/usr/bin/env bash
set -euo pipefail

# Push current branch to origin (sets upstream if needed)

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
cd "$ROOT_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[git-push] Not a git repository: $ROOT_DIR" >&2
  exit 1
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$BRANCH" == "HEAD" ]]; then
  BRANCH="main"
  git branch -M "$BRANCH" || true
fi

if git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
  git push
else
  if git remote get-url origin >/dev/null 2>&1; then
    git push -u origin "$BRANCH"
  else
    echo "[git-push] No 'origin' remote configured. Set it with:\n  git remote add origin <git-url>" >&2
    exit 1
  fi
fi

echo "[git-push] Pushed branch: $BRANCH"

