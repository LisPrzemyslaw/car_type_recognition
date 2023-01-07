from dataclasses import dataclass, field
from image_recognition.dataclasses.car import Car
from typing import Set


@dataclass
class Pictures:
    imgs: Set[Car] = field(default_factory=set)

    def add(self, element):
        self.imgs.add(element)
