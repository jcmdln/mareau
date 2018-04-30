from __future__   import print_function
from markan.utils import (ToCSV, ToJSON)
from threading    import Thread
import click
import json as j
import requests

@click.command(short_help = 'Pull data from the Envato API')
@click.option('--category', '-c', help='Category',
              default='wordpress/corporate')
@click.option('--domain', '-d', help='Domain', default='themeforest.net')
@click.option('--token', '-t', help='Auth token', default='')
@click.option('--csv', '-c', help='Export as CSV', is_flag=True, default=False)
@click.option('--json', '-j', help='Export as JSON', is_flag=True,
              default=False)

def envato(category, domain, token, csv, json):
    if token == '':
        print('markan: envato: no token? NO DATA!')
        return

    data  = []
    page  = 1
    pages = 2

    while page <= pages:
        print('markan: envato: getting page', str(page),
              'of', domain, category, '...')
        r = requests.get(
            'https://api.envato.com/v1/discovery/search/search/item'
            + '?page='+str(page) + '&site='+domain + '&category='+category
            + '&page_size=100', headers = {
            'Content-Type'  : 'application/json',
            'Authorization' : 'Bearer ' + token
        })
        s = r.json()
        pages = s['links']['last_page_url'].split('&')
        pages = pages[1].split('=')
        pages = int(pages[1])

        for i in ['matches']:
            d = {}
            d['site']           = s['matches'][i]['site']
            d['id']             = s['matches'][i]['id']
            d['url']            = s['matches'][i]['url']
            d['name']           = s['matches'][i]['name']
            #d['description']    = s['matches'][i]['description']
            d['summary']        = s['matches'][i]['summary']
            d['tags']           = s['matches'][i]['tags']
            d['classification'] = s['matches'][i]['classification']
            d['price_cents']    = s['matches'][i]['price_cents']
            d['total_sales']    = s['matches'][i]['number_of_sales']
            d['author']         = s['matches'][i]['author_username']
            d['rating']         = s['matches'][i]['rating']['rating']
            d['total_ratings']  = s['matches'][i]['rating']['count']
            d['updated']        = s['matches'][i]['updated_at']
            d['published']      = s['matches'][i]['published_at']
            d['trending']       = s['matches'][i]['trending']
            data.append(d)

        page = page + 1


    if "/" in category:
        category = category.split('/')
        category = category[-1]
    if json:
        ToJSON('envato-'+domain+'-'+category+'.json', j.dumps(data))
    if csv:
        ToCSV('envato-'+domain+'-'+category+'.csv', data)
