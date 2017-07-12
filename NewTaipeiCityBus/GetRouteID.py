# -*- coding: cp950 -*-
import httplib
import json
import sys, locale

routeName = raw_input("路線: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",routeName,"]"

conn = httplib.HTTPConnection("data.ntpc.gov.tw")
qryString = "/od/data/api/67BB3C2B-E7D1-43A7-B872-61B2F082E11B?$format=json&$filter=nameZh%20eq%20" + routeName

conn.request("GET",qryString.encode('utf8'))
response = conn.getresponse()
#print response.status, response.reason

data = response.read()
#print len(data)

if len(data) > 30:
    jBusRoutes = json.loads(data)

    routeId = jBusRoutes[0]['Id']
    print "RouteId:", routeId
    
else:
    print "Not found"
