#!/usr/bin/env python3

import re
import os
import sys

# git clone https://github.com/s0md3v/XSStrike
# ./xss-check-autoparam.py http://szerver.lan/vuln-examples/xss.php

for url in sys.argv[1:]:
    pars = []
    plines = os.popen("python3 XSStrike/xsstrike.py -u '%s' --params"%(url), "r").readlines()
    for p in plines:
        if re.search("Heuristics found a potentially valid parameter:", p):
            pars.append(p.split(':')[1].split(' ')[1][5:-5])
    print ("Vizsgált GET paraméterek:", pars)

    for p in pars:
        url_w_param = "%s?%s="%(url, p)
        xss = os.popen("echo | python3 XSStrike/xsstrike.py -u '%s'"%(url_w_param), "r").read()
        #print (xss) # debug
        if re.search("Reflections found:", xss) or re.search("Potentially vulnerable objects found", xss):
            print(url_w_param, " is vulnerable with XSS")
