import sys
import yaml

from src.singleton import Singleton


class GlobalParams(dict, metaclass=Singleton):
    """
    This is a class for managing the global params from a config yml file.
    """
    def __init__(self):
        """
        The constructor for the GlobalParams class.
        """
        super().__init__()
        self.update(self.get_yml_file())

    @staticmethod
    def get_yml_file() -> dict:
        """
        Opens a yaml file from sys.argv[-1].

        :return: (dict) data from yaml file
        """
        file_name = sys.argv[-1]
        if file_name == "tests":
            file_name = "dev_tools/config.yml"
        with open(file_name) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data
