import json
import os

import cv2

from data_reader.reader_interface import ReaderInterface
from image_recognition.data_objects.pictures import Pictures


class NameBasedReader(ReaderInterface):
    def __init__(self, pictures_obj: Pictures):
        super().__init__(pictures_obj)
        self.abs_path = os.path.join(os.getcwd(), "data/name_based_images")  # TODO
        self.last_index = 188

    def read_images(self):
        """
        TODO
        """
        all_pictures = [pic for pic in os.listdir(self.abs_path)]
        for car in all_pictures:
            car_type, car_model, production_year, *_ = car.split("_")
            pic = cv2.resize(cv2.imread(os.path.join(self.abs_path, car)), (self.width, self.height),)

    def _check_if_in_json(self, car_type, car_model, production_year):
        for key, value in self.car_data_from_json["stanford-car-dataset-by-classes-folder"].items():
            pass
        # TODO może jest łatwiejszy sposób