from classes.data_accesser import DataAccesser
from classes.data_exporter_factory import DataExporterFactory, DataExporterType
from utils.data_loader import load_adjust_data, select_local_countries

NAME = "output"

if __name__ == "__main__":
    # create data exporter factory and different types of data exporters
    data_exporter_factory = DataExporterFactory(NAME)
    html_data_exporter = data_exporter_factory.create_data_exporter(DataExporterType.HTML)
    csv_data_exporter = data_exporter_factory.create_data_exporter(DataExporterType.CSV)
    xlsx_data_exporter = data_exporter_factory.create_data_exporter(DataExporterType.EXCEL)

    # find countries in exchange dataset, choose to be used for loading and adjusting data
    local_countries = select_local_countries('datasets/exchange.xlsx') # index for Czech Republic is 2
    df = load_adjust_data("datasets/data.xlsx", "datasets/exchange.xlsx", local_countries[2])

    # create data accesser, supply loaded, adjusted dataset
    data_accesser = DataAccesser(df)

    # use data accesser to perform various actions - finding, sorting
    print(data_accesser.get_company_revenue_share('Apple'))
    print(data_accesser.get_company_row('Apple'))
    data_accesser.sort_alphabet_company()
    data_accesser.sort_revenue()

    # export sorted data to different formats
    html_data_exporter.export_data(df)
    csv_data_exporter.export_data(df)
    xlsx_data_exporter.export_data(df)
