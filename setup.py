import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pySignatureCR",
    version="1.0.0",
    description="Python Signature for Electronic Invoicing in Costa Rica",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Jason Ulloa",
    author_email="jhulloahernandez@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pySignatureCR"],
    include_package_data=True,
    install_requires=["xmlsig","pytz","xmlsig","lxml","datetime"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)