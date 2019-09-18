import os
import click
import logging
import configparser
from pathlib import Path
from .utils import echo
from .ReadConfig import ReadConfig
from .EmailHandler import EmailHandler
from .QueryHandler import QueryHandler


@click.command()
@click.argument("config_file")
def main(config_file):
    """Dchecker2 is a tool to perform data integrity checks on VIVO's Researcher Database."""

    # setup logging
    logging.basicConfig(filename='dchecker.log', level=logging.INFO, format='%(asctime)s %(message)s')

    config = ReadConfig(config_file)
    email = EmailHandler()
    query_handler = QueryHandler()

    echo("Starting dchecker2", "green")
    logging.info("starting dchecker.py")
    data_report = query_handler.query_iterator(config.sparql_endpoint, config.query_directory)

    logging.info("sending report")
    email.send(config.from_address, config.to_address, config.subject, data_report)

    logging.info("ending dchecker.py.")
