#mot = "Attack"
mot= str(input("Saisir votre mot : "))
#chaine de caractere vide dans laquelle on va stocker le resultat
res = ""
#On parcoure le mot dans la déclaration d'uhne boucle for
for i in mot:
    #On converti notre mot en nb ASCII + 1 (car décalage de plus 1 dans l'alphabet)
    x = ord(i) + 1
    #On converti le chiffre obtenu en chaine de caractere pour recup le mot
    y = chr(x)
#pour incrémenter le nb de lettre converti y pour obtenir le mot final
    res = res + y
print(res)
#"""ce programme consiste à changer toute les lettres d'un mot de 1 lettres au dessus """


#print("choissisez un mot à écrire :", end=" ")
# b = ""
# try:
#     nom = str(input(""))
#     nom=str.lower(nom)
#     change = int(input("Veuillez choisir le nombre de lettre de décallage: "))
#     if change > 26:
#         print("valeur trop grande")
#     else:
#         for i in nom:
#             if i == "Z" or i == "z":
#                 a = ord(i)
#                 a = (a-26)+change
#                 lettre = chr(a)
#             else:
#                 a = ord(i)
#                 a = a+change
#                 lettre = chr(a)
#             b = b+lettre
#         print(b)
# except ValueError:
#     print("mauvaise donnée", end="")
