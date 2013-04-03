import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    request = requests.get('http://www.einslive.de/musik/playlists/')
    bs = BeautifulSoup(request.content)
    table = bs.find('table', class_='wsPlaylistsEL')

    for tr in table.find_all('tr'):
        artist = tr.find('td', headers='pltab1artist')
        title = tr.find('td', headers='pltab1title')

        if artist and title:
            print "%s - %s" % (artist.text, title.text)