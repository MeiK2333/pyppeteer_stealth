from pyppeteer.page import Page


async def user_agent_override(
    page: Page,
    user_agent: str = None,
    language: str = "en-US,en",
    platform: str = "Win32",
    **kwargs
) -> None:
    if user_agent == None:
        ua = await page.browser.userAgent()
    else:
        ua = user_agent
    ua = ua.replace("HeadlessChrome", "Chrome")  # hide headless nature
    override = {"userAgent": ua, "acceptLanguage": language, "platform": platform}
    await page._client.send("Network.setUserAgentOverride", override)
