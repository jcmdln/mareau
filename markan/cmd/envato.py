from __future__ import print_function
from threading import Thread

import csv
import click
import json
import requests

@click.command(short_help = 'Pull data from the Envato API')
@click.option('--category', '-c', help='Target category',
              default='wordpress')
@click.option('--domain', '-d', help='Target domain',
              default='themeforest.net')
@click.option('--token',  '-t', help='Authentication token',
              default='')

def envato(category, domain, token):
    API = 'https://api.envato.com/v1/discovery/search/search/item'

    if token == '':
        print('markan: envato: No token? NO DATA! Exiting...')
        return

    def ToJSON(File, Data):
        f = open(File, 'w')
        print('markan: envato: writing json to file...')
        for i in Data:
            f.write(i)

    r = requests.get(
        API + '?site=' + domain + '&category=' + category,
        headers = {
            'Content-Type'  : 'application/json',
            'Authorization' : 'Bearer ' + token
        }
    )
    d = r.json()
    l = d['links']['last_page_url'].split('&')
    l = l[1].split('=')
    l = int(l[1])

    s = []

    p = 1
    while p <= l:
        print('markan: envato: getting page', p, 'of', str(l) + '...')
        r = requests.get(
            API + '?page=' + str(p) + '&site=' + domain + '&category=' + category,
            headers = {
                'Content-Type'  : 'application/json',
                'Authorization' : 'Bearer ' + token
            }
        )
        d = r.json()
        s.append(d)
        p += 1

    ToJSON('themeforest-'+category+'.json', json.dumps(s))
