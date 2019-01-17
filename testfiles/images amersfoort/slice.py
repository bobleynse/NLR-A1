import matplotlib.pyplot as plt
import PIL
from PIL import Image
import numpy as np
from tifffile import imread, imsave

PIL.Image.MAX_IMAGE_PIXELS = 725050001

im =  Image.open('top10nl_wegvlak_amersfoort.tif')

xmin = 2500
ymin = 0

xmax = 5000
ymax = 2500

sliced = np.array(im)
sliced = sliced[xmin:xmax, ymin:ymax]
print(sliced)

for row in range(len(sliced)):
    # time indication
    if (row % 25) == 0:
        print(round(row / (xmax - xmin) * 100), '%')
    for col in range(len(sliced[row])):
        if sliced[row][col] == 255:
            sliced[row][col] = 0
        else:
            sliced[row][col] = 255

imsave('x={}-{}_y={}-{}.tif'.format(xmin,xmax,ymin,ymax), sliced)
