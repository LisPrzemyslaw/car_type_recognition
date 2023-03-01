from image_recognition.data_objects.pictures import Pictures
from data_reader.reader_factory import ReaderFactory
from data_reader.reader_interface import ReaderInterface
from image_recognition.neuron_network.network import Network
import numpy as np


class EvaluatorManager:
    def __init__(self):
        self.pictures = Pictures()
        self.reader: ReaderInterface = ReaderFactory(self.pictures).get_reader()
        self.reader.read_images()
        self.network = Network(np.array([car.img for car in self.pictures.imgs]), np.array([car.num_value for car in self.pictures.imgs]))
        # TODO normalize picture size
