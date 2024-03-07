from nodeDefs import valueDefs as vd
import queue
import numpy as np
from queue import PriorityQueue
# # import valueDefs as vals
# # Generic Node initialisation into the dict

# # RETURN A DICTIONARY/grid OF DEFINITIONS AND ISLANDS AND STUFF.
# # FIXME maybe idea: add the islands in a min priority queue like
# dict = {}

class Node:
    currCapacity = 0
    row = -1
    col = -1

    def __init__(self, row, col, capacity):
        self.row = row
        self.col = col
        self.currCapacity = capacity
        return self
        
    def getCurrCapacity(self): 
        return self.currCapacity
    
      

# def print_nodes(nodes):
#     for key in sorted(nodes.keys()):
#         node = nodes[key]
#         print(f"Node at ({node.row}, {node.col}): {node.value if isinstance(node, WaterNode) else node.elevation}")