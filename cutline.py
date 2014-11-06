# Drop this .py script into the folder that contains the GeoPDFs to be converted. 

from osgeo import gdal
import os
import sys

ds = gdal.Open(sys.argv[1])
neatline_wkt = ds.GetMetadataItem("NEATLINE")
ds = None

f = open('cutline.csv', 'wt')
f.write('id,WKT\n')
f.write('1,"%s"\n' % neatline_wkt)
f.close()

os.system('gdalwarp %s %s.tif ' % (sys.argv[1], sys.argv[1]) + '-crop_to_cutline -cutline cutline.csv -overwrite')
