from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

os.makedirs("logs", exist_ok=True)

print(f"load mnist dataset")
#load of mnist
(X_train, y_train),(X_test, y_test) = keras.datasets.mnist.load_data()

#normalizing of the data
X_train = X_train.astype("float32")/255.0
X_test = X_test.astype("float32")/255.0

#reshaping of data to CNN
X_train = X_train.reshape(-1,28,28,1)
X_test = X_test.reshape(-1,28,28,1)

