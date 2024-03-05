# "NODE"
# TODO: to add implementations: 
# 1. Stack
# 2. Adjacency List
# 3. Capacity of the island
# 4. Visited or Not

def islandInit(num):
    print("HI ", num, "\n")
    findNeighbours(0, 0, 0)
    

def findNeighbours(row, col, map):
    print("Basically finding out the neighbours based on row, column and map\n")