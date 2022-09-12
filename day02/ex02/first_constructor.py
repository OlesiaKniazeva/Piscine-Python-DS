import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if not os.access(self.path, os.R_OK):
            raise Exception('Couldn\'t read file')
        with open(self.path, 'r') as f:
            file = f.read()
            data_to_check = file.split('\n')
            if len(data_to_check) < 2:
                raise Exception('Wrong data')
            header = data_to_check[0].split(',')
            if len(header) != 2 or header[0] != 'head' or header[1] != 'tail':
                raise Exception("Wrong header")
            data_to_check.pop(0)
            for line in data_to_check:
                nums = line.split(',')
                res = ''.join(nums)
                if len(nums) != 2 or (res != '01' and res != '10'):
                    raise Exception('Wrong data')
            return file


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Wrong argument amount")
    r = Research(sys.argv[1])
    print(r.file_reader())
