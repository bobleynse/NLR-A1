# NLR-A1
A UvA group project for Machine Learning and Decision Making. We used a project by https://github.com/mahmoudmohsen213/airs

## Tools
- Python 3.6.7
- Tensorflow 1.12.0
- Pillow 5.4.1

## Usage
### Prepare the data
1. Prepare the dataset in the directories contained in 'segmentationfiles/segmentation-dataset' directory.  Each input image (TIF) must have a corresponding binary (black and white) output image (TIF) of the same exact dimensions and same name in the corresponding output directory.
2. Run 'convertToFeatureFiles.py'. It should generate three csv files, train.csv, test.csv, and valid.csv.
### Train the network
3. Run 'train.py'. It should build the NN in a specified folder, and train it using the generated files in the previous step (this may take several minutes, hours, or days depending on the size of the files, the size of the network, and the number of training iterations).
### Classify images
4. Prepare the input image in 'image-input' directory.
5. Run 'classify.py' giving it two cmd arguments, the name if the input image file from the previous step, and the desired name of the output image file. It should generate the corresponding binary mask in 'image-output' directory.

## Adjust the neural network
You can adjust the neural network in train.py. Make sure you make the same adjustments in classify.py. The default settings are:
- 2 classes
- 4 hidden layers with 100, 150, 100 and 50 neurons respectively
