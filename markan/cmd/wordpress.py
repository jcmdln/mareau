from __future__ import print_function

import csv
import json
import click
import requests

@click.command(short_help = 'Pull data from WordPress.org')
@click.option('--plugins', '-p', help = 'Get list of all plugins',
              default = '')
@click.option('--themes',  '-t', help = 'Get list of all themes',
              default = '')

def wordpress():
    # API endpoints
    PLUGINS = 'https://api.wordpress.org/plugins/info/1.2/'
    THEMES  = 'https://api.wordpress.org/themes/info/1.2/'

    # Provide JSON results
    def results(api, action):
        req   = requests.get(api, action)
        page  = 0
        total = req['info']['results']
        pages = req['info']['pages']
        items = total / pages

        while page <= pages:
            print('markan: wordpress: getting page', page, 'of', pages, '...')
            req = requests.get(
                api, action,
                '&request[per_page]=' + str(items)
                + '&request[page]='   + str(page)
            )
            page += 1

        return req.json()

    # Themes
    req    = results(THEMES, 'query_plugins')
    plugin = req['plugins']

    for i in plugin:
        print('')

    psort = sorted(plugin)

    # Plugins
    req   = results(THEMES, 'query_themes')
    theme = req['themes']

    for i in themes:
        print('')

    tsort = sorted(theme)
