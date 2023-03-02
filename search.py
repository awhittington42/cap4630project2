import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation

from utils import *
from grid import *

def bfs(problem, dest):
    current = problem
    pathCost = 0
    if current == dest:
        return current

    frontier = [] # Fifo point queue
    reached = [] # set to check if point has been reached before.
    while !(len(frontier) == 0):
        node = frontier.pop(-1)

        for #need to finish expand before finishing this

def expand(point, informed): #expand order - up, right, down, left (clockwise)
    """
    general idea:

    for BFS and DFS, check if point would cause path to go into an enclosure, which is forbidden. Return first node found clockwise that satisfies this condition.

    for informed searches, need to calculate action cost for each move as well as check if enclosure is encountered.
    """
    if !informed: #BFS or DFS, don't worry about action cost.



def gen_polygons(worldfilepath):
    polygons = []
    with open(worldfilepath, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        for line in lines:
            polygon = []
            pts = line.split(';')
            for pt in pts:
                xy = pt.split(',')
                polygon.append(Point(int(xy[0]), int(xy[1])))
            polygons.append(polygon)
    return polygons

if __name__ == "__main__":
    epolygons = gen_polygons('TestingGrid/world1_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world1_turfs.txt')

    source = Point(24,17)
    dest = Point(28,20)

    fig, ax = draw_board()
    draw_grids(ax)
    draw_source(ax, source.x, source.y)  # source point
    draw_dest(ax, dest.x, dest.y)  # destination point
    
    # Draw enclosure polygons
    for polygon in epolygons:
        for p in polygon:
            draw_point(ax, p.x, p.y)
    for polygon in epolygons:
        for i in range(0, len(polygon)):
            draw_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw turf polygons
    for polygon in tpolygons:
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
    for polygon in tpolygons:
        for i in range(0, len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])

    #### Here call search to compute and collect res_path

    """
    TODO:

    Breadth-First Search
    Depth-First Search
    Greedy Best-First Search
    A* Search

    *Graph search versions*

    Create more turf and enclosure polygons

    """

    # BFS



    res_path = [Point(24,17), Point(25,17), Point(26,17), Point(27,17),  
                Point(28,17), Point(28,18), Point(28,19), Point(28,20)]
    
    for i in range(len(res_path)-1):
        draw_result_line(ax, [res_path[i].x, res_path[i+1].x], [res_path[i].y, res_path[i+1].y])
        plt.pause(0.1)
    
    plt.show()
