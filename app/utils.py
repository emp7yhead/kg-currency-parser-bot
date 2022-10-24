import logging
import traceback
import requests
import pandas as pd

CURRENCY = ['USD', 'EUR', 'RUB']

logger = logging.getLogger(__name__)


def parse_url_for_table(url):
    response = requests.get(url)
    response.raise_for_status()
    try:
        tables = pd.read_html(response.text)
    except ValueError as error:
        logger.debug(traceback.format_exc(8))
        logger.error(f'No tables found in {url}')
        raise error
    logger.debug(f'Found tables in {url}')
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
