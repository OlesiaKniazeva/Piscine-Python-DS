#!/usr/bin/env python3
import sys
import requests
import pytest
from bs4 import BeautifulSoup


class WrongArgumentAmount(Exception):
    def __str__(self):
        return 'Add ticker symbol and field of table as arguments'


class PageNotFound(Exception):
    def __str__(self):
        return 'Page with requested field not found'


class NoTickerSymbol(Exception):
    def __str__(self):
        return 'No page with such ticker symbol'


class NoRequestedField(Exception):
    def __str__(self):
        return 'No requested field found'


def test_connect_to_server():
    with pytest.raises(PageNotFound):
        get_page('ффф6')


def test_data_returned_not_empty():
    assert get_page('GOOG') is not None


def test_if_returned_data_is_right():
    assert start_parsing('GOOG', 'Total Revenue')[0] == 'Total Revenue'


def test_if_data_is_tuple():
    assert isinstance(start_parsing('GOOG', 'Net Interest Income'), tuple)


def test_if_ticker_symbol_exists():
    with pytest.raises(NoTickerSymbol):
        start_parsing('HO', 'no')


def test_if_field_exists():
    with pytest.raises(NoRequestedField):
        start_parsing('GOOG', 'item to')


def get_page(url):
    str = f'https://finance.yahoo.com/quote/{url}/financials?p={url}'
    html_get = requests.get(str, headers={'User-Agent': 'Custom'})
    if html_get.status_code != 200:
        raise PageNotFound()
    return html_get.text


def start_parsing(url, field):
    html_text = get_page(url)

    soup = BeautifulSoup(html_text, 'html.parser')
    data = soup.find_all(attrs={"data-test": "fin-row"})
    if len(data) == 0:
        raise NoTickerSymbol()
    values = []
    for i in data:
        data = i.findAll('span')
        res = []
        if data[0].text == field:
            for d in data:
                res.append(d.text)
            return tuple(res)
    raise NoRequestedField()


if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise WrongArgumentAmount()
        result = start_parsing(sys.argv[1], sys.argv[2])
        print(result)
    except (WrongArgumentAmount, PageNotFound, NoTickerSymbol, NoRequestedField) as e:
        print(e)

