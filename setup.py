from setuptools import setup, find_packages

setup(
    name="react.py",
    version="0.0.1",
    description="It's React, but in Python",
    author="Haja Florin-Gabriel",
    author_email="haja.fgabriel@gmail.com",
    package_dir={"": "react.py/"},
    packages=find_packages("react.py/"),
)
