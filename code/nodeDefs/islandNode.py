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
        self.findNeighbours(row, col, map, nrow, ncol)
        # return self
    
    def findNeighbours(self, row, col, grid, nrow, ncol):
        # initialisations
        above = below = row - 1
        left = right = col - 1
        # If no neighbours are found, then it must be water
        lNeighbour = rNeighbour = aNeighbour = bNeighbour = 0
        # LEFT ISLAND
        for i in range(left, 0, -1):
            if grid[row][i] > 0:
                lNeighbour = grid[row][i]
                break   
        # RIGHT ISLAND
        for i in range(right, ncol):
            if grid[row][right] > 0:
                rNeighbour = grid[row][right]
                break   
        # UP ISLAND
        for i in range(above, 0, -1):
            if grid[above][col] > 0:
                aNeighbour = grid[above][col]
                break
        
        # DOWN ISLAND
        for i in range(below, nrow):
            if grid[below][col] > 0:
                bNeighbour = grid[below][col]
                break

        # TODO: THERES FOR SURE A BETTER WAY TO DO THIS LOL
        neighbourList = []
        if lNeighbour > 0:
            neighbourList.append(lNeighbour)
        
        if rNeighbour > 0:
            neighbourList.append(rNeighbour)
            
        if aNeighbour > 0:
            neighbourList.append(aNeighbour)
            
        if bNeighbour > 0:
            neighbourList.append(bNeighbour)

        # neighbours = [lNeighbour, rNeighbour, aNeighbour, bNeighbour]
        self.appendStack(neighbourList, row, col)
        
        pass

    # TODO: append to Stack: also from Sophie's code
    def appendStack(self, neighbours, row, col):
        neighbours.sort()
        
        print(neighbours, " as of now")
        '''
        Need to find a way to access the current and max capacity of the neighbours/cells
        - taken the node: so we can access from the nodes itself later on!
        
        capacityNb.sort()

        '''

        print("Sorted neighbours", neighbours) # Remove later

        for i in range(len(neighbours)):
            print("val now, ", i)
            # Only including island neighbours
            self.stack.append(neighbours[i])
            
        print("Stack is", self.stack) # Remove later

        pass
    
    
    # getters
    def getStack(self): return self.stack
    def getCurrCapacity(self):
        return super().getCurrCapacity()
    def getAdjList(self): return self.adjList
    