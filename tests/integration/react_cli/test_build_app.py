import os
import shutil
import sys

from react_cli import ROOT_PATH
from react_cli import _build_html, build_app, _copy_python_assets, _resolve_imports


def test_build_app():
    build_app()
    _assert_is_not_template()


def test_build_html():
    _build_html()
    _assert_is_not_template()
    _assert_has_files_in_py_env()


def _assert_is_not_template():
    with open(os.path.join(ROOT_PATH, "build", "index.html"), "r") as f:
        content = f.read()
        assert "{{" not in content
        assert "}}" not in content
        assert "{%" not in content
        assert "%}" not in content


def _assert_has_files_in_py_env():
    src_path = os.path.join(ROOT_PATH, "src")
    with open(os.path.join(ROOT_PATH, "build", "index.html"), "r") as f:
        html_content = f.read()
        for root, dirs, files in os.walk(src_path):
            for file in files:
                if ".py" in file[-3:]:
                    src_relpath = os.path.join(os.path.relpath(root, start=src_path), file)
                    assert src_relpath in html_content


def test__copy_python_assets():
    _copy_python_assets()

    src_files = []
    for root, dirs, files in os.walk(os.path.join(ROOT_PATH, "src")):
        src_files += list(files)

    build_files = []
    for root, dirs, files in os.walk(os.path.join(ROOT_PATH, "build")):
        build_files += files

    for file in src_files:
        assert file in build_files


def test__resolve_imports():
    imports = _resolve_imports()
    assert len(imports) > 0
    assert all(".py" in path[-3:] for path in imports)
    assert all(os.path.exists(os.path.join(ROOT_PATH, "src", path)) for path in imports)
    pass
