class Shape:
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method")



class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method")


class ShapeFactory:
    def getShape(self, shape_type: 'str'):
        if shape_type == '':
            return Shape()
        elif shape_type == 'Rectangle':
            return Rectangle()
        elif shape_type == 'Square':
            return Square()
        elif shape_type == 'Circle':
            return Circle()
        return Shape()


factory = ShapeFactory()
shape = factory.getShape('Rectangle')
shape.draw()
shape = factory.getShape('Square')
shape.draw()
shape = factory.getShape('Circle')
shape.draw()


