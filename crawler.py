__author__ = "mko"
## 10.02.2015
## pycrawler
## 

import os
from urlparse2 import urlparse1
import urllib
from bs4 import BeautifulSoup

def clear(): # method to clear the console
    os.system(["clear","cls"][os.name == "nt"])

while True:
    clear() #clear console
    print "WELCOME TO CRAWLALOT"

    crawlall = False
    if raw_input("Do you want to crawl 1 page (1) or as many as I can find (a) ?") == "a":
        crawlall = True
    else:
        crawlall = False
    url = raw_input("Enter the url you want to get information from: ")
    try:
        response = urllib.urlopen(url)
    except BaseException, e:
        print "Crawlalot failed to reach a server."
        print "Could not find URL", url
    else:
        print "Nomnomnom..."
        print "A delicious URL! This one will do..."

        print "Crawling " + url + "..."

        urls = [url] # list of urls to search through
        visited = [url] # urls already visited
        print urls[0]
        while len(urls) > 0:
            try:
                htmltext = urllib.urlopen(urls[0]).read()
            except:
                print urls[0]
            soup = BeautifulSoup(htmltext)
            urls.pop(0)
            for tag in soup.findAll("a", href=True):
                tag["href"] = urlparse1.urljoin(url, tag["href"])
                #print tag["href"]
                if url in tag["href"] and tag["href"] not in visited: #if the url is from any other website than the one we wanted to search on
                    if crawlall:
                        print(tag["href"])
                        urls.append(tag["href"])
                    visited.append(tag["href"])
        print "\n\r\n\r"
        for visitedlink in visited:
            print "visited: " + visitedlink
    answer = raw_input("Do you want to crawl another website? (y/n) ")
    if answer != "y":
        break