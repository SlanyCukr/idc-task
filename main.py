from classes.data_accesser import DataAccesser
from classes.data_exporter_factory import DataExporterFactory, DataExporterType
from utils.data_loader import load_adjust_data, select_local_countries

NAME = "output"

if __name__ == "__main__":
    data_exporter_factory = DataExporterFactory(NAME)
    html_data_exporter = data_exporter_factory.create_data_exporter(DataExporterType.HTML)
    csv_data_exporter = data_exporter_factory.create_data_exporter(DataExporterType.CSV)
    xlsx_data_exporter = data_exporter_factory.create_data_exporter(DataExporterType.EXCEL)

    local_countries = select_local_countries('datasets/exchange.xlsx') # index for Czech Republic is 2
    df = load_adjust_data("datasets/data.xlsx", "datasets/exchange.xlsx", local_countries[2])

    data_accesser = DataAccesser(df)

    print(data_accesser.get_company_revenue_share('Apple'))
    print(data_accesser.get_company_row('Apple'))
    data_accesser.sort_alphabet_company()
    data_accesser.sort_revenue()

    html_data_exporter.export_data(df)
    csv_data_exporter.export_data(df)
    xlsx_data_exporter.export_data(df)
