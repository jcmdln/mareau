from __future__ import print_function
import os.path
import click
import praw
from praw.models import MoreComments

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

@click.command(short_help='Pull data from the Reddit API')
@click.option('--dictionary', '-d', is_flag=True, default=False,
              help='list of words to search for')
@click.option('--settings', '-s', default='settings.cfg',
              help='File containing settings')
@click.option('--subreddit', '-r', default='all',
              help='Target subreddit(s) to pull data from')

def reddit(dictionary, settings, subreddit):
    if os.path.isfile(settings):
        print('markan: reddit:', 'found', settings)
        config = configparser.ConfigParser()
        config.read(settings)
    else:
        print('markan: reddit:', 'ERROR:', settings, 'not found!')
        exit

    if dictionary:
        BaseWords    = config.get('Dictionary', 'base').split()
        CommentWords = config.get('Dictionary', 'comment').split()

    reddit = praw.Reddit(
        user_agent    = config.get('Default', 'useragent'),
        client_id     = config.get('Reddit',  'oauth2_id'),
        client_secret = config.get('Reddit',  'oauth2_secret')
    )
    reddit.read_only = True

    def Submission():
        current_submission = {
            'Score':     submission.score,
            'User':      submission.author,
            'Title':     submission.title,
            'URL':       submission.url,
            'Comments': {}
        }
        Submissions[submission.id] = current_submission

        print(
            '[',
            'r/'+subreddit, '|',
            'ID:', submission.id, '|',
            'Score:', current_submission['Score'], '|',
            'User:', current_submission['User'],
            ']', '\n' +
            current_submission['Title']
        )

    def Comment():
        current_comment = {
            'Score':      comment.score,
            'User':       comment.author,
            'Body':       comment.body,
            'Replies':    {}
        }
        Submissions[submission.id]['Comments'][comment.id] = current_comment

        print(
            '[',
            submission.id, '|',
            comment.id, '|',
            'Score:', current_comment['Score'], '|',
            'User:', current_comment['User'],
            ']', '\n' +
            current_comment['Body'], '\n'
        )

    Submissions = {}
    for submission in reddit.subreddit(subreddit).hot(limit=None):
        submission = reddit.submission(id=submission.id)
        submission.comments.replace_more(limit=None)

        if dictionary:
            for word in BaseWords and CommentWords:
                if word in submission.title:
                    Submission()
            for comment in submission.comments.list():
                for word in BaseWords and CommentWords:
                    if word in comment.body:
                        Comment()
        else:
            Submission()
            for comment in submission.comments.list():
                Comment()
