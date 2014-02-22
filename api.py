# -*- coding: utf8 -*-
import json
import urllib2

REQUEST_URL = 'http://ws.audioscrobbler.com/2.0/?method=user' \
              '.getrecenttracks&user=%s&api_key' \
              '=%s&limit=2&format=json'


def request_track_data(user, api_key):
    try:
        r = urllib2.urlopen(REQUEST_URL % (user, api_key))
        return json.loads(r.read())
    except urllib2.URLError:
        pass


def extract_track(data):
    last = data['recenttracks']['track'][0]
    if last.get('@attr', {}).get('nowplaying') == 'true':
        return '%s - %s' % (last['artist']['#text'], last['name'])


def check_track(user='enter_here', api_key='enter_here'):
    data = request_track_data(user, api_key)
    if data:
        return extract_track(data)
