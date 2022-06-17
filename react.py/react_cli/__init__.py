from contextlib import contextmanager
import os
import os.path
import shutil
import sys

from livereload import Server


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


PUBLIC_FOLDER = os.path.join(ROOT_PATH, "public")
SRC_FOLDER = os.path.join(ROOT_PATH, "src")
BUILD_FOLDER = os.path.join(ROOT_PATH, "build")


def build_app():
    """
    Compiles the HTML template and copies all assets into the build/ folder.
    """
    _create_build_folder()
    _build_html()
    _copy_python_assets()


def _create_build_folder(build_folder="build"):
    os.makedirs(BUILD_FOLDER, exist_ok=True)


def _build_html():
    """
    Searches through all user-developed modules and compiles the HTML templates, listing the custom modules
    """
    _create_build_folder()
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT_PATH, "public")))
    html_template = env.get_template("index.html.jinja")
    value = html_template.render(imports=_resolve_imports())

    with open(os.path.join(BUILD_FOLDER, "index.html"), "w") as g:
        g.write(value)


def _resolve_imports():
    """
    Walks all subfolders of src/ and returns a list of the existing Python files.
    """
    imports = []
    for root, dirs, files in os.walk(SRC_FOLDER):
        for file in files:
            if ".py" in file[-3:]:
                imports.append(os.path.join(os.path.relpath(root, start=SRC_FOLDER), file))
    return imports


def _copy_python_assets():
    """
    Copies all Python files from src/ to build/
    """
    shutil.copytree(SRC_FOLDER, BUILD_FOLDER, dirs_exist_ok=True)


def _start_livereload_server(port=5500):
    """
    Starts the LiveReload server

    Parameters:
    :port: default 5500 - the port the server will serve the application on.
    """

    server = Server()

    server.watch(PUBLIC_FOLDER, build_app)
    server.watch(SRC_FOLDER, build_app)

    server.serve(port=port, root=BUILD_FOLDER, debug=True, open_url_delay=4)


def start_dev():
    """
    Starts the web application with a development server: any saved changes are going to reload the server.
    """
    build_app()
    _start_livereload_server()
    pass
