#!/usr/bin/env python3
import sys


def encode(string, shift):
    result = ""
    for i in range(len(string)):
        char = string[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    print(result)


def decode(string, shift):
    result = ""
    for i in range(len(string)):
        char = string[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    print(result)


def isascii(s):
    return len(s) == len(s.encode())


def main():
    if len(sys.argv) == 4:
        if sys.argv[1] == 'encode' or sys.argv[1] == 'decode':
            if not isascii(sys.argv[2]):
                raise Exception('The script does not support your language yet')
            if not sys.argv[3].isnumeric():
                raise Exception('Enter the number as last argument')
            if sys.argv[1] == 'encode':
                encode(sys.argv[2], int(sys.argv[3]))
            else:
                decode(sys.argv[2], int(sys.argv[3]))
    else:
        raise Exception('Wrong data')


if __name__ == '__main__':
    main()
