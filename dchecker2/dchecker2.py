import os
import click
import configparser
from pathlib import Path


@click.command()
@click.argument("config_file")
def main(config_file):
    """Dchecker2 is a tool to perform data integrity checks on VIVO's Researcher Database."""

    # Echoes the text to the terminal using the specified color
    def echo(text, color): return click.echo(click.style(text, color))

    config_file = 'config/' + config_file

    config = configparser.ConfigParser()

    # Attempt to read config file. Show error if invalid file.
    try:
        config.read_file(open(config_file))
    except:
        echo("Configuration file path invalid.", "red")

    config.read(config_file)
    echo(str(config.sections()), "green")
