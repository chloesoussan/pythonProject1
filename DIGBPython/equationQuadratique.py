from math import *
import math

print(math.pi)

a = int(input("Saisir un chiffre: "))
b = int(input("Saisir un chiffre: "))
c = int(input("Saisir un chiffre: "))

delta = ((pow(b, 2)) - 4 * a * c)
if delta > 0:
    x1 = float(-b - sqrt(delta) / 2 * a)
    x2 = float(-b + sqrt(delta) / 2 * a)
    print("Les solutions sont : ", x1, x2)
elif delta < 0:
    print("Impossible")
else:
    x3 = (-b / (2 * a))
    print("Une seule solution : ", x3)

