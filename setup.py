from setuptools import setup, find_packages

setup(
    name="jspaste",
    version="0.1",
    packages=find_packages(),
    description="JSPaste Python API Wrapper. WIP.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="tnfAngel",
    author_email="git@tnfangel.com",
    url="https://github.com/tnfAngel/jspaste-py",
    license="EUPL",
    classifiers=[
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
    install_requires=[
        "aiohttp>=3.9.0",
        "aiodns>=3.2.0",
    ],
)
