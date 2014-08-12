import praw
import utils

subreddit = 'talesfromtechsupport'
timePeriod = 'week'
number = 5

# In this case, we use PRAW without logging into reddit
print "Connecting to reddit..."
r = praw.Reddit('reddit-selftext-to-Kindle converter by /u/Antrikshy')
print "Connected."
pickedSubreddit = r.get_subreddit(subreddit)

# Get reddit content
dataForEntries = utils.getContent(pickedSubreddit, timePeriod, number)
# Convert stories to HTML
dataWithHTMLContent = utils.convertToHTML(dataForEntries)
# Construct final HTML
finalEntriesInHTML = utils.convertToFinalHTML(dataWithHTMLContent)

print "Compiling almost-final HTML version of book..."
finalHTML = ""
for readyEntry in finalEntriesInHTML:
    finalHTML = finalHTML + readyEntry.HTML.encode("utf8") + "<mbp:pagebreak />"

print "Writing HTML version of book..."
fp = open("HTMLTest.htm", "w")
fp.write(finalHTML)
fp.close()
print "HTML version ready!"
