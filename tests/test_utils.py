import pytest
import requests_mock

from app.utils import TableHandler, parse_url_for_table, update_indexes, CURRENCY
from tests.fixtures import page_without_res, test_dataframe, test_tables, TEST_URL


def test_parse_url_for_tables(page_without_res):
    with pytest.raises(ValueError):
        assert parse_url_for_table(TEST_URL)


def test_update_indexes(test_dataframe):
    df = update_indexes(test_dataframe)
    assert df.index.tolist() == CURRENCY


def test_table_handler(test_tables):
    test = TableHandler(test_tables)
    assert test.tables == test_tables

    average_df = test.get_average()
    best_df = test.get_best_course()
    recommend_df = test.get_national_bank_course()

    assert len(average_df.index) == 3
    assert len(best_df.index) == 3
    assert len(recommend_df.index) == 3
