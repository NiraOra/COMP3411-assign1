from nodeDefs import islandNode as islN, waterNode as watN
import queue
from queue import PriorityQueue
# import valueDefs as vals
# Generic Node initialisation into the dict

# RETURN A DICTIONARY OF DEFINITIONS AND ISLANDS AND STUFF. OMG
# FIXME maybe idea: add the islands in a min priority queue like
dict = []
# if you can use priorityqueue in python. omg
queueIsland = queue.PriorityQueue()

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
    return dict

def finalInit(map):
    code = ".123456789abc "
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if code[map[i][j]] == '.':
                map[i][j] == WATER
    return map