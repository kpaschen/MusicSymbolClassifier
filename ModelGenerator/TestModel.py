#!/usr/bin/python
import sys, os, inspect

from argparse import ArgumentParser

import keras
import numpy
import skimage
from keras.utils import plot_model
from scipy import ndimage
from PIL import Image

from skimage.transform import resize

from models.ConfigurationFactory import ConfigurationFactory
from models.TrainingConfiguration import TrainingConfiguration

print("Parsing arguments ...")

parser = ArgumentParser("Classify an RGB-image with a pre-trained classifier")
parser.add_argument("-c", "--model", dest="model_path",
                    help="path to the classifier (*.h5)")
parser.add_argument("-i", "--image", dest="image_path",
                    help="path to the rgb image to classify")

args = parser.parse_args()

if len(sys.argv) < 5:
    parser.print_help()
    sys.exit(-1)

model_path = args.model_path
image_path = args.image_path

print(" Model: ", model_path)
print(" Image: ", image_path)

print("Loading image ...")
input_image = ndimage.imread(image_path, mode="RGB")
print(" Shape: {0}".format(input_image.shape))

print("Loading classifier...")
best_model = ConfigurationFactory().get_configuration_by_name("vgg4").classifier()
best_model.load_weights(model_path)
classifier = best_model

# classifier = keras.models.load_model(model_path)
classifier.summary()
input_shape = classifier.input_shape[1:4]  # For some reason, input-shape has the form (None, 1, 2, 3)
print(" Input shape: {0}, Output: {1} classes".format(input_shape, classifier.output_shape[1]))

print("Preprocessing image ...")
print("  Resizing to 128x244x3")
normalized_input_image = resize(input_image, output_shape=(244,128,3), preserve_range=True)
# normalized_input_image = normalized_input_image.astype(numpy.float32)
#
# print(" Result: shape: {0}, dtype: {1}, mean: {2:.3f}, std: {3:.3f}".format(normalized_input_image.shape,
#                                                                             normalized_input_image.dtype,
#                                                                             numpy.mean(normalized_input_image),
#                                                                             numpy.std(normalized_input_image)))
#
Image.fromarray(normalized_input_image.astype(numpy.uint8), mode="RGB").save("normalized_input.png")

#plot_model(classifier, to_file='classifier.png')

print("Classifying image ...")
print("1/1 [==============================] - 0s")

scores = classifier.predict(numpy.array([input_image]))#.flatten()
print(" Class scores: {0}".format(numpy.array2string(scores, formatter={'float_kind': lambda x: "%0.2f" % x})))
class_with_highest_probability = numpy.where(scores == scores.max())[0][0]

class_names = ['3-8-Time',
               'Cut-Time',
               'Double-Sharp',
               'Quarter-Rest',
               '6-8-Time',
               'Eighth-Rest',
               '2-2-Time',
               'G-Clef',
               'Half-Note',
               '3-4-Time',
               '12-8-Time',
               'Whole-Note',
               'Sixty-Four-Rest',
               'Thirty-Two-Note',
               'Sixteenth-Rest',
               '4-4-Time',
               'Sixteenth-Note',
               'Quarter-Note',
               'Sixty-Four-Note',
               'Common-Time',
               'F-Clef',
               '2-4-Time',
               'Sharp',
               'Barline',
               'Eighth-Note',
               'Natural',
               'Flat',
               'Whole-Half-Rest',
               'Thirty-Two-Rest',
               'C-Clef',
               'Dot',
               '9-8-Time']

print(" Image is most likely: {0} (certainty: {1:0.2f})".format(class_names[class_with_highest_probability], scores[class_with_highest_probability]))
