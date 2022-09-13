#!/usr/bin/env python3

import os

if __name__ == '__main__':
    env = os.getenv('VIRTUAL_ENV')
    if env:
        print('Your current virtual env is', env)
    else:
        print('No virtual env')

# virtualenv -p python3.10 myael
# source ./myael/bin/activate
# deactivate
