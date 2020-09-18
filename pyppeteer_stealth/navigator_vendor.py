from pathlib import Path

from pyppeteer.page import Page


async def navigator_vendor(page: Page, vendor: str = "Google Inc.", **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/navigator.vendor.js").read_text(), vendor
    )
