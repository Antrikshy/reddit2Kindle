import praw
import utils

subreddit = 'talesfromtechsupport'
timePeriod = 'week'
number = 5

# In this case, we use PRAW without logging into reddit
r = praw.Reddit('reddit-selftext-to-Kindle converter by /u/Antrikshy')
pickedSubreddit = r.get_subreddit(subreddit)

dataForEntries = utils.getContent(pickedSubreddit, timePeriod, number)
entriesinHTML = utils.convertToHTML(dataForEntries)

print entriesinHTML[0].HTML
