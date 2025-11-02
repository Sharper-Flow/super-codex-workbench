#!/usr/bin/env bash
set -euo pipefail

echo "[check] Running ruff format..."
uv run ruff format .

echo "[check] Running ruff check --fix..."
uv run ruff check . --fix

echo "[check] Running mypy..."
uv run mypy --config-file mypy.ini .

echo "[check] OK"

