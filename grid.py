import matplotlib.pyplot as plt

MAX = 50

class Point:
    def __init__(self, x, y, action = "empty"):
        self.x = x
        self.y = y
        self.illegal = False
        self.action = action
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < 51:
            z = self.i
            self.i += 1
            return z
        else:
            raise StopIteration
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def isLegal(self):
        if self.illegal == True:
            return False
        else:
            return True
    def getAction(self):
        return self.action
    def setIllegal(self):
        self.illegal = True
    def to_tuple(self):
        return self.x, self.y
    def adjacentPoints(self): # returns tuple of the ordered action points
        p1 = Point(self.x, self.y + 1, "up")
        p2 = Point(self.x + 1, self.y, "right")
        p3 = Point(self.x, self.y - 1, "down")
        p4 = Point(self.x - 1, self.y, "left")
        if self.y <= 0:
            print("vertical min found, illegal down point.")
            p3.setIllegal()
        elif self.y >= 50:
            print("vertical max found, illegal up point.")
            p1.setIllegal()
        if self.x <= 0:
            print("horizontal min found, illegal left point.")
            p4.setIllegal()
        elif self.x >= 50:
            print("horizontal max found, illegal right point.")
            p2.setIllegal()
        return p1, p2, p3, p4
        #return [(self.x, self.y + 1), (self.x + 1, self.y), (self.x, self.y + 1), (self.x - 1, self.y)]

def draw_board():
    # create a figure to draw the board
    fig = plt.figure(figsize=[8,8])
    # set the background color
    #fig.patch.set_facecolor((0.85,0.64,0.125))
    ax = fig.add_subplot(111)
    # turn off the axes
    ax.set_axis_off()
    return fig, ax
def draw_grids(ax):
    # draw the vertical lines
    for x in range(MAX):
        ax.plot([x, x], [0,MAX-1], color = '0.75', linestyle='dotted')
    # draw the horizontal lines
    for y in range(MAX):
        ax.plot([0, MAX-1], [y,y], color = '0.75', linestyle='dotted')
    ax.set_position([0,0.02,1,1])

def draw_point(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor=(0,0,0),
        markerfacecolor='k',
        markeredgewidth=1)

def draw_source(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='b',
        markerfacecolor='b',
        markeredgewidth=1)

def draw_dest(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='r',
        markerfacecolor='r',
        markeredgewidth=1)

def draw_red_point(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='r',
        markerfacecolor='r',
        markeredgewidth=1)

def draw_green_point(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='g',
        markerfacecolor='g',
        markeredgewidth=1)

def draw_line(ax, xs, ys):
    ax.plot(xs, ys, color='k')

def draw_result_line(ax, xs, ys):
    ax.plot(xs, ys, color='r')

def draw_green_line(ax, xs, ys):
    ax.plot(xs, ys, color='g')
