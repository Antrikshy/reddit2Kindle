#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import datetime
import subprocess
from distutils import spawn

import praw
import markdown2
from docopt import docopt
from jinja2 import Environment, PackageLoader

USAGE = """reddit2kindle

Compiles requested number of top posts from specified subreddit
into a Kindle-formatted MOBI book.

Usage:
    r2k.py top <subreddit> [--posts=<n>] [--period=<t>] [options]
    r2k.py hot <subreddit> [--posts=<n>] [options]

Options:
    --posts=<n>         The number of posts to include in the generated book.
                        [default: 10]
    --period=<t>        Pick the top posts from "hour", "day", "week", "month"
                        or "year".
                        [default: week]
    --debug             Enable debug logging.
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def from_cli():
    args = docopt(USAGE)

    max_posts = int(args['--posts'])
    period = args['--period']
    subreddit = args['<subreddit>']

    # Setup logging.
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if args['--debug'] else logging.INFO)
    fmt = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # This doesn't actually connect to Reddit. It creates a lazy proxy
    # that doesn't get resolved until you actually query for some
    # property.
    r = praw.Reddit(user_agent='reddit-selftext-to-kindle converter')
    sub = r.get_subreddit(subreddit)

    if args['top']:
        posts = {
            'all': sub.get_top_from_all,
            'year': sub.get_top_from_year,
            'month': sub.get_top_from_month,
            'week': sub.get_top_from_week,
            'day': sub.get_top_from_day,
            'hour': sub.get_top_from_hour
        }[period](limit=max_posts)
    elif args['hot']:
        posts = sub.get_hot(limit=max_posts)

    env = Environment(loader=PackageLoader('r2klib', 'templates'))
    thread_template = env.get_template('thread.jinja')

    logger.debug('generating html template...')
    with open('r2k_result.htm'.format(subreddit), 'wb') as fout:
        fout.write(thread_template.render(
            now=datetime.datetime.today(),
            post_count=max_posts,
            period=period,
            subreddit=subreddit,
            title=subreddit,
            posts=posts,
            markdown=markdown2.markdown,
            type_of_posts='top' if args['top'] else 'hot'
        ).encode('utf-8'))

    converted = False
    with open(os.devnull, 'w') as devnull:
        if os.path.isfile('./kindlegen'):
            subprocess.call([
                './kindlegen',
                'r2k_result.htm'
            ], stdout=devnull, stderr=subprocess.STDOUT)
            converted = True
        else:
            logger.info('could not locate kindlegen binary')

        if not converted:
            ebookconvert = spawn.find_executable("ebook-convert")
            if ebookconvert:
                subprocess.call([
                    ebookconvert,
                    'r2k_result.htm',
                    'r3k_result.mobi'
                ], stdout=devnull, stderr=subprocess.STDOUT)
                converted = True
            else:
                logger.info('could not locate ebook-convert binary')

    if converted:
        os.remove('r2k_result.htm')
        os.rename('r2k_result.mobi', 'r2k_{sub}_{period}_{dt}.mobi'.format(
            sub=subreddit,
            period=period,
            dt=datetime.datetime.today().strftime('%d-%m-%Y')
        ))
    else:
        logger.warning(
            'Could not locate kindlegen or ebook-convert for automatic'
            ' MOBI creation. Either download these tools, or email the'
            '.html to your kindle address.'
        )

if __name__ == '__main__':
    sys.exit(from_cli())
