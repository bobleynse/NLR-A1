from datetime import datetime
import numpy as np
import tensorflow as tf


print(str(datetime.now()) + ': loading data files')
# Data sets
trainDataFileName = 'segmentation-dataset/trainNIR.csv'
testDataFileName = 'segmentation-dataset/testNIR.csv'

# Load datasets.
trainData = np.loadtxt(trainDataFileName, delimiter=',')
testData =  np.loadtxt(testDataFileName, delimiter=',')

print(np.shape(trainData))
print(np.shape(testData))


# Specify the neural network you want to use
rectSize = 7
# Size between checkpoints
trainingSteps = 100
# total Size
totalTrainingSteps = 500

featureColumns = [tf.contrib.layers.real_valued_column("", dimension=rectSize*rectSize*4)]
hiddenUnits = [100, 150, 100, 50]
classes = 2

# specify a folder name for the model, model_steps_network
modelDir = 'models/modelNIR_{}_{}_{}x{}x{}x{}'.format(rectSize, totalTrainingSteps, hiddenUnits[0], hiddenUnits[1], hiddenUnits[2], hiddenUnits[3])

classifierConfig = tf.contrib.learn.RunConfig(save_checkpoints_secs = None, save_checkpoints_steps = trainingSteps)

classifier = tf.contrib.learn.DNNClassifier(feature_columns = featureColumns,
                                                hidden_units = hiddenUnits,
                                                n_classes = classes,
                                                model_dir = modelDir,
                                                config = classifierConfig)

# Define the training inputs
def getTrainData():
    x = tf.constant(trainData[:,:-1])
    y = tf.constant(trainData[:,-1:])
    print(x)
    print(y)
    return x, y

# Define the test inputs
def getTestData():
    x = tf.constant(testData[:,:-1])
    y = tf.constant(testData[:,-1:])
    return x, y

print(str(datetime.now()) + ': training...')
classifier.fit(input_fn=getTrainData, steps=totalTrainingSteps)
print(str(datetime.now()) + ': testing...')
accuracy = classifier.evaluate(input_fn=getTestData, steps=1)['accuracy']
print(str(datetime.now()) + ': done')
print(str(datetime.now()) + ': accuracy:', accuracy)
