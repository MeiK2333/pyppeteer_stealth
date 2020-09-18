from pathlib import Path

from pyppeteer.page import Page


async def iframe_content_window(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/iframe.contentWindow.js").read_text()
    )
