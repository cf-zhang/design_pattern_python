class Shape:
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")

class Circle(Shape):
    def draw(self):
        print("Shape : Circle")

class ShapeDecorator(Shape):
    def __init__(self, decorated_shape: 'Shape'):
        self.decorated_shape = decorated_shape
    def draw(self):
        self.decorated_shape.draw()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape: 'Shape'):
        ShapeDecorator.__init__(self, decorated_shape)

    def draw(self):
        self.decorated_shape.draw()
        self.setRedBorder(self.decorated_shape)

    def setRedBorder(self, decorated_shape: 'Shape'):
        print("Border Color: Red")

class GreenShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape: 'Shape'):
        ShapeDecorator.__init__(decorated_shape)

    def draw(self):
        self.decorated_shape.drwa()
        self.setRedBorder(self.decorated_shape)

    def setRedBorder(self, decorated_shape: 'Shape'):
        print("Border Color: Green")


circle = Circle()
red_circle = RedShapeDecorator(circle)
circle.draw()
red_circle.draw()


