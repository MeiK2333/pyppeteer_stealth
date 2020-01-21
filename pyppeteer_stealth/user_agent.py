from pyppeteer.page import Page
import re


async def user_agent(page: Page) -> None:
    ua = await page.browser.userAgent()
    ua = ua.replace("HeadlessChrome", "Chrome")  # hide headless nature
    ua = re.sub(r'\(([^)]+)\)', '(Windows NT 10.0; Win64; x64)', ua, 1)  # ensure windows
    await page.setUserAgent(ua)
