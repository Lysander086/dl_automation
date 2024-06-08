"""Console script for daily_life."""
import daily_life

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for daily_life."""
    console.print("Replace this message by putting your code into "
               "daily_life.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
