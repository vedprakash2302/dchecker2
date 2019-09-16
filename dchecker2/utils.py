import click

# Echoes the text to the terminal using the specified color
def echo(text, color): return click.echo(click.style(text, color))
