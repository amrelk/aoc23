import os
import sys
import re

r = re.compile('(\d+) red')
g = re.compile('(\d+) green')
b = re.compile('(\d+) blue')
gm = re.compile('Game (\d+):')

def run():
    with open(os.path.join(sys.path[0], 'input')) as f:
        lines = f.read().splitlines()

    sum = 0
    for line in lines:
        ri = [int(e) for e in r.findall(line)]
        gi = [int(e) for e in g.findall(line)]
        bi = [int(e) for e in b.findall(line)]
        sum += max(ri)*max(bi)*max(gi) 
    print(sum)
  

if __name__ == '__main__':
    run()
