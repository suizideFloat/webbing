#! /usr/bin/python

import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://www.einslive.de/musik/playlists/", params)
print f.read()

