#!/usr/bin/env python3

import sys
import http.client

URL = sys.argv[1]

if URL[:8].lower() == 'https://':
    conn = http.client.HTTPSConnection(URL[8:])
elif URL[:7].lower() == 'http://':
    conn = http.client.HTTPSConnection(URL[7:])
else:
    print ("Usage:", sys.argv[0], "https://www.myserver.hu")
    sys.exit(1)

conn.request("GET", "/")
resp = conn.getresponse()

#print (resp.getheaders())    # debug
if not resp.getheader("Strict-Transport-Security"): print ("Missing hdr: Strict-Transport-Security")
if not resp.getheader("X-XSS-Protection"): print ("Missing hdr: X-XSS-Protection")
if not resp.getheader("X-Content-Type-Options"): print ("Missing hdr: X-Content-Type-Options")
if not resp.getheader("Content-Security-Policy"): print ("Missing hdr: Content-Security-Policy")
if not resp.getheader("X-Frame-Options"): print ("Missing hdr: X-Frame-Options")
