from osgeo import gdal
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import sys

def accuracycalc(inptif, jpgoutput):
    #load and slice to match jpeg
    roadmap = gdal.Open(inptif)
    roadmap_array = roadmap.ReadAsArray()
    roadmap_array = roadmap_array[2:-2,2:-2]

    output_array = plt.imread(jpgoutput)
    width = output_array.shape[0]
    
    goodclass = 0
    
    for i in range(width):
        for j in range(width):
            sum = np.absolute(roadmap_array[i][j] - (output_array[i][j][0]))
    #         print(sum)
            if sum < 50: 
                goodclass += 1
    print('correct pixel classification is : {0:.2f}'.format((goodclass/width**2)))

accuracycalc(sys.argv[1], sys.argv[2])