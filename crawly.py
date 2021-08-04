#!/bin/python 
import sys
import requests
import datetime
import re
from bs4 import BeautifulSoup

hrefs = []
stamp = datetime.datetime.now().replace(microsecond=0).isoformat()

<<<<<<< HEAD
def probe(site):
	print("probing: " + site)
	apage = requests.get(site) 
	if apage.status_code != 200:
		print("returned: ", apage.status_code, " ERROR")	
	else:
		print("returned: ", apage.status_code)
	soup = BeautifulSoup(apage.content, features="lxml")
	links = soup.find_all("a")
	for link in links:
		if link.get("href") not in hrefs and link.get("href") != homepage:
			hrefs.append(link.get("href"))
			probe(link.get("href"))

if  len(sys.argv) < 2:
	print("\nUsage: crawly.py <Base URL to crawl>\n\n")
	quit
elif sys.argv[1].startswith('http') != True:
	print("\nURL must be well formed\n\n")
	quit
else:
	homepage = str(sys.argv[1])
	probe(homepage)
=======
def probe(site,top):
    if (top):
        crawlydoc.write("<site>")
    crawlydoc.write("<link>")
    crawlydoc.write("<url>"+site+"</url>")
    apage = requests.get(site) 
    crawlydoc.write("<status>"+str(apage.status_code)+"</status>")
    crawlydoc.write("<check>"+stamp+"</check>")
    crawlydoc.write("</link>")
    soup = BeautifulSoup(apage.content, features="lxml")
    links = soup.find_all("a")
    for link in links:
        if link.get("href") not in hrefs and link.get("href") != homepage:
            hrefs.append(link.get("href"))
            probe(link.get("href"),0)
    if (top):
        crawlydoc.write("</site>")

file='crawly.xml' 
with open(file, 'w') as crawlydoc:
    probe(homepage,1)
    crawlydoc.close()
>>>>>>> bbc3397c68b2b9cf879fa1a3a761aa071daef0df
