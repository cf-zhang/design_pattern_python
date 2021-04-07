
class DrawApi:
    def draw_circle(self, radius: 'int', x: 'int', y: 'int'):
        pass

class RedCircle(DrawApi):
    def draw_circle(self, radius: 'int', x: 'int', y: 'int'):
        print("drawing circle red")


class GreenCircle(DrawApi):
    def draw_circle(self, radius: 'int', x: 'int', y: 'int'):
        print("drawing circle green")


class Shape:
    def __init__(self, draw_api: 'DrawApi'):
        self.draw_api = draw_api

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x: 'int', y: 'int', radius: 'int', draw_api: 'DrawApi'):
        self.x = x
        self.y = y
        self.radius = radius
        Shape.__init__(self, draw_api)

    def draw(self):
        self.draw_api.draw_circle(self.radius, self.x, self.y)

red_circle = Circle(100, 100, 10, RedCircle())
red_circle.draw()

green_circle = Circle(1, 2, 1, GreenCircle())
green_circle.draw()





