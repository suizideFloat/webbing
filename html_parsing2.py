
from BeautifulSoup import BeautifulSoup
import urllib2
#import lxml
import re

html_url = "http://www.einslive.de/musik/playlists/"

fotze = urllib2.urlopen(html_url).read()


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_doc2 = """
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de"><head>
<title>Playlists - Musik - 1LIVE</title>
<hr class="inv"/><h3 class="level3">Die letzten 12 Titel</h3>
<table summary="Die letzten 12 gespielten Titel" class="wsPlaylistsEL">
<thead><tr class="wsColored">
<th id="pltab1time" scope="col">Uhrzeit</th>
<th id="pltab1artist" scope="col">Interpret</th>
<th id="pltab1title" scope="col">Titel</th>
</tr></thead><tbody><tr class="wsEven">
<td headers="pltab1time">20:33:42</td>
<td class="bold" headers="pltab1artist">Timid Tiger</td>
<td headers="pltab1title">Hangin&#039; in the Sun</td></tr>
<tr class="wsOdd"><td headers="pltab1time">20:30:30</td>
<td class="bold" headers="pltab1artist">Phoenix</td>
<td headers="pltab1title">Entertainment</td></tr>
<tr class="wsEven"><td headers="pltab1time">20:25:57</td>
<td class="bold" headers="pltab1artist">Disclosure feat. AlunaGeorge</td>
<td headers="pltab1title">White Noise</td></tr><tr class="wsOdd">
<td headers="pltab1time">20:22:22</td>
<td class="bold" headers="pltab1artist">The Wombats</td>
<td headers="pltab1title">Tokyo (Vampires &amp; Wolves)</td></tr>
<tr class="wsEven"><td headers="pltab1time">20:17:03</td>
<td class="bold" headers="pltab1artist">Grizzly Bear</td>
<td headers="pltab1title">Speak in rounds</td></tr>
<tr class="wsOdd"><td headers="pltab1time">20:13:11</td>
<td class="bold" headers="pltab1artist">Depeche Mode</td>
<td headers="pltab1title">Soothe My Soul</td></tr><tr class="wsEven">
<td headers="pltab1time">20:06:39</td>
<td class="bold" headers="pltab1artist">WhoMadeWho</td>
<td headers="pltab1title">Inside World</td></tr><tr class="wsOdd">
<td headers="pltab1time">20:04:01</td>
<td class="bold" headers="pltab1artist">Vampire Weekend</td>
<td headers="pltab1title">Diane Young</td></tr><tr class="wsEven">
<td headers="pltab1time">19:56:11</td>
<td class="bold" headers="pltab1artist">Passenger</td>
<td headers="pltab1title">Let her go</td></tr><tr class="wsOdd">
<td headers="pltab1time">19:53:09</td>
<td class="bold" headers="pltab1artist">The Black Keys</td>
<td headers="pltab1title">Lonely boy</td></tr><tr class="wsEven">
<td headers="pltab1time">19:50:01</td>
<td class="bold" headers="pltab1artist">Jason Derulo</td>
<td headers="pltab1title">In my head</td></tr>
<tr class="wsOdd"><td headers="pltab1time">19:45:30</td>
<td class="bold" headers="pltab1artist">Lena</td>
<td headers="pltab1title">Neon (Lonely People)</td>
</tr></tbody></table></div>
"""

soup = BeautifulSoup(html_doc2)


#print(soup.prettify())
#print (soup.find_all('td'))
#print (soup.find_all("td", "headers"))

print (soup.find_all(headers=re.compile("pltab1artist", "pltab1title")))

#print (soup.title.string)
#print (fotze)

"""
for headers in soup.find_all('td'):
    print (soup.find(headers="pltab1artist"))
    print (soup.find(headers="pltab1title"))
"""

#for headers in soup.find_all('td'):
#    print(headers.get('td'))

#headers="pltab1artist"