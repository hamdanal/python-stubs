#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from subprocess import list2cmdline as l2c

from rich.markdown import Markdown
from rich_argparse import RawTextRichHelpFormatter

default_args = {
    "ruff-check": ["tests", "stubs"],
    "ruff-format": ["tests", "stubs"],
    "mypy": ["tests", "stubs"],
    "pyright": ["tests", "stubs"],
    "stubtest": ["--allowlist=stubtest_allowlist.txt", "pandapower"],
    "pytest": [],
}

_newl = "\n"
description = f"""\
Run project development tools with proper environment setup.

The following commands are available:

Command | Default invocation |
------- | ------------------ |
{_newl.join(f"{tool} | {l2c((*tool.split('-'), *default))}" for tool, default in default_args.items())}

You can override the default invocation by passing extra args after the command.
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description=Markdown(description),  # pyright: ignore[reportArgumentType]
        epilog="Run [argparse.args]python -m pip install -r requirements.txt[/] to install project dependencies.",
        formatter_class=RawTextRichHelpFormatter,
        add_help=False,
    )
    parser.add_argument(
        "tool",
        nargs="?",
        metavar="command",
        choices=default_args,
        help="A command from (%(choices)s)\nto run, optionally with args.\n\nSee the table above for more information.\n\n",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message and exit.\nUse --help [i]CMD[/] to print the help of command [i]CMD[/].\n\n",
    )
    parser.add_argument("--all", action="store_true", help="Run all commands in the table above.")

    args, rest = parser.parse_known_args()
    tool: str | None = args.tool

    if args.help:
        parser.print_help(file=sys.stderr)
        if tool:
            print("\n" + "━" * 80 + "\n", file=sys.stderr)
            return subprocess.call([*tool.split("-"), "--help"])
        parser.exit(0)

    if args.all:
        tools = list(default_args)
    elif tool:
        tools = [tool]
    else:
        parser.print_usage(file=sys.stderr)
        formatter = parser.formatter_class(prog=parser.prog)
        formatter.add_text(
            f"\n[argparse.prog]{parser.prog}[/]: [red]error:[/] missing command from "
            f"({', '.join(f'[argparse.args]{a}[/]' for a in default_args)}) "
            f"or [argparse.args]--all[/]"
        )
        parser.exit(2, formatter.format_help())

    ret = 0
    for tool in tools:
        cmd = [*tool.split("-"), *(rest or default_args[tool])]
        print("Running:", l2c(cmd), file=sys.stderr)
        ret |= subprocess.call(cmd, env={**os.environ, "PYTHONPATH": "stubs"}, text=True)
        print(file=sys.stderr)
    return ret


if __name__ == "__main__":
    sys.exit(main())
