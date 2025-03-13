from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


# Функція, яка працює з будь-якою фігурою
def print_area(shape: Shape):
    print(f"Площа: {shape.calculate_area()}")


# Використання
square = Square(4)
circle = Circle(5)

print_area(square)  # Працює з квадратом
print_area(circle)  # Працює з колом