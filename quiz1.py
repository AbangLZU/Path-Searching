# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
from __future__ import print_function
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    open_list = []
    close_list = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    close_list[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    open_list.append([g, x, y,])

    found = False
    resign = False

    while found is False and resign is False:
        if len(open_list) == 0:
            resign = True
            print("Search fail")
        else:
            open_list.sort()
            open_list.reverse()
            next_item = open_list.pop()

            g = next_item[0]
            x = next_item[1]
            y = next_item[2]

            if x == goal[0] and y == goal[1]:
                found = True
                print(next_item)
            else:
                for action in delta:
                    new_x = x + action[0]
                    new_y = y + action[1]
                    if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                        if close_list[new_x][new_y] == 0 and grid[new_x][new_y] == 0:
                            new_g = g + cost
                            open_list.append([new_g, new_x, new_y])
                            close_list[new_x][new_y] = 1

search(grid, init, goal, cost)