from __future__ import print_function

import click
import csv

''' WARNING: This is a work-in-progress with notes

## API MAP
wew = {
    "data": {
        "after": "",
        "before": "",

        "children": [
            {
                "subreddit": "",
                "name": "",
                "id": "",
                "score": "",

                "created": "",
                "title": "",
                "author": "",
                "url": "",
                "selftext": "",

                "ups": "",
                "downs": "",
            }
        ]
    }
}
'''

@click.command(short_help = 'Pull data from the Reddit API')
@click.option('--subreddit', '-r', help = 'Target subreddit(s)',
              default = 'all')
@click.option('--user',      '-u', help = 'Target user(s)',
              default = '')

def reddit(subreddit, user):
    # API endpoints
    SUB  = "https://www.reddit.com/r/" + sub + ".json"
    USER = "https://www.reddit.com/u/" + user + ".json"
