# -*- coding: cp950 -*-
import httplib
import json
import sys, locale

routeName = raw_input("路線: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",routeName,"]"

conn = httplib.HTTPConnection("data.ntpc.gov.tw")
qryString = "/od/data/api/67BB3C2B-E7D1-43A7-B872-61B2F082E11B?$format=json&$filter=nameZh%20eq%20" + routeName
#print qryString.encode('utf8')

conn.request("GET",qryString)
response = conn.getresponse()
#print response.status, response.reason

data = response.read()
#print len(data)

if len(data) > 100:
    jBusRoutes = json.loads(data)

    for route in jBusRoutes:
        if route['nameZh'] == routeName:
            print "RouteId:", route['Id']
else:
    print "Not found"
