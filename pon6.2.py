import math

def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между двумя точками на плоскости по их координатам.
     x1: Координата x первой точки.
     y1: Координата y первой точки.
     x2: Координата x второй точки.
     y2: Координата y второй точки.
     Расстояние между точками.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по длинам его сторон с использованием формулы Герона.
     a: Длина первой стороны.
     b: Длина второй стороны.
     c: Длина третьей стороны.
     Площадь треугольника.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
x1, y1 = map(float, input("Введите координаты точки A: ").split())
x2, y2 = map(float, input("Введите координаты точки B: ").split())
x3, y3 = map(float, input("Введите координаты точки C: ").split())
a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x2, y2, x3, y3)
c = calculate_distance(x3, y3, x1, y1)
ploсhad = calculate_triangle_area(a, b, c)
print(f"Итоговая площадь треугольника: {ploсhad:.2f}")
