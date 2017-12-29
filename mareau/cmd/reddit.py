import click
import praw
from praw.models import MoreComments


@click.command(short_help='Interact with Reddit')
@click.option('--client_id',     '-i', help='Oauth2 client id')
@click.option('--client_secret', '-s', help='Oauth2 client secret')
@click.option('--subreddit',     '-r', help='Target subreddit')
@click.option('--user_agent',    '-u', help='Useragent')
#@click.option('--word_list',     '-w', help='Words to search for')


def reddit(client_id, client_secret, subreddit, user_agent):
    reddit = praw.Reddit(
        user_agent=user_agent,
        client_id=client_id,
        client_secret=client_secret
    )
    for comment in reddit.subreddit(subreddit).stream.comments():
        if isinstance(comment, MoreComments):
            continue
        print(comment.body)
