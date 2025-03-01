import setuptools

from mathtranslate import __version__, __author__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="mathtranslate",
    version=__version__,
    author=__author__,
    author_email="susyustc@gmail.com",
    description="Translate math-heavy papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SUSYUSTC/MathTranslate",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["mtranslate==1.8.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    scripts=['mathtranslate/translate_tex.py'],
)
