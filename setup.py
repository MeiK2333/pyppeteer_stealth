import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyppeteer_stealth",
    version="1.0.2",
    author="MeiK2333",
    author_email="meik2333@gmail.com",
    description="pyppeteer stealth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MeiK2333/pyppeteer-stealth",
    packages=setuptools.find_packages(),
)