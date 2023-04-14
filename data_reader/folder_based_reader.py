import os
from typing import Optional
import json
import cv2

from data_reader.reader_interface import ReaderInterface
from image_recognition.data_objects.pictures import Pictures
from image_recognition.data_objects.car import Car


class FolderBasedReader(ReaderInterface):

    def __init__(self, pictures_obj: Pictures):
        super().__init__(pictures_obj)
        self.is_train = True
        self.abs_path = os.path.join(os.getcwd(), "data/stanford-car-dataset-by-classes-folder/car_data/car_data",
                                     self.get_training_or_test())


    def read_images(self):
        for car_full_name in self.get_all_folders():
            for picture_name in os.listdir(os.path.join(self.abs_path, car_full_name)):
                car = Car(cv2.resize(cv2.imread(os.path.join(self.abs_path, car_full_name, picture_name)), (self.width, self.height),),
                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["car_type"],
                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["car_model"],
                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["production_year"],
                          self.car_data_from_json["stanford-car-dataset-by-classes-folder"][car_full_name]["num_value"],
                          )
                self.pictures_obj.add(car)
        print("all images read")



    def set_test(self):
        self.is_train = False

    def get_training_or_test(self) -> str:
        return "train" if self.is_train else "test"

    def get_all_folders(self) -> list:
        return os.listdir(self.abs_path)
