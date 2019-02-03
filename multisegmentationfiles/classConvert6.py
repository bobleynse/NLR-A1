import random
from os import listdir
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from datetime import datetime

# Saving path of every image.
trainInputImagesPath = 'multisegmentation-dataset/train-input'
trainOutputImagesPath = 'multisegmentation-dataset/train-output'
testInputImagesPath = 'multisegmentation-dataset/test-input'
testOutputImagesPath = 'multisegmentation-dataset/test-output'
#validInputImagesPath = 'multisegmentation-dataset/valid-input'
#validOutputImagesPath = 'multisegmentation-dataset/valid-output'

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
        print(str(datetime.now()) + ': processing image', i)
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
        out_pixels_Background = []        
        out_pixels_Highway = []
        out_pixels_Mainroad = []
        out_pixels_Regionalroad = []
        out_pixels_Localroad = []
        out_pixels_Street = []
        
        # This for loop assures that the algorithm only looks at pixel which have enough 
        # surrounding pixels (avoiding edges).
        # If there is a road in the output image, the pixel values of the input image are
        # appended to the corresponding array.

        # Grayscale value: Class
        #  0: Background (default)
        # 17: Highway
        # 34: Main road
        # 51: Regional road
        # 68: Local road
        # 85: Street

        for x in range(rectSize//2, inputImageXSize - (rectSize//2)):
            for y in range(rectSize//2, inputImageYSize - (rectSize//2)):
                isRoadPixel = outputImagePixels[x, y]
                if(isRoadPixel == 0):
                    out_pixels_Background.append((x, y))
                elif(isRoadPixel > 0 and isRoadPixel <= 20):
                    out_pixels_Highway.append((x, y))
                elif(isRoadPixel > 20 and isRoadPixel <= 40):
                    out_pixels_Mainroad.append((x, y))
                elif(isRoadPixel > 40 and isRoadPixel <= 60):
                    out_pixels_Regionalroad.append((x, y))
                elif(isRoadPixel > 60 and isRoadPixel <= 80):
                    out_pixels_Localroad.append((x, y))
                elif(isRoadPixel > 80):
                    out_pixels_Street.append((x, y))
                   

        # The pixel arrays are randomly shuffled, to get a random distribution of all the scanned images.
        outputImages = [random.sample(out_pixels_Background, len(out_pixels_Background)),
        random.sample(out_pixels_Highway, len(out_pixels_Highway)),
        random.sample(out_pixels_Mainroad, len(out_pixels_Mainroad)),
        random.sample(out_pixels_Regionalroad, len(out_pixels_Regionalroad)),
        random.sample(out_pixels_Localroad, len(out_pixels_Localroad)),
        random.sample(out_pixels_Street, len(out_pixels_Street))]

        outputSelector = 0
        for m in range(linesLimit):
            if(linesCountPerImage >= linesLimitPerImage):
                break
            
            if(((m*2) + 1) >= len(out_pixels_Background)):
                break
            
            # Select x and y coordinates from the output pixel arrays.
    
            if outputImages[outputSelector] != None:
                if len(outputImages[outputSelector]) > m:
                    x = outputImages[outputSelector][m][0]
                    y = outputImages[outputSelector][m][1]
                
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
                    line += str(outputSelector) + '\n'
                    linesCount += 1
                    linesCountPerImage += 1
                    dataFile.write(line)

            outputSelector = (outputSelector + 1) % 6
    
    print(str(datetime.now()) + ': ' + dataFileName + ' linesCount:', linesCount)

# Creating .csv files.
trainDataFileName = 'multisegmentation-dataset/train.csv'
testDataFileName = 'multisegmentation-dataset/test.csv'
validDataFileName = 'multisegmentation-dataset/valid.csv'

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
