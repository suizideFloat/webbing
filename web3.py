
### DEPRECATED !!!

#import re
import requests #,sys
from BeautifulSoup import BeautifulSoup


request = requests.get('http://www.einslive.de/musik/playlists/')

soup = BeautifulSoup(request.content)

interstep = soup.html.body

artistlist = interstep.find('table', attrs={'class': 'wsPlaylistsEL'})

print artistlist.find('tr', class_='wsPlaylistsEL')

for tr in artistlist.findAll('tr'):
         artist = tr.find('td', headers='pltab1artist')
         title = tr.find('td', headers='pltab1title')

if artist and title:
            print "%s - %s" % (artist.text, title.text)