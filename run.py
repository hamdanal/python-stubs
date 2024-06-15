#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from subprocess import list2cmdline as l2c

from rich.markdown import Markdown
from rich_argparse import RawDescriptionRichHelpFormatter

default_args = {
    "ruff-check": ["tests", "stubs"],
    "ruff-format": ["tests", "stubs"],
    "mypy": ["tests", "stubs"],
    "pyright": ["tests", "stubs"],
    "stubtest": ["--allowlist=stubtest_allowlist.txt", "geopandas"],
    "pytest": [],
}

_newl = "\n"
description = f"""\
Run project development tools with proper environment setup.

The following commands are available:

Command | Default invocation |
------- | ------------------ |
{_newl.join(f"{tool} | {l2c((*tool.split('-'), *default))}" for tool, default in default_args.items())}

You can override the default invocation by passing extra args after the command:

E.g: `python run.py mypy tests` invokes `mypy tests` instead.

Run `python -m pip install -r requirements-tests.txt` to install dependencies.
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description=Markdown(description),  # pyright: ignore[reportArgumentType]
        formatter_class=RawDescriptionRichHelpFormatter,
        add_help=False,
    )
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
        print("Running:", l2c(cmd), file=sys.stderr)
        ret |= subprocess.call(cmd, env={**os.environ, "PYTHONPATH": "stubs"}, text=True)
        print(file=sys.stderr)
    return ret


if __name__ == "__main__":
    sys.exit(main())
