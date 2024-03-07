# WaterNode
#import valueDefs as val

WATER = " "

# TODO: add
# 1. bridgeCapacity is 3; can't go beyond that
# 2. bridgeType: SINGLE, DOUBLE, TRIPLE or just water
# get functions as well I suppose

bridgeCapacity = 0 # is water. okay maybe I'll do the opposite
bridgeType = WATER # initial state

# initialise waterNode
def waterInit(row, col):
    # print("I am a waternode { ", row, " ", col, "}\n")
    # print("Here's my capacity: ",  bridgeCapacity)
    return [bridgeCapacity, bridgeType]
    
def setBridge(smth, smth1, smth2):
    # setting the bridge and also like. the capacity basically
    # um. this depends though hmm. maybe set it based on a thing that says its vertical or
    # horizontal
    if bridgeCapacity > 3:
        print("No more!!!")
        # don't pass
    elif bridgeCapacity == 1:
        print("1")
    elif bridgeCapacity == 2:
        print("2")
    elif bridgeCapacity == 3:
        print("3")
    pass
    
def iterateCapacity():
    bridgeCapacity = bridgeCapacity + 1