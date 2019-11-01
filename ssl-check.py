#!/usr/bin/env python3

import os
import re
import sys

# git clone https://github.com/drwetter/testssl.sh

URL = sys.argv[1]

print ("A TLS vizsgálat ideje körülbelül 2 perc ...")

for s in os.popen("testssl.sh/testssl.sh --quiet "+URL, "r").readlines():
    if "\x1b" in s and ( re.search("0;31m", s) or re.search("1;33m", s) ):
        print ("--->", s.rstrip())
