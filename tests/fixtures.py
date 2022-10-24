import pytest
from pandas import util

TEST_URL = 'http://test.com'

@pytest.fixture
def page_without_res(requests_mock):
    requests_mock.get(TEST_URL, text='<html>\n</html>')


@pytest.fixture
def test_dataframe():
    return util.testing.makeDataFrame().head(3)


@pytest.fixture
def test_tables():
    tables = []
    for i in range(5):
        df = util.testing.makeDataFrame()
        tables.append(df)
    return tables
