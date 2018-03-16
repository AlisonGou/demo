from arcgis.gis import GIS
import arcgis.geoanalytics
from arcgis.geoanalytics.manage_data import copy_to_data_store

#login in portal
gis = GIS("https://myportal/webadaptorname", "usrname", "password",verify_cert=False)

print("Logged in as: " + gis.properties.user.username)

#check if geoanalytics is supported in your portal
print (arcgis.geoanalytics.is_supported())

#use keywords to filter to get results
search_result = gis.content.search("keywords", item_type = "big data file share")

inputlayer =  search_result[0].layers[0]

#execute GA copytodatastore
copy_result= copy_to_data_store(inputlayer, output_name="test01")
