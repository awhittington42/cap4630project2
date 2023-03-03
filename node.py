from grid import *

class node:
    Point state
    node parent
    action
    pathCost

    def __init__(self, point, action, pathCost):
        this.state = point
        this.action = action
        this.pathCost = pathCost

    def getParent(self):
        return this.parent
    
    def setParent(self, node):
        this.parent = node

