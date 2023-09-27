
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self):
        return self.x ** 2 + self.y ** 2 <= self.radius ** 2


p = Point(1, 4)
c = Circle(p.x, p.y, 5)
print(c.contains())