from pathlib import Path

from pyppeteer.page import Page


async def navigator_permissions(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/navigator.permissions.js").read_text()
    )
