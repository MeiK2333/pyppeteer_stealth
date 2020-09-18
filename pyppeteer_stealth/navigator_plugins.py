from pathlib import Path

from pyppeteer.page import Page


async def navigator_plugins(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/navigator.plugins.js").read_text()
    )
