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
    wp_api      = "https://api.wordpress.org"

    plugins_api = "/plugins/info/1.2/?action=query_plugins"
    plugin_info = "/plugins/info/1.1/?action=plugin_information&request[slug]="
    plugin_dlh  = "/stats/plugin/1.0/downloads.php?slug="

    themes_api  = "/themes/info/1.2/?action=query_themes"
    theme_info  = "/themes/info/1.1/?action=theme_information&request[slug]="
    theme_dlh   = "/stats/themes/1.0/downloads.php?slug="

    def Get(API, Info, Hist, Type):
        print('markan: wordpress: getting total number of pages...')
        req   = requests.get(wp_api + API)
        get   = req.json()
        pages = get['info']['pages']

        data  = {}
        data[Type] = []

        page  = 1
        while page <= pages:
            print('markan: wordpress: getting page', str(page), 'of', str(pages)+ '...')
            r = requests.get(wp_api + API + '&request[page]=' + str(page))
            g = r.json()
            t = g[Type]

            for i in range(len(t)):
                s = t[i]['slug']
                print('markan: wordpress: getting info for', s + '...')
                f = requests.get(wp_api + Info + s)
                d = f.json()

                f = requests.get(wp_api + Hist + s)
                h = f.json()
                d['download_history'] = h
                data[Type].append(d)

            page = page + 1
        return data

    def ToCSV(File, Data):
        CSV = open(File, 'w')
        WRT = csv.writer(CSV)
        print('markan: wordpress: writing to csv ...')
        for i in Data:
            WRT.writerow(i)

    def ToJSON(File, Data):
        f = open(File, 'w')
        for i in Data:
            f.write(i)

    if plugins:
        print('markan: wordpress: getting plugins ...')
        r = Get(plugins_api, plugin_info, plugin_dlh, 'plugins')
        ToJSON('wordpress-plugins.json', json.dumps(r))

    if themes:
        print('markan: wordpress: getting themes ...')
        r = Get(themes_api, theme_info, theme_dlh, 'themes')
        ToJSON('wordpress-themes.json', json.dumps(r))
