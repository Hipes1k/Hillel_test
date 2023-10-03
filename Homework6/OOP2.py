#1
class frange:
    def __init__(self, *args):
        arg_number = len(args)
        if arg_number == 1:
            self.start = 0.0
            self.end = float(args[0])
            self.step = 1.0
        elif arg_number == 2:
            self.start = float(args[0])
            self.end = float(args[1])
            self.step = 1.0
        elif arg_number == 3:
            self.start = float(args[0])
            self.end = float(args[1])
            self.step = float(args[2])



    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.current < self.end or self.step < 0 and self.current > self.end:
            self.result = self.current
            self.current += self.step
            return self.result
        else:
            raise StopIteration
f = frange(0, 100, 3.5)
for i in f:
    print(i)
assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []

print('SUCCESS!')

#2
class Colorizer:
    colors = {
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'default': '\033[0m'
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):

        return print(self.colors.get(self.color, self.colors['default']), end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.colors['default'], end='')

with Colorizer('yellow'):
    print("Hello")
print("Hello")

#3
import math


class Shape: #class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi*self.radius**2


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width*self.height


class Triangle(Shape):
    def __init__(self, x, y, a, height):
        super().__init__(x, y)
        self.a = a
        self.height = height

    def square(self):
        return 0.5 * self.a * self.height


class Parallelogram(Shape):
    def __init__(self, x, y, a, height):
        super().__init__(x, y)
        self.a = a
        self.height = height

    def square(self):
        return self.a * self.height


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)


t = Triangle(0, 0, 10, 15)
t1 = Triangle(0, 10, 6, 5)
t2 = Triangle(10, 15, 8, 7)


c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)


p = Parallelogram(1, 2, 20, 30)
p1 = Parallelogram(1, 2, 20, 30)
p2 = Parallelogram(2, 4, 6, 8)


scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(t)
scene.add_figure(t1)
scene.add_figure(t2)
scene.add_figure(p)
scene.add_figure(p1)
scene.add_figure(p2)
scene.add_figure(c)
scene.add_figure(c1)


total_sq = scene.total_square()
print(total_sq)

#4
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __contains__(self, point):
        return self.x ** 2 + self.y ** 2 <= self.radius ** 2


p = Point(4, 4)
c = Circle(p.x, p.y, 5)
print(p in c)