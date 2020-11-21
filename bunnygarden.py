# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:40:37 2020

@author: Tim
"""

def eat(garden):
    n = len(garden)
    m = len(garden[0])
    
    # determine the center area
    # either a 1x1, 1x2, 2x1, or 2x2 area depending on even/odd size
    # use mod(2) to ensure that 2 center cells found when size is even
    # center_cells is a list of indices for cells in the center
    center_cells = []
    for i in range((n+1)//2 - 1, (n+1)//2 + (n+1)%2):
        for j in range((m+1)//2 - 1, (m+1)//2 + (m+1)%2):
            center_cells.append([i, j])
    
    # determine starting cell within center area
    max_carrot = -1 # initialize to negative to ensure even a 0 carrot max will be found
    for cell in center_cells:
        if garden[cell[0]][cell[1]] > max_carrot:
            max_carrot = garden[cell[0]][cell[1]]
            start = [cell[0], cell[1]]
    
    # main block to move bunny through the garden by adding neighboring cells to a list, 
    # finding the neighbor with max carrots, and setting that to be the new starting cell
    carrots = 0
    nonzero_neighbor = True # initialize to True to ensure block runs at least once
    while nonzero_neighbor:
        carrots += garden[start[0]][start[1]] # eat the carrots in current cell
        garden[start[0]][start[1]] = 0
        nonzero_neighbor = False
        
        # check if at edge of garden before adding indices for new neighbors to list
        # I initially tried this with try/except statements but because negative indices do not give an error,
        # it allowed bunny to loop from top/left edge to the bottom/right edge. Oops!
        neighbors = []
        if start[0] > 0:
            neighbors.append([start[0] - 1, start[1]])
        if start[0] < (n-1):
            neighbors.append([start[0] + 1, start[1]])
        if start[1] > 0:
            neighbors.append([start[0], start[1] - 1])
        if start[1] < (m-1):
            neighbors.append([start[0], start[1] + 1])

        
        # find neighbor with the most carrots and set it as start
        # uses similar code as in determing the initial starting cell - might want to break off into its own function
        max_neighbor = 0 # itialize to zero to ensure if no neighbors have >0 carrots, while loop will terminate
        for cell in neighbors:
                if garden[cell[0]][cell[1]] > max_neighbor:
                    max_neighbor = garden[cell[0]][cell[1]]
                    nonzero_neighbor = True # while loop condition
                    start = [cell[0], cell[1]]        
    return(carrots)

# test cases - various combos of even/odd length/width and starting on a 0 carrot cell
# based on the prompt, I think starting on a 0 carrot cell should not cause bunny to sleep immediately
gardens = {
"garden1": [[5, 7, 8, 6, 3],
           [0, 0, 7, 0, 4],
           [4, 6, 3, 4, 9],
           [3, 1, 0, 5, 8]]
,
"garden2": [[5, 7, 8, 6, 3, 0],
           [0, 0, 7, 0, 4, 0],
           [4, 6, 3, 4, 9, 0],
           [3, 1, 0, 5, 8, 0]]
,
"garden3": [[5, 7, 8, 6, 3, 0],
           [0, 0, 7, 0, 4, 0],
           [4, 6, 3, 4, 9, 0],
           [3, 1, 0, 5, 8, 0],
           [3, 1, 0, 5, 8, 0]]
,
"garden4": [[5, 7, 8, 6, 3],
           [0, 0, 7, 0, 4],
           [4, 6, 0, 4, 9],
           [3, 1, 0, 5, 8],
           [3, 1, 0, 5, 8]]
,
"garden5": [[5, 7, 8, 6, 3],
           [1, 0, 7, 0, 4],
           [4, 6, 3, 4, 9],
           [3, 1, 0, 5, 8]]
,
"garden6": [[5, 7, 8, 6, 3],
           [0, 0, 0, 0, 4],
           [4, 6, 3, 4, 9],
           [3, 1, 0, 5, 8]]      
}
for key, value in gardens.items():
    print("Bunny ate %s carrots in %s." % (eat(value), key))