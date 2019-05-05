#!/usr/bin/env python3

import re
import os
import sys
import urllib.request

for url in sys.argv[1:]:
    sqlmapres = os.popen("sqlmap --batch --forms --level=3 -u '%s'"%(url)).read()
    if re.search("Parameter: ", sqlmapres):
        print(url, "(or follower) is vulnerable with sql injection")
