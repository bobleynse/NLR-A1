import matplotlib.pyplot as plt
import PIL
from PIL import Image
import numpy as np
from tifffile import imread, imsave

PIL.Image.MAX_IMAGE_PIXELS = 725050001

# roadmap =  Image.open('top10nl_wegvlak_amersfoort.tif')
# roadmap = np.array(roadmap)

# print(len(roadmap))

xmin = 0
ymin = 0

xmax = 25000
ymax = 25000

# print(roadmap)

# function to write a tif file in a specified region
def convertToBlack(roadmap, xmin, xmax, ymin, ymax):

    slicedRoadmap = roadmap[xmin:xmax, ymin:ymax]

    print()
    for row in range(len(slicedRoadmap)):
        # time indication
        if (row % 25) == 0:
            print(round(row / (xmax - xmin) * 100, 1), '%')
        for col in range(len(slicedRoadmap[row])):
            if slicedRoadmap[row][col] == 255:
                slicedRoadmap[row][col] = 0
            else:
                slicedRoadmap[row][col] = 255

    imsave('x={}-{}_y={}-{}.tif'.format(xmin,xmax,ymin,ymax), slicedRoadmap)

# convertToBlack(roadmap, xmin, xmax, ymin, ymax)

# slice the full BlackRoadmap

roadmap =  Image.open('x=0-25000_y=0-25000.tif')
roadmap = np.array(roadmap)


stepsize = 2500
xtiles = 10
ytiles = 10


for y in range(0, ytiles * stepsize, stepsize):
    for x in range(0, xtiles * stepsize, stepsize):
        slicedRoadmap = roadmap[x:(x + stepsize), y:(y + stepsize)]
        imsave('x={}-{}_y={}-{}.tif'.format(y , (y + stepsize), x , (x + stepsize)), slicedRoadmap)
