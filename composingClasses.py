class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, points):
        self.points = points

triangle = Shape([
    Point(0,0),
    Point(5,5),
    Point(2,4)
])

topLeft = Point(0,0)
topRight = Point(0,10)
bottomLeft = Point(10,0)
bottomRight = Point(10,10)

square = Shape([topLeft,topRight,bottomLeft,bottomRight])

