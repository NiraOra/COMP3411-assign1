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

class IslandNode(node.Node):
    currentCapacity = 0
    # max capacity of island
    maxCapacity = 0
    # if visited or not
    visited = False
    # fill this with neighbouring bridges as time passes
    adjList = [] 
    # stack
    stack = []
    
    def __init__(self, row, col, map, nrow, ncol):
        super().__init__(row, col, 0)
        self.stack = []
        self.adjList = []
        self.maxCapacity = map[(row, col)]
        # self.findNeighbours(row, col, map, nrow, ncol)
        # return self
    
    def putStack(self, item):
        self.stack.append(item)
        
    def popStack(self, item):
        self.stack.remove(item)
        
    # NOW: 2 choices
    # 1. Adding bridges for now and then iteratively remove OR
    # 2. Add bridges later and then update capacity accordingly
    
    # GOING WITH 2    
    def putAdjList(self, item):
        
        # if the capacity is exceeded, then add to list
        if self.currCapacity > self.maxCapacity:
            return False
            # there is no way I can do this
        
        self.adjList.append(item)
        
        
        return True
        # print("Hello it is me {", self.row, ",", self.col, "} with water node ", item.getCurrCapacity())
        
    def removeFromAdjList(self, item):
        # FIXME don't even need this. lol
        for i in range(len(self.adjList)):
            # check if same object; if yes then remove
            if self.adjList[i] is item:
                self.adjList.remove(i)
                
    # getters
    def getStack(self): return self.stack
    def getAdjList(self): return self.adjList
    def getCapacity(self):
        return self.maxCapacity
    def getCurrCapacity(self):
        return super().getCurrCapacity()
    
    
    # TEMP: printing out the adjList
    def printAdjList(self):
        print("Adjacency list: ")
        for i in range(len(self.adjList)):
            print(self.adjList[i].getRow(), ",", self.adjList[i].getCol())