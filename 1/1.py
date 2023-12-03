import os
import sys
import re

p = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def run():
    with open(os.path.join(sys.path[0], 'input')) as f:
        lines = f.read().splitlines()
    x = 0
    for line in lines:
        m = re.search('^\D*?(\d|one|two|three|four|five|six|seven|eight|nine).*(\d|one|two|three|four|five|six|seven|eight|nine)\D*?$', line)
        if m == None:
            m = re.search('(\d|one|two|three|four|five|six|seven|eight|nine)', line)
            print(m.group(1))
            if m.group(1) in p:
                x += p[m.group(1)]
            else:
                x += int(m.group(1)) * 11
        else:
            print(m.group(1), m.group(2))
            if m.group(1) in p:
                x += p[m.group(1)]*10
            else:
                x += int(m.group(1))*10
            if m.group(2) in p:
                x += p[m.group(2)]*1
            else:
                x += int(m.group(2))*1
        print(x)
    print(x)

if __name__ == '__main__':
  run()
