#!/usr/bin/env python3

import os


class WrongEnvironment(Exception):
    pass


if __name__ == '__main__':
    try:
        env = os.getenv('VIRTUAL_ENV')
        if env is None or env.split('/')[-1] != 'myael':
            raise WrongEnvironment('Wrong environment!')
    except WrongEnvironment as v:
        print(v)
    else:
        os.system('pip install beautifulsoup4 PyTest')
        os.system('pip freeze | tee requirements.txt')
        os.system('tar -zcf myael.tar.gz ./myael')




