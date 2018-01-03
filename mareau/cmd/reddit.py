"""
# Example config.cfg

[Default]
useragent = 'mareau'

[Reddit]
# https://github.com/reddit/reddit/wiki/OAuth2
oauth2_id     = 'Reddit Oauth2 client ID'
oauth2_secret = 'Reddit Oauth2 client secret'

[Sheets]
# https://developers.google.com/sheets/api/quickstart/python
oauth2_id     = 'Google Sheets Oauth2 client ID'
oauth2_secret = 'Google Sheets Oauth2 client secret'
"""


import click
import praw
import os.path

from praw.models import MoreComments

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


@click.command(short_help='Interact with Reddit')
@click.option('--authfile', '-a', default='config.cfg',
              help='File containing Oauth2 credentials')
# @click.option('--dictionary', '-d',
#               help='list of words to search for')
@click.option('--subreddit', '-r', default='/r/linux',
              help='Target subreddit')
@click.option('--watch', '-w', is_flag=True, default=False,
              help='Get ongoing comments')


def reddit(authfile, subreddit, watch):
    # Confirm authfile exists, otherwise exit
    if os.path.isfile(authfile):
        print('mareau:', 'found', authfile)
    else:
        print('mareau:', 'ERROR:', authfile, 'not found!')
        exit

    # Read settings from authfile
    config = configparser.ConfigParser()
    config.read(authfile)

    # Define PRAW settings
    reddit = praw.Reddit(
        user_agent    = config.get('Default', 'useragent'),
        client_id     = config.get('Reddit',  'oauth2_id'),
        client_secret = config.get('Reddit',  'oauth2_secret')
    )

    if watch:
        # Start server to grab current comments
        for comment in reddit.subreddit(subreddit).stream.comments():
            if isinstance(comment, MoreComments):
                continue
            print(comment.body)
    else:
        # Grab comment history
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            print(top_level_comment.body)
