#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import datetime
import subprocess

import praw
import markdown2
from docopt import docopt
from jinja2 import Environment, PackageLoader

USAGE = """reddit2kindle

Compiles requested number of top posts from specified subreddit
into a Kindle-formatted MOBI book.

Usage:
    r2k <subreddit> [--posts=<n>] [--period=<t>]

Options:
    --posts=<n>         The number of posts to include in the generated book.
                        [default: 10]
    --period=<t>        Pick the top posts from "hour", "day", "week", "month"
                        or "year".
                        [default: week]
"""


def from_cli():
    args = docopt(USAGE)

    max_posts = int(args['--posts'])
    period = args['--period']
    subreddit = args['<subreddit>']

    print "\nConnecting to reddit..."
    r = praw.Reddit('reddit-selftext-to-kindle converter')
    sub = r.get_subreddit(subreddit)

    print "Getting posts...\n"
    posts = {
        # 'all': sub.get_top_from_all,
        'year': sub.get_top_from_year,
        'month': sub.get_top_from_month,
        'week': sub.get_top_from_week,
        'day': sub.get_top_from_day,
        'hour': sub.get_top_from_hour
    }[period](limit=max_posts)

    env = Environment(loader=PackageLoader('r2klib', 'templates'))
    thread_template = env.get_template('thread.jinja')

    with open('r2k-result.htm'.format(subreddit), 'wb') as fout:
        fout.write(thread_template.render(
            now=datetime.datetime.today(),
            post_count=max_posts,
            period=period,
            subreddit=subreddit,
            title=subreddit,
            posts=posts,
            markdown=markdown2.markdown
        ).encode('utf-8'))

    converted = False
    # First, check if KindleGen exists in current folder
    if os.path.isfile('./kindlegen'):
        # Conversion by KindleGen
        print "KindleGen detected. Converting to .mobi...\n"
        subprocess.call(['./kindlegen', 'r2k-result.htm'], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        converted = True

    if not converted:
        # Find if ebook-convert exists in PATH
        ebookconvert = spawn.find_executable("ebook-convert")
        if ebookconvert:
            # Conversion by ebook-convert
            print "ebook-convert detected. Converting to .mobi...\n"
            subprocess.call([ebookconvert, 'r2k-result.htm', 'r2k-result.mobi'], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
            converted = True

    if converted:
        # Clean up HTML file and rename output
        print "Cleaning up..."
        os.remove('r2k-result.htm')
        os.rename('r2k-result.mobi', 'r2k_' + str(subreddit) + '_' + period + datetime.datetime.today().strftime("_%d-%m-%Y") + '.mobi')
    else:
        # If no convert tool found, outputs HTML file
        print "\nFind 'r2k-result.htm' in your current directory and convert it to .mobi using ebook-convert from Calibre or KindleGen from Amazon."
        print "Install Calibre or place KindleGen in your current directory to automate conversion.\n"

    print "\nDone!"
    print "Message /u/Antrikshy for help, bug reports or feedback.\n"

if __name__ == '__main__':
    sys.exit(from_cli())
