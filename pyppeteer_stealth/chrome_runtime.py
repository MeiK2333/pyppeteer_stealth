from pathlib import Path

from pyppeteer.page import Page


async def chrome_runtime(page: Page, run_on_insecure_origins: bool = False, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/chrome.runtime.js").read_text(),
        run_on_insecure_origins,
    )
