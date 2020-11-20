import click
import os

@click.command()
def cli():
    os.system("/Library/PostgreSQL/13/scripts/runpsql.sh")