# "NODE"
# TODO: to add implementations: 
# 1. Stack
# 2. Adjacency List
# 3. Capacity of the island
# 4. Visited or Not
current_capacity = 0
max_capacity = 0
visited = False
adj_list = [] # fill this with neighbouring bridges as time passes

def islandInit(num):
    print("HI ", num, "\n")
    findNeighbours(0, 0, 0)

def findNeighbours(row, col, map):
    max_capacity = 0 # (of the node)
    print("Basically finding out the neighbours based on row, column and map\n")
    
def hasVisited():
    visited = True
    
def bridgeAdj(num, smth):
    # idea: just fill it up with the bridges ig ?
    # based on bridges, tweak current capacity accordingly
    print(" ")