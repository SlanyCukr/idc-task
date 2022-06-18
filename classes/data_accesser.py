import pandas as pd


class DataAccesser:
    def __init__(self, dataframe: pd.DataFrame):
        """
        This class is used to perform additional manipulation with dataframe - sorting.
        Also implements functions to fetch data.
        :param dataframe: Pandas dataframe
        """
        self.df = dataframe

    def get_company_revenue_share(self, company: str) -> str:
        # find revenue for specified company
        found_company = self.df[self.df['Company'] == company].iloc[0]
        return f"Company: {found_company.Company}. Revenue: {found_company['Revenue (USD)']}." \
               f" Share: {found_company.Share}."

    def get_company_row(self, company: str) -> str:
        # find on which row specific company resides
        row_number = self.df.index[self.df['Company'] == company][0]
        return f"Company: {company}. Row: {row_number + 1}." # + 1, because indexes start at 0

    def sort_alphabet_company(self):
        # sort data by company name descending
        self.df.sort_values(by='Company', ascending=False, inplace=True)

    def sort_revenue(self):
        # sort data by revenue - descending
        # '$' symbol would interfere, so just remove it, sort it, add it back again
        self.df['Revenue (USD)'] = self.df['Revenue (USD)'].str[1:].astype(float)
        self.df.sort_values(by='Revenue (USD)', ascending=False, inplace=True)
        self.df['Revenue (USD)'] = '$' + self.df['Revenue (USD)'].astype(str)
