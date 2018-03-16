import gdal
from osgeo import gdal

#open existing dataset
src_ds = gdal.Open(r'E:\ArcGIS_Tutor_data\ArcTutor\Raster\Data\Amberg_tif\test\090160.tif',gdal.GA_ReadOnly)

if src_ds:
    #Open output format driver
    format = "GRIB"
    driver = gdal.GetDriverByName( format)
    #set the output to new format
    output= gdal.Translate(r"E:\ArcGIS_Tutor_data\ArcTutor\Raster\Data\Amberg_tif\output.grib2",src_ds)
    #Properly close the datasets to flush to disk
    dst_ds = None
    src_ds = None







