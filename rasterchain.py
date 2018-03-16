import arcgis
from arcgis.gis import GIS
from arcgis.raster.functions import mask,clip,colormap,stretch
import urllib.request
import urllib.parse
import ssl
import json

#getting token
portal = 'https://myportal'
username = 'username' 
password = 'password'
clientip = 'client IP from which sends the request'
parameter = ({'username':username, 'password':password,'referer':clientip,'f':'json'})
params = urllib.parse.urlencode(parameter).encode('utf-8')
request = portal +  '/webadaptorname/sharing/rest/generateToken'
ssl._create_default_https_context = ssl._create_unverified_context
with urllib.request.urlopen(request, params) as url:
    subrequest = url.read()
    response = json.loads(subrequest.decode('utf-8'))
    print (response)
if "token" in response:
    token = response["token"]
    print (token)

#query layer to get geometry from a desired service
inputlayer = "https://myserver/webadaptorname/rest/services/myservice/MapServer/0/query"
queryparam = "1=1"
inputdata = ({'Where':queryparam,'f':'json','token':token})

params = urllib.parse.urlencode(inputdata).encode("utf-8")

with urllib.request.urlopen(inputlayer,params) as url:
    submitResponse = url.read()
    submitjson = json.loads(submitResponse.decode('utf-8'))

if 'features' in submitjson:
    print ('keep going')
    geo = submitjson['features'][0]['geometry']
    
#the raster chain starts here
#login portal
gis = GIS("https://myportal/webadaptorname", "username", "password",verify_cert=False)  
#get the imagery layer
imagery_item = gis.content.search('imageName','Imagery Layer',outside_org=False)[0]
input_image  = imagery_item.layers[0]
print (input_image)

#start to stretch
stretchrelt = stretch(input_image,stretch_type='MinMax')

#start to render
print('start to render')
colorrelt = colormap(stretchrelt,colorramp='Prediction',astype='u8')

#start to clip
print('start to clip')

clipre = clip(colorrelt,geo,clip_outside=False,astype='u8')

maskrelt = mask(clipre,no_data_values=None, included_ranges=[minvalue,maxvalue],no_data_interpretation=None,astype='f32')

print ('start to save the result as an image layer')
layer = maskrelt.save('result_name',for_viz=False)


