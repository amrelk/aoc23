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
        i = [int(e) for e in r.findall(line)]
        if max(i) > 12: continue
        i = [int(e) for e in g.findall(line)]
        if max(i) > 13: continue
        i = [int(e) for e in b.findall(line)]
        if max(i) > 14: continue
        sum += int(gm.match(line).group(1))
    print(sum)
  

if __name__ == '__main__':
    run()
