from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, cast

TS_FMT = "%Y-%m-%dT%H:%M:%SZ"


def now_iso() -> str:
    return datetime.utcnow().strftime(TS_FMT)


@dataclass
class Project:
    name: str
    description: str = ""
    created: str = now_iso()
    updated: str = now_iso()

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "created": self.created,
            "updated": self.updated,
        }


class Projects:
    def __init__(self, base: Path | str = Path("projects")) -> None:
        self.base = Path(base)
        self.manifest_path = self.base / "manifest.json"
        self.base.mkdir(parents=True, exist_ok=True)
        if not self.manifest_path.exists():
            self._write({"projects": {}, "current": None})

    def _read(self) -> Dict[str, Any]:
        try:
            return cast(
                Dict[str, Any],
                json.loads(self.manifest_path.read_text(encoding="utf-8")),
            )
        except Exception:
            return {"projects": {}, "current": None}

    def _write(self, data: Dict[str, Any]) -> None:
        self.manifest_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def list(self) -> Dict[str, Project]:
        d = self._read()
        return {
            name: Project(
                name=name,
                description=meta.get("description", ""),
                created=meta.get("created", now_iso()),
                updated=meta.get("updated", now_iso()),
            )
            for name, meta in d.get("projects", {}).items()
        }

    def current(self) -> Optional[str]:
        return self._read().get("current")

    def set_current(self, name: str) -> None:
        d = self._read()
        if name not in d.get("projects", {}):
            raise KeyError(f"Project '{name}' does not exist")
        d["current"] = name
        # bump updated time
        d["projects"][name]["updated"] = now_iso()
        self._write(d)

    def create(self, name: str, description: str = "") -> Project:
        d = self._read()
        if name in d.get("projects", {}):
            # idempotent: return existing
            meta = d["projects"][name]
            return Project(
                name=name,
                description=meta.get("description", ""),
                created=meta.get("created", now_iso()),
                updated=meta.get("updated", now_iso()),
            )
        p = Project(name=name, description=description)
        d.setdefault("projects", {})[name] = p.to_dict()
        self._write(d)
        # scaffold simple per-project directories
        root = self.base / name
        for sub in ["notes", "scratch", "reports", "artifacts", "templates"]:
            (root / sub).mkdir(parents=True, exist_ok=True)
        return p

    def context(self, recent: int = 10) -> Dict:
        items = self.list()
        # sort by updated desc
        ordered = sorted(items.values(), key=lambda p: p.updated, reverse=True)
        return {
            "current": self.current(),
            "projects": [p.name for p in ordered],
            "recent": [p.name for p in ordered[:recent]],
        }

    # Helpers for file layout
    def root_for(self, name: str) -> Path:
        return self.base / name

    def current_root(self) -> Optional[Path]:
        cur = self.current()
        if not cur:
            return None
        root = self.root_for(cur)
        root.mkdir(parents=True, exist_ok=True)
        return root
