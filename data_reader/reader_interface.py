import json
import os
from abc import ABC, abstractmethod
from typing import Optional

from image_recognition.data_objects.pictures import Pictures


class ReaderInterface(ABC):
    _JSON_CAR_DATA_PATH = os.path.join(os.getcwd(), "data_reader/_json_data/car_data.json")

    def __init__(self, pictures_obj: Pictures):
        self.pictures_obj = pictures_obj
        self.height = 128
        self.width = 128
        self.car_data_from_json: Optional[dict] = None
        self._read_car_data_from_json_file()

    @abstractmethod
    def read_images(self):
        """

        """
        pass

    def _read_car_data_from_json_file(self):
        """
        This method will read data from json file and assign to class variable
        """
        with open(self._JSON_CAR_DATA_PATH, "r") as file:
            self.car_data_from_json = json.load(file)
