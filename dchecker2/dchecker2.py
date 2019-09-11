import click
import configparser


@click.command()
@click.argument("config_file")
def main(config_file):
    """Dchecker2 is a tool to perform data integrity checks on VIVO's Researcher Database."""
    config_file = 'config/' + config_file
    config = configparser.ConfigParser()
    config.read(config_file)
    print(config.sections())
