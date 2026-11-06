"""Render the repository's brand images with headless Chromium (Playwright).

All images reuse the existing raster artwork of the book logo
(edap/images/logo_big.png: paper texture and the coffee cup with Python latte
art); the text is rendered as real text.

- docs/images/branding_*.png: two plots from the comfort chapter of the book,
  made with pyedautils and its bundled sample data (Mollier h,x diagram with
  outside air and ventilation line, comfort compass). Used by the social preview
  and at the top of the README.
- docs/banner.png (1280x320) from scripts/banner.html, the README header.
- docs/social-preview.png (1280x640) from scripts/social-preview.html. Upload it
  manually under the repository's Settings -> General -> Social preview (there is
  no API for it).
- edap/images/favicon.png (192x192), the cup cropped from the logo, used as the
  book's favicon (html.favicon in edap/_config.yml).

Needs network access (plotly.js, D3 and the Lexend font come from CDNs). Run
from the repository root with uv (no Node needed):

    uv run --no-project --with playwright python -m playwright install chromium   # once
    uv run --no-project --with playwright --with "pyedautils>=0.0.32" python scripts/render_branding.py
"""

import tempfile
from importlib import resources
from pathlib import Path

import pandas as pd
from playwright.sync_api import sync_playwright

from pyedautils._mollier import pressure_from_altitude
from pyedautils.comfort import comfort_compass_distribution
from pyedautils.plots import plot_comfort_compass, plot_mollier_hx

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LOGO = ROOT / "edap" / "images" / "logo_big.png"
DATA = resources.files("pyedautils") / "data"

# Cup in logo_big.png (1536x1024): centre and outer rim radius in pixels.
CUP_X, CUP_Y, CUP_R = 345, 450, 182


def plot_pages():
    """HTML pages of the example plots, as (name, html, viewport width, height)."""
    room = pd.read_csv(DATA / "room_climate_sample.csv", parse_dates=["timestamp"])

    # As in the book (comfortMollierHx): room data at 450 m a.s.l. with the room's target
    # band (8-18 °C, 40-70 %, the same band as the compass below), the warning bands with
    # their default offsets and the outside air on a cold, damp spring night.
    zone = {"temperature": (8, 18), "rel_humidity": (0.40, 0.70), "abs_humidity": None}
    mollier = plot_mollier_hx(data=room, outdoor=(2, 85),
                              altitude=450, pressure=pressure_from_altitude(450),
                              domain_x=(0.0, 0.016), domain_y=(-5.0, 32.0),
                              comfort_zone=zone, comfort_zone_orange=True, comfort_zone_red=True,
                              height=560)

    # As in the book (comfortCompass): the room's own target band.
    dist = comfort_compass_distribution(room.set_index("timestamp"), temp_band=(8, 18), hum_band=(40, 70))
    compass = plot_comfort_compass(dist, show_legend=False, scale="fit", width=420, height=420)

    return [
        ("branding_mollier_hx", mollier, 760, 580),
        ("branding_comfort_compass", compass.to_html(include_plotlyjs="cdn"), 420, 420),
    ]


def render_plots(browser, tmp):
    for name, html, width, height in plot_pages():
        src = Path(tmp) / f"{name}.html"
        src.write_text(html, encoding="utf-8")
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=2)
        page.goto(src.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(800)
        page.screenshot(path=str(DOCS / "images" / f"{name}.png"))
        print(f"docs/images/{name}.png")
        page.close()


def render_template(browser, template, out, height):
    page = browser.new_page(viewport={"width": 1280, "height": height}, device_scale_factor=1)
    page.goto((ROOT / "scripts" / template).as_uri(), wait_until="networkidle")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    page.screenshot(path=str(DOCS / out))
    print(f"docs/{out}")
    page.close()


def render_favicon(browser, tmp):
    """The cup (without the handle) as a round 192x192 icon with a transparent corner."""
    size = 192
    scale = size / (2 * CUP_R)
    src = Path(tmp) / "favicon.html"
    src.write_text(
        '<body style="margin:0;background:transparent">'
        f'<div style="width:{size}px;height:{size}px;border-radius:50%;'
        f"background:url('{LOGO.as_uri()}') no-repeat;"
        f'background-size:{1536 * scale}px {1024 * scale}px;'
        f'background-position:{-(CUP_X - CUP_R) * scale}px {-(CUP_Y - CUP_R) * scale}px"></div></body>',
        encoding="utf-8")
    page = browser.new_page(viewport={"width": size, "height": size}, device_scale_factor=1)
    page.goto(src.as_uri())
    page.wait_for_timeout(200)
    out = ROOT / "edap" / "images" / "favicon.png"
    page.screenshot(path=str(out), omit_background=True)
    print("edap/images/favicon.png")
    page.close()


with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
    browser = p.chromium.launch(args=["--hide-scrollbars", "--allow-file-access-from-files"])
    try:
        render_plots(browser, tmp)
        render_favicon(browser, tmp)
        render_template(browser, "banner.html", "banner.png", 320)
        render_template(browser, "social-preview.html", "social-preview.png", 640)
    finally:
        browser.close()
