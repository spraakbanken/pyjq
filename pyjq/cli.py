from pathlib import Path
from typing import Optional

import typer


cli = typer.Typer()


@cli.command()
def main(infile: Path, outfile: Optional[Path] = typer.Option(None, '--output', '-o')):
    typer.echo(f'infile: {infile}')
    typer.echo(f'outfile: {outfile}')
