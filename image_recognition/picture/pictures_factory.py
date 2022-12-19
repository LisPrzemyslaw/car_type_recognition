from dataclasses import dataclass
from typing import Set
from image_recognition.picture.picture import Picture


@dataclass
class PicturesFactory:
    imgs: Set[Picture]
