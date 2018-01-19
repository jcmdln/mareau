from __future__ import print_function
from praw.models import MoreComments
import click
import praw
import os.path
import subprocess


# Python 2/3 don't refer to the same package
try:
    # Python 3
    import configparser
except ImportError:
    # Python 2
    import ConfigParser as configparser


# This section is specific to 'click' and is for defining command line
# flags.
@click.command(short_help='Interact with Reddit')
@click.option('--dictionary', '-d', is_flag=True, default=False,
              help='list of words to search for')
@click.option('--settings', '-s', default='settings.cfg',
              help='File containing settings')
@click.option('--subreddit', '-r', default='all',
              help='Target subreddit')
# @click.option('--user', '-u', default='all',
#               help='Target user')


def reddit(settings, dictionary, subreddit):
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
        basedict     = config.get('Dictionary', 'base')
        BaseWords    = set(basedict.split())
        commentdict  = config.get('Dictionary', 'comment')
        CommentWords = set(commentdict.split())

    # praw.Reddit is used to initialize the PRAW worker with settings
    # such as the useragent and Oauth2 credentials to use. The
    # information to use is pulled from the configuration file.
    reddit = praw.Reddit(
        user_agent    = config.get('Default', 'useragent'),
        client_id     = config.get('Reddit',  'oauth2_id'),
        client_secret = config.get('Reddit',  'oauth2_secret')
    )
    reddit.read_only = True

    #
    for submission in reddit.subreddit(subreddit).hot(limit=None):
        submission = reddit.submission(id=submission.id)
        submission.comments.replace_more(limit=None)
        print('--- Submission ---------------------------')
        print('[', 'Score:', submission.score,',',
              'ID:', submission.id, ',',
              'User:', submission.author, ']',
              submission.title)
        print(submission.url)
        if dictionary:
            for comment in submission.comments.list():
                for word in BaseWords and CommentWords:
                    if word in comment.body:
                        print('--- Comment ---------------------------')
                        print('[', 'Score:', comment.score,',',
                              'ID:', comment.id, ',',
                              'User:', comment.author, ']')
                        print(comment.body)
        else:
            for comment in submission.comments.list():
                print('--- Comment ---------------------------')
                print('[', 'Score:', comment.score,',',
                      'ID:', comment.id, ',',
                      'User:', comment.author, ']')
                print(comment.body)
