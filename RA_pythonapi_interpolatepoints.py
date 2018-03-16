import arcgis
from arcgis.gis import GIS
from arcgis.raster.analytics import interpolate_points


gis = GIS("https://myportal/webadaptor", "username", "password",verify_cert=False)

print("Logged in as: " + gis.properties.user.username)

#check if GA is supported in portal
print (arcgis.raster.analytics.is_supported(gis))

arcgis.env.process_spatial_reference=4326


input_point_features  = "https://myserver/webadaptorname/rest/services/Hosted/2016012501/FeatureServer/0"
outputCellSize   = {"distance":1,"units":"Kilometers"}

#execute RA interpolatepoints               
copy_result= interpolate_points(input_point_features,  interpolate_field="col_14",optimize_for='BALANCE', transform_data=False,
                                size_of_local_models=None, number_of_neighbors=None, output_cell_size=outputCellSize, output_prediction_error=False,
                                output_name="2016012501_P")
