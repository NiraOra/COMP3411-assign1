# import valueDefs as vd
# "island NODE"
from nodeDefs import node
# # FOR DFS: append the bridges based on the connected components   
# # map maybe not needed but lmk. anyway
# def bridgeAdj(bridgeNode, map):
#     # idea: just fill it up with the bridges ig ?
#     # based on bridges, tweak current capacity accordingly
#     # 1. check current capacity
#     currentCapacity = currentCapacity + 1
#     # 2. assert if current capacity is gonna be greater than max capacity; then no bridge
#     # else. work
#     # 3. done. can also change the type of bridge by calling bridgeNode
#     print("DONE. ", adjList)
#     pass

# # get functions
# def getStack():
#     return stack

# def getAdjList():
#     return adjList

# def getCurrCapacity():
#     return currentCapacity


class IslandNode(node.Node):
    currentCapacity = 0
    # max capacity of island
    maxCapacity = 0
    # if visited or not
    visited = False
    adjList = [] # fill this with neighbouring bridges as time passes
    # stack
    stack = []
    
    def __init__(self, row, col, map, nrow, ncol):
        super().__init__(row, col, map[row][col])
        self.stack = []
        self.adjList = []
        # self.findNeighbours(row, col, map, nrow, ncol)
        # return self
    
    def putStack(self, item):
        self.stack.append(item)
        
    def popStack(self, item):
        self.stack.pop(item)
    
    # getters
    def getStack(self): return self.stack
    def getCurrCapacity(self):
        return super().getCurrCapacity()
    def getAdjList(self): return self.adjList
    