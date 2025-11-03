#!/usr/bin/env bash
# Usage: ./scripts/make-demo-gif.sh
set -euo pipefail

echo "[demo] Ensuring Playwright + Pillow are installed (uv)"
uv add playwright pillow >/dev/null 2>&1 || true

echo "[demo] Installing Chromium browser for Playwright"
uv run playwright install chromium

echo "[demo] Generating demo GIF via Playwright"
uv run python scripts/demo/make_gif.py

echo "[demo] Done. Output at docs/images/demo-60s.gif"

