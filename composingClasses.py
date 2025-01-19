class WrongNumberOfPoints(Exception):
    pass
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, points):
        for point in points:
            if not isinstance(point, Point):
                raise TypeError("All Member Should be members of Point class")
        self.points = points

class Square(Shape):
    def __init__(self, points):
        if(len(points)!=4):
            raise WrongNumberOfPoints
        super().__init__(points)

class Triangle(Shape):
    def __init__(self, points):
        if(len(points)!=3):
            raise WrongNumberOfPoints
        super().__init__(points)