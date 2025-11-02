from __future__ import annotations

import logging
import sys
from typing import Any

from loguru import logger as loguru_logger
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install as rich_traceback_install


def setup_logging(verbosity: int = 0) -> None:
    """Configure logging with Rich formatting and Loguru integration.

    - Installs rich tracebacks (with locals).
    - Configures stdlib logging to use RichHandler.
    - Forwards Loguru logs through stdlib logging so formatting is consistent.
    - `verbosity` increases log level (0=INFO, 1=DEBUG, >=2=TRACE via Loguru).
    """
    console = Console(stderr=True)
    rich_traceback_install(show_locals=False, width=120, extra_lines=2)

    # Determine level
    if verbosity >= 2:
        std_level = logging.DEBUG
        loguru_level = "TRACE"
    elif verbosity == 1:
        std_level = logging.DEBUG
        loguru_level = "DEBUG"
    else:
        std_level = logging.INFO
        loguru_level = "INFO"

    # Configure std logging with Rich
    logging.basicConfig(
        level=std_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(
                console=console,
                rich_tracebacks=True,
                show_time=True,
                show_level=True,
                show_path=False,
                markup=True,
            )
        ],
    )

    # Forward Loguru to stdlib logging (so it gets Rich formatting)
    class _StdlibSink:
        def write(self, message: str) -> None:  # pragma: no cover
            # Fallback plain write; Rich formatting handled by logging handler below.
            sys.stderr.write(message)

    # Remove default Loguru sink to avoid duplicate logs
    loguru_logger.remove()

    def _loguru_forwarder(message: Any) -> None:
        record = message.record
        # Map Loguru level to stdlib logging level
        level_name = record["level"].name
        level = getattr(logging, level_name, logging.INFO)
        logging.getLogger(record.get("name") or __name__).log(level, record["message"])

    loguru_logger.add(_loguru_forwarder, level=loguru_level, backtrace=True, diagnose=False)


__all__ = ["setup_logging", "loguru_logger"]
