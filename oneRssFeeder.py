"""
This RSS feeder can receive one URL at a time and output the top 
three entries.
"""

import feedparser
from itertools import islice

#Obtaining the url.
def getURL():
    url = input('Enter URL to fetch RSS feed:\n')
    return(url)

#Obtaining the rss feed.
def getFeed(url):
    mainFeed = feedparser.parse(url)
    return mainFeed

#Printing top 3 entries obtained in rss feed.
def main():
    url = getURL()
    print(f'Obtaining RSS feed for {url}.')

    feedOutput = getFeed(url)
    print(f'Received RSS feed of {len(feedOutput)}, will show top 3.')

    for entry in islice(feedOutput.entries, 3):
        print(f'****\nTitle: {entry.title}.')
        print(f'Link: {entry.link}')
        print(f'\nSummary: {entry.summary}\n')

#Actioning the code.
if __name__ == '__main__':
    main()

else:
    print('RSS feeder actioned from another source.')
