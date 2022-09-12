import sys
import os


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
        @staticmethod
        def counts(data):
            head = sum([row[0] for row in data])
            tail = sum([row[1] for row in data])
            return head, tail

        @staticmethod
        def fractions(h, t):
            s = h + t
            return 100.0 * h / s, 100.0 * t / s


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Wrong argument amount")
    r = Research(sys.argv[1])
    file = r.file_reader(False)
    print(file)

    head, tail = r.Calculations.counts(file)
    print(str(head) + ',' + str(tail))

    fr1, fr2 = r.Calculations.fractions(head, tail)
    print(str(fr1) + ',' + str(fr2))
