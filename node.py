from grid import *

class Node:

    def __init__(self, point, parent = "root", action = "empty", pathCost = 0):
        self.state = point
        self.action = action
        self.pathCost = pathCost
        self.parent = parent

    def getParent(self):
        return self.parent
    
    def getCost(self):
        return self.pathCost
    
    def setParent(self, node):
        self.parent = node

    def getPoint(self):
        return self.state

