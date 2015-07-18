from bs4 import BeautifulSoup
import urllib2

url="http://fiikus.net/?pokedex"
webpage = urllib2.urlopen(url)
soup = BeautifulSoup(webpage)
for anchor in soup.find_all('a'):
    try:
        k=str(anchor.string)
        if k[0]=="#":
            L=str(anchor.string).split(" ")[1:]
            print " ".join(L).replace('"','').replace('(','').replace(')','').replace(' ','').replace("'",'').replace(".",'')

        
    except:pass
