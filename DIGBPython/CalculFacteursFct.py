from math import *
import math

print(math.pi)


def CalculFacteurs(a, b):
    while b <= a:
        if a % b == 0:
            print(b)
            a = a / b
        else:
            b = b + 1


print("La décomposition en facteur de a est : ")
CalculFacteurs(800, 2)
