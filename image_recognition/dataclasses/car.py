from dataclasses import dataclass
import numpy as np


# @dataclass(unsafe_hash=True)
@dataclass
class Car:
    """
    TODO docstring
    """
    img: np.array
    __car_type: str
    __car_model: str
    __production_year: int

    @property
    def car_type(self):
        return self.__car_type

    @car_type.setter
    def car_type(self, value: str):
        self.__car_type = value.lower()

    @property
    def car_model(self):
        return self.__car_model

    @car_model.setter
    def car_model(self, value: str):
        self.__car_model = value.lower()

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, value: int):
        self.__production_year = int(value)

    def type_str(self):
        """string for car recognition"""
        return f"{self.car_type}_{self.car_model}_{self.production_year}"
