#!/usr/bin/env python3
class Research:
    def file_reader(self):
        try:
            with open('data.csv', 'r') as f:
                data = f.read()
        except IOError:
            print("Error with file")
            exit(1)
        return data


def main():
    r = Research()
    print(r.file_reader())


if __name__ == '__main__':
    main()
