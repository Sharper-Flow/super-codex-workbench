#!/usr/bin/env bash
# Usage: ./scripts/make-rocket-gif.sh
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
cd "$ROOT_DIR"

echo "[rocket] Ensuring Playwright + Pillow are installed (via uv)"
uv add playwright pillow >/dev/null 2>&1 || true

echo "[rocket] Installing Chromium for Playwright (if needed)"
uv run playwright install chromium

echo "[rocket] Generating rocket GIF from SVG via Playwright capture"
uv run python scripts/demo/make_gif.py \
  --html docs/demo/rocket.html \
  --out docs/images/anim/codex-rocket.gif \
  --width 920 \
  --height 220 \
  --duration 3.0 \
  --interval 0.08

echo "[rocket] Done → docs/images/anim/codex-rocket.gif"

