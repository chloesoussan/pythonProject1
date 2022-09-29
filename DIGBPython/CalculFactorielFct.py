from math import *
import math

print(math.pi)


def Calculfactoriel(n):
    fact = 1
    if n > 1:
        fact = fact * n
        n -= 1
        return fact
    elif n == 0:
        return 1
    elif n < 0:
        return print("Le calcul factoriel de n'existe pas pour les nombres négatifs")
    elif n == 1:
        return 1


n = 5
print("Le calcul factoriel de n", n, "est n!= ", factorial(n))
