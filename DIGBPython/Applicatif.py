# def Valide(chaine):
#     adn = ["a", "t", "g", "c"]
#     try:
#         for caractere in chaine:
#             if caractere not in adn:
#                 return False
#         return True
#     except chaine == "":
#         return False
#
#
# def Saisie():
#     brin = ""
#     while not Valide(brin):
#         brin = input("Veuillez saisir à nouveau erreur : ")
#     return brin
#
#
# chaine = Saisie()
# print(chaine)

# def verif(caractere):
#     x = []
#     count = 0
#     adn = ("at ta cg gc".split())
#     for caractere in adn:
#         count = count + 1
#         if caractere == "cg" or caractere == "gc" or caractere == "at" or caractere == "ta":
#             x.append(caractere)
#         return True
#     else:
#         return False
#
#
# x1 = input("veuillez Saisire un brin d'ADn : ")
# print(verif(x1))

# def Valide(ch):
#     c = ""
#     ch = (["at", "ta", "cg", "gc"])
#     try:
#         if c in ch:
#             return True
#     except ValueError:
#         return False
#
#
# def Saisie():
#     c = input("Veuillez saisir un brin d'ADN : ")
#     try:
#         while Valide(c):
#             return c
#     except ValueError:
#         return print("Mauvaise donnée", end="")
#
#
# chaine = Saisie()
# print(chaine)

# def Valide():
#     adn = (["at", "ta", "cg", "gc"])
#     try:
#         for caractere in ch:
#             if adn == "":
#                 return False
#             elif caractere in adn:
#                 return True
#     except:
#         return False
#
#
# def Saisie(c):
#     if Valide():
#         return c
#     else:
#         print("Erreur les valeurs de saisies sont incorrectes")
#
#
# chaine = input("Veuillez saisir un brin d'ADN ('at','ta','cg','gc') : ")
# x = Saisie(chaine)
# print(x)
# def Proportion(chaine, sequence):
#     c = len(chaine)
#     s = len(sequence)
#     count = 0
#     for i in range(0, c-s+1):
#         if chaine[i: i+s] == sequence:
#             count = count + 1
#         return count
#

#
# def Proportion(sequence, chaine):
#     totalA = sequence.count('a')
#     totalT = sequence.count('t')
#     totalC = sequence.count('c')
#     totalG = sequence.count('g')
#     CA = 100 * (totalC + totalA) / len(chaine)
#     return CA


# Fonction qui permet d'avoir toutes les combinaisons de séquences possibles d'ADN grâce à la libraire Python itertools
# from itertools import combinations_with_replacement
# def combinaison(a):
#     a = ['a', 'c', 'g', 't']
#     for i in combinations_with_replacement(a, 2):
#         print(i)
#     return i