from pyppeteer.page import Page


async def navigator_languages(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    Object.defineProperty(navigator, 'languages', {
        get: () => ['en-US', 'en']
    })
}
    """
    )
