# -*- coding: cp950 -*-
import httplib
import json
import sys, locale

def GetRoutId(routeName):
    routeId = ""
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

    return routeId

def GetStopId(routeId, stopName):
    stopId = ""
    conn = httplib.HTTPConnection("data.ntpc.gov.tw")
    qryString = "/od/data/api/62519D6B-9B6D-43E1-BFD7-D66007005E6F?$format=json&$filter=routeId%20eq%20" + routeId + "%20and%20nameZh%20eq%20" + stopName

    conn.request("GET",qryString.encode('utf8'))
    response = conn.getresponse()
    #print response.status, response.reason

    data = response.read()
    #print len(data)

    if len(data) > 30:
        jBusStops = json.loads(data)

        stopId = jBusStops[0]['Id']

    return stopId

def GetStopETA(routeId, stopId):
    stopETA = ""
    conn = httplib.HTTPConnection("data.ntpc.gov.tw")
    qryString = "/od/data/api/245793DB-0958-4C10-8D63-E7FA0D39207C?$format=json&$filter=RouteID%20eq%20" + routeId + "%20and%20StopID%20eq%20" + stopId
    #print qryString.encode('utf8')

    conn.request("GET",qryString)
    response = conn.getresponse()
    #print response.status, response.reason

    data = response.read()
    #print len(data)

    if len(data) > 30:
        jBusArrival = json.loads(data)

        #print jBusArrival[0]['StopID'], jBusArrival[0]['GoBack'], jBusArrival[0]['EstimateTime']

        if( jBusArrival[0]['EstimateTime'] == "-1" ):
            stopETA = u"尚未發車"
        elif( jBusArrival[0]['EstimateTime'] == "-2" ):
            stopETA = u"交管不停靠"                
        elif( jBusArrival[0]['EstimateTime'] == "-3" ):
            stopETA = u"末班車已過"
        elif( jBusArrival[0]['EstimateTime'] == "-4" ):
            stopETA = u"今日未營運"                
        else:
            goBack = ""
            stopETA = jBusArrival[0]['EstimateTime']

            if jBusArrival[0]['GoBack'] == "0":
                goBack = u" (去程)"
            elif jBusArrival[0]['GoBack'] == "1":
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
#print routeId, stopId
print stopETA
