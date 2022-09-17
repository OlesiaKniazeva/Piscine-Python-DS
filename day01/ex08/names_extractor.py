#!/usr/bin/env python3
import sys


def extract_names(file):
    name = 'employees.tsv'
    f = open(file, 'r')
    out = open(name, 'w')
    out.write('Name\tSurname\tE-mail\n')
    for mail in f:
        data = mail.split('@')[0].split('.')
        out.write(data[0].capitalize() + '\t' + data[1].capitalize() + '\t' +
                  mail)
    f.close()
    out.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        extract_names(sys.argv[1])
    else:
        print('You should enter one argument')
