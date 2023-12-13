#!/usr/bin/python3

import typer
from typing_extensions import Annotated

from rich import print
from rich.panel import Panel
from rich.table import Table

import os
import importlib.metadata


app = typer.Typer()


@app.command()
def about():
    """
    Returns information about this application.
    """
    metadata = importlib.metadata.metadata("python-app-template")
    table = Table(show_header=False, box=None, style="white")
    table.add_column("")
    table.add_column("")
    table.add_row("Name", metadata["Name"], style="white")
    table.add_row("Summary", metadata["Summary"], style="white")
    table.add_row("Author", metadata["Author"], style="white")
    table.add_row("Version", metadata["Version"], style="white")

    print(Panel.fit(table, title="[bold] About [/bold]", style="cyan"))


@app.command()
def print_content(file: Annotated[str, typer.Option(help="File to be printed")]):
    """
    Prints the content of the given file.
    """
    if not os.path.exists(file):
        print("[bold red]:boom: Invalid file ({})".format(file))
        raise typer.Abort()

    with open(file, "r") as f:
        print(f.read())
