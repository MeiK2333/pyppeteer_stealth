from pyppeteer.page import Page

from .chrome_app import chrome_app
from .chrome_runtime import chrome_runtime
from .iframe_content_window import iframe_content_window
from .media_codecs import media_codecs
from .sourceurl import sourceurl
from .navigator_hardware_concurrency import navigator_hardware_concurrency
from .navigator_languages import navigator_languages
from .navigator_permissions import navigator_permissions
from .navigator_plugins import navigator_plugins
from .navigator_vendor import navigator_vendor
from .navigator_webdriver import navigator_webdriver
from .user_agent_override import user_agent_override
from .utils import with_utils
from .webgl_vendor import webgl_vendor
from .window_outerdimensions import window_outerdimensions


async def stealth(page: Page, **kwargs) -> None:
    if not isinstance(page, Page):
        raise ValueError("page must be pyppeteer.page.Page")

    await with_utils(page, **kwargs)
    await chrome_app(page, **kwargs)
    await chrome_runtime(page, **kwargs)
    await iframe_content_window(page, **kwargs)
    await media_codecs(page, **kwargs)
    await sourceurl(page, **kwargs)
    await navigator_hardware_concurrency(page, **kwargs)
    await navigator_languages(page, **kwargs)
    await navigator_permissions(page, **kwargs)
    await navigator_plugins(page, **kwargs)
    await navigator_vendor(page, **kwargs)
    await navigator_webdriver(page, **kwargs)
    await user_agent_override(page, **kwargs)
    await webgl_vendor(page, **kwargs)
    await window_outerdimensions(page, **kwargs)
