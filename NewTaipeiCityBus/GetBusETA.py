# -*- coding: cp950 -*-
import httplib
import json
import sys, locale

routeID = raw_input("RouteID: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",routeID,"]"

stopID = raw_input("StopID: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",stopID,"]"

conn = httplib.HTTPConnection("data.ntpc.gov.tw")

qryString = "/od/data/api/245793DB-0958-4C10-8D63-E7FA0D39207C?$format=json&$filter=RouteID%20eq%20" + routeID
print qryString.encode('utf8')

conn.request("GET",qryString)
response = conn.getresponse()
#print response.status, response.reason

data = response.read()
print len(data)

if len(data) > 100:
    jBusArrival = json.loads(data)

    for route in jBusArrival:
        if route['StopID'] == stopID:
            if( route['EstimateTime'] == "-1" ):
                print "�|���o��"
            elif( route['EstimateTime'] == "-2" ):
                print "��ޤ����a"                
            elif( route['EstimateTime'] == "-3" ):
                print "���Z���w�L"
            elif( route['EstimateTime'] == "-4" ):
                print "���饼��B"                
            else:
                print "�쯸�Ѿl�ɶ�:",route['EstimateTime']
else:
    print "Not found"
