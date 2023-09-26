
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self):
        if self.x**2+self.y**2 <= self.radius**2:
            return True
        else:
            return False


class Circle2:
    def __init__(self, radius):
        self.radius = radius

    def contains(self, x, y):
        if x**2 + y**2 <= self.radius:
            return True
        else:
            return False

