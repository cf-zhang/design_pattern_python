from copy import deepcopy
class Shape:
    def __init__(self):
        self._id = ""
        self._type = ""

    def draw(self):
        pass

    def clone(self):
        return deepcopy(self)

    @property
    def type(self):
        return self._type
    @property
    def id(self):
        return self._id

    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._type = value

    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._id = value

class Rectangle(Shape):
    def __init__(self):
        self.type = "Rectangle"

    def draw(self):
        print("Inside Rectangle::draw() method")

class Square(Shape):
    def __init__(self):
        self.type = "Square"

    def draw(self):
        print("Inside Square::draw() method")


class Circle(Shape):
    def __init__(self):
        self.type = "Circle"

    def draw(self):
        print("Inside Circle::draw() method")

class ShapeCache:
    def __init__(self):
        self.shape_map = dict()

    def get_shape(self, shape_id):
        return self.shape_map.get(shape_id).clone()

    def load_cache(self):
        circle = Circle()
        circle.type = "circle"
        circle.id = "1"
        self.shape_map["1"] = circle

        rectangle = Rectangle()
        rectangle.type = "rectangle"
        rectangle.id = "2"
        self.shape_map["2"] = rectangle

        square = Square()
        square.type = "square"
        square.id = "3"
        self.shape_map["3"] = square


shape_cache = ShapeCache()
shape_cache.load_cache()
square = shape_cache.get_shape("3")
square.draw()

circle = shape_cache.get_shape('1')
circle.draw()

rectangle = shape_cache.get_shape('2')
rectangle.draw()