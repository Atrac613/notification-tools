#!/usr/bin/python
# coding: utf-8

import urllib
import urllib2

from config import HIPCHAT_TOKEN
from config import HIPCHAT_ROOM_ID

def send_hipchat(message):
    values = {'room_id' : HIPCHAT_ROOM_ID,
        'from' : 'Notification',
        'message' : message}
    data = urllib.urlencode(values)
 
    url = 'https://api.hipchat.com/v1/rooms/message?format=json&auth_token=%s' % HIPCHAT_TOKEN
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
