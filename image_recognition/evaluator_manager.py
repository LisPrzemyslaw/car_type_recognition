from image_recognition.dataclasses.pictures import Pictures
from data_reader.reader_factory import ReaderFactory

class EvaluatorManager:
    def __int__(self):
        self.pictures = Pictures()
        self.reader = ReaderFactory