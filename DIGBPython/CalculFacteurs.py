

a = int(input("Saisir un chiffre: "))

# Initialise le b à 0
b = 0
# On vérifie que b ets inférieur ou égal à a pour la division sinon ça marche pas
while b <= a:
    # Incrémenter à b+1 pour chaque diviseur pour les parcourir
    b = b + 1
    # Si le reste de la division (a%b) ->modulo est nul, afficher les diviseurs de b
    if a % b == 0:
        print(b)

# a = int(input("saisir un nombre : "))

# Lancement d'une boucle qui s'arrête à a en lui commandant a+1
# for b in range(1, a + 1):
# Si le reste de la division (a%i) est nul, afficher les diviseurs b
# if a % b == 0:
# print(b)
