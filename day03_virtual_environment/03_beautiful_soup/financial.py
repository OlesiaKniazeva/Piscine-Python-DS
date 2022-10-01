#!/usr/bin/env python3
import sys
import time
import requests
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
    url = f'https://finance.yahoo.com/quote/{url}/financials?p={url}'
    html_get = requests.get(url, headers={'User-Agent': 'Custom'})
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


def main():
    try:
        if len(sys.argv) != 3:
            raise WrongArgumentAmount()
        result = start_parsing(sys.argv[1], sys.argv[2])
        print(result)
        time.sleep(5)
    except (WrongArgumentAmount, PageNotFound, NoTickerSymbol, NoRequestedField) as e:
        print(e)


if __name__ == '__main__':
    main()
