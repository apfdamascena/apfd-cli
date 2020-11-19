import click
import os

@click.command()
@click.option('-m',default ='')
def cli(m):
    os.system("git add .")
    os.system(f'git commit -m "{m}"')
    os.system('git push')