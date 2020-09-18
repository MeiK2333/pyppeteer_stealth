from pathlib import Path

from pyppeteer.page import Page


async def webgl_vendor(
    page: Page,
    webgl_vendor: str = "Intel Inc.",
    renderer: str = "Intel Iris OpenGL Engine",
    **kwargs
) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/webgl.vendor.js").read_text(),
        webgl_vendor,
        renderer,
    )
