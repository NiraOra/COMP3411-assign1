from nodeDefs import node, waterNode as watN, islandNode as islN, valueDefs as vd

dict = {}

def nodeInit(map, nrow, ncol):
    code = ".123456789abc"
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if  code[map[i][j]] == '.':
                # initialise a water node
                tempNode = watN.WaterNode(i, j)
            else:
                # initialise an island node
                tempNode = islN.IslandNode(i, j, map, nrow, ncol)
            # assign node to tempNode
            dict[(i, j)] = tempNode
            # print(dict[(i, j)].getCurrCapacity())
            # # dict[(i, j)].callCheck()
        print("\n")
        # we can print dict here for now
    islNodesNeighbours(dict, nrow, ncol)
    # return dictionary of all nodes
    return dict

# just a setter for all island nodes to have neighbours; also put neighbouring water nodes in adj list or smth. or not.
# or in a queue. whichever works
def islNodesNeighbours(dict, nrow, ncol):
    for i in range(nrow):
        for j in range(ncol):
            if isinstance(dict[(i, j)], islN.IslandNode):
                findNeighbours(dict[i, j], dict, nrow, ncol)

# finds the neighbours accordingly
def findNeighbours(object, grid, nrow, ncol):
        # initialisations
        row = object.getRow()
        col = object.getCol()
        # checking all 4 sides
        above = row
        below = row
        left = col
        right = col
        
        # list of neighbours to add to stack
        neighbourList = []
        
        # append if island exists
        # LEFT ISLAND
        for i in range(left, -1, -1):
            # same case
            if i == col:
                pass 
            elif isinstance(grid[(row, i)],  islN.IslandNode):
                neighbourList.append(dict[(row, i)])
                break   
            else:
                # here, you can add all the bridges in i suppose. 
                # OK just test. after putting in bridge it should print out the stuff
                # yay
                dict[(row, col)].putAdjList(grid[(row, i)])
                pass
        # RIGHT ISLAND
        for i in range(right, ncol, 1):
            # case same
            if i == col:
                pass
            # otherwise
            elif isinstance(grid[(row, i)], islN.IslandNode):
                neighbourList.append(dict[(row, i)])
                break   
            else:
                dict[(row, col)].putAdjList(grid[(row, i)])
                pass
        
        # UP ISLAND
        for i in range(above, -1, -1):
            # same case
            if i == row:
                pass
            # otherwise if
            elif isinstance(grid[(i, col)], islN.IslandNode):
                # print("the thing up is in: ", above, col)
                neighbourList.append(dict[(i, col)])
                break
            else:
                dict[(row, col)].putAdjList(grid[(i, col)])
                pass
        
        # DOWN ISLAND
        for i in range(below, nrow):
            # edge case
            if i == row:
                pass
            # otherwise
            elif isinstance(grid[(i, col)], islN.IslandNode):
                # print("the thing down is in: ", below, col)
                neighbourList.append(dict[(i, col)])
                break
            else:
                dict[(row, col)].putAdjList(grid[(i, col)])
                pass

        # sort List over here ? -> based on island Capacity
        neighbourList = sorted(neighbourList, key=lambda x: x.getCurrCapacity())
        
        # print out the neighbour adjacency list
        object.printAdjList() 
        
        # append to stack
        appendStack(object, neighbourList)
        
        pass

# TODO: append to Stack: also from Sophie's code
def appendStack(object, neighbours):
    # print(object.getCurrCapacity(), "is the current island as of now")

    for i in range(len(neighbours)):
        print("Islands nearby: ", neighbours[i].getCapacity())
        # Only including island neighbours
        object.putStack(neighbours[i])
    
    pass
