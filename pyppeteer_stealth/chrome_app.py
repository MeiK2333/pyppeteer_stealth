from pathlib import Path

from pyppeteer.page import Page


async def chrome_app(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/chrome.app.js").read_text()
    )
