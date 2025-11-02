from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, cast

import duckdb
import pandas as pd

DEFAULT_DATASET_FORMAT = "csv"  # csv | jsonl | parquet (requires pyarrow)
TIMESTAMP_FMT = "%Y%m%d_%H%M%S%f"


def _now_stamp() -> str:
    return datetime.utcnow().strftime(TIMESTAMP_FMT)


@dataclass
class Dataset:
    name: str
    format: str = DEFAULT_DATASET_FORMAT
    partitioning: Optional[List[str]] = None

    def to_dict(self) -> Dict:
        return {
            "format": self.format,
            "partitioning": self.partitioning or [],
        }


class Warehouse:
    """Filesystem-backed data warehouse with simple manifest and partitions.

    Layout:
    - warehouse/
      - manifest.json
      - datasets/
        - <name>/
          - key=value/ ... / file.ext
    """

    def __init__(self, base_path: Path | str = Path("warehouse")) -> None:
        self.base_path = Path(base_path)
        self.datasets_path = self.base_path / "datasets"
        self.manifest_path = self.base_path / "manifest.json"
        self.base_path.mkdir(parents=True, exist_ok=True)
        self.datasets_path.mkdir(parents=True, exist_ok=True)
        if not self.manifest_path.exists():
            self._write_manifest({"datasets": {}})

    # Manifest handling
    def _read_manifest(self) -> Dict[str, Any]:
        try:
            with self.manifest_path.open("r", encoding="utf-8") as f:
                return cast(Dict[str, Any], json.load(f))
        except json.JSONDecodeError:
            return {"datasets": {}}

    def _write_manifest(self, manifest: Dict[str, Any]) -> None:
        with self.manifest_path.open("w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

    def list_datasets(self) -> Dict[str, Dataset]:
        manifest = self._read_manifest()
        result = {}
        for name, meta in manifest.get("datasets", {}).items():
            result[name] = Dataset(
                name=name,
                format=meta.get("format", DEFAULT_DATASET_FORMAT),
                partitioning=meta.get("partitioning", []),
            )
        return result

    def register_dataset(
        self,
        name: str,
        *,
        format: str = DEFAULT_DATASET_FORMAT,
        partitioning: Optional[List[str]] = None,
        overwrite: bool = False,
    ) -> Dataset:
        manifest = self._read_manifest()
        datasets = manifest.setdefault("datasets", {})
        if name in datasets and not overwrite:
            meta = datasets[name]
            return Dataset(
                name=name,
                format=meta.get("format", DEFAULT_DATASET_FORMAT),
                partitioning=meta.get("partitioning", []),
            )
        ds = Dataset(name=name, format=format, partitioning=partitioning or [])
        datasets[name] = ds.to_dict()
        self._write_manifest(manifest)
        (self.datasets_path / name).mkdir(parents=True, exist_ok=True)
        return ds

    # Paths and IO
    def dataset_dir(self, name: str, partition: Optional[Dict[str, str]] = None) -> Path:
        d = self.datasets_path / name
        if partition:
            for k, v in partition.items():
                d = d / f"{k}={v}"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def _ext_for_format(self, fmt: str) -> str:
        return {"csv": ".csv", "jsonl": ".jsonl", "parquet": ".parquet"}.get(fmt, ".csv")

    def _parquet_available(self) -> bool:
        try:
            import pyarrow  # noqa: F401

            return True
        except Exception:
            return False

    def write_df(
        self,
        name: str,
        df: pd.DataFrame,
        *,
        format: Optional[str] = None,
        partition: Optional[Dict[str, str]] = None,
        filename: Optional[str] = None,
        mode: str = "append",
    ) -> Path:
        datasets = self.list_datasets()
        ds = datasets.get(name) or self.register_dataset(
            name, format=format or DEFAULT_DATASET_FORMAT
        )
        fmt = format or ds.format
        if fmt == "parquet" and not self._parquet_available():
            raise RuntimeError(
                "Parquet requested but pyarrow not installed. Install with `uv add pyarrow`."
            )
        target_dir = self.dataset_dir(name, partition)
        if filename is None:
            filename = f"batch_{_now_stamp()}" + self._ext_for_format(fmt)
        path = target_dir / filename

        if fmt == "csv":
            header = True
            if mode == "append" and path.exists():
                header = False
            df.to_csv(path, index=False, mode="a" if mode == "append" else "w", header=header)
        elif fmt == "jsonl":
            df.to_json(path, orient="records", lines=True)
        elif fmt == "parquet":
            df.to_parquet(path, index=False)
        else:
            raise ValueError(f"Unsupported format: {fmt}")
        return path

    def read_df(
        self,
        name: str,
        *,
        format: Optional[str] = None,
        partition: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        datasets = self.list_datasets()
        if name not in datasets:
            raise KeyError(f"Dataset '{name}' not registered")
        fmt = format or datasets[name].format
        base = self.dataset_dir(name, partition)
        files = sorted([p for p in base.glob(f"**/*{self._ext_for_format(fmt)}") if p.is_file()])
        if not files:
            return pd.DataFrame()

        frames = []
        for p in files:
            if fmt == "csv":
                frames.append(pd.read_csv(p))
            elif fmt == "jsonl":
                frames.append(pd.read_json(p, lines=True))
            elif fmt == "parquet":
                if not self._parquet_available():
                    raise RuntimeError(
                        "Parquet requested but pyarrow not installed. "
                        "Install with `uv add pyarrow`."
                    )
                frames.append(pd.read_parquet(p))
        df = pd.concat(frames, ignore_index=True)
        if limit is not None:
            df = df.head(limit)
        return df

    # DuckDB SQL over datasets
    def sql(self, query: str, register: Optional[Dict[str, str]] = None) -> pd.DataFrame:
        """Execute a DuckDB SQL query.

        - Registers each dataset as a view `ds_<name>` scanning files of its default format.
        - Optionally pass `register` to map additional views to glob paths
          (e.g., {"extra": "path/to/*.parquet"}).
        """
        con = duckdb.connect()
        # Register datasets
        datasets = self.list_datasets()
        for name, meta in datasets.items():
            ext = self._ext_for_format(meta.format)
            glob = str((self.datasets_path / name / "**" / f"*{ext}").resolve())
            view = f"ds_{name}"
            if meta.format == "parquet":
                con.execute(
                    f"CREATE OR REPLACE VIEW {view} AS SELECT * FROM read_parquet('{glob}')"
                )
            elif meta.format == "csv":
                con.execute(
                    f"CREATE OR REPLACE VIEW {view} AS SELECT * FROM read_csv_auto('{glob}')"
                )
            elif meta.format == "jsonl":
                sql = (
                    f"CREATE OR REPLACE VIEW {view} AS SELECT * FROM read_json("
                    f"'{glob}', format='newline_delimited')"
                )
                con.execute(sql)
        # Extra registrations
        if register:
            for view, glob in register.items():
                if glob.endswith(".parquet") or glob.endswith("*.parquet"):
                    con.execute(
                        f"CREATE OR REPLACE VIEW {view} AS SELECT * FROM read_parquet('{glob}')"
                    )
                elif glob.endswith(".csv") or glob.endswith("*.csv"):
                    con.execute(
                        f"CREATE OR REPLACE VIEW {view} AS SELECT * FROM read_csv_auto('{glob}')"
                    )
                elif glob.endswith(".jsonl") or glob.endswith("*.jsonl"):
                    sql = (
                        f"CREATE OR REPLACE VIEW {view} AS SELECT * FROM read_json("
                        f"'{glob}', format='newline_delimited')"
                    )
                    con.execute(sql)
        return con.execute(query).df()
