from dataclasses import dataclass
from typing import Tuple

import numpy as np


# @dataclass(unsafe_hash=True)
# # @dataclass(frozen=True, eq=True)
# class Car:
#     """
#     TODO docstring
#     """
#     img: np.array
#     __car_type: str
#     __car_model: str
#     __production_year: int
#
#     @property
#     def car_type(self):
#         return self.__car_type
#
#     @property
#     def car_model(self):
#         return self.__car_model
#
#     @property
#     def production_year(self):
#         return self.__production_year
#
#     def type_str(self):
#         """string for car recognition"""
#         return f"{self.car_type}_{self.car_model}_{self.production_year}"
class Car:
    def __init__(self, img, car_type, car_model, production_year):
        self.img = img
        self.car_type = car_type
        self.car_model = car_model
        self.production_year = production_year

    def type_str(self):
        """string for car recognition"""
        return f"{self.car_type}_{self.car_model}_{self.production_year}"
