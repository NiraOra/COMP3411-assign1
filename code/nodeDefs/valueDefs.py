# enum defs
from enum import Enum
 
MAX_BRIDGE_CAPACITY = 3 
WATER = " "
 
class WaterNode(Enum):
    
    SINGLE_HORIZONTAL = '-',
    SINGLE_VERTICAL = '|',
    DOUBLE_HORIZONTAL = '=',
    DOUBLE_VERTICAL = '"',
    TRIPLE_HORIZONTAL = 'E',
    TRIPLE_VERTICAL = '#'