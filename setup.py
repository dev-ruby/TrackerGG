import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TrackerGG",  # Replace with your own username
    version="1.0.0",
    author="DevRuby",
    author_email="devruby7777@gmail.com",
    description="Game Stat Library with Tracker API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-ruby/TrackerGG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.3",
)
