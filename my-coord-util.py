import os
from convertbng.util import convert_bng, convert_lonlat  
import json
import urllib
import urllib.request

#I experimented with some public free in cost libraries for doing conversions from BNG to long/lat coordinated.

# This is the code the program from OS (GridInQuestII-Lin64-0101a) publicly available and free to use.
cmd = """./giqtrans --CGI='SourceSRID=27700&TargetSRID=4937&PreferredDatum=13&Geometry={"type":"Point","coordinates":[586500,245739,0]}'"""
#call = os.system("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'")
call = os.system(cmd)
print(call)

#an alternative
#this one works
#>>> from bng_to_latlon import OSGB36toWGS84
#>>> OSGB36toWGS84(538890, 177320)
#(51.47779538331092, -0.0014016837826672265)


#convertbng does not appear to work, throws error under basic usage.
#u = convert_bng(0.72021186399521286, 52.078605644194084)
#nor = []
#nor.append(586500)
#nor.append(586500)
#eas = []
#eas.append(245739)
#eas.append(245739)
#r = convert_lonlat(eas,nor)


#this uses a public webservice for the conversion and is very convinient
url = "https://www.bgs.ac.uk/data/webservices/CoordConvert_LL_BNG.cfc?method=BNGtoLatLng&easting=586500&northing=245739"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
data = response.read()
values = json.loads(data)
print(values)
