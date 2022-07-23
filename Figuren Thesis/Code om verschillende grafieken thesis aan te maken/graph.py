# import the necessary packages
#from pyimagesearch import config
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model
import numpy as np
import mimetypes
import argparse
import imutils
import cv2
import os
import pandas as pd

import itertools

# load our trained bounding box regressor from disk
model = load_model("/Users/stefgielen/Documents/school 2021-2022/thesis/Python_Workspace/CustCNN/modeltestset")


plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

