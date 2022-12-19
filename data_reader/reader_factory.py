import os.path
from data_reader.name_based_reader import NameBasedReader
from data_reader.folder_based_reader import FolderBasedReader
from data_reader.reader_interface import ReaderInterface


class ReaderFactory:
    __DATA_LINKS = {"name_based_images": "https://www.kaggle.com/datasets/prondeau/the-car-connection-picture-dataset",
                    "stanford-car-dataset-by-classes-folder": "https://www.kaggle.com/datasets/sungtheillest/vehicledetected-stanford-cars-data-classes-folder"}

    __READERS = {"name_based_images": NameBasedReader, "stanford-car-dataset-by-classes-folder": FolderBasedReader}

    def __init__(self, folder_name: str = "name_based_images"):
        self.folder_name = folder_name
        self.abs_path = os.path.join(os.getcwd(), "data", self.folder_name)
        self.check_if_folder_exist()

    def check_if_folder_exist(self):
        """
        TODO docstring
        :return:
        """
        if self.folder_name not in self.__DATA_LINKS.keys():
            raise KeyError(f"Reader not exist! Possible readers: {self.__DATA_LINKS.keys()}")
        if not os.path.exists(self.abs_path) or not os.listdir(self.abs_path):
            error_msg = f"Path {os.path.join(os.getcwd(), 'data', self.folder_name)} does not exit. " \
                        f"Download files to this folder from: {self.__DATA_LINKS[self.folder_name]}"
            raise FileNotFoundError(error_msg)

    def get_reader(self) -> ReaderInterface:
        return self.__READERS[self.folder_name]()
