#! /usr/bin/python

### DEPRECATED !!!

# coding: utf8
# Author: TestOr

import requests
#import lxml
from BeautifulSoup import BeautifulSoup


input = '''<html>
... <head><title>Page title</title></head>
... <body>
... <p id="firstpara" align="center">This is paragraph <b>one</b>.
... <p id="secondpara" align="blah">This is paragraph <b>two</b>.
... </html>'''


if __name__ == '__main__':

    request = requests.get('http://www.einslive.de/musik/playlists/')
#    nutte = lxml.parse(request)

    soup1 = BeautifulSoup(input)
    soup2 = BeautifulSoup(request.content)

    output= soup2.find(headers="pltab1artist")

#    print request.content
#    print(soup1.prettify())
    print output