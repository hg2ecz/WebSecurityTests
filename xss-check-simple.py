#!/usr/bin/env python3

import re
import os
import sys

# git clone https://github.com/s0md3v/XSStrike
# ./xss-check-simple.py http://szerver.lan/vuln-examples/xss.php?neve=

for url_w_param in sys.argv[1:]:
    xss = os.popen("echo | python3 XSStrike/xsstrike.py -u '%s'"%(url_w_param)).read()
    #print (xss) # debug
    if len(xss) == 0:
        print ("System error")
    elif re.search("Reflections found:", xss) or re.search("Potentially vulnerable objects found", xss):
        print(url_w_param, " is vulnerable with XSS")
