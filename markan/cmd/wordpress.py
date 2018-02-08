from __future__ import print_function
import click

import csv
import json
import requests
#import sqlite3


@click.command(short_help='Pull data from WordPress.org')


def wordpress():
    # WordPress API base URL
    wp_api  = 'https://api.wordpress.org/'

    # Should it be desired to run a server that automatically queries
    # the WordPress API on some interval, storing the information in a
    # database will be needed. I would like to have some method of
    # performing thread safe asynchronous writes to the in-memory
    # database that are queued until the target sqlite database becomes
    # available for writes.

    #mem = sqlite3.connect(':memory:')
    #sdb = sqlite3.connect('markan.db')


    # This section performs a test query of a single item to get the
    # total number of WordPress items such as themes or plugins. The
    # total number of results is retrieved from the built dictionary and
    # converted into a string to be concatenated to the request URL in
    # the next section.

    def Results(Type, Action):
        print('markan: wordpress: Getting total number of', Type+'...')
        r = requests.get(
            wp_api + Type + '/info/1.2/'
            + '?action=' + Action
            + '&request[per_page]=1'
        )
        results = r.json()
        total   = str(results['info']['results'])
        print('markan: wordpress: Getting list of', total, Type+'...')
        r = requests.get(
            wp_api + Type + '/info/1.2/'
            + '?action=' + Action
            + '&request[per_page]=' + total
        )
        return total, r.json()


    # This section defines the information we want to retrieve with
    # Results(), such as themes and plugins. We will create a dictionary
    # of the returned data from Results() and assign a key that will be
    # our reference to the actual list of data.

    print('markan: wordpress: Parsing results for themes...')
    themes_dict   = Results('themes', 'query_themes')
    themes_total  = int(themes_dict[0])
    themes        = themes_dict[1]['themes']

    print('markan: wordpress: Parsing results for plugins...')
    plugins_dict  = Results('plugins', 'query_plugins')
    plugins_total = int(plugins_dict[0])
    plugins       = plugins_dict[1]['plugins']


    # This section builds new lists that will be sorted by name before
    # we perform further actions.

    print('markan: wordpress: Building and sorting list of themes...')
    themes_list = []
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
    Sort = sorted(themes_list)

    print('markan: wordpress: Building and sorting list of plugins...')
    plugins_list = []
    for i in range(len(themes)):
        plugins_list.append([
            themes[i]['name'],
            themes[i]['slug'],
            themes[i]['version'],
            themes[i]['author']['user_nicename'],
            themes[i]['rating'],
            themes[i]['num_ratings'],
            themes[i]['homepage']
        ])
    Sort = sorted(plugins_list)


    # In this section we will write the information to two different CSV
    # files.
