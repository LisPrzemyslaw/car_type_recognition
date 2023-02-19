from abc import ABC, abstractmethod
from image_recognition.data_objects.pictures import Pictures


class ReaderInterface(ABC):
    def __init__(self, pictures_obj: Pictures):
        self.pictures_obj = pictures_obj

    @abstractmethod
    def read_images(self):
        """

        """
        pass
