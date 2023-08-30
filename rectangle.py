import math

class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Using Heron's formula to calculate the area of a triangle
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Create instances of different shapes
circle_radius = float(input("Enter the radius of the circle: "))
circle = Circle(circle_radius)

triangle_side1 = float(input("Enter the length of side 1 of the triangle: "))
triangle_side2 = float(input("Enter the length of side 2 of the triangle: "))
triangle_side3 = float(input("Enter the length of side 3 of the triangle: "))
triangle = Triangle(triangle_side1, triangle_side2, triangle_side3)

rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(rectangle_length, rectangle_width)

# Calculate and display the area and perimeter of each shape
print("Circle:")
print("Area:", circle.calculate_area())
print("Perimeter:", circle.calculate_perimeter())

print("\nTriangle:")
print("Area:", triangle.calculate_area())
print("Perimeter:", triangle.calculate_perimeter())

print("\nRectangle:")
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())







 
# 1. Start

# 1. Define the class Shape with the following methods:

#    - calculate_area(): Calculate and return the area of the shape.
#    - calculate_perimeter(): Calculate and return the perimeter of the shape.

# 1. Define the class Circle, which inherits from Shape, with the following methods:

#    - __init__(radius): Initialize the Circle object with the given radius.
#    - calculate_area(): Override the calculate_area() method to calculate and return the area of the circle (π * radius^2).
#    - calculate_perimeter(): Override the calculate_perimeter() method to calculate and return the perimeter of the circle (2 * π * radius).

# 1. Define the class Triangle, which inherits from Shape, with the following methods:

#    - __init__(side1, side2, side3): Initialize the Triangle object with the given side lengths.
#    - calculate_area(): Override the calculate_area() method to calculate and return the area of the triangle using Heron's formula.
#    - calculate_perimeter(): Override the calculate_perimeter() method to calculate and return the perimeter of the triangle (sum of all side lengths).

# 1. Define the class Rectangle, which inherits from Shape, with the following methods:

#    - __init__(length, width): Initialize the Rectangle object with the given length and width.
#    - calculate_area(): Override the calculate_area() method to calculate and return the area of the rectangle (length * width).
#    - calculate_perimeter(): Override the calculate_perimeter() method to calculate and return the perimeter of the rectangle (2 * (length + width)).

# 1. Create instances of the Circle, Triangle, and Rectangle classes based on user input or predefined values.

# 1. Call the calculate_area() and calculate_perimeter() methods for each shape instance.

# 1. Display the calculated area and perimeter for each shape.

# 1. End

 