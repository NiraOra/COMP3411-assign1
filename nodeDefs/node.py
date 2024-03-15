# Helper file which defines the `Node` class, which represents a node in a grid.

class Node:
    currCapacity = 0 # Initally, set the current capcity of the node to zero.
    row = -1         # The row index of the node.
    col = -1         # The column index of the node.
    visited = False  # Initially, set the node as unvisited.
    reachable = True # Initially, all nodes are reachable.

    # initialise the node
    def __init__(self, row, col, capacity):
        self.row = row 
        self.col = col
        self.currCapacity = capacity
        self.visited = False

    # Update the capacity of the node.
    def updateCapacity(self):
        self.currCapacity = self.currCapacity + 1

    # Function to print the correct character for the given cell.
    def printLook(self):
        return self.currCapacity
