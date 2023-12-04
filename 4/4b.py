import os
import sys
import re
sys.path.append('..')
import helpers

def run(inp = None):
    inp = helpers.get_input().splitlines()
    copies = [1] * len(inp)
    print(copies)
    for li, line in enumerate(inp):
        w = re.search(':([\d ]+)\|', line)
        o = re.search('\|([\d ]+)', line)
        winners = set()
        ours = set()
        for i in range(len(w.group(1))//3):
            winners.add(int(w.group(1)[i*3+1:i*3+3]))
        for i in range(len(o.group(1))//3):
            ours.add(int(o.group(1)[i*3+1:i*3+3]))
        p = len(ours & winners)
        print(p)
        for i in range(1, p+1):
            copies[li+i] += copies[li]
    print(copies)
    return sum(copies)


if __name__ == '__main__':
    ret = run()
    print(ret)
