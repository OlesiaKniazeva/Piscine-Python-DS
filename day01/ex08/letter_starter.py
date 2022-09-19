#!/usr/bin/env python3
import sys


def write_letter(email):
    f = open('employees.tsv', 'r')
    for ss in f:
        data = ss.strip().split('\t')
        if data[2] == email:
            print(f'Dear {data[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. '
                  f'That’s a precondition for the professionals that our company hires.')
            return
    print(f'Couldn\'t find user with email \'{email}\'')
    f.close()


def main():
    if len(sys.argv) == 2:
        write_letter(sys.argv[1])
    else:
        print('You should enter one argument')


if __name__ == '__main__':
    main()
