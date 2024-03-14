# import valueDefs as vd
# "island NODE"
from nodeDefs import node
from nodeDefs import valueDefs as vd

# node: islandNode
class IslandNode(node.Node):
    # max capacity of island
    maxCapacity = 0
    # if visited or not
    visited = False
    # fill this with neighboring bridges as time passes
    adjList = []

    def __init__(self, row, col, capacity):
        super().__init__(row, col, 0)
        self.adjList = []
        self.maxCapacity = capacity

    def putStack(self, item):
        self.adjList.append(item)

    def popStack(self, item):
        self.adjList.remove(item)
        
    def printDebugStack(self):
        for i in range(len(self.adjList)):
            print ("Here: ", self.adjList[i].maxCapacity)

    # NOW: 2 choices
    # 1. Adding bridges for now and then iteratively remove OR
    # 2. Add bridges later and then update capacity accordingly
    # GOING WITH 2
    def putAdjList(self, item):
        # if the capacity is NOT exceeded, then add to list
        if self.currCapacity >= self.maxCapacity or not item.bridgeCheck():
            # that means the capacity is done. done
            return False

        self.adjList.append(item)
        # add currCapacity of both bridge and island
        self.updateCapacity()
        item.updateCapacity()
        # basically saying that no more bridges can be made as it is done
        item.setChecks()
        # set that the bridge is made
        return True
        # print("Hello it is me {", self.row, ",", self.col, "} with water node ",
        # item.getCurrCapacity())
    
    # for printing
    def printLook(self):
        if self.maxCapacity == 10:
            return vd.A_DEF
        elif self.maxCapacity == 11:
            return vd.B_DEF
        elif self.maxCapacity == 12:
            return vd.C_DEF
        return self.maxCapacity

    # TEMP: printing out the adjList
    def printAdjList(self):
        print("Adjacency list: ")
        for i in range(len(self.adjList)):
            print(self.adjList[i].row, self.adjList[i].col)
