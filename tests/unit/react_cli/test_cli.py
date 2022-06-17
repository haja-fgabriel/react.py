import os.path
from unittest.mock import Mock, create_autospec, call

import livereload
import pytest

from react_cli import ROOT_PATH
from react_cli import start_dev, build_app, _create_build_folder, _start_livereload_server


@pytest.fixture
def mock_build_app(monkeypatch):
    mock = Mock()
    monkeypatch.setattr("react_cli.build_app", mock)
    return mock


@pytest.fixture
def mock__start_livereload_server(monkeypatch):
    mock = Mock()
    monkeypatch.setattr("react_cli._start_livereload_server", mock)
    return mock


@pytest.fixture
def mock__create_build_folder(monkeypatch):
    mock = Mock()
    monkeypatch.setattr("react_cli._create_build_folder", mock)
    return mock


@pytest.fixture
def mock_os_makedirs(monkeypatch):
    mock = Mock()
    monkeypatch.setattr("os.makedirs", mock)
    return mock


@pytest.fixture
def mock__build_html(monkeypatch):
    mock = Mock()
    monkeypatch.setattr("react_cli._build_html", mock)
    return mock


@pytest.fixture
def mock_livereload_server(monkeypatch):
    mock = Mock(spec=livereload.Server)
    mock_instance = mock()
    mock_instance.watch = Mock()
    mock_instance.serve = Mock()
    monkeypatch.setattr("react_cli.Server", mock)
    return mock


@pytest.fixture
def mock__copy_python_assets(monkeypatch):
    mock = Mock()
    monkeypatch.setattr("react_cli._copy_python_assets", mock)
    return mock


def test_start_dev_mode(mock_build_app, mock__start_livereload_server):
    start_dev()
    mock__start_livereload_server.assert_called_once()
    mock_build_app.assert_called_once()


def test_build_app(mock__create_build_folder, mock__build_html, mock__copy_python_assets):
    build_app()
    mock__create_build_folder.assert_called_once()
    mock__build_html.assert_called_once()
    mock__copy_python_assets.assert_called_once()


def test__create_build_folder(mock_os_makedirs):
    _create_build_folder()
    mock_os_makedirs.assert_called_with(os.path.join(ROOT_PATH, "build"), exist_ok=True)


def test__start_livereload_server(mock_build_app, mock_livereload_server):
    _start_livereload_server()
    mock_livereload_server.assert_called()
    mock_instance = mock_livereload_server()
    mock_instance.watch.has_calls(
        [
            call(os.path.join("ROOT_PATH", "public", "*"), mock_build_app),
            call(os.path.join("ROOT_PATH", "src", "*"), mock_build_app),
        ]
    )
    mock_instance.serve.assert_called_with(port=5500, root=os.path.join(ROOT_PATH, "build"), debug=True)
