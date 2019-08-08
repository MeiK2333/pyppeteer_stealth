from pyppeteer.page import Page


async def window_outerdimensions(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    try {
        if (window.outerWidth && window.outerHeight) {
            return
        }
        const windowFrame = 85
        window.outerWidth = window.innerWidth
        window.outerHeight = window.innerHeight + windowFrame
    } catch (err) { }
}
"""
    )
