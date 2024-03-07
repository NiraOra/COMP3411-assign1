# WaterNode
from nodeDefs import valueDefs as vd
#import valueDefs as val

WATER = " "

# TODO: add
# 1. bridgeCapacity is 3; can't go beyond that
# 2. bridgeType: SINGLE, DOUBLE, TRIPLE or just water
# get functions as well I suppose

bridgeCapacity = 0 # is water. okay maybe I'll do the opposite
bridgeType = vd.WATER # initial state

# initialise waterNode
def waterInit(row, col):
    # print("I am a waternode { ", row, " ", col, "}\n")
    # print("Here's my capacity: ",  bridgeCapacity)
    return [bridgeCapacity, bridgeType]
    
def setBridge(smth, bridgeOrientation):
    # setting the bridge and also like. the capacity basically
    # um. this depends though hmm. maybe set it based on a thing that says its vertical or
    # horizontal
    if bridgeCapacity > 3:
        print("No more!!!")
        # don't pass
        
    # DONE. maybe
    if bridgeOrientation == "horizontal":
        if bridgeCapacity == 1:
            bridgeType = vd.SINGLE_HORIZONTAL
            print("1")
        elif bridgeCapacity == 2:
            bridgeType =  vd.DOUBLE_HORIZONTAL
            print("2")
        elif bridgeCapacity == 3:
            bridgeType = vd.TRIPLE_HORIZONTAL
            print("3")
        pass
    else:
        if bridgeCapacity == 1:
            bridgeType = vd.SINGLE_VERTICAL
            print("1")
        elif bridgeCapacity == 2:
            bridgeType =  vd.DOUBLE_VERTICAL
            print("2")
        elif bridgeCapacity == 3:
            bridgeType = vd.TRIPLE_VERTICAL
            print("3")
        pass
    
def iterateCapacity():
    bridgeCapacity = bridgeCapacity + 1