import random
from os import listdir
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from datetime import datetime

# Saving path of every image.
trainInputImagesPath = 'segmentation-dataset/train-input'
trainOutputImagesPath = 'segmentation-dataset/train-output'
testInputImagesPath = 'segmentation-dataset/test-input'
testOutputImagesPath = 'segmentation-dataset/test-output'
validInputImagesPath = 'segmentation-dataset/valid-input'
validOutputImagesPath = 'segmentation-dataset/valid-output'

trainInputImagesFiles = listdir(trainInputImagesPath)
trainOutputImagesFiles = listdir(trainOutputImagesPath)
testInputImagesFiles = listdir(testInputImagesPath)
testOutputImagesFiles = listdir(testOutputImagesPath)
#validInputImagesFiles = listdir(validInputImagesPath)
#validOutputImagesFiles = listdir(validOutputImagesPath)

# Checking if number of input and output images match.
print(str(datetime.now()) + ': trainInputImagesFiles:', len(trainInputImagesFiles))
print(str(datetime.now()) + ': trainOutputImagesFiles:',  len(trainOutputImagesFiles))
if(len(trainInputImagesFiles) != len(trainOutputImagesFiles)):
    raise Exception('train input images and output images number mismatch')

print(str(datetime.now()) + ': testInputImagesFiles:', len(testInputImagesFiles))
print(str(datetime.now()) + ': testOutputImagesFiles:', len(testOutputImagesFiles))
if(len(testInputImagesFiles) != len(testOutputImagesFiles)):
    raise Exception('test input images and output images number mismatch')

#print(str(datetime.now()) + ': validInputImagesFiles:', len(validInputImagesFiles))
#print(str(datetime.now()) + ': validOutputImagesFiles:', len(validOutputImagesFiles))
#if(len(validInputImagesFiles) != len(validOutputImagesFiles)):
#    raise Exception('valid input images and output images number mismatch')

for i in range(len(trainInputImagesFiles)):
    inputImageFile = trainInputImagesFiles[i]#[:-5]
    outputImageFile = trainOutputImagesFiles[i]#[:-4]
    if(inputImageFile != outputImageFile):
        raise Exception('train inputImageFile and outputImageFile mismatch at index', str(i))

for i in range(len(testInputImagesFiles)):
    inputImageFile = testInputImagesFiles[i]#[:-5]
    outputImageFile = testOutputImagesFiles[i]#[:-4]
    if(inputImageFile != outputImageFile):
        raise Exception('test inputImageFile and outputImageFile mismatch at index', str(i))
        
#for i in range(len(validInputImagesFiles)):
#    inputImageFile = validInputImagesFiles[i][:-5]
#    outputImageFile = validOutputImagesFiles[i][:-4]
#    if(inputImageFile != outputImageFile):
#        raise Exception('valid inputImageFile and outputImageFile mismatch at index', str(i))

print(str(datetime.now()) + ': input and output files check success')

# Older version of writeDataFile:
def writeDataFileOld(inputImagePath, outputImagePath, inputImageFiles, outputImageFiles, dataFileName):
    dataFile = open(dataFileName, 'w')
    roadPixel = 1
    nonroadPixel = 0
    neededPixel = 0
    
    rectSize = 7
    
    for i in range(len(inputImageFiles)):
        #if(i > 0):
        #    break
        
        print(str(datetime.now()) + ': prcessing image', i)
        inputImage = Image.open(inputImagePath + '/' + inputImageFiles[i])
        inputImageXSize, inputImageYSize = inputImage.size
        # inputImagePixels = inputImage.load()
        
        outputImage = Image.open(outputImagePath + '/' + outputImageFiles[i])
        outputImageXSize, outputImageYSize = outputImage.size
        outputImagePixels = outputImage.load()
        
        if((inputImageXSize != outputImageXSize) or (inputImageYSize != outputImageYSize)):
            raise Exception('train inputImage and outputImage mismatch at index', str(i))

        # This for loop assures that the algorithm only looks at pixel which have enough 
        # surrounding pixels (avoiding edges).
        for x in range(rectSize//2, inputImageXSize - (rectSize//2)):
            for y in range(rectSize//2, inputImageYSize - (rectSize//2)):
                isRoadPixel = outputImagePixels[x, y]
                if((isRoadPixel) and (neededPixel != roadPixel)):
                    continue
                
                if((not(isRoadPixel)) and (neededPixel == roadPixel)):
                    continue
                
                neededPixel = ((neededPixel+1)%3)
                rect = (x - (rectSize//2), y - (rectSize//2), x + (rectSize//2) + 1, y + (rectSize//2) + 1)
                subImage = inputImage.crop(rect).load()
                line = ''
                for i in range(rectSize):
                    for j in range(rectSize):
                        line += str(subImage[i, j][0]) + ','
                        line += str(subImage[i, j][1]) + ','
                        line += str(subImage[i, j][2]) + ','
                
                line += str(roadPixel if isRoadPixel else nonroadPixel) + '\n'
                dataFile.write(line)
    
# Modify the size of the pixel window in this function.
# Modify the amound to pixel lines in the .csv file in this function.
def writeDataFile(inputImagePath, outputImagePath, inputImageFiles, outputImageFiles, dataFileName):
    dataFile = open(dataFileName, 'w')
    rectSize = 5
    linesCount = 0
    linesLimit = 200000
    linesCountPerImage = 0
    linesLimitPerImage = (linesLimit / len(inputImageFiles)) + 1
    
    # Looping through all input files.
    for i in range(len(inputImageFiles)):
        print(str(datetime.now()) + ': prcessing image', i)
        linesCountPerImage = 0
        inputImage = Image.open(inputImagePath + '/' + inputImageFiles[i])
        inputImageXSize, inputImageYSize = inputImage.size
        # inputImagePixels = inputImage.load()
        
        # Selecting output image file.
        outputImage = Image.open(outputImagePath + '/' + outputImageFiles[i])
        outputImageXSize, outputImageYSize = outputImage.size
        outputImagePixels = outputImage.load()
        
        if((inputImageXSize != outputImageXSize) or (inputImageYSize != outputImageYSize)):
            raise Exception('train inputImage and outputImage mismatch at index', str(i))

        # Creating the pixel arrays in which roads and non-roads are collected.
        outputImageRoadPixelsArr = []
        outputImageNonRoadPixelsArr= []
        
        # This for loop assures that the algorithm only looks at pixel which have enough 
        # surrounding pixels (avoiding edges).
        # If there is a road in the output image, the pixel values of the input image are
        # appended to the corresponding array.
        for x in range(rectSize//2, inputImageXSize - (rectSize//2)):
            for y in range(rectSize//2, inputImageYSize - (rectSize//2)):
                isRoadPixel = outputImagePixels[x, y]
                if(isRoadPixel):
                    outputImageRoadPixelsArr.append((x, y))
                else:
                    outputImageNonRoadPixelsArr.append((x, y))

        # The pixel arrays are randomly shuffled, to get a random distribution of all the scanned images.
        random.shuffle(outputImageRoadPixelsArr)
        random.shuffle(outputImageNonRoadPixelsArr)
        

        for m in range(len(outputImageRoadPixelsArr)):
            if(linesCountPerImage >= linesLimitPerImage):
                break
            
            if(((m*2) + 1) >= len(outputImageNonRoadPixelsArr)):
                break
            
            # Select x and y coordinates from the output pixel arrays.
            x = outputImageRoadPixelsArr[m][0]
            y = outputImageRoadPixelsArr[m][1]
            
            # Cropping the input image according to rectSize to create a 'sub image'.
            rect = (x - (rectSize//2), y - (rectSize//2), x + (rectSize//2) + 1, y + (rectSize//2) + 1)
            subImage = inputImage.crop(rect).load()
            line = ''
            for i in range(rectSize):
                for j in range(rectSize):
                    line += str(subImage[i, j][0]) + ','
                    line += str(subImage[i, j][1]) + ','
                    line += str(subImage[i, j][2]) + ','
            
            # Going to next line.
            line += str(1) + '\n'
            linesCount += 1
            linesCountPerImage += 1
            dataFile.write(line)
            
            # Non-road pixels are written in the .csv here.
            for n in range(2):
                x = outputImageNonRoadPixelsArr[(m*2) + n][0]
                y = outputImageNonRoadPixelsArr[(m*2) + n][1]
                
                # Cropping input image.
                rect = (x - (rectSize//2), y - (rectSize//2), x + (rectSize//2) + 1, y + (rectSize//2) + 1)
                subImage = inputImage.crop(rect).load()
                line = ''
                for i in range(rectSize):
                    for j in range(rectSize):
                        line += str(subImage[i, j][0]) + ','
                        line += str(subImage[i, j][1]) + ','
                        line += str(subImage[i, j][2]) + ','
                
                # Going to next line.
                line += str(0) + '\n'
                linesCount += 1
                linesCountPerImage += 1
                dataFile.write(line)
    
    print(str(datetime.now()) + ': ' + dataFileName + ' linesCount:', linesCount)

# Creating .csv files.
trainDataFileName = 'segmentation-dataset/train.csv'
testDataFileName = 'segmentation-dataset/test.csv'
validDataFileName = 'segmentation-dataset/valid.csv'

# Writing pixel arrays into .csv files.
print(str(datetime.now()) + ': writing trainDataFile')
writeDataFile(trainInputImagesPath, trainOutputImagesPath, trainInputImagesFiles, trainOutputImagesFiles, trainDataFileName)
print(str(datetime.now()) + ': trainDataFile complete')

print(str(datetime.now()) + ': writing testDataFile')
writeDataFile(testInputImagesPath, testOutputImagesPath, testInputImagesFiles, testOutputImagesFiles, testDataFileName)
print(str(datetime.now()) + ': testDataFile complete')

#print(str(datetime.now()) + ': writing validDataFile')
#writeDataFile(validInputImagesPath, validOutputImagesPath, validInputImagesFiles, validOutputImagesFiles, validDataFileName)
#print(str(datetime.now()) + ': validDataFile complete')
