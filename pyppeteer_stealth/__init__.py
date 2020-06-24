from pyppeteer.page import Page

from .chrome_runtime import chrome_runtime
from .console_debug import console_debug
from .iframe_content_window import iframe_content_window
from .navigator_languages import navigator_languages
from .navigator_permissions import navigator_permissions
from .navigator_plugins import navigator_plugins
from .navigator_webdriver import navigator_webdriver
from .user_agent import user_agent
from .webgl_vendor import webgl_vendor
from .window_outerdimensions import window_outerdimensions
from .media_codecs import media_codecs


async def stealth(page: Page) -> None:
    if not isinstance(page, Page):
        raise ValueError("page must is pyppeteer.page.Page")

    await chrome_runtime(page)
    await console_debug(page)
    await iframe_content_window(page)
    await navigator_languages(page)
    await navigator_permissions(page)
    await navigator_plugins(page)
    await navigator_webdriver(page)
    await user_agent(page)
    await webgl_vendor(page)
    await window_outerdimensions(page)
    await media_codecs(page)
