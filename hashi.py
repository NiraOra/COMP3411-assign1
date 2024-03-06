# Hashi Puzzle - COMP3411 Assignment 1
# Written by Sophie Lian z5418296
# on 5/3/2025

import numpy as np

row = 0 # Remove later
col = 0 # Remove later

grid = np.array([
    [0, 4, 1, 0],
    [1, 5, 0, 2],
    [3, 0, 2, 9],
    [0, 6, 4, 0]
]) # Remove later


# Function which iterates to the Left,Right,Above and Below of a cell for Neighbours
# Adds the Neighbours to the Stack
def findNeighbours(grid, row, col, stack):
    above = below = row
    left = right = col
    # If no neighbours are found, then it must be water
    lNeighbour = rNeighbour = aNeighbour = bNeighbour = 0

    # Checking the left and right of the cell for any possible neighbours
    while left != 0:
        left -= 1
        if grid[row][left] > 0:
            lNeighbour = grid[row][left]
            break
    while right != len(grid)-1:
        right += 1
        if grid[row][right] > 0:
            rNeighbour = grid[row][right]
            break
    # Checking the above and below of the cell for any possible neighbours
    while above != 0:
        above -= 1
        if grid[above][col] > 0:
            aNeighbour = grid[above][col]
            break
    while below != len(grid)-1:
        below += 1
        if grid[below][col] > 0:
            bNeighbour = grid[below][col]
            break

    print("Neighbours are", lNeighbour, rNeighbour, aNeighbour, bNeighbour) # Remove later

    # Might pass in the entire cells themselves instead of the value of the cells
    neighbours = [lNeighbour, rNeighbour, aNeighbour, bNeighbour]
    appendStack(stack, neighbours, row, col)
    
    pass


# Function which sorts the neighbours in order of Lowest Capacity Filled and 
# Adds them to the Stack for DFS Backtracking
def appendStack(stack, neighbours, row, col):
    neighbours.sort()

    '''
    Need to find a way to access the current and max capacity of the neighbours/cells
    capacityNb.sort()

    '''
    

    print("Sorted neighbours",neighbours) # Remove later

    for i in range(len(neighbours)):
        # Only including island neighbours
        if (neighbours[i] > 0): 
            stack.append(neighbours[i])
        
    print("Stack is", stack) # Remove later

    pass

def main():
    stack = []
    findNeighbours(grid, row, col, stack)
    
    pass

main()
    