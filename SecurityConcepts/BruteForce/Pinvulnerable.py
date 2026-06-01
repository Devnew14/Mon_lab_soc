import random

# Génère un nombre aléatoire entre 0 et 9999
# Exemple : 42, 1234, 7, etc.
nombre_aleatoire = random.randint(0, 9999)

# Transforme le nombre en chaîne de caractères sur 4 chiffres
# 7 devient "0007"
# 42 devient "0042"
# 1234 reste "1234"
pin_reel = str(nombre_aleatoire).zfill(4)

# Affiche le PIN choisi pour la démonstration
# Dans un vrai système, on ne l'afficherait jamais
print("PIN réel (démo) :", pin_reel)

# Affiche une ligne de séparation
print("-" * 30)

# Compteur de tentatives
tentatives = 0

# Boucle de 0 à 9999 inclus
# Cela représente toutes les combinaisons possibles d'un PIN à 4 chiffres
for i in range(10000):

    # Convertit le nombre testé en format PIN sur 4 chiffres
    # Exemple :
    # 0 -> "0000"
    # 1 -> "0001"
    # 12 -> "0012"
    pin_test = str(i).zfill(4)

    # Incrémente le compteur de tentatives
    tentatives += 1

    # Vérifie si le PIN testé correspond au PIN réel
    if pin_test == pin_reel:

        # Si oui, affiche un message de succès
        print(f"[{tentatives}] Tentative : {pin_test} -> SUCCÈS")

        # Affiche le nombre total de tentatives nécessaires
        print(f"PIN trouvé après {tentatives} tentatives")

        # Arrête immédiatement la boucle
        break

    else:
        # Si le PIN ne correspond pas, affiche un échec
        print(f"[{tentatives}] Tentative : {pin_test} -> ÉCHEC")



# l existe seulement 10 000 PIN à 4 chiffres (0000 à 9999).
# Un attaquant peut tous les essayer.
# Tôt ou tard, il trouve le bon.