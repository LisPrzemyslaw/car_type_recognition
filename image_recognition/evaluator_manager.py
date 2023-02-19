from image_recognition.data_objects.pictures import Pictures
from data_reader.reader_factory import ReaderFactory
from data_reader.reader_interface import ReaderInterface
from neuron_network.network import Network


class EvaluatorManager:
    def __init__(self):
        self.pictures = Pictures()
        self.reader: ReaderInterface = ReaderFactory(self.pictures).get_reader()
        self.reader.read_images()
        self.network = Network([car.img for car in self.pictures.imgs], [car.type_str() for car in self.pictures.imgs])
