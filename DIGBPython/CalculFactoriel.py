from math import *
import math

print(math.pi)

n = int(input("Saisir un chiffre: "))
# initialisée à 1
fact = 1

if n > 0:
    for i in range(1, n + 1):
        fact = fact * i
    print("Le calcul factoriel de n est : n!= ", fact)
elif n < 0:
    print("Le calcul factoriel de n'existe pas pour les nombres négatifs")
elif n == 0:
    print("Le calcul factoriel de 0 est 1: 0!=1")
elif n == 1:
    print("Le calcul factoriel de 1 est 1: 1!=1")
