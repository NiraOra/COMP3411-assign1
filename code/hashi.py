import numpy as np
import sys
from nodeDefs import node

# map = np.zeros()
# map = 0
# this is just a test. call into the node thing from here
# print(node.nodeInit(map))

def main():
    code = ".123456789abc"
    nrow, ncol, map = scan_map()
    node.nodeInit(map)
    for r in range(nrow):
        for c in range(ncol):
            print(code[map[r][c]],end="")
        print()
        
def scan_map():
    text = []
    for line in sys.stdin:
        row = []
        for ch in line:
            n = ord(ch)
            if n >= 48 and n <= 57:    # between '0' and '9'
                row.append(n - 48)
            elif n >= 97 and n <= 122: # between 'a' and 'z'
                row.append(n - 87)
            elif ch == '.':
                row.append(0)
        text.append(row)

    nrow = len(text)
    ncol = len(text[0])

    map = np.zeros((nrow,ncol),dtype=np.int32)
    for r in range(nrow):
        for c in range(ncol):
            map[r,c] = text[r][c]
    
    return nrow, ncol, map

if __name__ == '__main__':
    main()