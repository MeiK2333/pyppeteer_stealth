from pyppeteer.page import Page


async def console_debug(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    window.console.debug = () => {
        return null
    }
}
"""
    )
