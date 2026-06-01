import random

pin_reel = str(random.randint(0, 9999)).zfill(4)

print("PIN réel (pour la démo) :", pin_reel)

tentatives_max = 3

for tentative in range(tentatives_max):

    pin_test = str(random.randint(0, 9999)).zfill(4)

    print(f"Tentative {tentative + 1} : {pin_test}")

    if pin_test == pin_reel:
        print("PIN trouvé !")
        break

else:
    print("Carte bloquée après 3 erreurs.")