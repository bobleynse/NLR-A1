from os import listdir
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
from datetime import datetime

def dilute(tile, step):
    dilutedTile = np.array(Image.open( "input-roadmap/{}".format(tile)))

    # check if the roadmap is valid
    if len(np.unique(dilutedTile)) > 2:
        print('A multi-road dilutor has not been build yet')
        sys.exit()

    # declare variables
    shape = np.shape(dilutedTile)
    rectSize = 5
    rectBuf = (rectSize // 2)

    # rows
    for row in range(shape[0] - (rectBuf + 1)):
        for col in range(shape[1]):
            # rows top
            if dilutedTile[row, col] == 0 and dilutedTile[row + 1, col] == 255:
                for i in range(rectBuf):
                    dilutedTile[row + i + 1, col] = 180
            # rows bottom
            if dilutedTile[row, col] == 255 and dilutedTile[row + 1, col] == 0:
                for i in range(rectBuf):
                    dilutedTile[row + (i * -1), col] = 180
                    
    # columns
    for row in range(shape[0]):
        for col in range(shape[1] - (rectBuf + 1)):
            # colums top
            if dilutedTile[row, col] == 0 and dilutedTile[row, col + 1] > 175:
                for i in range(rectBuf):
                    dilutedTile[row, col + i + 1] = 100
            # colums bottom
            if dilutedTile[row, col] > 175 and dilutedTile[row, col+ 1] == 0:
                for i in range(rectBuf):
                    dilutedTile[row, col + (i * -1)] = 100

    # remove the marked pixels
    dilutedTile[dilutedTile == 100] = 0
    dilutedTile[dilutedTile == 180] = 0

    # save
    print(str(datetime.now()) + ': Saving tif')
    out_img = Image.fromarray(dilutedTile)
    out_img.save('output-roadmap/{}'.format(tile))

# open tile as np array
print(str(datetime.now()) + ': Import {} roadmap(s)'.format(len(listdir('input-roadmap'))))


for i in range(len(listdir('input-roadmap'))):
    print(str(datetime.now()) + ': Diluting roadmap {}'.format(i + 1))
    dilute(listdir('input-roadmap')[i], i)


            
print(str(datetime.now()) + ': Done:')
