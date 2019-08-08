from pyppeteer.page import Page


async def user_agent(page: Page) -> None:
    ua = await page.browser.userAgent()
    ua = ua.replace("HeadlessChrome", "Chrome")
    await page.setUserAgent(ua)
