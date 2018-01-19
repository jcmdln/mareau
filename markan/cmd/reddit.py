from __future__ import print_function
from praw.models import MoreComments
import click
import praw
import os.path


try:
    # Python 3
    import configparser
except ImportError:
    # Python 2
    import ConfigParser as configparser


@click.command(short_help='Interact with Reddit')
@click.option('--dictionary', '-d', is_flag=True, default=False,
              help='list of words to search for')
@click.option('--settings', '-a', default='settings.cfg',
              help='File containing settings')
@click.option('--subreddit', '-r', default='all',
              help='Target subreddit')
@click.option('--watch', '-w', is_flag=True, default=False,
              help='Get ongoing comments')


# def ContentFormatting:

def reddit(settings, dictionary, subreddit, watch):
    # It is required that the settings file exists in the current
    # directory, so we need to check that it exists and then read any
    # configuration settings.
    if os.path.isfile(settings):
        print('reddit:', 'found', settings)
        config = configparser.ConfigParser()
        config.read(settings)
    else:
        print('reddit:', 'ERROR:', settings, 'not found!')
        exit

    # We need to check if '-d' was passed to initialize some one-time
    # data to pull the list of words that will be checked against.
    if dictionary:
        mydict = config.get('Default', 'dictionary')
        WordList = set(mydict.split())

    # This section simply sets some reusable variables to be used in
    # place of performing a raw, verbose lookup later on. This is a
    # one-time
    UserAgent    = config.get('Default', 'useragent')
    Oauth2Id     = config.get('Reddit',  'oauth2_id')
    Oauth2Secret = config.get('Reddit',  'oauth2_secret')

    # praw.Reddit is used to initialize the PRAW worker with settings
    # such as the useragent and Oauth2 credentials to use.
    reddit = praw.Reddit(
        user_agent    = UserAgent,
        client_id     = Oauth2Id,
        client_secret = Oauth2Secret
    )

    if watch:
        # If specified with '-w', the http server will be left open to
        # continuously grab comments.
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
