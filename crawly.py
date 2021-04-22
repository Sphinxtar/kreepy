#!/bin/python -d
import requests
from bs4 import BeautifulSoup

homepage = "https://glhtracker.automationtrainer.com"
hrefs = []

def probe(site):
    print("probing: " + site)
    apage = requests.get(site) 
    print("returned: ", apage.status_code)
    soup = BeautifulSoup(apage.content, features="lxml")
    links = soup.find_all("a")
    for link in links:
        if link.get("href") not in hrefs and link.get("href") != homepage:
            hrefs.append(link.get("href"))
            probe(link.get("href"))

probe(homepage)
