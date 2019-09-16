import os
import click
import configparser
from pathlib import Path
from .ReadConfig import ReadConfig
from .EmailHandler import EmailHandler


@click.command()
@click.argument("config_file")
def main(config_file):
    """Dchecker2 is a tool to perform data integrity checks on VIVO's Researcher Database."""

    config = ReadConfig(config_file)
    email = EmailHandler()
    data_report = "Test"
    email.send(config.from_address, config.to_address, config.subject, data_report)
