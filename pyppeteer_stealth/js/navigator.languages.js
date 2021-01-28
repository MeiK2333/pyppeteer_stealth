// https://github.com/berstend/puppeteer-extra/blob/c44c8bb0224c6bba2554017bfb9d7a1d0119f92f/packages/puppeteer-extra-plugin-stealth/evasions/navigator.languages/index.js

(languages) => {
  // Overwrite the `languages` property to use a custom getter.
  const languages_to_pass = languages.length
    ? languages
    : ['en-US', 'en']
  utils.replaceGetterWithProxy(
    Object.getPrototypeOf(navigator),
    'languages',
    utils.makeHandler().getterValue(Object.freeze([...languages_to_pass]))
  )
}
