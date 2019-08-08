from pyppeteer.page import Page


async def navigator_permissions(page: Page) -> None:
    await page.evaluateOnNewDocument(
        """
() => {
    const originalQuery = window.navigator.permissions.query

    window.navigator.permissions.__proto__.query = parameters =>
        parameters.name === 'notifications'
            ? Promise.resolve({ state: Notification.permission })
            : originalQuery(parameters)


    const oldCall = Function.prototype.call
    function call () {
        return oldCall.apply(this, arguments)
    }

    Function.prototype.call = call

    const nativeToStringFunctionString = Error.toString().replace(
        /Error/g,
        'toString'
    )
    const oldToString = Function.prototype.toString

    function functionToString () {
        if (this === window.navigator.permissions.query) {
            return 'function query() { [native code] }'
        }
        if (this === functionToString) {
            return nativeToStringFunctionString
        }
        return oldCall.call(oldToString, this)
    }

    Function.prototype.toString = functionToString
}
    """
    )
