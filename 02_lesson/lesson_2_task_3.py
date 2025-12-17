import math


def square(a):
    return math.ceil(a ** 2)


s = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(s)}")
