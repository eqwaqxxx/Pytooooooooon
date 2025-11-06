import math
x = float(input("Введите угол в градусах пж: "))
radian = x * math.pi / 180
result = math.sin(radian) + math.cos(radian) + math.tan(radian) ** 2
print(result)
