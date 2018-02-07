''' WordPress
* https://codex.wordpress.org/WordPress.org_API

1) Get a json list of all themes/plugins:
* http://api.wordpress.org/themes/info/1.1/?action=query_themes&request[per_page]=9999999
* http://api.wordpress.org/plugins/info/1.1/?action=query_plugins&request[per_page]=9999999

2) For each item in the list, grab the release information
* https://api.wordpress.org/themes/info/1.1/?action=query_themes&request[theme]=twentyseventeen
* https://api.wordpress.org/plugins/info/1.0/boldgrid-easy-seo.json

3) For each item, grab the available historical download statistics
* https://api.wordpress.org/themes/info/1.1/?action=query_themes&request[theme]=twentyseventeen
* https://api.wordpress.org/stats/plugin/1.0/downloads.php?slug=akismet
'''

from __future__ import print_function
import click

import httplib2 # http://httplib2.readthedocs.io/en/latest/
import json     # https://docs.python.org/3/library/json.html
import sqlite3  # https://docs.python.org/3/library/sqlite3.html


@click.command(short_help='Pull data from WordPress.org')


#
def wordpress():
    mdb = sqlite3.connect(":memory:")   # In-memory intermediary database
    pdb = sqlite3.connect('plugins.db') # Plugin database
    tdb = sqlite3.connect('themes.db')  # Themes database
