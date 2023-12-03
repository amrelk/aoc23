import os
import sys
import re

def run(inp = None):
    if inp != None:
        lines = inp.splitlines()
    else:
        with open(os.path.join(sys.path[0], 'input')) as f:
            lines = f.read().splitlines()

    syms = [[m.start() for m in re.finditer('[^\w\.\\n]', line)] for line in lines]
    sum = 0
    t = False
    for i, line in enumerate(lines):
        for m in re.finditer('\d+', line):
            print(m)
            if i > 0:
                if bool(set(range(m.start()-1, m.end()+1)) & set(syms[i-1])):
                    t = True
            if bool(set(range(m.start()-1, m.end()+1)) & set(syms[i])):
                t = True
            if i < len(lines)-1:
                if bool(set(range(m.start()-1, m.end()+1)) & set(syms[i+1])):
                    t = True
            if t:
                sum += int(m.group())
            t = False
    print(sum)
    #print(syms)


if __name__ == '__main__':
    try:
        run(sys.argv[1])
    except:
        run()
