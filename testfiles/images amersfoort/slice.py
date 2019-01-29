import matplotlib.pyplot as plt
import PIL
from PIL import Image
import numpy as np
from tifffile import imread, imsave

PIL.Image.MAX_IMAGE_PIXELS = 725050001

# 255: Background (default)
#  17: Highway
#  34: Main road
#  51: Regional road
#  68: Local road
#  85: Street

# function to write a tif file in a specified region
def convertToBlack(roadmap, xmin, xmax, ymin, ymax):

    slicedRoadmap = roadmap[xmin:xmax, ymin:ymax]
    
    slicedRoadmap[slicedRoadmap == 255] = 0
    slicedRoadmap[slicedRoadmap > 85] = 0
    slicedRoadmap[slicedRoadmap > 0] = 255
    return slicedRoadmap
    # imsave('x={}-{}_y={}-{}.tif'.format(xmin,xmax,ymin,ymax), slicedRoadmap)

# slice the full BlackRoadmap

roadmap =  Image.open('top10nl_wegvlak_amersfoort.tif')
roadmap = np.array(roadmap)
print(roadmap)
print(np.unique(roadmap))


xmin = 0
ymin = 0

xmax = 25000
ymax = 25000

stepsize = 2500
xtiles = 10
ytiles = 10


for y in range(0, ytiles * stepsize, stepsize):
    for x in range(0, xtiles * stepsize, stepsize):
        slicedRoadmap = roadmap[x:(x + stepsize), y:(y + stepsize)]
        slicedRoadmap = convertToBlack(slicedRoadmap, xmin, xmax, ymin, ymax)
        imsave('roadmap_2500_6-classes/x={}-{}_y={}-{}.tif'.format(y , (y + stepsize), x , (x + stepsize)), slicedRoadmap)
