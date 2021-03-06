import pandas as pd
from classes.data_exporter import DataExporter


class ExcelExporter(DataExporter):
    def export_data(self, dataframe: pd.DataFrame):
        """
        Exports dataframe as Excel file.
        :param dataframe: Pandas dataframe
        :return: None
        """
        dataframe.to_excel(f"{self.name}.xlsx", index=False)