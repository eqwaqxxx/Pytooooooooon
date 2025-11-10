import math
def calculate_rectangle_area(width, height):
    return width * height
def calculate_circle_area(radius):
    return math.pi * radius ** 2
width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))
rect_area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника: {rect_area}")
radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)
print(f"Площадь круга: {circle_area}")
