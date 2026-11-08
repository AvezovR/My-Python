import math

def side_cylinder(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * math.pi * (r ** 2)
    return side, full

radius = float(input("Введите радиус:"))
height  = float(input("Введите высота:"))

a, b = side_cylinder(radius, height)

print(a)
print(b)
