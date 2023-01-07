import os
from typing import Optional
import json
import cv2

from data_reader.reader_interface import ReaderInterface
from image_recognition.dataclasses.pictures import Pictures
from image_recognition.dataclasses.car import Car

class FolderBasedReader(ReaderInterface):
    _JSON_CAR_DATA_PATH = os.path.join(os.getcwd(), "data_reader/_json_data/car_data.json")

    def __init__(self, pictures_obj: Pictures):
        super().__init__(pictures_obj)
        self.is_train = True
        self.abs_path = os.path.join(os.getcwd(), "data/stanford-car-dataset-by-classes-folder/car_data/car_data", self.get_training_or_test())
        self.car_data_from_json: Optional[dict] = None
        self._read_car_data_from_json_file()

    def read_images(self):
        for car_full_name in self.get_all_folders():
            for picture_name in os.listdir(os.path.join(self.abs_path, car_full_name)):
                self.pictures_obj.add(Car(cv2.imread(os.path.join(self.abs_path, car_full_name, picture_name)),
                                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["car_type"],
                                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["car_model"],
                                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["production_year"],
                                          ))

    def _read_car_data_from_json_file(self):
        """
        This method will read data from json file and assign to class variable
        """
        with open(self._JSON_CAR_DATA_PATH, "r") as file:
            self.car_data_from_json = json.load(file)

    def set_test(self):
        self.is_train = False

    def get_training_or_test(self) -> str:
        return "train" if self.is_train else "test"

    def get_all_folders(self) -> list:
        return os.listdir(self.abs_path)
