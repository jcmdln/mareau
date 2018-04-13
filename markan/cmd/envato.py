from __future__   import print_function
from markan.utils import (ToCSV, ToJSON)
from threading    import Thread
import click
import json
import requests

@click.command(short_help = 'Pull data from the Envato API')
@click.option('--category', '-c', help='Category',   default='wordpress')
@click.option('--domain',   '-d', help='Domain',     default='themeforest.net')
@click.option('--token',    '-t', help='Auth token', default='')

def envato(category, domain, token):
    page = 60
    url  = 'https://api.envato.com/v1/discovery/search/search/item'
    opts = '?page=' + str(page) + '&site=' + domain + '&category=' + category
    data = []
    while url:
        print('markan: envato: getting page', str(page) + '...')
        r = requests.get(url + opts, headers = {
            'Content-Type'  : 'application/json',
            'Authorization' : 'Bearer ' + token
        })
        s = r.json()
        data.append(s)
        if s['links']['next_page_url'] is None:
            ToJSON('themeforest-'+category+'.json', json.dumps(data))
            return
        else:
            page = page + 1
