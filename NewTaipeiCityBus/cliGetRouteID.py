import sys, getopt
import sys, locale
import httplib
import json

#sys.argv = [sys.argv[0], '--id=275', '--ofile=275.json']

def getRouteId(routeName, out_filename):
    conn = httplib.HTTPConnection("data.ntpc.gov.tw")
    qryString = "/od/data/api/67BB3C2B-E7D1-43A7-B872-61B2F082E11B?$format=json&$filter=nameZh%20eq%20" + routeName
    conn.request("GET",qryString.encode('utf8'))
    response = conn.getresponse()
    print response.status, response.reason

    data = response.read()
    print len(data)

    ofile = open(out_filename, "w")
    ofile.write(data)
    ofile.close()
    
def main(argv):
   route_id = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["id=","ofile="])
   except getopt.GetoptError:
      print 'cliGetRouteID.py -i <route id> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'cliGetRouteID.py -i <route id> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--id"):
         route_id = arg         
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   getRouteId(route_id, outputfile)
   print 'Route ID is', route_id
   print 'Output file is', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
