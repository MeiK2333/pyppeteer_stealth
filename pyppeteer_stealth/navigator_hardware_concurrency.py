from pathlib import Path

from pyppeteer.page import Page


async def navigator_hardware_concurrency(page: Page, hardwareConcurrency: int = 4, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/navigator.hardwareConcurrency.js").read_text(),
        hardwareConcurrency,
    )
