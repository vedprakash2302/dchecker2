import os
import click
import configparser
from datetime import datetime
from .utils import echo


class ReadConfig:

    def __init__(self, config_file):
        config_file = 'config/' + config_file

        config = configparser.ConfigParser()

        # Attempt to read config file. Show error if invalid file.
        try:
            config.read_file(open(config_file))
        except:
            echo("Configuration file path invalid.", "red")

        config.read(config_file)
        self.read_arguments_from_config(config)

    def read_arguments_from_config(self, config):
        # Read email info
        self.from_address = config.get('Email', 'from_address')
        self.to_address = config.get('Email', 'to_address')
        try:
            self.subject = config.get('Email', 'subject')
        except configparser.NoOptionError:
            self.subject = "VIVO Data Quality report for"
        self.subject = self.subject + " " + str(datetime.now())

        # Read SPARQL endpoint
        self.sparql_endpoint = config.get('SPARQL', 'endpoint')

        # Read the directory which contains query files
        try:
            self.query_directory = config.get('Queries', 'folder')
        except (configparser.NoSectionError, configparser.NoOptionError):
            # portable for *NIX/Windows
            if os.name == "nt":
                self.query_directory = os.getcwd() + "\\queries\\"
            elif os.name == "posix":
                self.query_directory = os.getcwd() + "/queries/"
