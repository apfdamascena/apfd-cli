import click
import os

@click.command()
def cli():
    os.system("g++-9 -std=c++17 main.cpp -o main && time ./main < input.txt")