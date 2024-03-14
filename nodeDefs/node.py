"""
This module defines the `Node` class, which represents a node in a grid.
Each
"""


"""
Class representing a node in a grid.

Methods:
    __init__(row, col, capacity): Initializes a Node object with 
    the given row, column, and capacity.
    updateCapacity(): Updates the capacity of the node by incrementing it by 1.
    printLook(): Returns the current capacity of the node.

Args:
    row (int): The row index of the node.
    col (int): The column index of the node.
    capacity (int): The current capacity of the node.

Returns:
    None
"""

class Node:
    currCapacity = 0
    row = -1
    col = -1
    visited = False

    # init function
    def __init__(self, row, col, capacity):
        self.row = row
        self.col = col
        self.currCapacity = capacity
        self.visited = False
        # return self

    # iterate through capacity
    def updateCapacity(self):
        self.currCapacity = self.currCapacity + 1

    # for final printing :P
    def printLook(self):
        return self.currCapacity
        # just overriding over island and other one !
