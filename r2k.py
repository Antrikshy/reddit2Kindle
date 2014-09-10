#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime

import praw
from docopt import docopt

from redditKindleLib import utils


USAGE = """r2k.py

Compiles requested number of top posts from specified subreddit
into a Kindle-formatted MOBI book.

Usage:
    r2k.py <subreddit> [--posts=<n>] [--period=<t>]

Options:
    --posts=<n>         The number of posts to include in the generated book.
                        [default: 5]
    --period=<t>        Pick the top posts from "hour", "day", "week", "month"
                        or "year".
                        [default: "day"]
"""


def from_cli():
    args = docopt(USAGE)
    max_posts = int(args['--posts'])
    period = args['--period']
    subreddit = args['<subreddit>']

    head_text = "<h3 style='text-align:center;'>Created using <a href='http://antrikshy.com/projects/reddit2Kindle.htm'>reddit2Kindle</a>\
                 by /u/Antrikshy</h3><p style='text-align:center;'>Download for your own use at Antrikshy.com/projects/reddit2Kindle.htm</p>\
                 <mbp:pagebreak /></body>"

    book_title_text = "<h1 style='text-align:center;'>Top " + str(max_posts) + " posts of the " + period + " from /r/" + str(subreddit) + "</h1>"

    today = datetime.date.today()
    date_time_text = "<h3 style='text-align:center;'>" + today.strftime("Compiled on %d, %b %Y") + "</h3>"

    r = praw.Reddit('reddit-selftext-to-Kindle converter by /u/Antrikshy')
    pickedSubreddit = r.get_subreddit(subreddit)

    dataForEntries = utils.getContent(pickedSubreddit, period, max_posts)
    dataWithHTMLContent = utils.convertToHTML(dataForEntries)
    finalEntriesInHTML = utils.convertToFinalHTML(dataWithHTMLContent)

    finalHTML = "<body>" + book_title_text + date_time_text + "<br/><br/><br/>" + head_text + "</body>"
    for readyEntry in finalEntriesInHTML:
        finalHTML = finalHTML + readyEntry.HTML.encode("utf8") + "<mbp:pagebreak />"

    destination = '{subreddit}.html'.format(subreddit=subreddit)
    with open(destination, 'wb') as fout:
        fout.write(finalHTML)


if __name__ == '__main__':
    sys.exit(from_cli())
