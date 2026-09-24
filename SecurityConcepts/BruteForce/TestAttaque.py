# Démonstration pédagogique uniquement

mot_de_passe = "abc"

alphabet = "abcdefghijklmnopqrstuvwxyz"

tentatives = 0

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            tentative = a + b + c
            tentatives += 1

            if tentative == mot_de_passe:
                print(f"Mot de passe trouvé : {tentative}")
                print(f"Nombre de tentatives : {tentatives}")
                exit()