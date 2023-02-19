from dataclasses import dataclass, field
from image_recognition.data_objects.car import Car
from typing import Set


@dataclass(unsafe_hash=True)
# @dataclass
class Pictures:
    __imgs: Set[Car] = field(default_factory=set)

    def add(self, element: Car):
        self.__imgs.add(element)

    @property
    def imgs(self):
        return self.__imgs

    @imgs.setter
    def imgs(self, value):
        pass