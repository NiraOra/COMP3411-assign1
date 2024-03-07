import numpy as np
import sys
from nodeDefs import node, valueDefs

def main():
    # get map
    nrow, ncol, map = scan_map()
    # get resultant dict
    result = node.nodeInit(map)
    # TEMP: just for debugging purposes
    debug(nrow, ncol, result)
    # print the map
    printE(nrow, ncol, map)
    
    
# print map
def printE(nrow, ncol, map):
    code = ".123456789abc"
    print("\nMAP:")
    for r in range(nrow):
        for c in range(ncol):
            print(code[map[r][c]],end=" ")
        print()
        
# just for debugging purposes
def debug(nrow, ncol, dict):
    print("Dict as follows\n")
    for i in range(nrow):
        for j in range(ncol):
            array = dict[(i, j)]
            print("the value at the node {", i, j, "} is ", array[0])
      
# 1st step: to scan the map  
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