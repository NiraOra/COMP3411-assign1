
'''
!/usr/bin/python3
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
formed is obtained from the minimum of 3 and the max capacities of each of the island nodes. 

'''

###################################################################################################

import numpy as np
import sys
import nodeInit
from nodeDefs import waterNode as watN, islandNode as islN

###################################################################################################

def main():
    # Scanning in the map.
    nrow, ncol, map = scan_map()
    # Translating the map into a workable grid.
    grid = nodeInit.nodeInit(map, nrow, ncol)
    
    dfsStack = []

    # Iterate through the grid and fill in the bridges for the special cases first.
    for i in range(nrow):
        for j in range(ncol):
            specialIslands(grid, i , j)

    # Find the starting point of our DFS search.
    startFound, i, j, dfsStack = findStart(grid, nrow, ncol, dfsStack)
    
    # If there are no more possible starting points and the goal is successfully reached,
    # then the puzzle is complete.
    if startFound == False and goalReached(grid, nrow, ncol):
        print("puzzle is FINISHED we are lit!")
        pass
    # Else, call the DFS search.
    else: 
        # print("We continue")
        # print("starting neighbours", grid[(i, j)].printAdjList())
        result = DFSbacktracking(grid[(i, j)], grid, nrow, ncol)
        print(result)
        if goalReached(grid, nrow, ncol):
            print("puzzle is FINISHED!")
        else:
            print("puzzle is NOT finished!")

    # Finally, print the completed grid.
    printMap(nrow, ncol, grid)

###################################################################################################

# Function which prints the entire map.
def printMap(nrow, ncol, map):
    # code = ".123456789abc"
    print("\nMAP:")
    for r in range(nrow):
        for c in range(ncol):
            # to change: once we add the bridge stuff
            # temp = map[(r, c)].getCapacity()
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
def specialIslands(grid, row, col):
    # Only proceed if the node is an island and unvisited.
    if not isinstance(grid[(row, col)],islN.IslandNode):    
        return
    elif grid[(row, col)].visited:
        return
    
    numNeighbours = len(grid[(row, col)].adjList)
    islandCap = grid[(row, col)].maxCapacity - grid[(row, col)].currCapacity
    
    # If the island only has one neighbour, then it must be joined to that
    # neighbour with the amount of bridges that is its own capacity.
    if numNeighbours == 1 and islandCap in [1, 2, 3]:
        numBridges = islandCap
    # If the island is of capacity 6, 9 or 12 with 2, 3 or 4 neighbours respectively,
    # then there is only one possible configuration that it can be connected by.
    elif (numNeighbours == 2 and islandCap == 6) \
        or (numNeighbours == 3 and islandCap == 9) \
        or (numNeighbours == 4 and islandCap == 12):
        numBridges = 3
    else: 
        # If the island is not any of the above cases, return.
        return
    
    # Mark the current island as visited
    grid[(row, col)].visited = True

    # Fill in the bridges between the island and its neighbours.
    for i in range(numNeighbours):
        buildBridge(grid, grid[(row, col)], grid[(row, col)].adjList[i], numBridges)

# Function which builds a given number of bridges in the water nodes between two given islands.
def buildBridge(grid, object, endObject, numBridges):
    row, col = object.row, object.col
    endRow, endCol = endObject.row, endObject.col
    left = up = -1
    right = down = 1

    # If the capacities are already at max or will overflow after adding
    # additional bridges, then return.
    if not updateCapacity(object, endObject, numBridges):
        return False
    # Building bridges to the right.
    elif row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            grid[(row, i)].setBridge(numBridges, "horizontal")
            # grid[(row, i)].verticalCheck = False
    # Building bridges to the left.
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            grid[(row, i)].setBridge(numBridges, "horizontal")
            # grid[(row, i)].verticalCheck = False
    # Building bridges downwards.
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            grid[(i, col)].setBridge(numBridges, "vertical")
            # grid[(i, col)].horizontalCheck = False
    # Building bridges upwards.
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            grid[(i, col)].setBridge(numBridges, "vertical")
            # grid[(i, col)].horizontalCheck = False
            
    return True

# Function which checks if the capacity of the given islands is overfilled.
# Returns true if it is a valid capacity and false if it is overfilled.
def validCapacity(object, endObject, numBridges):
    objectNewCap = object.currCapacity + numBridges
    endObjectNewCap = endObject.currCapacity + numBridges

    # If the current capacity of the islands is already overflowing then return false.
    if object.currCapacity > object.maxCapacity or \
    endObject.currCapacity > endObject.maxCapacity:
        return False
    # Else if the capacity of the islands after adding the bridges will be overflowing,
    # then return false.
    elif objectNewCap > object.maxCapacity or \
    endObjectNewCap > endObject.maxCapacity:
        return False
    else:
        return True

# Function which updates the capacity of the island and its neighbour. 
def updateCapacity(object, endObject, numBridges):
    # First checks if the capacities are valid and will not overflow after the assignment.
    if validCapacity(object, endObject, numBridges):
        object.currCapacity += numBridges
        endObject.currCapacity += numBridges
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
                numBridges = min(3, node.maxCapacity - node.currCapacity, neighbor.maxCapacity - neighbor.currCapacity)
                if numBridges > 0:
                    # Push neighbor to stack with potential bridge info
                    stack.append((neighbor, (node, neighbor, numBridges)))

    return False

# Function to calculate the remaining capacity to be filled for the node.
def remainingValues(node):
    # Calculate the remaining valid connections for the node
    # TODO: change if necessary
    return node.maxCapacity - node.currCapacity

# Function which backtracks on the visited array.
def backtrackingBuild(grid, visited):
    if len(visited) == 1:
        visited.clear()
        return visited
    
    for i in range(len(visited), 1, -1):
        numBridges = min(visited[i].maxCapacity, visited[i - 1].maxCapacity, 3)
        buildBridge(grid, visited[i], visited[i - 1], numBridges)
        visited.remove(visited[i])
    
    return visited

# Function which undoes a bridge between two nodes and reupdates their capacities.
def undoBridge(grid, startNode, endNode, numBridges):
    startNode.currCapacity -= numBridges
    endNode.currCapacity -= numBridges
    # Also, clear the bridge on water nodes between these islands
    clearBridge(grid, startNode, endNode)

# Function which clears the bridges off water nodes, between the starting and end nodes.
def clearBridge(grid, startNode, endNode):
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
                if object.visited and object.currCapacity == object.maxCapacity: 
                    numSolved += 1
                    print("This is island", object.maxCapacity, "and it has current capacity:", object.currCapacity)
    
    print("Number of solved islands is", numSolved, "and Total number of islands is", numIslands)
    # If the number of solved islands is equal to the total number of islands, 
    # then the puzzle is solved and return True.
    if (numSolved == numIslands):
        return True
    else: 
        return False

###################################################################################################

if __name__ == '__main__':
    main()