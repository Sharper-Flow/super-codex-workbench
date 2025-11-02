from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import List, Optional

import httpx
import pandas as pd
from loguru import logger

from .models import StrictBaseModel


class CrawledPage(StrictBaseModel):
    url: str
    title: Optional[str] = None
    snippet: Optional[str] = None


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def firecrawl_crawl(url: str, *, limit: int = 5, timeout_s: int = 30) -> List[CrawledPage]:
    """Fetch pages via Firecrawl API.

    Requires FIRECRAWL_API_KEY. Optionally configure base via FIRECRAWL_BASE_URL.
    Returns up to `limit` pages with url/title/snippet.
    """
    api_key = os.getenv("FIRECRAWL_API_KEY")
    base = os.getenv("FIRECRAWL_BASE_URL", "https://api.firecrawl.dev")
    if not api_key:
        logger.warning("FIRECRAWL_API_KEY not set; skipping Firecrawl crawl.")
        return []
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    client = httpx.Client(base_url=base, headers=headers, timeout=timeout_s)
    try:
        # This endpoint may differ by plan; adjust if needed.
        # Fallback to search when crawl endpoint not available.
        resp = client.post(
            "/v1/crawl",
            json={"url": url, "depth": 1, "include_subdomains": False, "max_pages": limit},
        )
        if resp.status_code >= 400:
            logger.warning("Firecrawl crawl failed (%s): %s", resp.status_code, resp.text[:200])
            return []
        data = resp.json()
        items = data.get("pages") or data.get("data") or []
        results: List[CrawledPage] = []
        for it in items[:limit]:
            # Common fields may vary by API; attempt to map.
            results.append(
                CrawledPage(
                    url=it.get("url") or it.get("link") or url,
                    title=it.get("title"),
                    snippet=(it.get("snippet") or (it.get("content") or "")[:200]) or None,
                )
            )
        return results
    except Exception as e:
        logger.warning("Firecrawl request failed: %s", e)
        return []
    finally:
        client.close()


def pages_to_dataframe(pages: List[CrawledPage]) -> pd.DataFrame:
    if not pages:
        return pd.DataFrame(columns=["url", "title", "snippet", "fetched_at"])  # empty
    rows = [{**p.model_dump(), "fetched_at": _now_iso()} for p in pages]
    return pd.DataFrame(rows)


class Context7Doc(StrictBaseModel):
    title: Optional[str] = None
    url: Optional[str] = None
    snippet: Optional[str] = None


def context7_search(query: str, *, limit: int = 5, timeout_s: int = 30) -> List[Context7Doc]:
    """Search via Context7 HTTP API if available. Falls back to empty list.

    Env vars:
    - CONTEXT7_API_KEY (required)
    - CONTEXT7_BASE_URL (optional), default "https://api.context7.com"
    Endpoint assumed: GET /v1/search?q=...&limit=...
    """
    api_key = os.getenv("CONTEXT7_API_KEY")
    base = os.getenv("CONTEXT7_BASE_URL", "https://api.context7.com")
    if not api_key:
        logger.warning("CONTEXT7_API_KEY not set; skipping Context7 search.")
        return []
    try:
        resp = httpx.get(
            f"{base}/v1/search",
            params={"q": query, "limit": limit},
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout_s,
        )
        if resp.status_code >= 400:
            logger.warning("Context7 search failed (%s): %s", resp.status_code, resp.text[:200])
            return []
        items = resp.json().get("results", [])
        return [
            Context7Doc(title=it.get("title"), url=it.get("url"), snippet=it.get("snippet"))
            for it in items[:limit]
        ]
    except Exception as e:
        logger.warning("Context7 request failed: %s", e)
        return []


__all__ = [
    "CrawledPage",
    "Context7Doc",
    "firecrawl_crawl",
    "context7_search",
    "pages_to_dataframe",
]
