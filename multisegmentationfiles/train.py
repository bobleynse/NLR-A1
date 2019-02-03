from datetime import datetime
import numpy as np
import tensorflow as tf


print(str(datetime.now()) + ': loading data files')
# Data sets
trainDataFileName = 'multisegmentation-dataset/train.csv'
testDataFileName = 'multisegmentation-dataset/test.csv'
validationDataFileName = 'multisegmentation-dataset/valid.csv'
# Load datasets.
trainData = np.loadtxt(trainDataFileName, delimiter=',').astype(int)
testData =  np.loadtxt(testDataFileName, delimiter=',').astype(int)
# validationData = tf.contrib.learn.datasets.base.load_csv_without_header(
#     filename=validationDataFileName,
#     target_dtype=np.int,
#     features_dtype=np.int)

# Specify the neural network you want to use
trainingSteps = 100
totalTrainingSteps = 500

featureColumns = [tf.contrib.layers.real_valued_column("", dimension=75)]
hiddenUnits = [100, 150, 100, 100, 50]
classes = 6

# specify a folder name for the model
modelDir = 'models/model_28-01'
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

# Define the validation inputs
# def getValidationData():
#     x = tf.constant(validationData.data)
#     y = tf.constant(validationData.target)
#     return x, y

# print(str(datetime.now()) + ': training...')
# prevAccuracy = -1.0
# for i in range(totalTrainingSteps // trainingSteps):
#     classifier.fit(input_fn=getTrainData, steps=trainingSteps)
#     currentAccuracy = classifier.evaluate(input_fn=getValidationData, steps=1)['accuracy']
#     print(str(datetime.now()) + ': training: validation step: ' + str(i) + ' currentAccuracy:', currentAccuracy)
#     #if(currentAccuracy <= prevAccuracy):
#     #    break
#     prevAccuracy = currentAccuracy

print(str(datetime.now()) + ': training...')
classifier.fit(input_fn=getTrainData, steps=totalTrainingSteps)
print(str(datetime.now()) + ': testing...')
accuracy = classifier.evaluate(input_fn=getTestData, steps=1)['accuracy']
print(str(datetime.now()) + ': done')
print(str(datetime.now()) + ': accuracy:', accuracy)
