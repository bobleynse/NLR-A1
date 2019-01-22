from datetime import datetime
from PIL import Image
import sys
import numpy as np
import tensorflow as tf

# check if the input is correct
if(len(sys.argv) != 4):
	raise Exception('invalid command line arguments')

# create an output image
totalOutputImage = Image.new('RGB', (2496,2496))

rectSize = 5
# the amount of parts you devide the input images in, when you don't devide your input can get to big (tensor proto error)
parts = 4
partSize = 2500 / parts

# adjust the neural network, make sure you use the same model as in train.py
hiddenUnits = [110, 100, 75, 50]
classes = 2


print(str(datetime.now()) + ': initializing model...')
featureColumns = [tf.contrib.layers.real_valued_column("", dimension=rectSize*rectSize*4)]

# specify which trained model you want to use
classifier = tf.contrib.learn.DNNClassifier(feature_columns = featureColumns,
												hidden_units = hiddenUnits,
												n_classes = classes,
												model_dir = 'models/modelNIR_22-01')

def extractFeatures():
    features = np.zeros((((inputImageXSize - ((rectSize//2)*2)) * (inputImageYSize - ((rectSize//2)*2))), rectSize*rectSize*4), dtype=np.int)
    rowIndex = 0
    print(np.shape(features))
    
    for x in range(rectSize//2, inputImageXSize - (rectSize//2)):
        if x % 200 == 0:
            print('Progress: {}%'.format(round(x / inputImageXSize * 100, 1)))
        for y in range(rectSize//2, inputImageYSize - (rectSize//2)):            
            rect = (x - (rectSize//2), y - (rectSize//2), x + (rectSize//2) + 1, y + (rectSize//2) + 1)
            subImage = inputImage.crop(rect).load()
            subNIR = inputNIR.crop(rect).load()
            
            colIndex = 0
            for i in range(rectSize):
                for j in range(rectSize):
                    features[rowIndex, colIndex] = subImage[i, j][0]
                    colIndex += 1
                    features[rowIndex, colIndex] = subImage[i, j][1]
                    colIndex += 1
                    features[rowIndex, colIndex] = subImage[i, j][2]
                    colIndex += 1
                    # NIR
                    features[rowIndex, colIndex] = subNIR[i, j]
                    colIndex += 1
            rowIndex += 1

    return features
    
def constructOutputImage(predictions):
    outputImagePixels = outputImage.load()
    rowIndex = 0
    for x in range(outputImageXSize):
        for y in range(outputImageYSize):
            outputImagePixels[x, y] = ((255, 255, 255) if predictions[rowIndex] else (0, 0, 0))
            rowIndex += 1

# classify        
for i in range(parts):
    print(str(datetime.now()) + ": initializing input data part {} of {}".format(i + 1, parts))
    # Devide the input images
    inputImagePath = 'image-input'
    inputImageFile = sys.argv[1]
    inputImage = Image.open(inputImagePath + '/' + inputImageFile)
    XSize, YSize = inputImage.size

    # devide in x parts
    if i == 0:
        partYstart = i * partSize
        partYend = partSize + i * partSize + (rectSize//2)
    if i < parts and i > 0:
        partYstart = i * partSize - (rectSize//2)
        partYend = partSize + i * partSize + (rectSize//2)
    else:
        partYstart = i * partSize
        partYend = partSize + i * partSize


    inputImage = inputImage.crop((0, partYstart , 2500, partYend))
    inputImageXSize, inputImageYSize = inputImage.size

    inputNIRPath = 'NIR-input'
    inputNIRFile = sys.argv[2]
    inputNIR = Image.open(inputNIRPath + '/' + inputNIRFile)
    inputNIR = inputNIR.crop((0, partYstart , 2500, partYend))
    inputNIRXSize, inputNIRYSize = inputNIR.size

    outputImagePath = 'image-output'
    outputImageFile = sys.argv[3]
    outputImage = inputImage.crop((rectSize//2, rectSize//2, inputImageXSize - (rectSize//2), inputImageYSize - (rectSize//2)))
    outputImageXSize, outputImageYSize = outputImage.size

    # start the classifier
    print(str(datetime.now()) + ': processing image', inputImageFile)
    predictions = list(classifier.predict(input_fn=extractFeatures))

    print(str(datetime.now()) + ': constructing output image...')
    constructOutputImage(predictions)

    print(str(datetime.now()) + ': saving output image...')
    outputImage.save(outputImagePath + '/' + '{}_'.format(i) + outputImageFile.format(i), 'JPEG')

    # append to the output image
    totalOutputImage.paste(outputImage, (0, int(i * (partSize - rectSize//2))))

    # append in parts
    if i == 0:
        totalOutputImage.paste(outputImage, (0, 0))
        partYstart = i * partSize
        partYend = partSize + i * partSize + (rectSize//2)
    if i > 0:
        totalOutputImage.paste(outputImage, (0, int(i * partSize - (rectSize//2))))

totalOutputImage.save(outputImagePath + '/' + outputImageFile, 'JPEG')
print(str(datetime.now()) + ': done')