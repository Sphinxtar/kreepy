#!/bin/python -d
import requests
from bs4 import BeautifulSoup

homepage = "https://glhtracker.automationtrainer.com"
hrefs = []

def probe(site,top):
    if (top):
        print("<site>")
    print("<link>")
    print("<url>" + site + "</url>")
    apage = requests.get(site) 
    print("<status>"+str(apage.status_code)+"</status>")
    print("</link>")
    soup = BeautifulSoup(apage.content, features="lxml")
    links = soup.find_all("a")
    for link in links:
        if link.get("href") not in hrefs and link.get("href") != homepage:
            hrefs.append(link.get("href"))
            probe(link.get("href"),0)
    if (top):
        print("</site>")

probe(homepage,1)
