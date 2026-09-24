Bandit Level 9 → 10
Commandes utilisées :
strings data.txt
strings data.txt | grep =

Notes :
Le fichier était binaire, pas lisible avec cat.
strings permet d’extraire le texte lisible.
Ensuite, grep aide à repérer ce qui ressemble à un mot de passe.
