class Shape:
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")

class Circle(Shape):
    def draw(self):
        print("Shape : Circle")
class Square(Shape):
    def draw(self):
        print("Shape : Square")

class ShapeMaker():
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()

    def draw_circle(self):
        self.circle.draw()

    def draw_rectangle(self):
        self.rectangle.draw()

    def draw_square(self):
        self.square.draw()

shape_maker = ShapeMaker()
shape_maker.draw_square()
shape_maker.draw_rectangle()
shape_maker.draw_circle()

