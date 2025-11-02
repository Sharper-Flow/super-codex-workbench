import json
import os
import platform
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd
import typer
from loguru import logger
from rich import print

from workbench.logging_setup import setup_logging
from workbench.mcp_clients import context7_search, firecrawl_crawl, pages_to_dataframe
from workbench.projects import Projects
from workbench.warehouse import Warehouse

app = typer.Typer(help="Codex Workbench: data, reports, APIs")
warehouse_app = typer.Typer(help="Data warehouse commands")
reports_app = typer.Typer(help="Reporting commands")
projects_app = typer.Typer(help="Projects management commands")
mcp_app = typer.Typer(help="MCP helper commands")
workflow_app = typer.Typer(help="Sample end-to-end workflows")


@app.callback()
def _configure(
    verbose: int = typer.Option(
        0, "-v", "--verbose", count=True, help="Increase log verbosity (-v, -vv)"
    ),
) -> None:
    """Global CLI configuration hook (logging, env, etc.)."""
    setup_logging(verbose)
    logger.debug("Logging configured (verbosity=%s)", verbose)


@app.command()
def hello(name: str = "world") -> None:
    """Say hello."""
    logger.success(f"Hello from Codex Workbench, {name}!")


@app.command("check-mcp")
def check_mcp() -> None:
    """Show MCP-related env vars presence (no values printed)."""
    keys = [
        "CONTEXT7_API_KEY",
        "CONTEXT7_MCP_URL",
        "FIRECRAWL_API_KEY",
        "FIRECRAWL_MCP_URL",
    ]
    missing = []
    for k in keys:
        if os.getenv(k):
            logger.info(f"{k}: set")
        else:
            logger.warning(f"{k}: missing")
            missing.append(k)
    if missing:
        raise typer.Exit(code=1)


@app.command("diagnose")
def diagnose(
    json_out: bool = typer.Option(False, "--json", help="Output machine-readable JSON"),
) -> None:
    """Print environment and workspace diagnostics for Codex CLI."""

    def pkg_version(name: str) -> Optional[str]:
        try:
            from importlib.metadata import version

            return version(name)
        except Exception:
            return None

    project_root = Path(__file__).resolve().parent
    venv = os.environ.get("VIRTUAL_ENV")
    venv_active = bool(venv) or (str(project_root) in sys.prefix)
    dirs = {
        "data_raw": (project_root / "data" / "raw").exists(),
        "data_processed": (project_root / "data" / "processed").exists(),
        "reports_excel": (project_root / "reports" / "excel").exists(),
        "reports_pdf": (project_root / "reports" / "pdf").exists(),
        "templates": (project_root / "templates").exists(),
        "logs": (project_root / "logs").exists(),
        "warehouse": (project_root / "warehouse").exists(),
    }
    mcp_env = {
        "CONTEXT7_API_KEY": bool(os.getenv("CONTEXT7_API_KEY")),
        "CONTEXT7_MCP_URL": bool(os.getenv("CONTEXT7_MCP_URL")),
        "FIRECRAWL_API_KEY": bool(os.getenv("FIRECRAWL_API_KEY")),
        "FIRECRAWL_MCP_URL": bool(os.getenv("FIRECRAWL_MCP_URL")),
    }
    mcp_config_path = project_root / "mcp.config.json"
    mcp_config_ok = False
    mcp_servers = []
    if mcp_config_path.exists():
        try:
            cfg = json.loads(mcp_config_path.read_text(encoding="utf-8"))
            mcp_servers = sorted(list((cfg.get("mcpServers") or {}).keys()))
            mcp_config_ok = True
        except Exception:
            mcp_config_ok = False

    versions = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "httpx": pkg_version("httpx"),
        "pandas": pkg_version("pandas"),
        "pydantic": pkg_version("pydantic"),
        "jinja2": pkg_version("jinja2"),
        "typer": pkg_version("typer"),
        "rich": pkg_version("rich"),
        "loguru": pkg_version("loguru"),
        "openpyxl": pkg_version("openpyxl"),
        "reportlab": pkg_version("reportlab"),
        "pyarrow": pkg_version("pyarrow"),
    }

    summary = {
        "venv_active": venv_active,
        "venv_path": venv or sys.prefix,
        "project_root": str(project_root),
        "dirs": dirs,
        "mcp_env": mcp_env,
        "mcp_config_present": mcp_config_path.exists(),
        "mcp_config_ok": mcp_config_ok,
        "mcp_servers": mcp_servers,
        "versions": versions,
    }

    if json_out:
        print(json.dumps(summary, indent=2))
        return

    logger.info(f"Python {versions['python']} on {versions['platform']}")
    logger.info(f"Virtualenv active: {venv_active} ({venv or sys.prefix})")
    for key, exists in dirs.items():
        logger.info(f"dir:{key} => {'ok' if exists else 'missing'}")
    logger.info(
        "MCP config present: %s valid:%s servers:%s",
        mcp_config_path.exists(),
        mcp_config_ok,
        mcp_servers,
    )
    for k, present in mcp_env.items():
        logger.info(f"env:{k} => {'set' if present else 'missing'}")
    logger.info("Key package versions:")
    for k, v in versions.items():
        logger.info(f"  {k}={v}")


@app.command("init")
def init_workspace(base: Path = Path(".")) -> None:
    """Create standard folders for data, reports, templates, logs."""
    folders = [
        base / "data" / "raw",
        base / "data" / "processed",
        base / "reports" / "excel",
        base / "reports" / "pdf",
        base / "templates",
        base / "logs",
    ]
    for d in folders:
        d.mkdir(parents=True, exist_ok=True)
    logger.success("Workspace folders ensured.")
    logger.info("data/{raw,processed}, reports/{excel,pdf}, templates, logs")


@app.command("make-excel")
def make_excel(output: Optional[Path] = None) -> None:
    """Generate a sample Excel file using pandas/openpyxl."""
    if output is None:
        pr = Projects()
        base = pr.current_root()
        output = (base / "reports/excel/sample.xlsx") if base else Path("reports/excel/sample.xlsx")
    output.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame({"item": ["alpha", "beta", "gamma"], "value": [1, 2, 3]})
    df.to_excel(output, index=False, engine="openpyxl")
    logger.success(f"Wrote Excel: {output}")


@app.command("make-pdf")
def make_pdf(output: Optional[Path] = None) -> None:
    """Generate a simple PDF using reportlab."""
    if output is None:
        pr = Projects()
        base = pr.current_root()
        output = (base / "reports/pdf/sample.pdf") if base else Path("reports/pdf/sample.pdf")
    from reportlab.lib.pagesizes import LETTER
    from reportlab.pdfgen import canvas

    output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output), pagesize=LETTER)
    width, height = LETTER
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "Codex Workbench Sample Report")
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 100, "This PDF was generated by reportlab.")
    c.drawString(72, height - 120, "Customize templates in the templates/ folder.")
    c.showPage()
    c.save()
    logger.success(f"Wrote PDF: {output}")


def main() -> None:
    app()


# ----------------------
# Warehouse CLI commands
# ----------------------


@warehouse_app.command("list")
def warehouse_list() -> None:
    wh = Warehouse()
    datasets = wh.list_datasets()
    if not datasets:
        logger.warning("No datasets registered.")
        raise typer.Exit()
    for name, ds in datasets.items():
        parts = ",".join(ds.partitioning or []) or "-"
        logger.info(f"{name} format={ds.format} partitions={parts}")


@warehouse_app.command("register")
def warehouse_register(
    name: str = typer.Option(..., "--name", help="Dataset name"),
    format: str = typer.Option("csv", "--format", help="csv|jsonl|parquet"),
    partitioning: str = typer.Option("", "--partitioning", help="Comma-separated keys"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing registration"),
) -> None:
    wh = Warehouse()
    parts = [p for p in (partitioning.split(",") if partitioning else []) if p]
    ds = wh.register_dataset(name, format=format, partitioning=parts, overwrite=overwrite)
    part_display = ",".join(ds.partitioning or []) or "-"
    logger.success(f"Registered: {ds.name} format={ds.format} partitions={part_display}")


@warehouse_app.command("write-sample")
def warehouse_write_sample(
    name: str = typer.Option(..., "--name", help="Dataset name"),
    partition: Optional[str] = typer.Option(
        None, "--partition", help="Comma-separated k=v pairs (e.g., date=2025-01-01,source=api)"
    ),
    format: Optional[str] = typer.Option(None, "--format", help="Override dataset format"),
) -> None:
    wh = Warehouse()
    # Simple sample DataFrame
    df = pd.DataFrame(
        {
            "when": ["2025-01-01T00:00:00Z", "2025-01-01T01:00:00Z"],
            "value": [1, 2],
            "note": ["sample", "sample"],
        }
    )
    part_dict = {}
    if partition:
        for pair in partition.split(","):
            if not pair:
                continue
            if "=" not in pair:
                raise typer.BadParameter("Partition must be k=v pairs")
            k, v = pair.split("=", 1)
            part_dict[k] = v
    path = wh.write_df(name, df, format=format, partition=part_dict or None)
    logger.success(f"Wrote sample batch: {path}")


@warehouse_app.command("show")
def warehouse_show(
    name: str = typer.Option(..., "--name", help="Dataset name"),
    limit: int = typer.Option(5, "--limit", help="Rows to show"),
) -> None:
    wh = Warehouse()
    df = wh.read_df(name, limit=limit)
    if df.empty:
        logger.warning("Dataset is empty or not found.")
        raise typer.Exit()
    print(df)


@warehouse_app.command("sql")
def warehouse_sql(
    query: str = typer.Option(..., "--query", help="DuckDB SQL; views available as ds_<dataset>"),
    limit: Optional[int] = typer.Option(None, "--limit", help="Limit rows after query"),
    output: Optional[Path] = typer.Option(
        None, "--output", help="Save result as CSV/Parquet based on extension"
    ),
) -> None:
    """Run SQL against warehouse datasets using DuckDB.

    Views `ds_<dataset>` are auto-created for every registered dataset.
    """
    try:
        from workbench.warehouse import Warehouse
    except Exception:
        logger.error("Warehouse module not available")
        raise typer.Exit(code=1)
    wh = Warehouse()
    df = wh.sql(query)
    if limit is not None:
        df = df.head(limit)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.suffix == ".parquet":
            try:
                import pyarrow  # noqa: F401

                df.to_parquet(output, index=False)
            except Exception:
                logger.error("Writing Parquet requires pyarrow. Install with `uv add pyarrow`.")
                raise typer.Exit(code=1)
        else:
            df.to_csv(output, index=False)
        logger.success(f"Saved query result: {output}")
    else:
        print(df)


# ----------------------
# Projects CLI commands
# ----------------------


@projects_app.command("list")
def projects_list() -> None:
    pr = Projects()
    current = pr.current()
    items = pr.list()
    if not items:
        logger.warning("No projects found. Create one with: projects create --name <NAME>")
        raise typer.Exit()
    for name, meta in items.items():
        star = "*" if name == current else "-"
        logger.info(f"{star} {name} — {meta.description}")


@projects_app.command("create")
def projects_create(
    name: str = typer.Option(..., "--name"),
    description: str = typer.Option("", "--desc", help="Short description"),
    set_current: bool = typer.Option(True, "--current/--no-current", help="Set as current project"),
) -> None:
    pr = Projects()
    p = pr.create(name, description)
    logger.success(f"Project created: {p.name}")
    if set_current:
        pr.set_current(name)
        logger.info(f"Current project set to: {name}")


@projects_app.command("resume")
def projects_resume(
    name: Optional[str] = typer.Option(None, "--name", help="Project to resume"),
) -> None:
    pr = Projects()
    if not name:
        ctx = pr.context()
        logger.info("No project specified. Available to resume (most recent first):")
        for n in ctx["projects"]:
            logger.info(f"- {n}")
        logger.info("Select with: projects resume --name <NAME>")
        raise typer.Exit(code=1)
    pr.set_current(name)
    logger.success(f"Resumed project: {name}")


@projects_app.command("context")
def projects_context(json_out: bool = typer.Option(False, "--json")) -> None:
    pr = Projects()
    ctx = pr.context()
    if json_out:
        print(json.dumps(ctx, indent=2))
    else:
        current = ctx.get("current")
        logger.info(f"Current project: {current}")
        logger.info("Recent projects:")
        for n in ctx.get("recent", []):
            logger.info(f"- {n}")


# ----------------------
# Reports CLI commands
# ----------------------


def _jinja_env() -> Any:
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    # Search precedence: project templates (if current) then global templates
    loaders = []
    pr = Projects()
    base_dir = Path(__file__).resolve().parent
    cur = pr.current_root()
    if cur and (cur / "templates").exists():
        loaders.append(str(cur / "templates"))
    loaders.append(str(base_dir / "templates"))
    env = Environment(
        loader=FileSystemLoader(loaders),
        autoescape=select_autoescape(["html", "xml"]),
    )
    return env


@reports_app.command("render-html")
def reports_render_html(
    template: str = typer.Option(
        "sample.html.j2", "--template", help="Template filename under templates/"
    ),
    output: Optional[Path] = typer.Option(None, "--output", help="Output HTML path"),
    title: str = typer.Option("Codex Workbench Report", "--title"),
) -> None:
    from datetime import datetime

    env = _jinja_env()
    tpl = env.get_template(template)
    df = pd.DataFrame({"item": ["alpha", "beta", "gamma"], "value": [1, 2, 3]})
    rows = df.to_dict(orient="records")
    html = tpl.render(
        title=title, generated_at=datetime.utcnow().isoformat() + "Z", table=df, rows=rows
    )
    pr = Projects()
    base = pr.current_root()
    out = output or (
        (base / "reports/html/sample.html") if base else Path("reports/html/sample.html")
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    logger.success(f"Rendered HTML: {out}")


@reports_app.command("export-pdf")
def reports_export_pdf(
    html: Optional[Path] = typer.Option(None, "--html", help="Input HTML file"),
    output: Optional[Path] = typer.Option(None, "--output", help="Output PDF path"),
) -> None:
    """Export an HTML file to PDF via WeasyPrint or pdfkit.

    Codex CLI may install `weasyprint` or `pdfkit` + system `wkhtmltopdf` as needed.
    """
    pr = Projects()
    base = pr.current_root()
    if html is None:
        html = (base / "reports/html/sample.html") if base else Path("reports/html/sample.html")
    out = output or (
        (base / "reports/pdf/sample_from_html.pdf")
        if base
        else Path("reports/pdf/sample_from_html.pdf")
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        import weasyprint

        pdf = weasyprint.HTML(filename=str(html)).write_pdf()
        out.write_bytes(pdf)
        logger.success(f"Wrote PDF via WeasyPrint: {out}")
        return
    except Exception:
        pass
    try:
        import pdfkit

        pdfkit.from_file(str(html), str(out))
        logger.success(f"Wrote PDF via pdfkit: {out}")
        return
    except Exception:
        logger.error(
            "No HTML->PDF backend available. Install one of: "
            "`uv add weasyprint` (may need system deps) or "
            "`uv add pdfkit` and install `wkhtmltopdf`."
        )
        raise typer.Exit(code=1)


# ----------------------
# MCP helper commands
# ----------------------


@mcp_app.command("info")
def mcp_info() -> None:
    root = Path(__file__).resolve().parent
    cfg_path = root / "mcp.config.json"
    servers = []
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        servers = sorted(list((cfg.get("mcpServers") or {}).keys()))
    except Exception:
        pass
    env_presence = {
        "CONTEXT7_API_KEY": bool(os.getenv("CONTEXT7_API_KEY")),
        "CONTEXT7_MCP_URL": bool(os.getenv("CONTEXT7_MCP_URL")),
        "FIRECRAWL_API_KEY": bool(os.getenv("FIRECRAWL_API_KEY")),
        "FIRECRAWL_MCP_URL": bool(os.getenv("FIRECRAWL_MCP_URL")),
    }
    logger.info(f"MCP config: {cfg_path} servers={servers}")
    for k, set_ in env_presence.items():
        logger.info(f"env:{k} => {'set' if set_ else 'missing'}")


# ----------------------
# Workflow CLI commands
# ----------------------


@workflow_app.command("sample")
def workflow_sample() -> None:
    """Run a sample end-to-end workflow using current project if set.

    Steps:
    1) Generate sample data and land into warehouse dataset `events` (partitioned by date).
    2) Run DuckDB SQL over `ds_events` to aggregate counts.
    3) Render HTML and export PDF into `projects/<current>/reports` when a
       current project exists.
    """
    from datetime import datetime, timezone

    # 1) Generate data and land to warehouse
    wh = Warehouse()
    today = datetime.now(timezone.utc).date().isoformat()
    df = pd.DataFrame({"event": ["alpha", "beta", "alpha", "gamma"], "value": [1, 2, 1, 3]})
    path = wh.write_df("events_demo", df, partition={"date": today})
    logger.success(f"Landed sample data: {path}")

    # 2) Run SQL aggregation
    agg = wh.sql(
        "select event, count(*) as n, sum(value) as sum_value "
        "from ds_events_demo group by event order by event"
    )

    # Save aggregation as artifact (CSV) in project if available
    pr = Projects()
    base = pr.current_root()
    art = (base / "artifacts/agg.csv") if base else Path("artifacts/agg.csv")
    art.parent.mkdir(parents=True, exist_ok=True)
    agg.to_csv(art, index=False)
    logger.success(f"Saved aggregation: {art}")

    # 3) Render HTML + export PDF into project reports
    env = _jinja_env()
    tpl = env.get_template("sample.html.j2")
    rows = agg.to_dict(orient="records")
    html_text = tpl.render(
        title="Sample Workflow Report",
        generated_at=datetime.now(timezone.utc).isoformat(),
        table=agg,
        rows=rows,
    )
    html_out = (base / "reports/html/workflow.html") if base else Path("reports/html/workflow.html")
    html_out.parent.mkdir(parents=True, exist_ok=True)
    html_out.write_text(html_text, encoding="utf-8")
    logger.success(f"Rendered HTML: {html_out}")

    # Try PDF
    try:
        import weasyprint

        pdf_bytes = weasyprint.HTML(string=html_text).write_pdf()
        pdf_out = (base / "reports/pdf/workflow.pdf") if base else Path("reports/pdf/workflow.pdf")
        pdf_out.parent.mkdir(parents=True, exist_ok=True)
        pdf_out.write_bytes(pdf_bytes)
        logger.success(f"Wrote PDF via WeasyPrint: {pdf_out}")
    except Exception:
        try:
            import pdfkit

            pdf_out = (
                (base / "reports/pdf/workflow.pdf") if base else Path("reports/pdf/workflow.pdf")
            )
            pdf_out.parent.mkdir(parents=True, exist_ok=True)
            pdfkit.from_string(html_text, str(pdf_out))
            logger.success(f"Wrote PDF via pdfkit: {pdf_out}")
        except Exception:
            logger.warning(
                "PDF export skipped: install `weasyprint` or `pdfkit`+`wkhtmltopdf` to enable."
            )


@workflow_app.command("mcp-web")
def workflow_mcp_web(
    url: str = typer.Option(..., "--url", help="Seed URL to crawl with Firecrawl"),
    limit: int = typer.Option(5, "--limit", help="Max pages to collect"),
    query: Optional[str] = typer.Option(None, "--c7-query", help="Optional Context7 search query"),
) -> None:
    """MCP-backed workflow: crawl via Firecrawl and optionally search via Context7.

    - Writes crawled pages to warehouse dataset `mcp_pages` partitioned by date/source.
    - Renders an HTML report (and tries to export PDF) under the current project.
    """
    from datetime import datetime, timezone

    today = datetime.now(timezone.utc).date().isoformat()

    # 1) Firecrawl crawl
    pages = firecrawl_crawl(url, limit=limit)
    df = pages_to_dataframe(pages)
    wh = Warehouse()
    if not df.empty:
        p = wh.write_df("mcp_pages", df, partition={"date": today, "source": "firecrawl"})
        logger.success(f"Landed Firecrawl pages: {p}")
    else:
        logger.warning("No Firecrawl pages collected.")

    # 2) Optional Context7 search
    c7_docs = []
    if query:
        c7_docs = context7_search(query, limit=limit)
        if c7_docs:
            df_c7 = pd.DataFrame([d.model_dump() for d in c7_docs])
            p2 = wh.write_df("mcp_pages", df_c7, partition={"date": today, "source": "context7"})
            logger.success(f"Landed Context7 docs: {p2}")
        else:
            logger.warning("No Context7 results.")

    # 3) Render a combined report at project path
    env = _jinja_env()
    tpl = env.get_template("mcp_report.html.j2")
    pr = Projects()
    base = pr.current_root()
    html_out = (
        (base / "reports/html/mcp_report.html") if base else Path("reports/html/mcp_report.html")
    )
    html_out.parent.mkdir(parents=True, exist_ok=True)
    html_text = tpl.render(
        title="MCP Web Report",
        generated_at=datetime.now(timezone.utc).isoformat(),
        url=url,
        pages=[p.model_dump() for p in pages],
        context7=[d.model_dump() for d in c7_docs],
    )
    html_out.write_text(html_text, encoding="utf-8")
    logger.success(f"Rendered MCP HTML: {html_out}")

    # Try PDF export
    try:
        import weasyprint

        pdf_bytes = weasyprint.HTML(string=html_text).write_pdf()
        pdf_out = (
            (base / "reports/pdf/mcp_report.pdf") if base else Path("reports/pdf/mcp_report.pdf")
        )
        pdf_out.parent.mkdir(parents=True, exist_ok=True)
        pdf_out.write_bytes(pdf_bytes)
        logger.success(f"Wrote MCP PDF via WeasyPrint: {pdf_out}")
    except Exception:
        logger.warning(
            "PDF export skipped: install `weasyprint` or `pdfkit`+`wkhtmltopdf` to enable."
        )


@workflow_app.command("first-project")
def workflow_first_project(
    name: str = typer.Option("demo", "--name", help="Project name to create/select"),
    include_mcp: bool = typer.Option(
        False, "--with-mcp", help="Attempt MCP web step if Firecrawl key is present"
    ),
) -> None:
    """Guided setup for the first project (project-aware outputs).

    Steps:
    - Ensure workspace folders
    - Create/select project
    - Land minimal example data into the warehouse
    - Run a simple SQL aggregation
    - Render HTML and try to export PDF under the project reports
    - Optionally run MCP-backed web step if requested and configured
    """
    # Ensure folders
    init_workspace()

    # Create/select project
    pr = Projects()
    pr.create(name, description="First project")
    pr.set_current(name)
    logger.success(f"Project ready: {name}")

    # Run the standard sample workflow (project-aware paths already used by commands)
    workflow_sample()

    # Optional MCP step
    if include_mcp and os.getenv("FIRECRAWL_API_KEY"):
        try:
            workflow_mcp_web(url="https://example.com", limit=3, query=None)
        except Exception:
            logger.warning("Skipping MCP web step due to errors.")


# Attach sub-commands under main app
app.add_typer(warehouse_app, name="warehouse")
app.add_typer(reports_app, name="reports")
app.add_typer(projects_app, name="projects")
app.add_typer(mcp_app, name="mcp")
app.add_typer(workflow_app, name="workflow")


if __name__ == "__main__":
    main()
