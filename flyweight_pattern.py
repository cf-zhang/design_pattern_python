class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, color: 'str'):
        self.x = 0
        self.y = 0
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw(self):
        print("Shape : Circle [" + str(self.x) + ',' + str(self.y) + '] color: ' + self.color)


class ShapeFactory:
    def __init__(self):
        self.circle_map = dict()

    def getCircle(self, color: 'str'):
        circle = self.circle_map.get(color)
        if circle is None:
            circle = Circle(color)
            self.circle_map[color] = circle
            print("creating circle of color: " + color)
        return circle


import random

shape_factory = ShapeFactory()
colors = ['Red', 'Green', 'Blue', 'White', 'Black']
for x in range(1, 20):
    circle = shape_factory.getCircle(random.choice(colors))
    circle.set_x(random.randint(1, 5))
    circle.set_y(random.randint(6, 9))
    circle.draw()
