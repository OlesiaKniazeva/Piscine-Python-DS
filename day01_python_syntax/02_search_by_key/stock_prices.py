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


def main():
    if len(sys.argv) == 2:
        comp = sys.argv[1].capitalize()
        companies, stocks = companies_stocks()
        stock = companies.get(comp)
        if stock is None:
            print("Unknown company")
        else:
            print(stocks.get(stock))


if __name__ == '__main__':
    main()
