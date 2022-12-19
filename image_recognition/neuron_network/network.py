import tensorflow as tf


class Network:
    def __init__(self, data_x, data_y):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(1, input_shape=(1,))
        ])
        self.data_x = data_x
        self.data_y = data_y

    def model_compile(self):
        self.model.compile(loss='mse', optimizer='adam')

    def model_fit(self, epochs: int = 100):
        self.model.fit(self.data_x, self.data_y, epochs=epochs)


if __name__ == '__main__':
    neuron = Network("X","Y")  # TODO
    neuron.model.summary()
    neuron.model_compile()
    neuron.model_fit()
