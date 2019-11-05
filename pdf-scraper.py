from urllib import request
from bs4 import BeautifulSoup
import re
import os
import urllib
import wget

# connect to website and get list of all pdfs
url=open("listurls.txt",'r')
links_list=[]
for l in url:
    response = request.urlopen(l).read()
    soup= BeautifulSoup(response, "html.parser")
    links_list.append( soup.find_all('a', href=re.compile(r'(.pdf)')))
  

links=[]
for i in links_list:
    links.append(re.findall(r'http.+pdf',str(i)))

for l in links:
   wget.download(l[0])
