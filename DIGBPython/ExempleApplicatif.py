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
        brin = input("Veuillez saisir un chaîne d'ADN : ")
    # Fin du tant que, la fonction retourne la chaine valide en majuscule si l'utilisateur a rentré la chaine en
    # minuscule
    return brin.upper()


# Fonction pour extraire les combinaisons (couples) d'une chaîne d'ADN : extraction d'une sous-chaîne
def Proportion(sequence, chaine):
    # On déclare un compteur à 0
    count = 0
    # On vérifie que la longueur de la séquence saisie n'est pas supérieur à la longueur de la chaine pour pouvoir
    # calculer le pourcentage
    if len(sequence) > len(chaine):
        return 0
    # Si la condition de longueur de la chaine est plus grande que la sequence alors :
    elif len(sequence) <= len(chaine):
        # On parcoure notre liste : de 0 à la longueur n-1 afin de récupérer toutes les occurences de la liste
        for i in range(0, len(chaine) - 1):
            # On va comparer les index(position) de début et de fin de notre chaine aux index de début et de fin de
            # la séquence saisie :
            # sequence[0] = position 1 : ex C
            # sequence[1] = position 2 : ex C-A
            if chaine[i] == sequence[0].upper():
                # Si ces 2 positions : i et i+1 correspondent à la séquence saisie alors :
                # On ajoute au compteur pour calculer le nb de fois où il apparaît
                if chaine[i + 1] == sequence[1].upper():
                    count = count + 1
        # On affiche à la fin du Pour, une fonction qui calcule le pourcentage des couples de séquences saisies
        return (100 * count) / len(chaine)


# Programme principal :

# Appel de la fonction de Saisie() d'une chaine et qui vérifie sa validité
chaine = Saisie()
print("Votre chaîne d'ADN saisie :", chaine)

seq = input("Saisir une séquence : ")
# Appel de la fonction Proportion qui extrait la séquence saisie et calcule son pourcentage par rapport à la chaine

x = Proportion(seq, chaine)
# Gestion des cas d'erreurs : si la séquence saisie n'existe pas ou qu'il n'y a pas d'occurences
if x:
    print("Il y a", x, "% de", seq.upper(), "dans votre chaîne")
else:
    print("Erreur,il n'y a pas d'occurences de la séquence saisie ou la séquence n'existe pas dans la chaîne !")
