#!/usr/bin/python
# coding: utf-8

import sys
import urllib2
import urllib
from bs4 import BeautifulSoup
from common import send_message

send_message('Apple Dev Center System Status')

try:
    response = urllib2.urlopen('https://developer.apple.com/support/system-status/')
    html = response.read()
 
    parsed_html = BeautifulSoup(html)
    result = parsed_html.body.find('table', attrs={'class':'status-table'})
 
    for row in result.find_all('td'):
        message = '%s - %s' % (row.span.text, row['class'][0].title())
        send_message(message)
 
    send_message('https://developer.apple.com/support/system-status/')
except Exception, e:
    send_message('Error: %s' % str(sys.exc_info()))

