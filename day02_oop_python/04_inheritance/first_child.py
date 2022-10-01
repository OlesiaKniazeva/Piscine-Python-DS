#!/usr/bin/env python3
import sys
import os
from random import randint


class Research:
    def __init__(self, path):
        self.path = path

    def check_header(self, head):
        header = head.split(',')
        if len(header) != 2 or header[0] != 'head' or header[1] != 'tail':
            raise Exception("Wrong header")

    def file_reader(self, has_header=True):
        if not os.access(self.path, os.R_OK):
            raise Exception('Couldn\'t read file')
        with open(self.path, 'r') as f:
            data_to_check = f.read().split('\n')
            if len(data_to_check) < 2:
                raise Exception('Wrong data')
            if has_header is True:
                self.check_header(data_to_check[0])
                data_to_check.pop(0)
            result = []
            for line in data_to_check:
                nums = line.split(',')
                res = ''.join(nums)
                if len(nums) != 2 or (res != '01' and res != '10'):
                    raise Exception('Wrong data')
                result.append([int(x) for x in nums])
            return result

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            head = sum([row[0] for row in self.data])
            tail = sum([row[1] for row in self.data])
            return head, tail

        def fractions(self, h, t):
            s = h + t
            return 100.0 * h / s, 100.0 * t / s

    class Analytics(Calculations):
        def predict_random(self, amount):
            data = []
            for s in range(amount):
                if randint(0, 1) == 0:
                    data.append([0, 1])
                else:
                    data.append([1, 0])
            return data

        def predict_last(self):
            return self.data


def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("Wrong argument amount")
        r = Research(sys.argv[1])
        file = r.file_reader(True)
        print(file)

        calc = r.Calculations(file)
        head, tail = calc.counts()
        print(str(head) + ',' + str(tail))

        fr1, fr2 = calc.fractions(head, tail)
        print(str(fr1) + ',' + str(fr2))

        analys = r.Analytics(file)
        print('-----------\nrandom lists')
        for i in range(3):
            rand = randint(1, 25)
            print(rand)
            data = analys.predict_random(rand)
            print(data)

        print('---------------\nlast list')
        res = analys.predict_last()
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
