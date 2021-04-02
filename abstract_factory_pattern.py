
class AbstractFactory:
    def get_color(self, color: 'str'):
        pass

    def get_shape(self, shape: 'str'):
        pass

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


class Color:
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        print("Inside Red::fill() method.")

class Green(Color):
    def fill(self):
        print("Inside Green::fill() method.")

class Blue(Color):
    def fill(self):
        print("Inside Blue::fill() method.")


class ColorFactory(AbstractFactory):
    def get_shape(self, shape: 'str'):
        return Shape()

    def get_color(self, color: 'str'):
        if color == '':
            return Color()
        elif color == 'Red':
            return Red()
        elif color == 'Green':
            return Green()
        elif color == 'Blue':
            return Blue()
        return Color()


class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_type: 'str'):
        if shape_type == '':
            return Shape()
        elif shape_type == 'Rectangle':
            return Rectangle()
        elif shape_type == 'Square':
            return Square()
        elif shape_type == 'Circle':
            return Circle()
        return Shape()
    def get_color(self, color: 'str'):
        return Color()

class FactoryProducer:
    def getFactory(self, choice: 'str'):
        if choice == 'Shape':
            return ShapeFactory()
        elif choice == 'Color':
            return ColorFactory()
        return None




factory_producer = FactoryProducer()
color_factor = factory_producer.getFactory('Color')
red = color_factor.get_color('Red')
red.fill()

shape_factory = factory_producer.getFactory('Shape')
circle = shape_factory.get_shape('Circle')
circle.draw()

