from pathlib import Path

from pyppeteer.page import Page


async def navigator_webdriver(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/navigator.webdriver.js").read_text()
    )
