#!/usr/bin/env python3

import re
import sys
import urllib.request
import html.parser

def check_wordpress(ver):
    print ('--> WordPress version:', ver)
    print ('URL: https://www.cvedetails.com/vulnerability-list/vendor_id-2337/Wordpress.html')

def check_drupal(ver):
    print ('--> Drupal version:', ver)
    print ('URL: https://www.cvedetails.com/vulnerability-list/vendor_id-1367/Drupal.html')

def check_mediawiki(ver):
    print ('--> MediaWiki version:', ver)
    print ('URL: https://www.cvedetails.com/vulnerability-list/vendor_id-2360/Mediawiki.html')

def check_joomla(ver):
    print ('--> Joomla! without web-readable version. Please check root → libraries → joomla → version.php.')
    print ('URL: https://www.cvedetails.com/vulnerability-list/vendor_id-3496/Joomla.html')

# <a href="http://www.simpleportal.net/" target="_blank" class="new_win">SimplePortal 2.3.5 &copy; 2008-2012, SimplePortal</a>
def check_simpleportal(html):
    generators = re.findall(">SimplePortal ([0-9.]*)", html)
    for gen in generators:
        print ('--> SimplePortal:', gen)
        print ('URL: https://www.cvedetails.com/vulnerability-list/vendor_id-2069/product_id-3598/Simple-Machines-SMF.html')

def check_web(html):
    generators = re.findall("name=\"[gG]enerator\" content=\"([^\"]*)\"", html)
    for gen in generators:
        gf = gen.split()
        ver = ''
        if len(gf) > 1:
            ver = gf[1]
        if gf[0] == 'WordPress':
            check_wordpress(ver)
        elif gf[0] == 'Drupal':
            check_drupal(ver)
        elif gf[0] == 'MediaWiki':
            check_mediawiki(ver)
        elif gf[0] == 'Joomla!':
            check_joomla(ver)
        else:
            print ('Unknown/unhandled generator:', gf)
    if len(generators) == 0:
        check_simpleportal(html)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Requered arguments: urls')
        sys.exit(1)
    for url in sys.argv[1:]:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            html = response.read().decode('utf-8')
            check_web(html)

