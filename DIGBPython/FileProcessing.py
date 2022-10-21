# x = open("DNA.txt").read()
# print(x)

#On déclare un compteur à 0
count = 0
#On déclare un tableau vide
liste = []
#On parcoure le fichier texte DNA avec le compteur incrémenter à n+1 pour parcourir tous les étélments du fichier
for caractere in open("DNA.txt").read():
    count = count + 1
    #Si dans le fichier il y a le caractère C et G
    if caractere == "C" or caractere == "G":
        #Alors on l'ajoute à la liste vide crée au début
        liste.append(caractere)
        #print(liste)
#On calcul le pourcentage d'avoir les caractères c+g dans la liste
pourcentage = 100 * len(liste) / count
#On affiche le résultat
print("Le fichier DNA contient", pourcentage, "%", "de caractères C+G")
