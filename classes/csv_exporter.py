import pandas as pd
from classes.data_exporter import DataExporter


class CSVExporter(DataExporter):
    def export_data(self, dataframe: pd.DataFrame):
        dataframe.to_csv(f"{self.name}.csv")
