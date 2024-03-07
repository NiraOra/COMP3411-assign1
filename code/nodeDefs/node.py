from nodeDefs import islandNode as islN, waterNode as watN
import queue
import numpy as np
from queue import PriorityQueue
# import valueDefs as vals
# Generic Node initialisation into the dict

# RETURN A DICTIONARY/grid OF DEFINITIONS AND ISLANDS AND STUFF.
# FIXME maybe idea: add the islands in a min priority queue like
dict = {}
# if you can use priorityqueue in python. omg
queueIsland = queue.PriorityQueue()
# TODO: to remove
WATER = " "

# node initialisation on the grid to return
def nodeInit(map):
    code = ".123456789abc"
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if  code[map[i][j]] == '.':
                # initialise a water node
                tempNode = watN.waterInit(i, j)
                # initialise the node to the dictionary
                dict[(i, j)] = tempNode
                print(dict[(i, j)])
            else:
                # initialise an island node
                tempNode = islN.islandInit(i, j, map)
                # um added
                dict[(i, j)] = tempNode
                # just check
                print(dict[(i, j)])
                # find out neighbours (just put it within islandInit later on; here for convenience)
                # islN.findNeighbours(i, j, map)
        print("\n")
        # we can print dict here for now
    return dict

def finalInit(map):
    code = ".123456789abc "
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if code[map[i][j]] == '.':
                map[i][j] == WATER
    return map
