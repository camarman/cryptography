from random import uniform
from math import sqrt

L = 1


def distance(P1, P2):
    return sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)


count = 0
for j in range(10**6):
    position_triangle = []
    for i in range(3):
        x_1 = uniform(0, 1)
        y_1 = uniform(0, L)
        position_triangle.append((x_1, y_1))
    a = distance(position_triangle[0], position_triangle[1])
    b = distance(position_triangle[1], position_triangle[2])
    c = distance(position_triangle[2], position_triangle[0])
    cos_A = (b**2 + c**2 - a**2)
    cos_B = (a**2 + c**2 - b**2)
    cos_C = (a**2 + b**2 - c**2)
    if not(cos_A > 0 and cos_B > 0 and cos_C > 0):
        count += 1
print(count / 10**6)
