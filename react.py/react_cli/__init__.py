import os
import os.path
import shutil

from livereload import Server


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def build_app():
    _create_build_folder()
    _build_html()
    _copy_python_assets()


def _create_build_folder(build_folder="build"):
    os.makedirs(os.path.join(ROOT_PATH, build_folder), exist_ok=True)


def _build_html():
    """
    Searches through all user-developed modules and compiles the HTML templates, listing the custom modules
    """
    _create_build_folder()
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT_PATH, "public")))
    html_template = env.get_template("index.html.jinja")
    value = html_template.render()
    with open(os.path.join(ROOT_PATH, "build", "index.html"), "w") as g:
        g.write(value)


def _copy_python_assets():
    shutil.copytree(os.path.join(ROOT_PATH, "src"), os.path.join(ROOT_PATH, "build"), dirs_exist_ok=True)


def _start_livereload_server(port=5500):
    """
    Starts the LiveReload server
    """

    server = Server()

    public_folder = os.path.join(ROOT_PATH, "public", "*")
    src_folder = os.path.join(ROOT_PATH, "src", "*")
    build_folder = os.path.join(ROOT_PATH, "build")

    server.watch(public_folder, build_app)
    server.watch(src_folder, build_app)

    server.serve(port=port, root=build_folder, debug=True, open_url_delay=4)


def start_dev():
    """
    Starts the web application with a development server: any saved changes are going to reload the server.
    """
    build_app()
    _start_livereload_server()
    pass
