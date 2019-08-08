from pyppeteer.page import Page


async def navigator_webdriver(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    const newProto = navigator.__proto__
    delete newProto.webdriver
    navigator.__proto__ = newProto
}
    """
    )
