# pyppeteer-stealth

Transplanted from [puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth), **Not perfect**.

## Install

```
$ pip install pyppeteer_stealth
```

## Usage

```python
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    await stealth(page)  # <-- Here

    await page.goto("https://bot.sannysoft.com/")
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
```

## Args

```python
stealth(
  page: Page,
  run_on_insecure_origins: bool = False,
  languages: [str] = ["en-US", "en"],
  vendor: str = "Google Inc."
  user_agent: str = None,
  language: str = "en-US,en",
  platform: str = "Win32",
  webgl_vendor: str = "Intel Inc.",
  renderer: str = "Intel Iris OpenGL Engine",
)
```

## Test results

### Pyppeteer without stealth

<table class="image">
<tr>
  <td><figure class="image"><a href="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headless_without_stealth.png"><img src="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headless_without_stealth.png"></a><figcaption>headless</figcaption></figure></td>
  <td><figure class="image"><a href="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headful_without_stealth.png"><img src="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headful_without_stealth.png"></a><figcaption>headful</figcaption></figure></td>
</tr>
</table>

### Pyppeteer with stealth

<table class="image">
<tr>
  <td><figure class="image"><a href="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headless_with_stealth.png"><img src="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headless_with_stealth.png"></a><figcaption>headless</figcaption></figure></td>
  <td><figure class="image"><a href="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headful_with_stealth.png"><img src="https://github.com/MeiK2333/pyppeteer_stealth/blob/master/headful_with_stealth.png"></a><figcaption>headful</figcaption></figure></td>
</tr>
</table>
