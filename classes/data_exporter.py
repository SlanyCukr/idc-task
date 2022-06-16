from abc import ABC, abstractmethod
import pandas as pd


class DataExporter(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def export_data(self, dataframe: pd.DataFrame):
        pass