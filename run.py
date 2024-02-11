#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import subprocess
import sys

default_args = {
    "mypy": ["tests", "stubs/shapely-stubs", "stubs/geopandas-stubs"],
    "pyright": ["tests", "stubs/shapely-stubs", "stubs/geopandas-stubs"],
    "stubtest": ["--allowlist=stubtest_allowlist.txt", "shapely", "geopandas"],
    "ruff-check": ["tests", "stubs"],
    "ruff-format": ["tests", "stubs"],
    "pytest": [],
}

description = """\
Run project development tools with proper environment setup.

The following commands are available:
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Command     ┃ Default invocation                                             ┃
"""
for tool, default in default_args.items():
    description += "┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\n"
    description += f"┃ {tool:<11s} ┃ {subprocess.list2cmdline((*tool.split('-'), *default)):<63s}┃\n"
description += """\
┗━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

You can override the default invocation by passing extra args after the command:
E.g: `python run.py mypy tests` invokes `mypy tests` instead.

Run `python -m pip install -r requirements-tests.txt` to install dependencies.
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [-h] command [args]",
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
    )
    parser.add_argument("tool", nargs="?", metavar="tool", choices=default_args, help=argparse.SUPPRESS)
    options = parser.add_argument_group("Options")
    options.add_argument("-h", "--help", action="store_true", help="show this help message and exit")
    options.add_argument("--all", action="store_true", help="run all checks")

    args, rest = parser.parse_known_args()

    tool: str | None = args.tool

    if args.help:
        help_text = parser.format_help()
        help_text = help_text[0].upper() + help_text[1:]
        print(help_text, end="", file=sys.stderr)
        if tool:
            print("\n" + "━" * 80 + "\n", file=sys.stderr)
            return subprocess.call([*tool.split("-"), "--help"])
        parser.exit(0)

    if args.all:
        tools = list(default_args)
    elif tool:
        tools = [tool]
    else:
        parser.print_usage()
        parser.exit(1)

    ret = 0
    for tool in tools:
        cmd = [*tool.split("-"), *(rest or default_args[tool])]
        print("Running:", subprocess.list2cmdline(cmd), file=sys.stderr)
        ret |= subprocess.call(cmd, env={**os.environ, "PYTHONPATH": "stubs"}, text=True)
        print(file=sys.stderr)
    return ret


if __name__ == "__main__":
    sys.exit(main())
