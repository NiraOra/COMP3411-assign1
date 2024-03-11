from nodeDefs import valueDefs as vd
import queue
import numpy as np
from queue import PriorityQueue
# # import valueDefs as vals
# # Generic Node initialization into the dict

# # RETURN A DICTIONARY/grid OF DEFINITIONS AND ISLANDS AND STUFF.
# # FIXME maybe idea: add the islands in a min priority queue like
# dict = {}

class Node:
    currCapacity = 0
    row = -1
    col = -1

    # init function
    def __init__(self, row, col, capacity):
        self.row = row
        self.col = col
        self.currCapacity = capacity
        return self
    
    # iterate through capacity
    def updateCapacity(self):
        self.capacity = self.capacity + 1
        
    # all the getter functions
    # def getCapacity(self): 
    #     return self.currCapacity
    
    # def getCurrCapacity(self):
    #     return self.getCapacity()
    
    # # get row and col pair ?
    # def getPosition(self):
    #     return (self.row, self.col)
    
    # for final printing :P
    def printLook(self):
        return self.currCapacity
        # just overriding over island and other one !
    
    # def getRow(self): return self.row
    # def getCol(self): return self.col