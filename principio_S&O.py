class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        self.kwargs = kwargs

    def area(self):
        if self.shape_type == "circle":
            radius = self.kwargs.get("radius", 0)
            return 3.14 * radius ** 2
        elif self.shape_type == "rectangle":
            width = self.kwargs.get("width", 0)
            height = self.kwargs.get("height", 0)
            return width * height
        elif self.shape_type == "triangle":
            base = self.kwargs.get("base", 0)
            height = self.kwargs.get("height", 0)
            return 0.5 * base * height
        else:
            raise ValueError("Unsupported shape type")

shape1 = Shape("circle", radius=5)
shape2 = Shape("rectangle", width=3, height=4)
total_area = shape1.area() + shape2.area()
print("Total area:", total_area)

#------------------------------------------------------------------------------------

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

circle = Circle(5)
rectangle = Rectangle(3, 4)
total_area = calculate_total_area([circle, rectangle])
print("Total area:", total_area)
