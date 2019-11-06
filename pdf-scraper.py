from urllib import request
from bs4 import BeautifulSoup
import re
import os
import urllib
import wget

def scraphtml(single_url):
    links_list=[]
    response = request.urlopen(single_url).read()
    soup= BeautifulSoup(response, "html.parser")
    links_list.append( soup.find_all('a', href=re.compile(r'(.pdf)')))
    return links_list

def html_to_link(links_list):
    links=[]
    for i in links_list:
        links.append(re.findall(r'http.+pdf',str(i)))
    return links

def download_from_links(links):
    for l in links:
        wget.download(l[0])

def final_download_single_link(single_url):
    links_list=scraphtml(single_url)
    links=html_to_link(links_list)
    download_from_links(links)

def final_download_multiple_link(list_urls):
    for l in list_urls:
        final_download_single_link(l)

def main():
    #import list of urls
    url=open("listurls.txt",'r')
    final_download_multiple_link(url)
  
if __name__== "__main__":
  main()
 
