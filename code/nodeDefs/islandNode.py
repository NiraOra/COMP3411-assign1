# import valueDefs as vd
# "island NODE"
# TODO: to add implementations: 
# 1. Stack
# 2. Adjacency List
# 3. Capacity of the island
# 4. Visited or Not

# THIS can be a shared var between nodes
currentCapacity = 0
# max capacity of island
maxCapacity = 0
# if visited or not
visited = False
adjList = [] # fill this with neighbouring bridges as time passes
# stack
stack = []

# initialising island
def islandInit(row, col, map):
    # FIXME: this is all just temp stuff; to remove
    print("HI ISLAND {", row, " ", col, "}\n")
    maxCapacity = map[row][col]
    findNeighbours(row, col, map)
    # here. can change depending upon what you want but go for it
    return [maxCapacity, currentCapacity, stack]

# TODO: incorporated from Sophie's code: find neighbours
# removed stack: used as a part of islandNode anyway
def findNeighbours(row, col, grid):
    above = below = row
    left = right = col
    # If no neighbours are found, then it must be water
    lNeighbour = rNeighbour = aNeighbour = bNeighbour = 0

    # Checking the left and right of the cell for any possible neighbours
    while left != 0:
        left -= 1
        if grid[row][left] > 0:
            lNeighbour = grid[row][left]
            break
    while right != len(grid)-1:
        right += 1
        if grid[row][right] > 0:
            rNeighbour = grid[row][right]
            break
    # Checking the above and below of the cell for any possible neighbours
    while above != 0:
        above -= 1
        if grid[above][col] > 0:
            aNeighbour = grid[above][col]
            break
    while below != len(grid)-1:
        below += 1
        if grid[below][col] > 0:
            bNeighbour = grid[below][col]
            break
    
    print("Neighbours are", lNeighbour, rNeighbour, aNeighbour, bNeighbour) # Remove later

    # Might pass in the entire cells themselves instead of the value of the cells
    neighbours = [lNeighbour, rNeighbour, aNeighbour, bNeighbour]
    appendStack(stack, neighbours, row, col)
    
    pass

# TODO: append to Stack: also from Sophie's code
def appendStack(stack, neighbours, row, col):
    neighbours.sort()

    '''
    Need to find a way to access the current and max capacity of the neighbours/cells
    capacityNb.sort()

    '''

    print("Sorted neighbours",neighbours) # Remove later

    for i in range(len(neighbours)):
        # Only including island neighbours
        if (neighbours[i] > 0): 
            stack.append(neighbours[i])
        
    print("Stack is", stack) # Remove later

    pass

# FOR DFS: append the bridges based on the connected components   
# map maybe not needed but lmk. anyway
def bridgeAdj(bridgeNode, map):
    # idea: just fill it up with the bridges ig ?
    # based on bridges, tweak current capacity accordingly
    # 1. check current capacity
    currentCapacity = currentCapacity + 1
    # 2. assert if current capacity is gonna be greater than max capacity; then no bridge
    # else. work
    # 3. done. can also change the type of bridge by calling bridgeNode
    print("DONE. ", adjList)
    pass

# get functions
def getStack():
    return stack

def getAdjList():
    return adjList

def getCurrCapacity():
    return 
