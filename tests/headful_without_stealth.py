import asyncio

from pyppeteer import launch

from pyppeteer_stealth import stealth


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()

    # await stealth(page)

    await page.goto("https://bot.sannysoft.com/")
    await page.screenshot({"path": "headful_without_stealth.png", "fullPage": True})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
