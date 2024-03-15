#!/usr/bin/python3

'''
Hashi Puzzle - COMP3411 Assignment 1
by Niranjana Arun Menon z5417727 and Sophie Lian z5418296

ANSWER / PROGRAM EXPLANATION
To solve the hashi puzzle, we decided to incorporate a DFS backtracking algorithm along with MRV as a general heuristic. 
Our constraints were that (i) bridges could be of only values 1, 2 or 3 and (ii) bridges could not cross one another.
Furthermore, we used an adjacency list for each island to track its neighbours.

Initially, we considered some constraints for special islands, where they would have only one possible configuration,
and added all the guarenteed bridges.(An example of such a case would be if there is an island 1 with only 1 other node 
connected to it, which would fall under this special island category and allow us to solve for this case immediately.)
Then, we could have a recursive DFS algorithm where it would look at each particular path formed from the parent island to 
the neighbouring island and keep iterating till either
(i) A cyclical path is reached (it reached the parent node)
(ii) The last reached node has no other connections
After which we decide to backtrack the nodes visited and form bridges between them if possible. The number of bridges 
formed is obtained from the minimum and max capacities of each of the island nodes. 

'''

###################################################################################################

import numpy as np
import sys
import nodeInit
from nodeDefs import waterNode as watN, islandNode as islN, valueDefs as vd

###################################################################################################

def main():
    # Scanning in the map.
    nrow, ncol, map = scan_map()
    # Translating the map into a workable grid.
    grid = nodeInit.nodeInit(map, nrow, ncol)
    
    dfsStack = []
    
    # Iterate through the grid and fill in the bridges for the special cases first.
    specialIslands(grid, nrow, ncol, 0)

    # Find the starting point of our DFS search.
    startFound, i, j, dfsStack = findStart(grid, nrow, ncol, dfsStack)
    
    # If there are no more possible starting points and the goal is successfully reached,
    # then the puzzle is complete.
    if startFound == False and goalReached(grid, nrow, ncol):
        pass
    # Else, call the DFS search.
    else: 
        DFSbacktracking(grid[(i, j)], grid, nrow, ncol)

    # Finally, print the completed grid.
    printMap(nrow, ncol, grid)

###################################################################################################

# Function which prints the entire map.
def printMap(nrow, ncol, map):
    print("\n")
    for r in range(nrow):
        for c in range(ncol):
            print(map[(r, c)].printLook(), end=" ")
        print()

# Function to scan in the map.
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

###################################################################################################

# Function which finds the starting point for the DFS search
def findStart(grid, nrow, ncol, dfsStack):
    startFound = False
    startRow = -1
    startCol = -1
    
    # Iterate until we find the first unvisited island 
    for row in range(nrow):
        for col in range(ncol):
            if isinstance(grid[(row, col)], islN.IslandNode) and not grid[(row, col)].visited:
                startRow = row
                startCol = col
                startFound = True
                break
        if startFound:
            break
    
    # If there is a valid start point then 
    # Append the starting island and its neighbours to the DFS Stack
    if startFound:
        dfsStack.append(grid[(startRow, startCol)])

        # Mark the starting island as visited
        grid[(startRow, startCol)].visited = True
        return True, startRow, startCol, dfsStack
    
    # If a start point was not found, then there are no more islands to append
    # to the DFS stack, so return False.
    return False, startRow, startCol, dfsStack

# Function which fills in the bridges of islands which only have one certain 
# bridge configuration possible.
def specialIslands(grid, nrow, ncol, it):
    if goalReached(grid, nrow, ncol):
        return
    for i in range(nrow):
        for j in range(ncol):
            doSpecialIslands(grid, grid[(i, j)])
    it += 1
    if it < nrow * ncol:
        specialIslands(grid, nrow, ncol, it)
    else:
        return

def doSpecialIslands(grid, island):    
    # only proceed if the node is an unvisited island node
    if not isinstance(island, islN.IslandNode):    
        return
    
    numNeighbours = 0
    # counting the number of valid neighbours
    for i in range(len(island.adjList)):
        neighbour = island.adjList[i]
        if validNeighbour(grid, island, neighbour):
            numNeighbours += 1

    # the island's current empty capacity
    islandCap = remainingValues(island)

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
        # if the cases are not there, then returning!
        return
    
    # mark the island as visited
    island.visited = True

    # fill in the bridges between the island and its neighbours 
    for i in range(numNeighbours):
        buildBridge(grid, island, island.adjList[i], numBridges)

    pass

###################################################################################################

def validNeighbour(grid, island, neighbour):
    row, col = island.row, island.col
    endRow, endCol = neighbour.row, neighbour.col
    left = up = -1
    right = down = 1

    if remainingValues(neighbour) == 0:
        return False

    if row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], watN.WaterNode) and grid[(row, i)].bridgeExists:
                return False
    # checking for bridges to the left
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], watN.WaterNode) and grid[(row, i)].bridgeExists:
                return False
    # checking for bridges downwards
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], watN.WaterNode) and grid[(i, col)].bridgeExists:
                return False
    # checking for bridges upwards
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], watN.WaterNode) and grid[(i, col)].bridgeExists:
                return False

    return True

# Function which builds a given number of bridges in the water nodes between two given islands.
def buildBridge(grid, island, neighbour, numBridges):
    if not validNeighbour(grid, island, neighbour):
        return False
    # If the capacities are already at max or will overflow after adding additional bridges, 
    # then return.
    elif not updateCapacity(island, neighbour, numBridges):
        return False

    row, col = island.row, island.col
    endRow, endCol = neighbour.row, neighbour.col
    left = up = -1
    right = down = 1
   
    # Else if the island is unreachable as there are existing bridges, then return.
    if not neighbour.reachable:
        return False
    # Building bridges to the right.
    elif row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            doBuildBridge(neighbour, grid[(row, i)], "horizontal", numBridges)
    # Building bridges to the left.
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            doBuildBridge(neighbour, grid[(row, i)], "horizontal", numBridges)
    # Building bridges downwards.
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            doBuildBridge(neighbour, grid[(i, col)], "vertical", numBridges)
    # Building bridges upwards.
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            doBuildBridge(neighbour, grid[(i, col)], "vertical", numBridges)
            
    return True

# Function which checks if a bridge already exists on the water node
# If so, it does not let new bridges cross over it.
def doBuildBridge(island, water, direction, numBridges):
    if water.bridgeExists:
        island.reachable = False
        return False
    else:
        water.bridgeExists = True
        water.setBridge(numBridges, direction)
        return True

# Function which checks if the capacity of the given islands is overfilled.
# Returns true if it is a valid capacity and false if it is overfilled.
def validCapacity(island, neighbour, numBridges):
    islandNewCap = island.currCapacity + numBridges
    neighbourNewCap = neighbour.currCapacity + numBridges

    # If the current capacity of the islands is already overflowing then return false.
    if island.currCapacity > island.maxCapacity or \
    neighbour.currCapacity > neighbour.maxCapacity:
        return False
    # Else if the capacity of the islands after adding the bridges will be overflowing,
    # then return false.
    elif islandNewCap > island.maxCapacity or \
    neighbourNewCap > neighbour.maxCapacity:
        return False
    else:
        return True

# Function which updates the capacity of the island and its neighbour. 
def updateCapacity(island, neighbour, numBridges):
    # First checks if the capacities are valid and will not overflow after the assignment.
    if validCapacity(island, neighbour, numBridges):
        island.currCapacity += numBridges
        neighbour.currCapacity += numBridges
        return True
    else:
        return False

###################################################################################################

# DFS BACKTRACKING Algorithm
# Checks if the goal is reached, if not, then iterate through the neighbours
# and checks if the bridge can be built, if so, then build the bridge and 
# call the function recursively.
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
        
        # Mark the node as visited and append it to the visited array.
        visited.add(node)
        node.visited = True

        # Optionally build a bridge to the parent node if specified
        if bridge_to_parent:
            buildBridge(grid, *bridge_to_parent)

        # Check if the goal is reached
        if goalReached(grid, nrow, ncol):
            return True

        # Apply MRV heuristic here (sorting the remaining number of islands)
        neighbors = sorted(node.adjList, key=lambda neighbor: remainingValues(neighbor))

        for neighbor in neighbors:
            if neighbor not in visited:
                numBridges = min(3, remainingValues(node), remainingValues(neighbor))
                if numBridges > 0:
                    # Push neighbor to stack with potential bridge info
                    stack.append((neighbor, (node, neighbor, numBridges)))

    return False

# Function to calculate the remaining capacity to be filled for the node.
def remainingValues(node):
    return node.maxCapacity - node.currCapacity
    
# Function which undoes a bridge between two nodes and reupdates their capacities.
def undoBridge(grid, island, neighbour, numBridges):
    island.currCapacity -= numBridges
    neighbour.currCapacity -= numBridges
    neighbour.reachable = True
    # Also, clear the bridge on water nodes between these islands
    clearBridge(grid, island, neighbour)

# Function which clears the bridges off water nodes, between the starting and end nodes.
def clearBridge(grid, island, neighbour):
    row, col = island.row, island.col
    endRow, endCol = neighbour.row, neighbour.col

    if row == endRow:  # Horizontal bridge
        for i in range(min(col, endCol) + 1, max(col, endCol)):
            if isinstance(grid[(row, i)], watN.WaterNode):
                grid[(row, i)].clearBridge()
    elif col == endCol:  # Vertical bridge
        for i in range(min(row, endRow) + 1, max(row, endRow)):
            if isinstance(grid[(i, col)], watN.WaterNode):
                grid[(i, col)].clearBridge()

###################################################################################################

# Function which checks if the goal has been reached and hence whether the puzzle has been solved.
def goalReached(grid, nrow, ncol):
    numSolved = 0
    numIslands = 0
    # End condition: if all the islands have been visited and their capacities are full.
    for i in range(nrow):
        for j in range(ncol):
            if isinstance(grid[(i, j)], islN.IslandNode):
                numIslands += 1
                object = grid[(i, j)]
                if object.currCapacity == object.maxCapacity: 
                    numSolved += 1
    
    # If the number of solved islands is equal to the total number of islands, 
    # then the puzzle is solved and return True.
    if (numSolved == numIslands):
        return True
    else: 
        return False

###################################################################################################

if __name__ == '__main__':
    main()

###################################################################################################

