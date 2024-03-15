# Initialisation file for the Island Node class and helper functions for islands.

from nodeDefs import node
from nodeDefs import valueDefs as vd

class IslandNode(node.Node):
    maxCapacity = 0  # max capacity of island, initially set to zero until it is scanned in.
    visited = False  # initially all islands are unvisited.
    adjList = []     # a list containing all the neighbouring islands.
    reachable = True # whether or not we are able to traverse to this island.

    # initialise islandNode
    def __init__(self, row, col, capacity):
        super().__init__(row, col, 0)
        self.adjList = []
        self.maxCapacity = capacity

    # Adds a neighbour to the island's adjacency list.
    def addAdjList(self, item):
        self.adjList.append(item)

    # Removes a neighbour from the island's adjacency list.
    def removeAdjList(self, item):
        self.adjList.remove(item)
    
    # Printing the correct character according to the island's max capacity.
    def printLook(self):
        if self.maxCapacity == 10:
            return vd.A_DEF
        elif self.maxCapacity == 11:
            return vd.B_DEF
        elif self.maxCapacity == 12:
            return vd.C_DEF
        return self.maxCapacity

##############################################################################

