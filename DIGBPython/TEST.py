from math import *
import math

print(math.pi)

# a = int(input("saisir un nombre : "))

# Lancement d'une boucle qui s'arrête à a en lui commandant a+1
# for b in range(1, a + 1):
# Si le reste de la division (a%i) est nul, afficher les diviseurs b
# if a % b == 0:
# print(b)


# ce programme consiste à changer toute les lettres d'un mot de 1 lettres au dessus

# print("choissisez un mot à écrire :", end=" ")
#
# b = ""
# try:
#     nom = str(input(""))
#     nom = str.lower(nom)
#     change = int(input("Veuillez choisir le nombre de lettre de décallage: "))
#     if change > 26:
#         print("valeur trop grande")
#     else:
#         for i in nom:
#             if i == "Z" or i == "z":
#                 a = ord(i)
#                 a = (a - 26) + change
#                 lettre = chr(a)
#             else:
#                 a = ord(i)
#                 a = a + change
#                 lettre = chr(a)
#             b = b + lettre
#         print(b)
# except ValueError:
#     print("mauvaise donnée", end="")

# count = 0
# compteurC=0
# compteurG=0
#
# for i in open("DNA.txt").read():
#     count = count+1
#     if i=="G":
#         compteurG =compteurG+1
#     elif i =="C":
#         compteurC = compteurC+1
# for j in range(len(i)):
#     print(j)
#
# pourcentageC = (compteurC * 100)/count
# pourcentageG = (compteurG * 100) /count
#
# print("Le nombre de caractères de la chaîne est",count)
# print("Le pourcentage de C dans la chaîne est :", compteurC,"%")
# print("Le pourcentage de G dans la chaîne est :", compteurG,"%")


# count = 0
# x=open("DNA.txt").read()
# for i in range(0,len(x)-1):
#     if x[i] == "G":
#         if x[i+1] == "C":
#             count = count + 1
# print(x.count("GC"))
# print(x.find("G"))
# print(x.find("G"))

#On ouvre et on lit notre fichier DNA
x = open("DNA.txt").read()
#On déclare un compteur à 0
nbGC = 0
#On parcoure notre liste : de 0 à la longueur n-1
for i in range(0,len(x)-1):
    #Si lors du parcours de la liste,
    if x[i] in "G":
        print(x[i])
        if x[i+1] in "C":
            print(x[i+1])
            nbGC = nbGC + 1
            #print(nbGC)
print(round(nbGC * 100) // len(x))


# def Valide(seq):
#     # Retourne True si la séquence est vrai, sinon False
#     for c in seq:  # pour chaque c de ch
#         if c in "atgc":
#             return True
#         else:
#             return False
#
#
# def Saisie(ch):
#     n = ""
#     while not Valide(n):
#         print("Erreur les valeurs de saisies sont incorrectes")
#         n = input("Veuillez saisir un brin d'ADN ('at','ta','cg','gc') : ")
#     return n


# ch = input("Saisir une chaine : ")
# print(Saisie(ch))
