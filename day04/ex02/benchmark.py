#!/usr/bin/env python3
import timeit
import sys


def emails_data():
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return emails * 5


def filter_function():
    emails = emails_data()
    return list(filter(lambda x: x.partition('@')[2] == 'gmail.com', emails))


def list_comprehension():
    emails = emails_data()
    return [x for x in emails if x.partition('@')[2] == 'gmail.com']


def map_function():
    emails = emails_data()
    return list(map(lambda x: x if x.partition('@')[2] == 'gmail.com' else None, emails))


def loop():
    emails = emails_data()
    result = []
    for data in emails:
        if data.partition('@')[2] == 'gmail.com':
            result.append(data)
    return result


def functions(type_name, time):
    if type_name == 'loop':
        print(timeit.timeit("loop()", setup="from __main__ import loop", number=time))
    elif type_name == 'list_comprehension':
        print(timeit.timeit("list_comprehension()", setup="from __main__ import list_comprehension", number=time))
    elif type_name == 'map':
        print(timeit.timeit("map_function()", setup="from __main__ import map_function", number=time))
    elif type_name == 'filter':
        print(timeit.timeit("filter_function()", setup="from __main__ import filter_function", number=time))
    else:
        print("Wrong type")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        functions(sys.argv[1], int(sys.argv[2]))
    else:
        print("Enter as arguments type of function and amount to call it")
