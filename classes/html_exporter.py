import pandas as pd
from classes.data_exporter import DataExporter


class HTMLExporter(DataExporter):
    def export_data(self, dataframe: pd.DataFrame):
        """
        Exports data as HTML file.
        :param dataframe: Pandas dataframe
        :return: None
        """
        with open(f"{self.name}.html", "w") as f:
            f.write(dataframe.to_html(index=False))
