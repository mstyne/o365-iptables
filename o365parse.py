#!/usr/bin/env python

import httplib
import xml.etree.ElementTree as ET
import pprint
import sys

host = 'support.content.office.net'

url = '/en-us/static/O365IPAddresses.xml'

conn = httplib.HTTPSConnection(host)

try:
    conn.request('GET', url)
except:
    print "Couldn't query support.content.office.net! Sorry!\n"
    sys.exit()

try:
    response = conn.getresponse()
except:
    print "Couldn't get a response from support.content.office.net! Sorry!\n"
    sys.exit()

result = response.read()

try:
    tree = ET.fromstring(result)
except:
    print "Couldn't parse XML from support.content.office.net! Sorry!\n"
    sys.exit()

for address in tree.findall(".//*[@name='o365']/*[@type='IPv4']/address"):
    print '-A O365_INPUT -s ' + address.text + ' -p tcp -m tcp --dport 25 -m state --state NEW -j ACCEPT'

