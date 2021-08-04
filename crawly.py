#!/bin/python 
import sys
import requests
from bs4 import BeautifulSoup

hrefs = []

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
