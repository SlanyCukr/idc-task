import pandas as pd
from classes.data_exporter import DataExporter


class HTMLExporter(DataExporter):
    def export_data(self, dataframe: pd.DataFrame):
        with open(f"{self.name}.html") as f:
            f.write(dataframe.to_html())
