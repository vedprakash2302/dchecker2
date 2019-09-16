import os
import click
import configparser
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
        echo(str(config.sections()), "green")
