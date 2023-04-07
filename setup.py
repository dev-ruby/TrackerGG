import setuptools

with open("README.md", "r") as fs:
    long_description = fs.read()

setuptools.setup(
    name="TrackerGG",
    version="2.1.3",
    author="DevRuby",
    author_email="hiveruby@gmail.com",
    description="TrackerGG API Wrapper Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-ruby/TrackerGG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["requests", "aiohttp"],
    python_requires=">=3.3",
)
