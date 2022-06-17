# react.py
It's React, but in Python

# Preparing the development environment

1. Create a new virtual environment: `python -m venv env/`
2. Install the dependencies: `pip install -r requirements-dev.txt`
3. Install the library as editable (for development or until it is available on PyPI): `pip install -e .` - searches for setup.py, which is going to install the `react` and `react_cli` packages as editable

# Developing a project

    python -m react_cli dev

It is going to start a live development server, which is going to reload the page automatically when saving

# Building a project

    python -m react_cli build

It is going to deliver the built assets in the build/ folder