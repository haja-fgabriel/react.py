import os
import shutil

from react_cli import ROOT_PATH
from react_cli import _build_html, build_app, _copy_python_assets


def test_build_app():
    build_app()
    _assert_is_not_template()


def test_build_html():
    _build_html()
    _assert_is_not_template()


def _assert_is_not_template():
    with open(os.path.join(ROOT_PATH, "build", "index.html"), "r") as f:
        content = f.read()
        assert "{{" not in content
        assert "}}" not in content
        assert "{%" not in content
        assert "%}" not in content


def test__copy_python_assets():
    _copy_python_assets()

    src_files = []
    for root, dirs, files in os.walk(os.path.join(ROOT_PATH, "src")):
        src_files += list(files)

    for root, dirs, files in os.walk(os.path.join(ROOT_PATH, "build")):
        for file in src_files:
            assert file in files
