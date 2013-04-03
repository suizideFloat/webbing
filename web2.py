
### DEPRECATED !!!

import requests
from BeautifulSoup import BeautifulSoup



if __name__ == '__main__':

    request = requests.get('http://www.einslive.de/musik/playlists/')
    bs = BeautifulSoup(request.content)
    table = bs.find('table', class_="wsPlaylistsEL")
    #table = bs.find('table', summary="Die letzten 12 gespielten Titel")
    kokolores = bs.body.findAll('table')

    for tr in kokolores.find('tr', class_='wsPlaylistsEL'):
        artist = tr.find('td', headers='pltab1artist')
        title = tr.find('td', headers='pltab1title')

#    for tr in bs.findAll('tr', attrs={'class': 'list-authors'}):

    # for tr in table.find_all('tr'):
    #      artist = tr.find('td', headers='pltab1artist')
    #      title = tr.find('td', headers='pltab1title')

        if artist and title:
            print "%s - %s" % (artist.text, title.text)

    # print request.status_code
    # print kokolores
#    print table.__class__