#!/bin/python -d
import sys
import requests
import datetime
import re
from bs4 import BeautifulSoup

hrefs = []
stamp = datetime.datetime.now().replace(microsecond=0).isoformat()

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

#homepage = "https://glhtracker.automationtrainer.com"
#file = "crawly.xml"

if  len(sys.argv) < 2:
	print("\nUsage: crawly.py <Filename.xml> <Base URL To Crawl>\n\n")
	quit()
elif sys.argv[2].startswith('http') != True:
	print("\nURL arg must be well formed\n\n")
	quit()
else:
	homepage = str(sys.argv[2])
	file = str(sys.argv[1])
	with open(file, 'w') as crawlydoc:
		probe(homepage,1)
		crawlydoc.close()
	quit()

