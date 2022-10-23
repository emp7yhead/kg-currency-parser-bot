import requests
import pandas as pd

CURRENCY = ['USD', 'EUR', 'RUB']


def parse_url_for_table(url):
    response = requests.get(url)
    tables = pd.read_html(response.text)
    return tables


class TableHandler:
    def __init__(self, tables):
        self.tables = tables

    def get_average(self):
        return self.tables[1].head(3)

    def get_best_course(self):
        return self.tables[2].head(3)

    def get_national_bank_course(self):
        return self.tables[3].head(3)


def update_indexes(table):
    return table.set_index(
        [pd.Index(CURRENCY)]
    )
