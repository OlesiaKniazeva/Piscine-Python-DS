#!/usr/bin/env python3

import os


def main():
    env = os.getenv('VIRTUAL_ENV')
    if env:
        print('Your current virtual env is', env)
    else:
        print('No virtual env')


if __name__ == '__main__':
    main()

# virtualenv -p python3.10 myael
# source ./myael/bin/activate
# deactivate
