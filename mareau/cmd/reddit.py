"""
TODO:
- Pull comments from a target subreddit
  - Probably /r/linux/ and /r/windows/
  - Build a list of all comments that contain a word
"""

import click
import praw

@click.command(short_help='Interact with Reddit')
@click.option('--client_id',     help='Your Client ID',     default='client_id')
@click.option('--client_secret', help='Your Client Secret', default='client_secret')
@click.option('--subreddit',     help='Target subreddit',   default='/r/subreddit')

def reddit(client_id, client_secret, subreddit):
    """ """
    reddit = praw.Reddit(
        user_agent='Comment Extraction (by /r/subreddit)',
        client_id=client_id,
        client_secret=client_secret
    )
    print('Target:', client_id, client_secret, subreddit)
