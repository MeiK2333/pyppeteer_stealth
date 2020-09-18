from pathlib import Path

from pyppeteer.page import Page


async def window_outerdimensions(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/window.outerdimensions.js").read_text()
    )
