Bandit Level 6 → 7
Commandes utilisées :
find / -type f -user bandit7 -group bandit6 2>/dev/null
cat chemin_du_fichier

Notes :
Le fichier était n’importe où sur le système.
Il fallait chercher par propriétaire et groupe.
2>/dev/null sert à cacher les messages d’erreur (très pratique).
