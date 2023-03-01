import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Convolution2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization


class Network:
    def __init__(self, data_x: np.array, data_y: np.array):
        self.model = tf.keras.models.Sequential([
            Convolution2D(filters=128, kernel_size=(5, 5), input_shape=None, activation='relu', padding='same'),
            BatchNormalization(),
            Convolution2D(filters=128, kernel_size=(5, 5), activation='relu', padding='same'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=64, kernel_size=(5, 5), activation='relu', padding='same'),
            BatchNormalization(),
            Convolution2D(filters=64, kernel_size=(5, 5), activation='relu', padding='same'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=32, kernel_size=(5, 5), activation='relu', padding='same'),
            BatchNormalization(),
            Convolution2D(filters=32, kernel_size=(5, 5), activation='relu', padding='same'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same'),
            BatchNormalization(),
            Convolution2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same'),
            BatchNormalization(),
            Flatten(),
            Dense(units=32, activation="relu"),
            Dropout(0.15),
            Dense(units=16, activation="relu"),
            Dropout(0.05),
            Dense(units=10, activation="softmax")])

        self.data_x = data_x
        self.data_x /= 255  # normalize data
        self.data_y = data_y

        self.batch_size = 128

    def model_compile(self):
        self.model.compile(loss='mse', optimizer='adam')

    def model_fit(self, epochs: int = 50):
        self.model.fit(self.data_x, self.data_y, epochs=epochs)
