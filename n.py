import os
import sys
import re
sys.path.append('..')
import helpers

def run(inp = None):
    inp = helpers.get_input()
    print(inp)


if __name__ == '__main__':
    ret = run()
    print(ret)
    os.system(f"echo -n '{ret}' | xclip -selection c")
