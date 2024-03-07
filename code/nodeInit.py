from nodeDefs import node, waterNode as watN, islandNode as islN, valueDefs as vd
dict = {}

def nodeInit(map, nrow, ncol):
    code = ".123456789abc"
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if  code[map[i][j]] == '.':
                # initialise a water node
                 # self.currCapacity = capacity
                tempNode = watN.WaterNode(i, j, map[i][j])
            else:
                tempNode = islN.IslandNode(i, j, map, nrow, ncol)

            # # row, col, capacity, type, map, size_row, size_col
            # tempNode = node.Node(i, j, map[i][j], type, map, nrow, ncol)
            # initialise the node to the dictionary
            dict[(i, j)] = tempNode
            print(dict[(i, j)].getCurrCapacity())
            # dict[(i, j)].callCheck()
        print("\n")
        # we can print dict here for now
    # return dictionary of all nodes
    return dict
