#!/usr/bin/python3
import numpy as np
import sys
import nodeInit
from nodeDefs import waterNode as watN, islandNode as islN

def main():
    # get map
    nrow, ncol, map = scan_map()
    # get resultant dict
    result = nodeInit.nodeInit(map, nrow, ncol)
    # TEMP: just for debugging purposes
    # debug(nrow, ncol, result)

    grid = map
    dfsStack = []

    case_one_neighbour()

    DFSbacktracking(dfsStack, grid, nrow, ncol)

    # TO REMOVE: small test LOL
    # print("Just test, ", result[result[(0, 0)].getPosition()].getCapacity()) 
    # -> we can get the position directly (useful for map iteration for example)
    # result = DFShashi(result) -> get a good result
    # print the map
    printE(nrow, ncol, result)
    
# print map: now can print dictionary
def printE(nrow, ncol, map):
    # code = ".123456789abc"
    print("\nMAP:")
    for r in range(nrow):
        for c in range(ncol):
            # to change: once we add the bridge stuff
            # temp = map[(r, c)].getCapacity()
            print(map[(r, c)].printLook(), end=" ")
        print()
        
# just for debugging purposes
def debug(nrow, ncol, dict):
    print("Dict as follows\n")
    for i in range(nrow):
        for j in range(ncol):
            # here, ideally should be able to call the function in itself in the end
            print("the value at the node {", i, j, "} is ", dict[(i, j)].getCurrCapacity())
      
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

# If an only has one neighbour, then it must be connected
# by the same number of bridges as the max capacity of the island
def case_one_neighbour(grid, row, col):
    if grid[row, col].Visited:
        return
    # checking if the node has only one neighbour
    elif len(grid[row, col].stack) == 1:
        grid[row, col].Visited = True
        buildBridge(grid[row, col].stack[0])
    pass

def case_two_neighbours():
        pass

# DFS backtracking function which iterates through the stack and 
# attempts to connect the neighbours under the constraints.
# If a constraint is violated, it backtracks and retries.
def DFSbacktracking(grid, nrow, ncol):
    if goalReached(): 
        return 

    # If the stack is empty, find the new starting point
    if len(islN.IslandNode.stack) == 0:
        row, col = findStart(grid, nrow, ncol)

    # Iterate through the stack and attempt to place down bridges
    for i in islN.IslandNode.stack[i]:
        neighbourRow, neighbourCol = islN.IslandNode.stack.pop()
        if row == neighbourRow:
            col - neighbourCol
            pass
        elif col == neighbourCol:
            pass
    pass

# Function which finds the starting point for the search
def findStart(grid, nrow, ncol):
    # Iterate until we find the first island that is unvisited
    for i in range(0, nrow):
        for j in range(0, ncol):
            if isinstance(grid[(i, j)], islN.IslandNode) and \
                not grid[(i, j)].Visited:
                # Append the start to the stack and find its neighbours
                islN.IslandNode.stack.putStack(grid[(i,j)])
                nodeInit.findNeighbours(grid[(i,j)], grid, nrow, ncol)
                break
    return i, j


# Function which checks if the goal has been reached.
def goalReached():
    numSolved = 0
    # End condition: if all the islands have been visited and
    # their capacities are full.
    for i in islN.IslandNode.adjList[i]: # iterating through all the adj list and not the neighbours? needs to check
        if islN.getCurrCapacity(islN.IslandNode.adjList[i]) == islN.getCapacity(islN.IslandNode.adjList[i]) \
            and islN.IslandNode.Visited:
            numSolved += 1
    # If all the adjacency lists are solved then the puzzle is complete
    if (numSolved == i):
        return True
    return False

def buildBridge():
    
    pass


# TODO print the resultant map with all the appropriate bridges in place
def printMap(map):
    print()
    pass

if __name__ == '__main__':
    main()