#!/usr/bin/python3
# EXPLANATION
# For solving the hashi puzzle, we decided to incorporate a DFS backtracking method along with a MRV approach
# and add some constraints to make sure that we were able to find a correct path for the hashi puzzle given.
#
# Data Structure: To implement this approach, we decided to convert each value on the map scanned from input
# to a node, which can be classified as:
# 1. IslandNode: nodes  representing islands which contain the maximum capacity of the bridges that the island can hold.
# 2. WaterNode: nodes representing the water "." in which a bridge may or may not be built.
# 
# IslandNode consists of:
# 1. Row value
# 2. Column value
# 3. Capacity
# 4. Neighbours array: holds the neighbours and orientation of connection it makes (horizontal or vertical)
# and it is ordered based on the capacity
# 
# and WaterNode consists of:
# 1. Row value
# 2. Column value
# 3. Capacity
# 4. bridgeType: if a bridge was built, then we could assign it the value so it is easier to print
#
# Algorithm:
# 1. We first iterate through the map scanned from input and create islandNodes and waterNodes. 
# 2. We then iterate through the map to add the neighbours for each instance of an island node
# 3. Then, we consider some constraints (ie, some special cases for the hashi puzzle) and add all the guarenteed bridges
# An example of such a case would be if there is an island 1 with only 1 other node connected to it, which would fall under this 
# category and allow us to solve for this case easily
# 4. We then move on to find out the island that we need to start from after solving for the special cases.
# 5. After this, we use DFS backtracking to build the bridges recursively. The idea here is to 
# look at each particular path formed from the parent to the neighbour and keep iterating till either
# (i) A cyclical path is reached (it reached the parent node)
# (ii) The last reached node has no other connections
# After which we decide to backtrack the nodes visited and form bridges between them if possible. 
# The number of bridges formed is obtained from the minimum of 3 and the max capacities of each of the island nodes. 
#
# EXAMPLE (just special cases)
# Input: 
# 1 . 1
# . . .
# 
# Here, we see that the island at (0, 0) has only one other connection [1], which
# makes it easy for us to form a connection without having to backtrack, giving us
# the following output:
#
# Output: 
# 1 - 1
# 
#
# EXAMPLE (normal)
# Input: 


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

    grid = result
    
    dfsStack = []

    # iterate through the grid and fill in the bridges for the special cases first
    for i in range(nrow):
        for j in range(ncol):
            specialIslands(grid, i , j)

    found, i, j, dfsStack = findStart(grid, nrow, ncol, dfsStack)
    
    if found == False and goalReached(grid, nrow, ncol):
        print("puzzle is FINISHED we are lit!")
    else: 
        print('We continue')
        print("starting neighbours", grid[(i, j)].printAdjList())
        # print("dfs adjList", dfsStack)
        hi = DFSbacktracking(grid[(i, j)], grid, nrow, ncol)
        print(hi)
        if goalReached(grid, nrow, ncol):
            print("puzzle is FINISHED!")
        else:
            print("puzzle is NOT finished!")

    # TO REMOVE: small test LOL
    # print("Just test, ", result[result[(0, 0)].getPosition()].getCapacity()) 
    # -> we can get the position directly (useful for map iteration for example)
    # result = DFShashi(result) -> get a good result
    # print the map
    printMap(nrow, ncol, grid)
    
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

# Function which finds the starting point for the search
def findStart(grid, nrow, ncol, dfsStack):
    # Iterate until we find the first island that is unvisited
    # startFound = False
    startRow = -1
    startCol = -1
    
    for row in range(nrow):
        for col in range(ncol):
            # print(grid[(row, col)].printLook())
            if isinstance(grid[(row, col)], islN.IslandNode) and \
            not grid[(row, col)].visited:
                startRow = row
                startCol = col
                break
    
    # If there is a valid start point then continue
    # Append the starting island and its neighbours to the DFS Stack
    if startRow != -1 and startCol != -1:
        print("111 ", startRow, startCol)
        dfsStack.append(grid[(startRow, startCol)])
        # for i in range(len(grid[(startRow, startCol)].adjList)):
        #     dfsStack.append(grid[(startRow, startCol)].adjList[i])
        # Mark the starting island as visited
        grid[(startRow, startCol)].visited = True
        return True, startRow, startCol, dfsStack
    
    # SMALL case: if all the special islands are filled and there is no more
    # to be appended then take care of that -> ie, return that there is no more
    # islands to be appended
    return False, startRow, startCol, dfsStack

# Filling in the islands which only have one certain bridge configuration possible
def specialIslands(grid, row, col):
    # only proceed if the node is an unvisited island node
    if not isinstance(grid[(row, col)],islN.IslandNode):    
        return
    elif grid[(row, col)].visited:
        # print(grid[(row, col)])
        return
    
    numNeighbours = len(grid[(row, col)].adjList)
    islandCap = grid[(row, col)].maxCapacity - grid[(row, col)].currCapacity
    
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
        # if the cases r not there, then returning!
        return
    
    # mark the island as visited
    grid[(row, col)].visited = True

    # fill in the bridges between the island and its neighbours 
    for i in range(numNeighbours):
        buildBridge(grid, grid[(row, col)], grid[(row, col)].adjList[i], numBridges)

# Function which builds bridges in the water nodes between islands
def buildBridge(grid, object, endObject, numBridges):
    row, col = object.row, object.col
    endRow, endCol = endObject.row, endObject.col
    left = up = -1
    right = down = 1

    # if the capacities are already at max or will overflow after adding
    # the bridges, then return early
    if not updateCapacity(object, endObject, numBridges):
        return False
    # building bridges to the right
    elif row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            grid[(row, i)].setBridge(numBridges, "horizontal")
            # grid[(row, i)].verticalCheck = False
    # building bridges to the left
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            grid[(row, i)].setBridge(numBridges, "horizontal")
            # grid[(row, i)].verticalCheck = False
    # building bridges downwards
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            grid[(i, col)].setBridge(numBridges, "vertical")
            # grid[(i, col)].horizontalCheck = False
    # building bridges upwards
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            grid[(i, col)].setBridge(numBridges, "vertical")
            # grid[(i, col)].horizontalCheck = False
            
    return True

# Checks if the capacity of the given islands is overfilled
# Returns true if it is a valid capacity and false if it is overfilled.
def validCapacity(object, endObject, numBridges):
    objectNewCap = object.currCapacity + numBridges
    endObjectNewCap = endObject.currCapacity + numBridges

    # If the current capacity of the islands is already overflowing
    # then return false 
    if object.currCapacity > object.maxCapacity or \
    endObject.currCapacity > endObject.maxCapacity:
        return False
    # Else if the capacity of the islands after adding the bridges
    # will be overflowing then return false
    elif objectNewCap > object.maxCapacity or \
    endObjectNewCap > endObject.maxCapacity:
        return False
    else:
        return True

# Updates the capacity of the island and its neighbour. 
def updateCapacity(object, endObject, numBridges):
    if validCapacity(object, endObject, numBridges):
        object.currCapacity += numBridges
        endObject.currCapacity += numBridges
        return True
    else:
        return False


# DFS BACKTRACKING code
# basically: check if the goal is reached, if not, then iterate through the neighbours
# and check if the bridge can be built, if yes, then build the bridge and call the function
# recursively
def DFSbacktracking(currNode, grid, nrow, ncol):
    stack = [(currNode, None)]  # Stack now holds tuples of (node, bridge_to_parent)
    visited = set()

    while stack:
        node, bridge_to_parent = stack.pop()
        if node in visited:
            # If revisiting a node, undo the last bridge if it exists
            if bridge_to_parent:
                undoBridge(grid, *bridge_to_parent)
            continue

        visited.add(node)
        node.visited = True

        # Optionally build a bridge to the parent node if specified
        if bridge_to_parent:
            buildBridge(grid, *bridge_to_parent)

        # Check if goal is reached
        if goalReached(grid, nrow, ncol):
            return True

        # Apply MRV heuristic here (sorting the remaining number of islands. yes)
        neighbors = sorted(node.adjList, key=lambda neighbor: remainingValues(neighbor))

        for neighbor in neighbors:
            if neighbor not in visited:
                numBridges = min(3, node.maxCapacity - node.currCapacity, neighbor.maxCapacity - neighbor.currCapacity)
                if numBridges > 0:
                    # Push neighbor to stack with potential bridge info
                    stack.append((neighbor, (node, neighbor, numBridges)))

    return False

def remainingValues(node):
    # Calculate the remaining valid connections for the node
    # TODO: change if necessary
    return node.maxCapacity - node.currCapacity

def backtrackingBuild(grid, visited):
    if len(visited) == 1:
        visited.clear()
        return visited
    
    for i in range(len(visited), 1, -1):
        numBridges = min(visited[i].maxCapacity, visited[i - 1].maxCapacity, 3)
        buildBridge(grid, visited[i], visited[i - 1], numBridges)
        visited.remove(visited[i])
    
    return visited

def undoBridge(grid, startNode, endNode, numBridges):
    # This function undoes a bridge between two nodes, adjusting their capacities back
    startNode.currCapacity -= numBridges
    endNode.currCapacity -= numBridges
    # Also, clear the bridge on water nodes between these islands
    clearBridge(grid, startNode, endNode)

def clearBridge(grid, startNode, endNode):
    # Clears the bridge between startNode and endNode
    row, col = startNode.row, startNode.col
    endRow, endCol = endNode.row, endNode.col

    if row == endRow:  # Horizontal bridge
        for i in range(min(col, endCol) + 1, max(col, endCol)):
            if isinstance(grid[(row, i)], watN.WaterNode):
                grid[(row, i)].clearBridge()
    elif col == endCol:  # Vertical bridge
        for i in range(min(row, endRow) + 1, max(row, endRow)):
            if isinstance(grid[(i, col)], watN.WaterNode):
                grid[(i, col)].clearBridge()

# Function which checks if the goal has been reached.
def goalReached(grid, nrow, ncol):
    numSolved = 0
    numIslands = 0
    # End condition: if all the islands have been visited and
    # their capacities are full.
    for i in range(nrow):
        for j in range(ncol):
            if isinstance(grid[(i, j)], islN.IslandNode):
                numIslands += 1
                object = grid[(i, j)]
                if object.visited and object.currCapacity == object.maxCapacity: 
                    numSolved += 1
                    print("This is island", object.maxCapacity, "and it has current capacity:", object.currCapacity)
    
    print("Number of solved islands is", numSolved, "and Total number of islands is", numIslands)
    # If the number of solved islands is equal to the total number of islands,
    # then the puzzle is solved.
    if (numSolved == numIslands):
        return True
    else: 
        return False

if __name__ == '__main__':
    main()