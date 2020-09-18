from pathlib import Path

from pyppeteer.page import Page


async def navigator_languages(page: Page, languages: [str] = ["en-US", "en"], **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/navigator.languages.js").read_text(),
        languages,
    )
