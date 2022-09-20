#!/usr/bin/env python3
import timeit
import sys


def emails_data():
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return emails * 5


def filter_function(emails):
    return list(filter(lambda x: x.partition('@')[2] == 'gmail.com', emails))


def list_comprehension(emails):
    return [x for x in emails if x.partition('@')[2] == 'gmail.com']


def map_function(emails):
    return list(map(lambda x: x if x.partition('@')[2] == 'gmail.com' else None, emails))


def loop(emails):
    result = []
    for data in emails:
        if data.partition('@')[2] == 'gmail.com':
            result.append(data)
    return result


def functions(type_name, time):
    emails = emails_data()
    if type_name == 'loop':
        print(timeit.timeit(f"loop({emails})", setup="from __main__ import loop", number=time))
    elif type_name == 'list_comprehension':
        print(timeit.timeit(f"list_comprehension({emails})", setup="from __main__ import list_comprehension", number=time))
    elif type_name == 'map':
        print(timeit.timeit(f"map_function({emails})", setup="from __main__ import map_function", number=time))
    elif type_name == 'filter':
        print(timeit.timeit(f"filter_function({emails})", setup="from __main__ import filter_function", number=time))
    else:
        print("Wrong type")


def main():
    try:
        if len(sys.argv) == 3:
            functions(sys.argv[1], int(sys.argv[2]))
        else:
            raise Exception("Enter as arguments type of function and amount to call it")
    except ValueError:
        print("Enter number as second argument")
    except KeyboardInterrupt:
        print("\nStopped")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

