# WaterNode
from nodeDefs import valueDefs as vd
from nodeDefs import node

class WaterNode(node.Node):
    # 1. bridgeCapacity is 3; can't go beyond that
    # 2. bridgeType: SINGLE, DOUBLE, TRIPLE or just water
    # get functions as well I suppose

    # TO_REMOVE: bridge Capacity as it already exists
    bridgeCapacity = 0
    # initial state
    bridgeType = vd.WATER 

    # initialise waterNode
    def __init__(self, row, col, capacity):
        super().__init__(row, col, 0)
        # return self
    
    # set the bridge type based on bridge made    
    def setBridge(self, smth, bridgeOrientation):
        # setting the bridge and also like. the capacity basically
        # um. this depends though hmm. maybe set it based on a thing that says its vertical or
        # horizontal
        if self.bridgeCapacity <= 0:
            print("No more!!!")
            # don't pass
            
        # DONE. maybe
        if bridgeOrientation == "horizontal":
            if self.bridgeCapacity == 1:
                self.bridgeType = vd.SINGLE_HORIZONTAL
                print("1")
            elif self.bridgeCapacity == 2:
                self.bridgeType =  vd.DOUBLE_HORIZONTAL
                print("2")
            elif self.bridgeCapacity == 3:
                self.bridgeType = vd.TRIPLE_HORIZONTAL
                print("3")
            pass
        else:
            if self.bridgeCapacity == 1:
                self.bridgeType = vd.SINGLE_VERTICAL
                print("1")
            elif self.bridgeCapacity == 2:
                self.bridgeType = vd.DOUBLE_VERTICAL
                print("2")
            elif self.bridgeCapacity == 3:
                self.bridgeType = vd.TRIPLE_VERTICAL
                print("3")
            pass
     
    # just to iterate capacity of the bridge   
    def iterateCapacity(self):
        self.bridgeCapacity = self.bridgeCapacity - 1

    # getters
    # overriding the main function
    def getCurrCapacity(self):
        return self.bridgeCapacity
    
    def getBridgeType(self): return self.bridgeType