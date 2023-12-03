import os
import sys
import re

def run(inp = None):
    if inp != None:
        lines = inp.splitlines()
    else:
        with open(os.path.join(sys.path[0], 'input')) as f:
            lines = f.read().splitlines()

    syms = [{m.start(): [0, 1] for m in re.finditer('[*]', line)} for line in lines]
    t = False
    for i, line in enumerate(lines):
        for m in re.finditer('\d+', line):
            print(m)
            if i > 0:
                s = set(range(m.start()-1, m.end()+1)) & set(syms[i-1].keys())
                if bool(s):
                    for e in s:
                        syms[i-1][e][0] += 1
                        syms[i-1][e][1] *= int(m.group())
            s = set(range(m.start()-1, m.end()+1)) & set(syms[i].keys())
            if bool(s):
                for e in s:
                    syms[i][e][0] += 1
                    syms[i][e][1] *= int(m.group())

            if i < len(lines) - 1:
                s = set(range(m.start()-1, m.end()+1)) & set(syms[i+1].keys())
                if bool(s):
                    for e in s:
                        syms[i+1][e][0] += 1
                        syms[i+1][e][1] *= int(m.group())
    print(syms)
    print([s.values() for s in syms if s.values()][0])
    s = sum([b if a == 2 else 0 for a, b in [i for s in syms if s.values() for i in s.values()]])
    print(s)


if __name__ == '__main__':
    try:
        run(sys.argv[1])
    except:
        run()
