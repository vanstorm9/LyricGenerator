from bs4 import BeautifulSoup
from urllib2 import urlopen
import re


BASE_URL = "http://www.azlyrics.com"

def get_category_links00(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    cont = soup.find("div", "cont")
    for div in cont.findAll("div"):
        for a in div.findAll("a"):
            b = str(a["href"])
            if b[0] == 'a':
                get_category_links01("http://www.darklyrics.com/" + b)
    
    #category_links = [BASE_URL + div for div in cont.findAll("div")]
    #return category_links'''

def get_category_links01(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    lyrics = soup.find("div", "cont")
    for div in lyrics.findAll("div"):
        for a in div.findAll("a"):
            c= str(a["href"])
            get_category_links02("http://www.darklyrics.com/" + c[3:])
            
def get_category_links02(category_url):
    html = urlopen(category_url).read()
    soup = BeautifulSoup(html, "lxml")
    lyrics = soup.find("div","lyrics")
    all_lyrics = []
    current_lyric = ''
    for br in lyrics.findAll('br'):
        next = br.nextSibling
        try:
            current_lyric = current_lyric + next.split('<br/>')[0]
        except TypeError:
            all_lyrics.append(current_lyric)
    print all_lyrics[0]
            #current_lyric = ''
        # if not next == None:
            # print next.split('<br/><br/><br/>')
        #searchResult = re.search('<br/>',next, re.M|re.I)
        #if searchResult:
            #print(blah)
    #Title = soup.find("h3").string
    #winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
    #return {"lyrics": }'''
    

def print_func( par):
   return 

print_func(get_category_links00("http://www.darklyrics.com/a.html"))
