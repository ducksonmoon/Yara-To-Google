import os

DIR = os.path.dirname(os.path.realpath(__file__))
DIR_FILE = f'{DIR}/fields'


def chaeck_data():
    with open(DIR_FILE, 'r+') as f:
        line = f.readline().strip()
        if line == '':
            username = input("input username: ")
            password = input("input password: ")
            newline = f'{username}:{password}'
            f.write(newline)
            return newline
        else:
            return line


def spilit_data(data):
    a = data.split(':')
    return a
