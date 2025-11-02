# Warehouse

Filesystem-backed data warehouse with a simple JSON manifest and Hive-style partition folders.

Layout:
- `warehouse/manifest.json` — registry of datasets
- `warehouse/datasets/<name>/[key=value/...]/file.(csv|jsonl|parquet)`

Use the CLI `warehouse` commands to register datasets, write sample data, and inspect.

