from grid import *

class Node:
    Point state
    Node parent
    action
    pathCost

    def __init__(self, point, parent, action, pathCost):
        this.state = point
        this.action = action
        this.pathCost = pathCost
        this.parent = parent

    def getParent(self):
        return this.parent
    
    def setParent(self, node):
        this.parent = node

