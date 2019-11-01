#!/usr/bin/env python3

import re
import os
import sys

# git clone https://github.com/s0md3v/XSStrike
# ./xss-check-autoparam.py "" http://szerver.lan/vuln-examples/xss.php
# ./xss-check-autoparam.py "id;name;age" http://szerver.lan/vuln-examples/xss.php

init_pars = sys.argv[1].split(";")

for url in sys.argv[2:]:
    pars = init_pars
    plines = os.popen("python3 XSStrike/xsstrike.py -u '%s' --params"%(url)).readlines()
    for p in plines:
        if re.search("Heuristics found a potentially valid parameter:", p):
            pars.append(p.split(':')[1].split(' ')[1][5:-5])

    par_set = set()
    for p in pars:
        if p == '': continue
        par_set.add(p)

    print ("Vizsgált GET paraméterek:", par_set)
    for p in par_set:
        url_w_param = "%s?%s="%(url, p)
        xss = os.popen("echo | python3 XSStrike/xsstrike.py -u '%s'"%(url_w_param)).read()
        #print (xss) # debug
        if re.search("Reflections found:", xss) or \
           re.search("Potentially vulnerable objects found", xss):
            print(url_w_param, " is vulnerable with XSS")
