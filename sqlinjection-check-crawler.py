#!/usr/bin/env python3

import re
import os
import sys
import requests
from parsel import Selector

if len(sys.argv) != 2:
    print ('Parameter: url, e.g.: http://localhost')
    sys.exit(-1)

all_php = {}
baseurl = sys.argv[1]
response = requests.get(baseurl)
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
href_links.append(baseurl)

for url in href_links:
    if url[:4] != 'http':
        url = baseurl + '/' + url
    if url[:len(baseurl)] == baseurl:
        print ('#debug: ', url)
        sqlmapres = os.popen("sqlmap --batch --forms --level=3 -u '%s'"%(url)).read()
        if re.search("Parameter: ", sqlmapres):
            print(url, "(or follower) is vulnerable with sql injection")
