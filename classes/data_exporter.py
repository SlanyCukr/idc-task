from abc import ABC, abstractmethod
import pandas as pd


class DataExporter(ABC):
    def __init__(self, name: str):
        """
        Name of the file is automatically set in child classes,
        because it is in this base abstract class.
        :param name: Name of the file
        """
        self.name = name

    @abstractmethod
    def export_data(self, dataframe: pd.DataFrame):
        """
        Is implemented in child classes.
        :param dataframe: Pandas dataframe
        :return: None
        """
        pass