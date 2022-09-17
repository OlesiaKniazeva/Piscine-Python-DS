#!/usr/bin/env python3
import timeit
import random
from collections import Counter


def generate_random_list():
    length = 1_000_000
    return [random.randint(0, 100) for x in range(length)]


def dictionary_by_counter(rand_list):
    return Counter(rand_list)


def list_to_dictionary(rand_list):
    res = {}
    for i in rand_list:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res


def top_data_standard(rand_list):
    d = list_to_dictionary(rand_list)
    tuple_d = (sorted(d, key=d.get, reverse=True)[:10])
    res = {}
    for w in tuple_d:
        res[w] = d[w]
    return res


def top_data_counter(rand_list):
    return dict(Counter(rand_list).most_common(10))


def start():
    amount = 1
    random_list = generate_random_list()
    print('my function:', timeit.timeit(f"list_to_dictionary({random_list})", setup="from __main__ import "
                                        "list_to_dictionary", number=amount))
    print('Counter:', timeit.timeit(f"dictionary_by_counter({random_list})",
                                    setup="from __main__ import dictionary_by_counter", number=amount))
    print('my top:', timeit.timeit(f"top_data_standard({random_list})",
                                   setup="from __main__ import top_data_standard", number=amount))
    print('Counter\'s top:', timeit.timeit(f"top_data_counter({random_list})",
                                           setup="from __main__ import top_data_counter", number=amount))


if __name__ == '__main__':
    start()
