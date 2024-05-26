#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import subprocess
import sys

try:
    from rich.text import Text  # pyright: ignore[reportAssignmentType]
    from rich_argparse import RawDescriptionRichHelpFormatter as RawDescriptionHelpFormatter
except ModuleNotFoundError:
    RawDescriptionHelpFormatter = argparse.RawDescriptionHelpFormatter

    class Text(str): ...


default_args = {
    "ruff-check": ["tests", "stubs"],
    "ruff-format": ["tests", "stubs"],
    "mypy": ["tests", "stubs"],
    "pyright": ["tests", "stubs"],
    "stubtest": ["--allowlist=stubtest_allowlist.txt", "geopandas"],
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
    parser = argparse.ArgumentParser(description=Text(description), formatter_class=RawDescriptionHelpFormatter, add_help=False)
    parser.add_argument(
        "tool",
        nargs="?",
        metavar="command",
        choices=default_args,
        help="A command from (%(choices)s) to run, optionally with args. See the table above for more information.",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message and exit. Use `--help CMD` to print the help of a command `CMD`.",
    )
    parser.add_argument("--all", action="store_true", help="Run all the commands in the table above.")

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
        parser.error(f"missing command from ({', '.join(default_args)}) or `--all`")

    ret = 0
    for tool in tools:
        cmd = [*tool.split("-"), *(rest or default_args[tool])]
        print("Running:", subprocess.list2cmdline(cmd), file=sys.stderr)
        ret |= subprocess.call(cmd, env={**os.environ, "PYTHONPATH": "stubs"}, text=True)
        print(file=sys.stderr)
    return ret


if __name__ == "__main__":
    sys.exit(main())
