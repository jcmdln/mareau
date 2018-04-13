from __future__   import print_function
from markan.utils import (ToCSV, ToJSON)
from threading    import Thread
import click
import json
import requests

@click.command(short_help = 'Pull data from WordPress.org')
@click.option('--plugins', '-p', help='Get list of all plugins',
              is_flag=True, default=False)
@click.option('--themes',  '-t', help='Get list of all themes',
              is_flag=True, default=False)

def wordpress(plugins, themes):
    wp_api = "https://api.wordpress.org"
    if plugins:
        api  = "/plugins/info/1.2/?action=query_plugins"
        info = "/plugins/info/1.1/?action=plugin_information&request[slug]="
        hist = "/stats/plugin/1.0/downloads.php?slug="
        targ = 'plugins'
    if themes:
        api  = "/themes/info/1.2/?action=query_themes"
        info = "/themes/info/1.1/?action=theme_information&request[slug]="
        hist = "/stats/themes/1.0/downloads.php?slug="
        targ = 'themes'

    data = []

    def Get(API, Info, Hist):
        page = 1
        while wp_api:
            print('markan: wordpress: getting page', str(page) + '...')
            r = requests.get(wp_api + API + '&request[page]=' + str(page))
            g = r.json()

            def Getter(i):
                s = g[targ][i]['slug']
                print('markan: wordpress: getting info for', s + '...')
                f = requests.get(wp_api + Info + s)
                d = f.json()
                f = requests.get(wp_api + Hist + s)
                h = f.json()
                d['download_history'] = h
                data.append(d)

            queue = []
            if plugins:
                for i in g[targ]:
                    thread = Thread(target=Getter, args=(i,))
                    queue.append(thread)
                    thread.start()
            if themes:
                for i in range(len(g[targ])):
                    thread = Thread(target=Getter, args=(i,))
                    queue.append(thread)
                    thread.start()
            for q in queue:
                q.join()
            if g['info']['pages'] == page:
                return
            else:
                page = page + 1

    if plugins:
        print('markan: wordpress: getting plugins ...')
        r = Get(api, info, hist)
        ToJSON('wordpress-plugins.json', json.dumps(data))
    if themes:
        print('markan: wordpress: getting themes ...')
        r = Get(api, info, hist)
        ToJSON('wordpress-themes.json', json.dumps(data))
