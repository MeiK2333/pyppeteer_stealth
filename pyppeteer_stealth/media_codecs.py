from pathlib import Path

from pyppeteer.page import Page


async def media_codecs(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/media.codecs.js").read_text()
    )
