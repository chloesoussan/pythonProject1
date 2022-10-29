# Fonction qui valide la chaîne de caractere de la fonction Saisie(), prend en paramètre d'entrée une chaîne
def Valide(ch):
    # On stocke dans une liste, les composants unique d'un brin d'ADN qui sont : a,t,g,c
    adn = ['a', 'g', 't', 'c']
    # On vérifie  d'abord pour que la chaîne soit valide qu'elle ne soit pas vide : renvoit False
    if ch == "":
        return False
    # Sinon, on parcoure notre liste de composants d'adn, et on vérifie :
    else:
        for caractere in ch:
            # Si les caracteres saisis dans notre chaîne ne sont pas dans notre liste de composants ADN on retourne faux
            if caractere not in adn:
                return False
        # sinon, on sort de la boucle et on retourne vrai
        return True


# Fonction de Saisie d'un brin d'ADN qui appelle la fonction Valide pour vérifier
def Saisie():
    # On déclare une chaîne de caractere vide
    brin = ""
    # Condition tant que la chaine de caractere "brin" n'est pas valide, on demande à l'utilisateur de saisir un
    # nouveau brin
    while not Valide(brin):
        brin = input("Veuillez saisir un brin d'ADN : ")
    # Fin du tant que, la fonction retourne la chaine valide
    return brin


# Fonction pour compter le nombre d'occurences d'un brin d'ADN
def Proportion(sequence, chaine):
    # On déclare un compteur à 0
    count = 0
    # On vérifie que la longueur de la séquence saisie n'est pas supérieur à la longueur de la chaine pour pouvoir
    # calculer le pourcentage
    if len(sequence) > len(chaine):
        return 0
    # Si la condition de longueur de chaine est plus grande que la sequence alors :
    elif len(sequence) <= len(chaine):
        # On parcoure notre liste : de 0 à lalongueur n-1 afin de récupérer toutes les occurences de la liste
        for i in range(0, len(chaine) - 1):
            # Si lors du parcours de la liste, notre index(position) tombe sur un "c"
            if chaine[i] in "c":
                # On affiche la première occurence de c
                # print(chaine[i])
                # Si après avoir parcouru tout mes c, à index+1 on a un a(donc c-a)
                if chaine[i + 1] in "a":
                    # On l'ajoute à notre compteur pour indiquer, qu'il y a un couple c-a
                    count = count + 1
                    # print(chaine[i + 1])
        # On affiche à la fin du Pour, une fonction qui calcule le pourcentage des couples c-a
        return (100 * count) / len(chaine)
    return 1


chaine = Saisie()
print("Votre chaine d'ADN saisie :", chaine)
seq = input("Saisir une séquence : ")
x = Proportion(seq, chaine)
print("Il y a", x, "% de", seq, "dans votre chaîne")
