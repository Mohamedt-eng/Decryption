from colorama import *
import io,sys,os
import urllib
import bs4
from bs4 import BeautifulSoup
"\n"
ul = raw_input("entre vore URL  >>")

req = urllib.urlopen(ul)
soup = BeautifulSoup(req, 'html.parser')
for i in soup.find_all('a'):
    
    print "A","\033[35m ", i.get('href'),"\033[0m "

for c in soup.findAll( 'link'):

    print "L","\033[32m ", c.get('href'),"\033[0m "

for s in soup.find_all('script'):

    print "S","\033[31m ", s.get('src'),"\033[0m "
