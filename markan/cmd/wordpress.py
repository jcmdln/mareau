from __future__ import print_function
import csv
import json
import click
import requests

@click.command(short_help='Pull data from WordPress.org')

def wordpress():
    wp_api  = 'https://api.wordpress.org/'

    def Results(Type, Action):
        print('markan: wordpress: Getting total number of', Type+'...')
        r = requests.get(
            wp_api + Type + '/info/1.2/'
            + '?action=' + Action
            + '&request[per_page]=250'
        )
        results = r.json()
        total   = results['info']['results']
        pages   = results['info']['pages']
        ipp     = total / pages
        print('markan: wordpress: Getting list of', total, Type+'...')
        req = []
        page = 1
        while page <= pages:
            print('markan: wordpress: Getting page', str(page), 'of', str(pages)+'...')
            r = requests.get(
                wp_api + Type + '/info/1.2/'
                + '?action=' + Action
                + '&request[per_page]=' + str(ipp)
                + '&request[page]=' + str(page)
            )
            req.append(r.json())
            page = int(page) + 1
        return total, pages, req

    print('markan: wordpress: Building and sorting list of themes...')
    themes_res   = Results('themes', 'query_themes')
    themes_stage = themes_res[-1]
    themes_total = int(themes_res[0])
    themes       = themes_stage[0]['themes']
    themes_list  = []

    for i in range(len(themes)):
        themes_list.append([
            themes[i]['name'],
            themes[i]['slug'],
            themes[i]['version'],
            themes[i]['author']['user_nicename'],
            themes[i]['rating'],
            themes[i]['num_ratings'],
            themes[i]['homepage']
        ])
    themes_sorted = sorted(themes_list)

    print('markan: wordpress: Writing themes to wordpress-themes.csv...')
    theme_csv  = open('wordpress-themes.csv', 'w')
    theme_wr   = csv.writer(theme_csv)
    theme_head = ['name', 'slug', 'version', 'author', 'rating',
                  'total ratings','homepage']
    theme_wr.writerow(theme_head)
    for i in themes_sorted:
        theme_wr.writerow(i)

    # print('markan: wordpress: Building and sorting list of plugins...')
    # plugins_dict  = Results('plugins', 'query_plugins')
    # plugins_total = int(plugins_dict[0])
    # plugins       = plugins_dict[-1]['plugins']
    # plugins_list  = []

    # for i in plugins:
    #     plugins_list.append([
    #         plugins[i]['name'],
    #         plugins[i]['slug'],
    #         plugins[i]['version'],
    #         plugins[i]['author'],
    #         plugins[i]['downloaded'],
    #         plugins[i]['rating'],
    #         plugins[i]['num_ratings'],
    #         plugins[i]['homepage']
    #     ])
    # plugins_sorted = sorted(plugins_list)

    # print('markan: wordpress: Writing plugins to wordpress-plugins.csv...')
    # plugins_csv  = open('wordpress-plugins.csv', 'w')
    # plugins_wr   = csv.writer(plugins_csv)
    # plugins_head = ['name', 'slug', 'version', 'author', 'downloaded',
    #                 'rating', 'total ratings', 'homepage']
    # plugins_wr.writerow(plugins_head)
    # for i in plugins_sorted:
    #     plugins_wr.writerow(i)
