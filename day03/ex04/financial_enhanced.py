#!/usr/bin/env python3
import sys
import urllib3
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


def get_page(url):
    str = f'https://finance.yahoo.com/quote/{url}/financials?p={url}'
    http = urllib3.PoolManager()
    html_get = http.request('GET',
                            str,
                            headers={'User-Agent': 'Custom'}
                            )
    if html_get.status != 200:
        raise PageNotFound()
    return html_get.data


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
