#!/usr/bin/env bash
set -euo pipefail

# Add or update an MCP server entry in mcp.config.json
# Usage: ./scripts/mcp-add.sh <name> <sse-url> <apiKeyEnvVar>

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
cd "$ROOT_DIR"

if [[ $# -lt 3 ]]; then
  echo "Usage: $0 <name> <sse-url> <apiKeyEnvVar>" >&2
  exit 1
fi

NAME="$1"; URL="$2"; KEYENV="$3"

python3 - "$NAME" "$URL" "$KEYENV" << 'PY'
import json, sys, os
name, url, keyenv = sys.argv[1:4]
path = 'mcp.config.json'
cfg = {"mcpServers": {}}
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            cfg = json.load(f)
        except Exception:
            pass
cfg.setdefault('mcpServers', {})[name] = {
    "transport": {"type": "sse", "url": url},
    "credentials": {"apiKey": f"${{{keyenv}}}"},
    "metadata": {"description": f"{name} MCP server"}
}
with open(path, 'w', encoding='utf-8') as f:
    json.dump(cfg, f, indent=2)
print(f"[mcp-add] Added/updated MCP server '{name}' -> {url} (apiKeyVar={keyenv})")
PY

