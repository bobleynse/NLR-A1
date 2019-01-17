from osgeo import gdal
import numpy as np

file_in = './amersfoort_9band.tif'
file_out = './amersfoort_test.tif'

tile = gdal.Open(file_in)

print ("[ RASTER BAND COUNT ]: ", tile.RasterCount)

for band in range( tile.RasterCount ):
    band += 1
    print ("[ GETTING BAND ]: ", band)
    srcband = tile.GetRasterBand(band)
    if srcband is None:
        continue

    stats = srcband.GetStatistics( True, True )
    if stats is None:
        continue

    print ("[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
                stats[0], stats[1], stats[2], stats[3] ) )


myarray = np.array(tile.ReadAsArray())
print(myarray.shape)  # (num_bands, y_size, x_size)


# Create tif image (but only 3 bands in order 3-2-1)
# with the same metadata (projection and geotransform) as reference
driver = gdal.GetDriverByName("GTiff")
band = tile.GetRasterBand(1)
arr = band.ReadAsArray()
[cols, rows] = arr.shape

out_data = driver.Create(file_out, xsize=rows, ysize=cols, bands=1, eType=gdal.GDT_UInt16, options=['COMPRESS=LZW'])
out_data.SetGeoTransform(tile.GetGeoTransform())  # sets same geotransform as input
out_data.SetProjection(tile.GetProjection())  # sets same projection as input
out_data.GetRasterBand(1).WriteArray(myarray[2,:,:])
out_data.FlushCache()  # saves to disk!!
