from nodeDefs import islandNode as islN, waterNode as watN
# import valueDefs as vals
# Generic Node initialisation into the dict

WATER = " "

def nodeInit(map):
    code = ".123456789abc"
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            # print(code[map[i][j]], end=" ")
            if  code[map[i][j]] == '.':
                # initialise a water node
                watN.waterInit(1)
            else:
                # initialise an island node
                islN.islandInit(0)
                # find out neighbours (just put it within islandInit later on; here for convenience)
                islN.findNeighbours(i, j, map)
        print("\n")
    return map

def finalInit(map):
    code = ".123456789abc "
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if code[map[i][j]] == '.':
                map[i][j] == WATER
    return map