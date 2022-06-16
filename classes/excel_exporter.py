import pandas as pd
from classes.data_exporter import DataExporter


class ExcelExporter(DataExporter):
    def export_data(self, dataframe: pd.DataFrame):
        dataframe.to_excel(f"{self.name}.xlsx")