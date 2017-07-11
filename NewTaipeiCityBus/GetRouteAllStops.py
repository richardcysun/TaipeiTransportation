# -*- coding: cp950 -*-
import httplib
import json
import sys, locale

routeID = raw_input("RouteID: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",routeID,"]"

conn = httplib.HTTPConnection("data.ntpc.gov.tw")
qryString = "/od/data/api/62519D6B-9B6D-43E1-BFD7-D66007005E6F?$format=json&$filter=routeId%20eq%20" + routeID
print qryString.encode('utf8')

conn.request("GET",qryString)
response = conn.getresponse()
#print response.status, response.reason

data = response.read()
#print len(data)

if len(data) > 100:
    jAllStops = json.loads(data)

    for stop in jAllStops:
        print "站牌:",stop['nameZh'], "Id:", stop['Id']
else:
    print "Not found"

