import HTMLParser, markdown2

class entryData(object):
    title = None
    author = None
    content = None
    ID = None
    HTML = None

    '''Constructor initializes object with only five-digit post ID, in case I want to add something to the mechanism.'''
    def __init__(self, ID):
        self.ID = ID

    '''Separate method to add content into entry data'''
    def setEntryData(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content        



'''Gets content to put into magazine from reddit and returns a list of entryData objects corresponding to each submission.'''
def getContent(pickedSubreddit, timePeriod, number):
    # This is where the submissions will go
    stories = None

    print "Getting requested top posts from " + str(pickedSubreddit)
    # Get top submissions based on user-defined time period
    if timePeriod == 'hour':
        stories = pickedSubreddit.get_top_from_hour(limit = number)
    elif timePeriod == 'day':
        stories = pickedSubreddit.get_top_from_day(limit = number)
    elif timePeriod == 'week':
        stories = pickedSubreddit.get_top_from_week(limit = number)
    elif timePeriod == 'month':
        stories = pickedSubreddit.get_top_from_month(limit = number)
    elif timePeriod == 'year':
        stories = pickedSubreddit.get_top_from_year(limit = number)
    else:
        stories = pickedSubreddit.get_top_from_all(limit = number)

    # This is where a series of entryData objects will go
    dataForEntries = []
    # Create each entryData and append to above list
    storyNumber = 1
    for story in stories:
        storyData = entryData(vars(story)['id'])
        
        author = str(vars(story)['author'])
        title = vars(story)['title']
        content = vars(story)['selftext']

        storyData.setEntryData(author, title, content)

        dataForEntries.append(storyData)
        storyNumber += 1
    # Return list with data
    return dataForEntries

def convertToHTML(dataForEntries):
    print "\nDoing some text decoding/conversion magic..."

    unescape = HTMLParser.HTMLParser().unescape

    for data in dataForEntries:
        unescapedText = unescape(data.content)
        convertedToHTML = markdown2.markdown(unescapedText)
        
        data.HTML = convertedToHTML

    return dataForEntries

def convertToFinalHTML(dataWithHTMLContent):
    print "Creating HTML versions of posts...\n"

    storyNumber = 1
    for data in dataWithHTMLContent:
        print "HTMLifying story #" + str(storyNumber) + "..."

        HTMLHead = '<?xml version="1.0" encoding="UTF-8" ?>\n<head><meta charset=UTF-8" ></head>'
        titleH1 = '<h1>' + data.title + '</h1>\n\n'
        linkToOriginal = '<em>Original post: <a href="http://redd.it/' + str(data.ID) + '">redd.it/' + str(data.ID) + '</a></em>\n'
        authorEm = '<em>by /u/' + data.author + '</em><br/>'

        prettyHTMLContent = HTMLHead + '<body>' + titleH1 + linkToOriginal + '<br/>' + authorEm + '\n\n' + data.HTML + '</body>'
        data.HTML = prettyHTMLContent

        storyNumber += 1

    return dataWithHTMLContent
