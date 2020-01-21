from pyppeteer.page import Page


async def webgl_vendor(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    try {
        const getParameter = WebGLRenderingContext.prototype.getParameter
        WebGLRenderingContext.prototype.getParameter = function (parameter) {
          if (parameter === 37445) {
            return 'Intel Inc.'
          }
          if (parameter === 37446) {
            return 'Intel Iris OpenGL Engine'
          }
          return getParameter.apply(this, [parameter])
        }
      } catch (err) {}
}
"""
    )
