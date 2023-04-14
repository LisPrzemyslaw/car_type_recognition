import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Convolution2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import to_categorical


class Network:
    def __init__(self, data_x: np.array, data_y: np.array):
        self.data_x = data_x.astype(np.float32)
        self.data_x /= 255 - 0.5  # normalize data
        print(f"{self.data_x.shape=}")
        self.data_y = to_categorical(data_y, num_classes=189)
        print(f"{self.data_y.shape=}")
        self.batch_size = 64

        self.__configure_gpu()
        self.model = tf.keras.models.Sequential([
            Convolution2D(filters=16, kernel_size=(5, 5), input_shape=(128, 128, 3), activation='relu', padding='same'),
            BatchNormalization(),
            Convolution2D(filters=128, kernel_size=(5, 5), activation='relu', padding='same'),
            BatchNormalization(),
            MaxPool2D((2, 2)),
            Convolution2D(filters=16, kernel_size=(5, 5), activation='relu', padding='same'),
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
            Dense(units=400, activation="relu"),
            Dropout(0.15),
            Dense(units=300, activation="relu"),
            Dropout(0.05),
            Dense(units=189, activation="softmax")])

    def model_compile(self):
        self.model.compile(optimizer=RMSprop(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

    def model_fit(self, epochs: int = 10):
        return self.model.fit(self.data_x,
                              self.data_y,
                              batch_size=self.batch_size,
                              epochs=epochs,
                              validation_split=0.1,
                              validation_freq=1,
                              verbose=2)
