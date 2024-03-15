# Helper file which contains functions to help configure the islands' neighbours.

from nodeDefs import node, waterNode as watN, islandNode as islN, valueDefs as vd

grid = {}

def nodeInit(map, nrow, ncol):
    code = ".123456789abc"
    for i in range(len(map)):
        for j in range(len(map[i])):
            if  code[map[i][j]] == '.':
                # initialise a water node
                tempNode = watN.WaterNode(i, j)
            elif map[i][j] == vd.A_DEF:
                tempNode = islN.IslandNode(i, j, 10)
            elif map[i][j] == vd.B_DEF:
                tempNode = islN.IslandNode(i, j, 11)
            elif map[i][j] == vd.C_DEF:
                tempNode = islN.IslandNode(i, j, 12)
            else:
                # initialise an island node
                tempNode = islN.IslandNode(i, j, map[i][j])
            # assign node to tempNode
            grid[(i, j)] = tempNode
    islNodesNeighbours(grid, nrow, ncol)
    return grid

# Function which sets all the island's neighbours into the island's adjacency lists.
def islNodesNeighbours(grid, nrow, ncol):
    for i in range(nrow):
        for j in range(ncol):
            if isinstance(grid[(i, j)], islN.IslandNode):
                findNeighbours(grid[i, j], grid, nrow, ncol)

# Function which searches for the island's neighbours in all four directions. 
def findNeighbours(object, grid, nrow, ncol):
    row, col = object.row, object.col
    # checking all 4 sides
    above = row
    below = row
    left = col
    right = col

    # list of neighbours to add to adjList
    neighbourList = []

    # Append if a neighbouring island exists
    # LEFT NEIGHBOURING ISLAND
    for i in range(left, -1, -1):
        if i in [col, col - 1]:
            pass
        elif isinstance(grid[(row, i)], islN.IslandNode):
            neighbourList.append(grid[(row, i)])
            break
    # RIGHT NEIGHBOURING ISLAND
    for i in range(right, ncol):
        if i in [col, col + 1]:
            pass
        elif isinstance(grid[(row, i)], islN.IslandNode):
            neighbourList.append(grid[(row, i)])
            break
    # UP NEIGHBOURING ISLAND
    for i in range(above, -1, -1):
        if i in [row, row - 1]:
            pass
        elif isinstance(grid[(i, col)], islN.IslandNode):
            neighbourList.append(grid[(i, col)])
            break
    # DOWN NEIGHBOURING ISLAND
    for i in range(below, nrow):
        if i in [row, row + 1]:
            pass
        elif isinstance(grid[(i, col)], islN.IslandNode):
            neighbourList.append(grid[(i, col)])
            break

    # Sorting the neighbours depending on the max capacity.
    neighbourList = sorted(neighbourList, key=lambda x: x.maxCapacity)

    # Use the list of neighbours to append to the adjacency list of the island.
    appendAdjList(object, neighbourList)

# Function which appends the neighbours into the island's adjacency list.
def appendAdjList(object, neighbours):
    for i in range(len(neighbours)):
        object.addAdjList(neighbours[i])
    pass
