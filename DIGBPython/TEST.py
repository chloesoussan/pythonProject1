from math import *
import math

print(math.pi)

# a = int(input("saisir un nombre : "))

# Lancement d'une boucle qui s'arrête à a en lui commandant a+1
# for b in range(1, a + 1):
# Si le reste de la division (a%i) est nul, afficher les diviseurs b
# if a % b == 0:
# print(b)


#ce programme consiste à changer toute les lettres d'un mot de 1 lettres au dessus

print("choissisez un mot à écrire :", end=" ")

b = ""
try:
    nom = str(input(""))
    nom = str.lower(nom)
    change = int(input("Veuillez choisir le nombre de lettre de décallage: "))
    if change > 26:
        print("valeur trop grande")
    else:
        for i in nom:
            if i == "Z" or i == "z":
                a = ord(i)
                a = (a - 26) + change
                lettre = chr(a)
            else:
                a = ord(i)
                a = a + change
                lettre = chr(a)
            b = b + lettre
        print(b)
except ValueError:
    print("mauvaise donnée", end="")
