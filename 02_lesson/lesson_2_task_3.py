import math


def square(side):
    return (side * side)


side = float(input("Введите сторону квадрата: "))
area = square(side)
round_area = math.ceil(area)

print(f'Площадь квадрата равна: {round_area}')
