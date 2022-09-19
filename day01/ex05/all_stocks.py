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


def start(arg):
    strs = []
    companies, stocks = companies_stocks()
    res = arg.split(',')
    for word in res:
        value = word.strip()
        if len(value) == 0:
            return
        if value.upper() in stocks:
            strs.append(value.upper() + ' is a ticker symbol for ' + get_company(value.upper(), companies))
        elif value.capitalize() in companies:
            strs.append(value.capitalize() + ' stock price is ' + str(stocks.get(companies.get(value.capitalize()))))
        else:
            strs.append(str(value) + ' is an unknown company or an unknown ticker symbol')
    for sentence in strs:
        print(sentence)


def main():
    if len(sys.argv) == 2:
        start(sys.argv[1])


if __name__ == '__main__':
    main()
