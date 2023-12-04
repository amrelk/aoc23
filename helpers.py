import os
import sys
import requests
def get_input(day=os.path.basename(os.getcwd())):
    if len(sys.argv) == 2:
        return sys.argv[1]
    if not os.path.isfile('input'):
        inpr = requests.get(f'https://adventofcode.com/2023/day/{day}/input', cookies={'session': '53616c7465645f5f538c2d5716af1c00562e19f66a5dcae989b5dca2b31b4c06a6e25f78c51b316d73ff2d0cc8050c83e01448df0c7f98c09e5d4dbc1fcbda02'})
        with open('input', 'w') as f:
            f.write(inpr.text)
    with open('input') as f:
        return f.read()

def get_lines(day):
    get_input(day).splitlines()
