#!/usr/bin/env python3
import timeit
import sys
from functools import reduce


def loop():
    num = int(sys.argv[3])
    res = 0

    for i in range(num + 1):
        res += i * i
    return res


def reduce_func():
    num = int(sys.argv[3])
    return reduce(lambda a, b: a + b * b, range(1, num + 1), 0)


def functions():
    func_name = sys.argv[1]
    time = int(sys.argv[2])
    if func_name == 'loop':
        print(timeit.timeit("loop()", setup="from __main__ import loop", number=time))
    elif func_name == 'reduce':
        print(timeit.timeit("reduce_func()", setup="from __main__ import reduce_func", number=time))
    else:
        raise Exception('Wrong type of function')


def main():
    try:
        if len(sys.argv) != 4:
            raise Exception("Enter as arguments: function name, amount to call function and number for the sum of the "
                            "calculation squares")
        functions()
    except ValueError:
        print('You should enter nums as second and third arguments')
    except KeyboardInterrupt:
        print("\nStopped")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

