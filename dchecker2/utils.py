import click


# Echoes the text to the terminal using the specified color
def echo(data, color):
    if isinstance(data, list):
        data = "\n".join(data)
    if isinstance(data, str):
        data = data
    click.echo(click.style(data, color))


def sparql_variable_rename(var_name):
    """Rename the variables in a SPARQL query to be human-readable.
    Keyword argument:
    var_name -- the variable's name
    """
    var_name = var_name.replace('_', ' ')
    return var_name
