from abc import ABC, abstractmethod


# Інтерфейс Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Клас Коло
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * self.radius ** 2


# Клас Прямокутник
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# Новий клас для обчислення площі
class AreaCalculator:
    def calculate(self, shape: Shape):
        return shape.calculate_area()


# Використання
circle = Circle(5)
rectangle = Rectangle(4, 6)
calculator = AreaCalculator()

print(f"Площа кола: {calculator.calculate(circle):}")
print(f"Площа прямокутника: {calculator.calculate(rectangle)}")