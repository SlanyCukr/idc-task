from enum import Enum

from classes.csv_exporter import CSVExporter
from classes.data_exporter import DataExporter
from classes.html_exporter import HTMLExporter


class DataExporterType(Enum):
    HTML = 1
    CSV = 2
    EXCEL = 3


class DataExporterFactory:
    def __init__(self, name: str):
        """
        Constructor for the data exporter factory.
        :param name: Name of the file to be exported (without suffix).
        """
        self.name = name
        self.data_exporter_class_dict = {
            DataExporterType.HTML: HTMLExporter,
            DataExporterType.CSV: CSVExporter
        }

    def create_data_exporter(self, data_exporter_type: DataExporterType) -> DataExporter:
        """
        Fetches class from dictionary, then creates object from that class with specified name.
        :param data_exporter_type: Type of the data exporter
        :return: Concrete data exporter
        """
        return self.data_exporter_class_dict[data_exporter_type](self.name)

