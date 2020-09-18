from pathlib import Path

from pyppeteer.page import Page


async def with_utils(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/utils.js").read_text()
    )
