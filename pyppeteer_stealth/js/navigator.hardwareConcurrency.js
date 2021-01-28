// https://github.com/berstend/puppeteer-extra/blob/3ea4ebca4237bb45ce402ba6a44d852e3499cb5f/packages/puppeteer-extra-plugin-stealth/evasions/navigator.hardwareConcurrency/index.js

(hardwareConcurrency) => {
    utils.replaceGetterWithProxy(
        Object.getPrototypeOf(navigator),
        'hardwareConcurrency',
        utils.makeHandler().getterValue(hardwareConcurrency)
      )
}
    