# -*- coding: cp950 -*-
import httplib
import json
import sys, locale

def GetRoutId(routeName):
    routeId = ""
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
                routeId = route['Id']
    return routeId

def GetStopId(routeId, stopName):
    stopId = ""
    conn = httplib.HTTPConnection("data.ntpc.gov.tw")
    qryString = "/od/data/api/62519D6B-9B6D-43E1-BFD7-D66007005E6F?$format=json&$filter=routeId%20eq%20" + routeId
    #print qryString.encode('utf8')

    conn.request("GET",qryString)
    response = conn.getresponse()
    #print response.status, response.reason

    data = response.read()
    #print len(data)

    if len(data) > 100:
        jAllStops = json.loads(data)

    for stop in jAllStops:
        if stop['nameZh'] == stopName:
            stopId = stop['Id']

    return stopId

def GetStopETA(routeId, stopId):
    stopETA = ""
    conn = httplib.HTTPConnection("data.ntpc.gov.tw")
    qryString = "/od/data/api/245793DB-0958-4C10-8D63-E7FA0D39207C?$format=json&$filter=RouteID%20eq%20" + routeId
    #print qryString.encode('utf8')

    conn.request("GET",qryString)
    response = conn.getresponse()
    #print response.status, response.reason

    data = response.read()
    #print len(data)

    if len(data) > 100:
        jBusArrival = json.loads(data)

        for route in jBusArrival:
            if route['StopID'] == stopId:
                if( route['EstimateTime'] == "-1" ):
                    stopETA = "尚未發車"
                elif( route['EstimateTime'] == "-2" ):
                    stopETA = "交管不停靠"                
                elif( route['EstimateTime'] == "-3" ):
                    stopETA = "末班車已過"
                elif( route['EstimateTime'] == "-4" ):
                    stopETA = "今日未營運"                
                else:
                    goBack = ""
                    stopETA = route['EstimateTime']

                    if route['GoBack'] == "0":
                        goBack = u" (去程)"
                    elif route['GoBack'] == "1":
                        goBack = u" (返程)"
                    stopETA = stopETA + " sec" + goBack

    return stopETA

routeName = raw_input("路線: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",routeName,"]"
stopName = raw_input("站牌: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#print "Echo [",stopName,"]"

routeId = GetRoutId(routeName)
stopId = GetStopId(routeId, stopName)
stopETA = GetStopETA(routeId, stopId)
print routeId, stopId
print stopETA
