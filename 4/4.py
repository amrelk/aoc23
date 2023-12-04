import os
import sys
import re
sys.path.append('..')
import helpers

def run(inp = None):
    inp = helpers.get_input().splitlines()
    print(inp)
    sum = 0
    for line in inp:
        w = re.search(':([\d ]+)\|', line)
        o = re.search('\|([\d ]+)', line)
        winners = set()
        ours = set()
        for i in range(len(w.group(1))//3):
            winners.add(int(w.group(1)[i*3+1:i*3+3]))
        for i in range(len(o.group(1))//3):
            ours.add(int(o.group(1)[i*3+1:i*3+3]))
        if len(ours & winners) != 0:
            sum += 2**(len(ours & winners) -1)
    return sum


if __name__ == '__main__':
    ret = run()
    print(ret)
    os.system(f"echo -n '{ret}' | xclip -selection c")
