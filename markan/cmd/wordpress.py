from __future__ import print_function

import csv
import click
import json
import requests

@click.command(short_help = 'Pull data from WordPress.org')
@click.option('--plugins', '-p', help='Get list of all plugins',
              is_flag=True, default=False)
@click.option('--themes',  '-t', help='Get list of all themes',
              is_flag=True, default=False)

def wordpress(plugins, themes):
    def ToCSV(File, Head, Data):
        "Write data to a CSV."
        CSV  = open(File, 'w')
        WRT  = csv.writer(CSV)
        print('markan: wordpress: writing to csv ...')
        WRT.writerow(Head)
        for i in Data:
            WRT.writerow(i)

    if plugins:
        print('markan: wordpress: getting plugins ...')
        req = requests.get(
            'https://api.wordpress.org/plugins/info/1.2/'
            +'?action=query_plugins'
        )
        res  = req.json()
        data = res['plugins']

        ToCSV(
            'plugins.csv',
            ['name', 'slug', 'version', 'author', 'downloaded',
             'rating', 'total ratings','homepage'],
            data
        )

    if themes:
        print('markan: wordpress: getting themes ...')
        req = requests.get(
            'https://api.wordpress.org/themes/info/1.2/'
            +'?action=query_themes&request[per_page]=-1'
        )
        res  = req.json()
        data = res['themes']

        ToCSV(
            'themes.csv',
            ['name', 'slug', 'version', 'author', 'rating',
             'total ratings','homepage'],
            data
        )
