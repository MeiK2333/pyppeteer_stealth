from pyppeteer.page import Page


# https://github.com/berstend/puppeteer-extra/blob/9eacda61fc34f7994a0aa253097c473c19c0d1bf/packages/puppeteer-extra-plugin-stealth/evasions/sourceurl/index.js
async def sourceurl(page: Page, **kwargs) -> None:
    if (not page or not page._client or not page._client.send):
        return
    
    def new_send(method, params = None):
        if not method or not params:
            return page._client.old_send(method, params)

        methodsToPatch = {
            'Runtime.evaluate': 'expression',
            'Runtime.callFunctionOn': 'functionDeclaration'
        }
        SOURCE_URL_SUFFIX = '//# sourceURL=__pyppeteer_evaluation_script__'
        if method in methodsToPatch:
            params[methodsToPatch[method]] = params[methodsToPatch[method]].replace(SOURCE_URL_SUFFIX, '')
        return page._client.old_send(method, params)
            
    page._client.old_send = page._client.send
    page._client.send = new_send
