from distutils.core import setup, Extension
from Cython.Build import cythonize


ext_modules = cythonize(
    [
        Extension("usfm_tools.transform", ["usfm_tools/transform.py"]),
        Extension(
            "usfm_tools.support.singlehtmlRenderer",
            ["usfm_tools/support/singlehtmlRenderer.py"],
        ),
        Extension("usfm_tools.support.parseUsfm", ["usfm_tools/support/parseUsfm.py"]),
        Extension("usfm_tools.support.books", ["usfm_tools/support/books.py"]),
        Extension(
            "usfm_tools.support.exceptions", ["usfm_tools/support/exceptions.py"]
        ),
    ],
    language_level="3",
)

setup(
    name="usfm_tools",
    version="0.0.31",
    author="unfoldingWord",
    author_email="info@unfoldingWord.org",
    description="A framework for transforming .usfm files into specified targets",
    license="MIT",
    keywords="unfoldingWord usfm tools",
    url="https://github.com/linearcombination/USFM-Tools",
    packages=["usfm_tools", "usfm_tools/support"],
    package_data={"usfm_tools": ["py.typed"], "usfm_tools/support": ["py.typed"]},
    long_description="This project comprises a framework for transforming .usfm files into specified targets. It is "
    "primarily used for the Open English Bible, and may need adjustment if used for other purposes. ",
    classifiers=[],
    install_requires=["future", "pyparsing"],
    ext_modules=ext_modules,
)
