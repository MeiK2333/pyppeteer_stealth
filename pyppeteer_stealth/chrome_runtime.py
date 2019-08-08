from pyppeteer.page import Page


async def chrome_runtime(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    window.chrome = {
        runtime: {}
    }
}
"""
    )
