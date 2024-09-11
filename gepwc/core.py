import sys
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('file_txt', type=str, nargs=-1)
def gepcat(file_txt):
    click.echo(file_txt[0])