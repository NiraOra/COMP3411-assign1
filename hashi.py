#!/usr/bin/python3
import numpy as np
import sys
import nodeInit
from nodeDefs import waterNode as watN, islandNode as islN, valueDefs as vd

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

    it = 0
    doSolver(grid, nrow, ncol, it)

    '''
    startFound, i, j, dfsStack = findStart(grid, nrow, ncol, dfsStack)
    
    if startFound == False and goalReached(grid, nrow, ncol):
        print("puzzle is FINISHED we are lit!")
    else: 
        print('We continue')
        print("starting neighbours", grid[(i, j)].printAdjList())
        # print("dfs adjList", dfsStack)
        res = DFSbacktracking(grid[(i, j)], grid, nrow, ncol, dfsStack)
        print("resulting map reads:", res)
        # if goalReached(grid, nrow, ncol):
        #     print("puzzle is FINISHED!")
        # else:
        #     print("puzzle is NOT finished!")

    '''
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
    startFound = False
    startRow = -1
    startCol = -1
    
    for row in range(nrow):
        for col in range(ncol):
            # print(grid[(row, col)].printLook())
            if isinstance(grid[(row, col)], islN.IslandNode) and \
            not grid[(row, col)].visited:
                startFound = True
                break
        if startFound:
            break

    startRow = row
    startCol = col

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
    if not isinstance(grid[(row, col)], islN.IslandNode):    
        return
    elif grid[(row, col)].visited:
        # print(grid[(row, col)])
        return
    
    numNeighbours = len(grid[(row, col)].adjList)
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
        # if the cases r not there, then returning!
        return
    
    # mark the island as visited
    grid[(row, col)].visited = True

    # fill in the bridges between the island and its neighbours 
    for i in range(numNeighbours):
        buildBridge(grid, grid[(row, col)], grid[(row, col)].adjList[i], numBridges)
    
    pass

def doSolver(grid, nrow, ncol, it):
    if allVisited(grid, nrow, ncol):
        print("all has been visited")
        return
    if goalReached(grid, nrow, ncol):
        print("goal has been reached in doSolver")
        return
    for i in range(nrow):
        for j in range(ncol):
            recursiveSolver(grid, grid[(i, j)])
    it += 1
    if it < nrow * ncol:
        doSolver(grid, nrow, ncol, it)
    else:
        return
    pass
        
def allVisited(grid, nrow, ncol):
    numIslands = numVisited = 0
    for i in range(nrow):
        for j in range(ncol):
            if isinstance(grid[(i, j)], islN.IslandNode):
                numIslands += 1
                object = grid[(i, j)]
                if object.visited: 
                    numVisited += 1
   
    if numVisited == numIslands:
        return True
    else:
        return False

def recursiveSolver(grid, object):    
    # only proceed if the node is an unvisited island node
    if not isinstance(object, islN.IslandNode):    
        return
    elif object.visited:
        return
    
    numNeighbours = 0
    # counting the number of unsolved or unvisited neighbours
    for neighbour in range(len(object.adjList)):
        if not object.adjList[neighbour].visited:
            numNeighbours+=1

    # the island's current empty capacity
    islandCap = object.maxCapacity - object.currentCapacity
    actualNeighbours = 0

    for i in range(numNeighbours):
        neighbour = object.adjList[i]
        if validNeighbours(grid, object, neighbour):
            object.popStack(neighbour)
            actualNeighbours += 1

    print("numNeighbours vs actualNeighbours for island", object.row, object.col, "is", numNeighbours, actualNeighbours)
    numNeighbours = actualNeighbours

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
    object.visited = True

    # fill in the bridges between the island and its neighbours 
    for i in range(numNeighbours):
        buildBridge(grid, object, object.adjList[i], numBridges)

    pass

def validNeighbours(grid, object, endObject):
    row, col = object.row, object.col
    endRow, endCol = endObject.row, endObject.col

    left = up = -1
    right = down = 1
    
    if row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            if not grid[(row, i)].bridgeType == vd.WATER:
                return False
    # building bridges to the left
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            if not grid[(row, i)].bridgeType == vd.WATER:
                return False
    # building bridges downwards
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            if not grid[(i, col)].bridgeType == vd.WATER:
                return False
    # building bridges upwards
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            if not grid[(i, col)].bridgeType == vd.WATER:
                return False

    return True

def skipNeighbour(object, endObject):
    for i in range(len(object.adjList)):
        if object.adjList[i].row == endObject.row and object.adjList[i].col == endObject.col:
            return True
    return False

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
            if grid[(row, i)].horizontalCheck:
                grid[(row, i)].setBridge(numBridges, "horizontal")
                grid[(row, i)].verticalCheck = False
    # building bridges to the left
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            if grid[(row, i)].horizontalCheck:
                grid[(row, i)].setBridge(numBridges, "horizontal")
                grid[(row, i)].verticalCheck = False
    # building bridges downwards
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            if grid[(i, col)].verticalCheck:
                grid[(i, col)].setBridge(numBridges, "vertical")
                grid[(i, col)].horizontalCheck = False
    # building bridges upwards
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            if grid[(i, col)].verticalCheck:
                grid[(i, col)].setBridge(numBridges, "vertical")
                grid[(i, col)].horizontalCheck = False
    pass


# Checks if the capacity of the given islands is overfilled
# Returns true if it is a valid capacity and false if it is overfilled.
def validCapacity(object, endObject, numBridges):
    objectNewCap = object.currentCapacity + numBridges
    endObjectNewCap = endObject.currentCapacity + numBridges

    # If the current capacity of the islands is already overflowing
    # then return false 
    if object.currentCapacity > object.maxCapacity or \
    endObject.currentCapacity > endObject.maxCapacity:
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
        object.currentCapacity += numBridges
        endObject.currentCapacity += numBridges
        print("capacities updated for island", object.row, object.col, "by this number of bridges", numBridges)
        print("capacities of island and neighbour are", object.currentCapacity, endObject.currentCapacity)
        return True
    else:
        return False

# DFS backtracking function which iterates through the adjList and 
# attempts to connect the neighbours under the constraints.
# If a constraint is violated, it backtracks and retries.
def DFSbacktracking(currNode: islN.IslandNode, grid, nrow, ncol, visited_temp):
    # Base case: If the current node has been visited, return that its done ?
    # if len(visited_temp) == 1 and currNode in visited_temp:
    #     print("here")
    #     return True
    
    # TODO
    # if the stack is empty, then the current connections are finished
    # so find the new starting position. 
  
    '''
    # if cyclical 
    if visited_temp[0].row == currNode.row and visited_temp[0].col == currNode.col:
        visited_temp = backtrackBuild(grid, visited_temp, 1)
        return True
        # DFSbacktracking(some[i][0], grid, nrow, ncol, visited_temp)
    '''

    some = currNode.adjList
    print("current node's adjacency list", currNode.printAdjList())
    counter = 0
    
    for i in range(len(some)):
        # if there is nothing more, backtrack build
        counter = counter + 1
        # if the visited array has 1 more left and it is the current node
        # backtrack build the array and then update the visited array accordingly
        if len(some) == 1 and currNode in some:
            visited_temp = backtrackBuild(grid, visited_temp, counter)
            DFSbacktracking(some[i][0], grid, nrow, ncol, visited_temp)
        # else if it is cyclical (like 4 -> 4 -> 4 -> 4 (first node))
        # implement this!!
        
        # if it is satisfied, then done
        visited_temp.append(some[i])
        # otherwise, continue on
        DFSbacktracking(some[i][0], grid, nrow, ncol, visited_temp)
    
    return False

def backtrackBuild(grid, visited, endNum):
    for i in range(len(visited), endNum, -1):
        # basically setting the bridge 
        buildBridge(grid, visited[i], visited[i - 1], min(visited[i], visited[i - 1]))
        # remove the node that the bridge was built on
        visited.remove(visited[i])
        
    return visited


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
                if object.visited and object.currentCapacity == object.maxCapacity: 
                    numSolved += 1
                    print("This is island", object.maxCapacity, "and it has current capacity:", object.currentCapacity)
    
    print("Number of solved islands is", numSolved, "and Total number of islands is", numIslands)
    # If the number of solved islands is equal to the total number of islands,
    # then the puzzle is solved.
    if (numSolved == numIslands):
        return True
    else: 
        return False

if __name__ == '__main__':
    main()

'''
# Function which finds the starting point for the search
def findStart(grid, nrow, ncol, dfsStack):
    # Iterate until we find the first island that is unvisited
    startFound = False
    startRow = -1
    startCol = -1
    
    for row in range(nrow):
        for col in range(ncol):
            # print(grid[(row, col)].printLook())
            if isinstance(grid[(row, col)], islN.IslandNode) and \
            not grid[(row, col)].visited:
                startFound = True
                break
        if startFound:
            break

    startRow = row
    startCol = col

    # If there is a valid start point then continue
    # Append the starting island and its neighbours to the DFS Stack
    if startRow != -1 and startCol != -1:
        print("111 ", startRow, startCol)
        pushNeighbours(grid[(row, col)], dfsStack)

        # Mark the starting island as visited
        grid[(startRow, startCol)].visited = True
        return True, startRow, startCol, dfsStack
    
    # SMALL case: if all the special islands are filled and there is no more
    # to be appended then take care of that -> ie, return that there is no more
    # islands to be appended
    return False, startRow, startCol, dfsStack


# Function which builds bridges in the water nodes between islands
def buildBridge(grid, object, endObject, numBridges):
    row, col = object.row, object.col
    endRow, endCol = endObject.row, endObject.col
    left = up = -1
    right = down = 1

    numBridges += object.currentCapacity

    # if the capacities are already at max or will overflow after adding
    # the bridges, then return early
    if not updateCapacity(object, endObject, numBridges):
        return False
    # building bridges to the right
    elif row == endRow and col < endCol: 
        for i in range(col, endCol, right):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            if grid[(row, i)].horizontalCheck:
                grid[(row, i)].setBridge(numBridges, "horizontal")
                grid[(row, i)].verticalCheck = False
    # building bridges to the left
    elif row == endRow and col > endCol:
        for i in range(col, endCol, left):
            if isinstance(grid[(row, i)], islN.IslandNode):
                continue
            if grid[(row, i)].horizontalCheck:
                grid[(row, i)].setBridge(numBridges, "horizontal")
                grid[(row, i)].verticalCheck = False
    # building bridges downwards
    elif col == endCol and row < endRow:
        for i in range(row, endRow, down):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            if grid[(i, col)].verticalCheck:
                grid[(i, col)].setBridge(numBridges, "vertical")
                grid[(i, col)].horizontalCheck = False
    # building bridges upwards
    else: 
        for i in range(row, endRow, up):
            if isinstance(grid[(i, col)], islN.IslandNode):
                continue
            if grid[(i, col)].verticalCheck:
                grid[(i, col)].setBridge(numBridges, "vertical")
                grid[(i, col)].horizontalCheck = False

    pass


# Pushes the neighbours of the island onto the DFS stack
def pushNeighbours(object, dfsStack):
    for i in range(0, len(object.adjList)):
        dfsStack.append([object, object.adjList[i][0]])
    pass

# Checks if the capacity of the given islands is overfilled
# Returns true if it is a valid capacity and false if it is overfilled.
def validCapacity(object, endObject, numBridges):
    objectNewCap = object.currentCapacity + numBridges
    endObjectNewCap = endObject.currentCapacity + numBridges

    # If the current capacity of the islands is already overflowing
    # then return false 
    if object.currentCapacity > object.maxCapacity or \
    endObject.currentCapacity > endObject.maxCapacity:
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
        object.currentCapacity += numBridges
        endObject.currentCapacity += numBridges
        return True
    else:
        return False

<<<<<<< HEAD
# Checks if the island is unvisited and below max capacity.
def validStep(object):
    if not object.visited:
        return True 
    elif object.visited and object.currentCapacity < object.maxCapacity:
        return True
    else:
        return False

#**********************************************************************

def DFSbacktracking2(grid, nrow, ncol, dfsStack, start, neighbour):
    visited = []

    doDFSbacktracking(grid, nrow, ncol, dfsStack, visited, start, neighbour)
    pass

# DFS backtracking function which iterates through the stack and 
# attempts to connect the neighbours under the constraints.
# If a constraint is violated, it backtracks and retries.
def doDFSbacktracking(grid, nrow, ncol, dfsStack, visited, parent, island):
    printMap(nrow, ncol, grid)

    if goalReached(grid, nrow, ncol): 
        return True
    
    # If the stack is empty, find the new starting point
    if len(dfsStack) == 0:
        row, col = findStart(grid, nrow, ncol)
        parent = grid[(row, col)]
        island = parent.stack[0][0]

    visited.append([parent, island])

    for i in range(len(dfsStack)-1, 0, -1):
        island = dfsStack[i][0]
        neighbour = dfsStack[i][1]
        dfsStack.pop()

        for numBridges in range (1, 3):
            if validStep(neighbour):
                pushNeighbours(island, dfsStack)
                buildBridge(grid, island, neighbour, numBridges)
                neighbour.visited = True
                doDFSbacktracking(grid, nrow, ncol, dfsStack, visited, island, neighbour)
            
                # failed so bactkrack
                neighbour.visited = False
                visited = backtrackBuild(grid, visited, len(visited)-1)
                doDFSbacktracking(grid, nrow, ncol, dfsStack, visited, island, visited[len(visited)-1][0])

    
    pass
=======


# DFS backtracking function which iterates through the adjList and 
# attempts to connect the neighbours under the constraints.
# If a constraint is violated, it backtracks and retries.
def DFSbacktracking(currNode: islN.IslandNode, grid, nrow, ncol, visited_temp):
    # Base case: If the current node has been visited, return that its done ?
    # if len(visited_temp) == 1 and currNode in visited_temp:
    #     print("here")
    #     return True
    
    # if cyclical
    if visited_temp[0].row == currNode.row and visited_temp[0].col == currNode.col:
        visited_temp = backtrackBuild(grid, visited_temp, 1)
        return True
        # DFSbacktracking(some[i][0], grid, nrow, ncol, visited_temp)

    some = currNode.adjList
    # print(some)
    counter = 0
    
    for i in range(len(some)):
        # if there is nothing more, backtrack build
        counter = counter + 1
        # if the visited array has 1 more left and it is the current node
        # backtrack build the array and then update the visited array accordingly
        if len(some) == 1 and currNode in some:
            visited_temp = backtrackBuild(grid, visited_temp, counter)
            DFSbacktracking(some[i][0], grid, nrow, ncol, visited_temp)
        # else if it is cyclical (like 4 -> 4 -> 4 -> 4 (first node))
        # implement this!!
        
        # if it is satisfied, then done
        visited_temp.append(some[i])
        # otherwise, continue on
        DFSbacktracking(some[i][0], grid, nrow, ncol, visited_temp)
    
    return False

def backtrackBuild(grid, visited, endNum):
    for i in range(len(visited), endNum, -1):
        # basically setting the bridge 
        buildBridge(grid, visited[i], visited[i - 1], min(visited[i], visited[i - 1]))
        # remove the node that the bridge was built on
        visited.remove(visited[i])
        
    return visited


def backtrackBuild(grid, visited, endNum):
    for i in range(len(visited), endNum, -1):
        # basically setting the bridge 
        buildBridge(grid, visited[i][1], visited[i - 1][1], -visited[i][1].currentCapacity)
        # remove the node that the bridge was built on
        visited.remove(visited[i])
        
    return visited

#**********************************************************************

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
                if object.visited and object.currentCapacity == object.maxCapacity: 
                    numSolved += 1
    
    print("Number of solved islands is", numSolved, "and Total number of islands is", numIslands)
    # If the number of solved islands is equal to the total number of islands,
    # then the puzzle is solved.
    if (numSolved == numIslands):
        return True
    else: 
        return False


#**********************************************************************

if __name__ == '__main__':
    main()

'''