from math import *
import math

print(math.pi)


# Fonction pour calculer le Delta
def Delta(a, b, c):
    return b * b - 4 * a * c


# Fonction pour résoudre l'équation en fonction de la valeur de delta (conditions)
def resoudreEquation(a, b, c):
    delta = Delta(a, b, c)
    if delta > 0:
        x1 = float(-b - sqrt(delta) / 2 * a)
        x2 = float(-b + sqrt(delta) / 2 * a)
        return print("Les solutions sont : ", x1, x2)
    elif delta < 0:
        return print("Impossible")
    else:
        x3 = (-b / (2 * a))
        return print("Une seule solution : ", x3)


# Appel de la fonction
print("Résoudre une équation du second degré : ")
Delta(1, 0, -1)
resoudreEquation(1, 0, -1)
