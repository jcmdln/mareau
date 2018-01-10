import click
import praw
import os.path

from praw.models import MoreComments

try:
    # Python 3
    import configparser
except ImportError:
    # Python 2
    import ConfigParser as configparser


@click.command(short_help='Interact with Reddit')
@click.option('--authfile', '-a', default='settings.cfg',
              help='File containing Oauth2 credentials')
@click.option('--dictionary', '-d', is_flag=True, default=False,
              help='list of words to search for')
@click.option('--subreddit', '-r', default='all',
              help='Target subreddit')
@click.option('--watch', '-w', is_flag=True, default=False,
              help='Get ongoing comments')


def reddit(authfile, dictionary, subreddit, watch):
    # Confirm authfile exists, otherwise exit
    if os.path.isfile(authfile):
        print('reddit:', 'found', authfile)
    else:
        print('reddit:', 'ERROR:', authfile, 'not found!')
        exit

    # Read authfile for settings
    config = configparser.ConfigParser()
    config.read(authfile)

    if dictionary:
        mydict = config.get('Default', 'dictionary')
        WordList = set(mydict.split())

    UserAgent    = config.get('Default', 'useragent')
    Oauth2Id     = config.get('Reddit',  'oauth2_id')
    Oauth2Secret = config.get('Reddit',  'oauth2_secret')

    # Setup PRAW using authfile config
    reddit = praw.Reddit(
        user_agent    = UserAgent,
        client_id     = Oauth2Id,
        client_secret = Oauth2Secret
    )

    if watch:
        # Start server to grab live comments
        for comment in reddit.subreddit(subreddit).stream.comments():
            if isinstance(comment, MoreComments):
                continue
            if dictionary:
                for word in WordList:
                    if word in comment.body:
                        print(comment.body)
                        print('------------------------------')
            else:
                print(comment.body)
                print('------------------------------')
    else:
        # Grab comment history
        for submission in reddit.subreddit(subreddit).hot():
            if dictionary:
                for word in WordList:
                    if word in submission.title:
                        print(submission.title)
                        print('------------------------------')
            else:
                print(submission.title)
                print('------------------------------')
