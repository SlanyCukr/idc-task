import pandas as pd
from classes.data_exporter import DataExporter


class CSVExporter(DataExporter):
    def export_data(self, dataframe: pd.DataFrame):
        """
        Exports data as CSV file.
        :param dataframe: Pandas dataframe
        :return: None
        """
        dataframe.to_csv(f"{self.name}.csv", index=False)
