import praw, argparse, os
import utils

parser = argparse.ArgumentParser(description="Compiles requested number of top posts from specified subreddit into a Kindle book")
parser.add_argument('subreddit', help="Subreddit you want to scan", type=str)
parser.add_argument('time', help="Top posts from hour/day/week/month/year", type=str)
parser.add_argument('number', help="Number of top posts to scan", type=int)
args = parser.parse_args()

subreddit = args.subreddit
timePeriod = args.time
number = args.number

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
# Write to 'File To Convert.htm' in the current directory
fp = open(os.getcwd() + "/File To Convert.htm", "w")
fp.write(finalHTML)
fp.close()
print "HTML version ready!"
print "Find 'File To Convert.htm' in your current working directory and convert it to .mobi using KindleGen from Amazon."