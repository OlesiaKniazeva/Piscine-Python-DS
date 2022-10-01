#!/usr/bin/env python3
import sys


def companies_stocks():
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return companies, stocks


def get_company(stock_name, comp):
    for k, v in comp.items():
        if v == stock_name:
            return k


def main():
    if len(sys.argv) == 2:
        stock = sys.argv[1].upper()
        companies, stocks = companies_stocks()
        st_value = stocks.get(stock)
        if st_value is None:
            print('Unknown ticker')
        else:
            print(get_company(stock, companies), st_value)


if __name__ == '__main__':
    main()
