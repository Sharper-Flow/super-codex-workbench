#!/usr/bin/env python
"""
Generate a 60s demo GIF by driving a local HTML storyboard via Playwright
and stitching screenshots into docs/images/demo-60s.gif.

Usage: uv run python scripts/demo/make_gif.py
"""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import List

from PIL import Image
from playwright.sync_api import Browser, Page, sync_playwright


@dataclass
class CaptureConfig:
    html_path: Path
    output_gif: Path
    width: int = 1280
    height: int = 720
    duration_s: float = 60.0
    interval_s: float = 0.7  # ~85 frames for ~60s


def ensure_dirs(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def open_page(browser: Browser, cfg: CaptureConfig) -> Page:
    context = browser.new_context(
        viewport={"width": cfg.width, "height": cfg.height}, record_video_dir=None
    )
    page = context.new_page()
    url = cfg.html_path.resolve().as_uri()
    page.goto(url)
    page.wait_for_timeout(1000)  # settle
    return page


def capture_frames(page: Page, cfg: CaptureConfig) -> List[Image.Image]:
    frames: List[Image.Image] = []
    start = time.time()
    next_ts = start
    while True:
        now = time.time()
        if now - start >= cfg.duration_s:
            break
        if now >= next_ts:
            buf = page.screenshot(full_page=False)
            frames.append(Image.open(BytesIO(buf)))
            next_ts += cfg.interval_s
        else:
            time.sleep(0.02)
    return frames


def save_gif(frames: List[Image.Image], out_path: Path, interval_s: float) -> None:
    if not frames:
        raise RuntimeError("No frames captured; aborting.")
    duration_ms = max(50, int(interval_s * 1000))
    first, *rest = frames
    first.save(
        out_path,
        save_all=True,
        append_images=rest,
        duration=duration_ms,
        loop=0,
        optimize=True,
        disposal=2,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--html",
        type=Path,
        default=Path("docs/demo/demo.html"),
        help="Path to the demo HTML storyboard",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("docs/images/demo-60s.gif"),
        help="Output GIF path",
    )
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--duration", type=float, default=60.0)
    parser.add_argument("--interval", type=float, default=0.7)
    args = parser.parse_args()

    cfg = CaptureConfig(
        html_path=args.html,
        output_gif=args.out,
        width=args.width,
        height=args.height,
        duration_s=args.duration,
        interval_s=args.interval,
    )

    ensure_dirs(cfg.output_gif)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = open_page(browser, cfg)
        frames = capture_frames(page, cfg)
        save_gif(frames, cfg.output_gif, cfg.interval_s)
        browser.close()

    print(f"[demo] Wrote GIF → {cfg.output_gif}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
