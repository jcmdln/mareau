import click
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


@click.command(short_help='Interact with Google Sheets')
@click.option('--auth',  help='File containing Oauth2 ClientID')
@click.option('--data',  help='File containing data to parse')
@click.option('--sheet', help='Hash key of target Google Sheet')


def sheets(auth, data, sheet):
    """ """
