#!/usr/bin/env python3
class MustRead:
    try:
        with open('data.csv', 'r') as f:
            data = f.read()
            print(data)
    except IOError:
        print("Error with file")


if __name__ == '__main__':
    MustRead()
