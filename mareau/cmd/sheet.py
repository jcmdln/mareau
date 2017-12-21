"""
TODO:
- Allow user to specify their auth file (ie 'client_id.json') and give help URL
  if empty
  - '--auth CLIENT_ID'
- Users should be able to define which spreadsheet they want to use
  - '--sheet SHEET_KEY'
- Need to read existing spreadsheet and intelligently add new data to it
  - Give option to split into date range?
    - Probably easier to split all data into quarterly sections with the first
      page being the complete overview?
"""

import click
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

@click.command(short_help='Interact with Google Sheets')
@click.option('--auth',  help='File containing Oauth2 ClientID')
@click.option('--data',  help='File containing data to parse')
@click.option('--sheet', help='Hash key of target Google Sheet')

def sheet(auth, data, sheet):
    """ """
