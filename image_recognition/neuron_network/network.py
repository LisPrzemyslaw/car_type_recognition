import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Convolution2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import RMSprop


class Network:
    def __init__(self, data_x: np.array, data_y: np.array):
        self.data_x = data_x.astype(np.float32)
        self.data_x /= 255 - 0.5  # normalize data
        self.data_y = data_y
        self.batch_size = 64

        self.model = tf.keras.models.Sequential([
            Convolution2D(filters=128, kernel_size=(5, 5), input_shape=(256, 256, 3), activation='relu', padding='same'),
            BatchNormalization(),
            Convolution2D(filters=128, kernel_size=(5, 5), activation='relu', padding='valid'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=64, kernel_size=(5, 5), activation='relu', padding='valid'),
            BatchNormalization(),
            Convolution2D(filters=64, kernel_size=(5, 5), activation='relu', padding='valid'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=32, kernel_size=(5, 5), activation='relu', padding='valid'),
            BatchNormalization(),
            Convolution2D(filters=32, kernel_size=(5, 5), activation='relu', padding='valid'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=16, kernel_size=(3, 3), activation='relu', padding='valid'),
            BatchNormalization(),
            Convolution2D(filters=16, kernel_size=(3, 3), activation='relu', padding='valid'),
            BatchNormalization(),
            Flatten(),
            Dense(units=400, activation="relu"),
            Dropout(0.15),
            Dense(units=300, activation="relu"),
            Dropout(0.05),
            Dense(units=189, activation="softmax")])

    def model_compile(self):
        self.model.compile(optimizer=RMSprop(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    def model_fit(self, epochs: int = 50):
        return self.model.fit(self.data_x,
                              self.data_y,
                              batch_size=self.batch_size,
                              epochs=epochs,
                              validation_split=0.1,
                              validation_freq=1,
                              verbose=2)
