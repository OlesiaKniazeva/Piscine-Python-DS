#!/usr/bin/env python3
import timeit


def emails_data():
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return emails * 5


def list_comprehension(emails):
    return [x for x in emails if x.partition('@')[2] == 'gmail.com']


def loop(emails):
    result = []
    for data in emails:
        if data.partition('@')[2] == 'gmail.com':
            result.append(data)
    return result


def compare_functions():
    time = 900_000
    emails = emails_data()
    compr_res = timeit.timeit(f"list_comprehension({emails})", setup="from __main__ import list_comprehension", number=time)
    loop_res = timeit.timeit(f"loop({emails})", setup="from __main__ import loop", number=time)
    if compr_res < loop_res:
        print('it is better to use a list comprehension')
        print(compr_res, 'vs', loop_res)
    else:
        print('it is better to use a loop')
        print(loop_res, 'vs', compr_res)


if __name__ == '__main__':
    compare_functions()
