from math import *
import math

print(math.pi)

a = int(input("Saisir un chiffre: "))
b = int(input("Saisir un diviseur: "))
print("La décomposition en facteur de a est : ")
while b <= a:
    if a % b == 0:
        print(b)
        a = a / b
    else:
        b = b + 1
