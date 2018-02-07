from __future__ import print_function

import click
import os.path
import subprocess

import praw
from praw.models import MoreComments

try:
    # Python 3
    import configparser
except ImportError:
    # Python 2
    import ConfigParser as configparser

#
@click.command(short_help='Interact with Reddit')
@click.option('--dictionary', '-d', is_flag=True, default=False,
              help='list of words to search for')
@click.option('--settings', '-s', default='settings.cfg',
              help='File containing settings')
@click.option('--subreddit', '-r', default='all',
              help='Target subreddit')
# @click.option('--user', '-u', default='all',
#               help='Target user')


#
def reddit(dictionary, settings, subreddit):
    #
    if os.path.isfile(settings):
        print('reddit:', 'found', settings)
        config = configparser.ConfigParser()
        config.read(settings)
    else:
        print('reddit:', 'ERROR:', settings, 'not found!')
        exit

    #
    if dictionary:
        BaseWords    = config.get('Dictionary', 'base').split()
        CommentWords = config.get('Dictionary', 'comment').split()

    #
    reddit = praw.Reddit(
        user_agent    = config.get('Default', 'useragent'),
        client_id     = config.get('Reddit',  'oauth2_id'),
        client_secret = config.get('Reddit',  'oauth2_secret')
    )
    reddit.read_only = True

    #
    Submissions = []

    #
    for submission in reddit.subreddit(subreddit).hot(limit=2):
        print("reddit: Looking through", subreddit)
        submission = reddit.submission(id=submission.id)
        submission.comments.replace_more(limit=None)

        #
        if dictionary:
            #
            for title in submission.title:
                for word in BaseWords and CommentWords:
                    if word in submission.title:
                        current_submission = {
                            'ID':       submission.id,
                            'Score':    submission.score,
                            'User':     submission.author,
                            'Title':    submission.title,
                            'URL':      submission.url,
                            'Comments': []
                        }
                        Submissions.append(current_submission)

                        print(
                            current_submission['ID'],
                            current_submission['Score'],
                            current_submission['User'],
                            '\n', current_submission['Title'],
                            '\n', current_submission['Body']
                        )

            #
            for comment in submission.comments.list():
                for word in BaseWords and CommentWords:
                    if word in comment.body:
                        current_comment = {
                            'ID':      comment.id,
                            'Score':   comment.score,
                            'User':    comment.author,
                            'Body':    comment.body,
                            'Replies': []
                        }
                        current_submission['Comments'].append(current_comment)
                        print(
                            current_comment['ID'],
                            current_comment['Score'],
                            current_comment['User'],
                            '\n', current_comment['Body']
                        )

        #
        else:
            current_submission = {
                'ID':       submission.id,
                'Score':    submission.score,
                'User':     submission.author,
                'Title':    submission.title,
                'URL':      submission.url,
                'Comments': []
            }
            Submissions.append(current_submission)

            print(
                current_submission['ID'],
                current_submission['Score'],
                current_submission['User'],
                '\n', current_submission['Title'],
                '\n', current_submission['Body']
            )

            for comment in submission.comments.list():
                current_comment = {
                    'ID':      comment.id,
                    'Score':   comment.score,
                    'User':    comment.author,
                    'Body':    comment.body,
                    'Replies': []
                }
                current_submission['Comments'].append(current_comment)

                print(
                    current_comment['ID'],
                    current_comment['Score'],
                    current_comment['User'],
                    '\n', current_comment['Body']
                )
