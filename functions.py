import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.models import Model


def image_net_classification():
    try:

        img: np.ndarray = cv2.imread('temp/classification.png')
        img = cv2.resize(img, (224, 224)) / 255
        img = np.expand_dims(img, axis=0)
        model = MobileNetV2()
        obj = model.predict(img).argmax()

        with open('data/classes/ImageNetClasses.txt') as file:
            data = file.readlines()

        if obj != 999 or obj >= 0:
            return data[obj].split("'")[1]
        else:
            return ''

    except Exception as error:
        return ''
