# -*- coding: utf-8 -*-

"""Console script for pygesasso."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for pygesasso."""
    click.echo("Replace this message by putting your code into "
               "pygesasso.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
