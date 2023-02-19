from data_reader.reader_interface import ReaderInterface
from image_recognition.data_objects.pictures import Pictures


class NameBasedReader(ReaderInterface):
    def __init__(self, pictures_obj: Pictures):
        super().__init__(pictures_obj)
        pass

    def read_images(self):
        """
        TODO
        """
        pass
