from argparse import ArgumentParser

from . import start_dev, build_app

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="react_cli",
        description="A command-line interface used for developing React-like web applications using Python and PyScript",
    )
    parser.add_argument("command", choices=["dev", "build"])

    args = parser.parse_args()
    if args.command == "dev":
        start_dev()
    elif args.command == "build":
        build_app()
