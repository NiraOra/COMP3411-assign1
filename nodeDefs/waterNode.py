# Initialisation file of the Water Node class and helper functions for water cells.

from nodeDefs import valueDefs as vd
from nodeDefs import node

class WaterNode(node.Node):
    bridgeMaxCapacity = vd.MAX_BRIDGE_CAPACITY # Bridges can only have a max weight of 3.
    bridgeType = vd.WATER # All bridges are initally water i.e there are no bridges.
    bridgeExists = False  # A check to see if a bridge already exists on a given node.

    # initialise waterNode
    def __init__(self, row, col):
        super().__init__(row, col, 0)
    
    # Function to check the capacity of a bridge.
    # Return true if the capacity is less than max capacity; else return false
    def bridgeCheck(self):
        return self.currCapacity < self.bridgeMaxCapacity
    
    # Function to set the bridge type based on the given number of bridges.    
    def setBridge(self, numBridges, bridgeOrientation):
        # Check that the bridge is not at max capacity.
        if self.bridgeCheck() == False:
            return
            
        # Horizontal bridge types
        if bridgeOrientation == "horizontal":
            if numBridges == 1:
                self.bridgeType = vd.SINGLE_HORIZONTAL
            elif numBridges == 2:
                self.bridgeType =  vd.DOUBLE_HORIZONTAL
            elif numBridges == 3:
                self.bridgeType = vd.TRIPLE_HORIZONTAL
            pass
        # Vertical bridge types
        else:
            if numBridges == 1:
                self.bridgeType = vd.SINGLE_VERTICAL
            elif numBridges == 2:
                self.bridgeType = vd.DOUBLE_VERTICAL
            elif numBridges == 3:
                self.bridgeType = vd.TRIPLE_VERTICAL
            pass
        self.setChecks()
        
    # Function which sets that no more bridges can be formed on the cell.
    def setChecks(self):
        self.horizontalCheck = False
        self.verticalCheck = False

    # Function which clears the bridges on the cell and resetting it back to water.
    def clearBridge(self): 
        self.bridgeType = vd.WATER
        self.bridgeExists = False
        
    # Function to print out the correct character for the cell.
    def printLook(self):
        return self.bridgeType