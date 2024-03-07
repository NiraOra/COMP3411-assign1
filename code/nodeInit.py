from nodeDefs import node, waterNode as watN, islandNode as islN, valueDefs as vd
dict = {}

def nodeInit(map, nrow, ncol):
    code = ".123456789abc"
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if  code[map[i][j]] == '.':
                # initialise a water node
                tempNode = watN.WaterNode(i, j, map[i][j])
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

def islNodesNeighbours(dict, nrow, ncol):
    for i in range(nrow):
        for j in range(ncol):
            if isinstance(dict[(i, j)], islN.IslandNode):
                findNeighbours(dict[i, j], i, j, dict, nrow, ncol)

def findNeighbours(object, row, col, grid, nrow, ncol):
        # initialisations
        above = row
        below = row
        left = col
        right = col
        
        # If no neighbours are found, then it must be water but i need -1 so. yeah
        lCoords = [row, -1]
        rCoords = [row, -1]
        aCoords = [-1, col]
        bCoords = [-1, col]

        # LEFT ISLAND
        for i in range(left, -1, -1):
            temp = grid[(row, i)].getCurrCapacity()
            # same case
            if i == col:
                pass 
            elif temp > 0:
                lCoords[1] = i
                break   
            else:
                pass
        # RIGHT ISLAND
        for i in range(right, ncol, 1):
            temp = grid[(row, i)].getCurrCapacity()
            # case same
            if i == col:
                pass
            # otherwise
            elif temp > 0:
                rCoords[1] = i
                break   
            else:
                pass
        
        # UP ISLAND
        for i in range(above, -1, -1):
            temp = grid[(i, col)].getCurrCapacity()
            # same case
            if i == row:
                pass
            # otherwise if
            elif temp > 0:
                # print("the thing up is in: ", above, col)
                aCoords[0] = i
                break
            else:
                pass
        
        # DOWN ISLAND
        for i in range(below, nrow):
            temp = grid[(i, col)].getCurrCapacity()
            # edge case
            if i == row:
                pass
            # otherwise
            elif temp > 0:
                # print("the thing down is in: ", below, col)
                bCoords[0] = i
                break
            else:
                pass
        
        # debugging neighbours list: TODO: delete
        # print("Neighbours: ", lNeighbour, rNeighbour, aNeighbour, bNeighbour)

        # TODO: THERES FOR SURE A BETTER WAY TO DO THIS LOL
        neighbourList = []
        if lCoords[1] > -1:
            neighbourList.append(dict[(lCoords[0], lCoords[1])])
        
        if rCoords[1] > -1:
            neighbourList.append(dict[(rCoords[0], rCoords[1])])
            
        if aCoords[0] > -1:
            neighbourList.append(dict[(aCoords[0], aCoords[1])])
            
        if bCoords[0] > -1:
            neighbourList.append(dict[(bCoords[0], bCoords[1])])

        # neighbours = [lNeighbour, rNeighbour, aNeighbour, bNeighbour]
        appendStack(object, neighbourList, row, col)
        
        pass

# TODO: append to Stack: also from Sophie's code
def appendStack(object, neighbours):
    neighbours = sorted(neighbours, key=lambda x: x.getCurrCapacity())
    
    print(object.getCurrCapacity(), "is the current island as of now")
    
    # print("Sorted neighbours", neighbours) # Remove later

    for i in range(len(neighbours)):
        print("Island number, ", neighbours[i].getCurrCapacity())
        # Only including island neighbours
        object.putStack(neighbours[i])
    
    pass
