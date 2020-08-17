from pyppeteer.page import Page


async def navigator_webdriver(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    delete Object.getPrototypeOf(navigator).webdriver
}
    """
    )
