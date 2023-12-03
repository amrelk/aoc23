import os
import sys
import re

def run(inp = None):
    if inp != None:
        lines = inp.splitlines()
    else:
        with open(os.path.join(sys.path[0], 'input')) as f:
            lines = f.read().splitlines()

    print(lines)

if __name__ == '__main__':
    try:
        run(sys.argv[1])
    except:
        run()
