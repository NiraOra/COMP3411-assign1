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

    # iterate through the grid and fill in the bridges for the special cases first
    for i in range(0, nrow-1):
        for j in range(0, ncol-1):
            specialIslands(grid, i , j)

    DFSbacktracking(dfsStack, grid, nrow, ncol)

    # TO REMOVE: small test LOL
    # print("Just test, ", result[result[(0, 0)].getPosition()].getCapacity()) 
    # -> we can get the position directly (useful for map iteration for example)
    # result = DFShashi(result) -> get a good result
    # print the map
    printMap(nrow, ncol, result)
    
# print map: now can print dictionary
def printMap(nrow, ncol, map):
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

# Filling in the islands which only have one certain bridge configuration possible
def specialIslands(grid, row, col):
    # only proceed if the node is an unvisited island node
    if not isinstance(grid[(row, col)],islN.IslandNode):    
        return
    elif grid[(row, col)].Visited:
        return
    
    numNeighbours = len(grid[(row, col)].stack)
    islandCap = grid[(row, col)].maxCapacity
    
    # checking if the node has only one neighbour and
    # island has capacity 1,2 or 3
    if numNeighbours == 1 and islandCap in [1, 2, 3]:
        numBridges = islandCap
    # checking the number of neighbours for islands of size 6,9 or 12
    elif (numNeighbours == 2 and islandCap == 6) \
        or (numNeighbours == 3 and islandCap == 9) \
        or (numNeighbours == 4 and islandCap == 12):
        numBridges = 3
    else: 
        return
    
    # mark the island as visited
    grid[(row, col)].Visited = True
    # fill in the bridges between the island and its neighbours 
    for i in range[0, numNeighbours-1]:
        buildBridge(grid, grid[(row, col)], grid[(row, col)].stack[i], numBridges)
    
    pass

# DFS backtracking function which iterates through the stack and 
# attempts to connect the neighbours under the constraints.
# If a constraint is violated, it backtracks and retries.
def DFSbacktracking(grid, nrow, ncol, dfsStack):
    if goalReached(): 
        return 

    # If the stack is empty, find the new starting point
    if len(islN.IslandNode.stack) == 0:
        row, col = findStart(grid, nrow, ncol)

    # Iterate through the stack and attempt to place down bridges
    for i in dfsStack[i]:
        neighbourRow, neighbourCol = dfsStack.pop()
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

def buildBridge(grid, object, endObject, numBridges):
    row, col = object.row, object.col
    endRow, endCol = endObject.row, endObject.col
    left = up = -1
    right = down = 1
    
    # building bridges to the right
    if row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            watN.setBridge(grid[(row, i)], numBridges, "horizontal")
            grid[(row, i)].verticalCheck = False
    # building bridges to the left
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            watN.setBridge(grid[(row, i)], numBridges, "horizontal")
            grid[(row, i)].verticalCheck = False
    # building bridges downwards
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            watN.setBridge(grid[(i, col)], numBridges, "vertical")
            grid[(i, col)].horizontalCheck = False
    # building bridges upwards
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            watN.setBridge(grid[(i, col)], numBridges, "vertical")
            grid[(i, col)].horizontalCheck = False

    pass

if __name__ == '__main__':
    main()