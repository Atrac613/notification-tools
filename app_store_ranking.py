#!/usr/bin/python
# coding: utf-8

import sys
import feedparser
from common import send_message
 
COUNTRIES = ['jp', 'us']
LIMIT = 10
URLS = ['https://itunes.apple.com/%s/rss/topfreeapplications/limit=%d/xml',
    'https://itunes.apple.com/%s/rss/toppaidapplications/limit=%d/xml',
    'https://itunes.apple.com/%s/rss/topgrossingapplications/limit=%d/xml']
 
def get_feed(url):
    rss = feedparser.parse(url)
    send_message(rss['feed']['title'].encode('utf8'))
    rank = 1
    for entry in rss['entries']:
        title = entry['title'].encode('utf8')
        message = '%d: %s' % (rank, title)
        send_message(message)
        rank = rank + 1
 
for country in COUNTRIES:
    for url in URLS:
        try:
            url = url % (country, LIMIT)
            get_feed(url)
        except Exception, e:
            send_message('Error: %s' % str(sys.exc_info()))

