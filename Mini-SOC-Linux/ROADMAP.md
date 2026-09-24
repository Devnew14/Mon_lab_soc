# 🛡️ Mini SOC Linux — Roadmap

## 🎯 Objectif

Construire progressivement un laboratoire personnel permettant de comprendre le fonctionnement d'un environnement SOC : réseau, logs, détection, investigation et SIEM.

---

## 🟢 Niveau 1 — Environnement Linux

* [ ] Préparer les machines virtuelles
* [ ] Comprendre la configuration réseau
* [ ] `ip addr`
* [ ] `ip route`
* [ ] `ss`
* [ ] `ps`
* [ ] Utilisateurs et groupes
* [ ] Permissions Linux
* [ ] Services Linux

---

## 🟢 Niveau 2 — Analyse réseau

* [ ] Comprendre Ethernet
* [ ] Comprendre IPv4
* [ ] Comprendre ARP
* [ ] Comprendre ICMP
* [ ] Comprendre TCP / UDP
* [ ] Comprendre DNS
* [ ] Utiliser Wireshark
* [ ] Analyser une capture PCAP
* [ ] Utiliser tcpdump

---

## 🟡 Niveau 3 — Logs

* [ ] Comprendre les logs Linux
* [ ] Identifier les fichiers de logs importants
* [ ] Analyser les événements SSH
* [ ] Identifier les tentatives de connexion
* [ ] Rechercher des événements suspects
* [ ] Automatiser une recherche simple

---

## 🟡 Niveau 4 — Détection

* [ ] Définir un comportement normal
* [ ] Créer des scénarios suspects dans le laboratoire
* [ ] Identifier des tentatives SSH répétées
* [ ] Détecter des anomalies dans les logs
* [ ] Créer des règles simples de détection
* [ ] Documenter les résultats

---

## 🟠 Niveau 5 — Python

* [ ] Lire un fichier de logs
* [ ] Parser des événements
* [ ] Extraire des adresses IP
* [ ] Compter les événements
* [ ] Identifier des répétitions
* [ ] Générer un rapport
* [ ] Automatiser une détection simple

---

## 🔴 Niveau 6 — SIEM

* [ ] Installer/configurer un SIEM
* [ ] Envoyer des logs Linux
* [ ] Rechercher des événements
* [ ] Créer des requêtes de détection
* [ ] Créer des alertes
* [ ] Créer un dashboard
* [ ] Documenter une investigation

---

## ⭐ Niveau 7 — Investigation SOC

Pour chaque incident simulé :

1. Identifier l'événement
2. Collecter les preuves
3. Analyser les logs
4. Analyser le trafic réseau
5. Identifier les indicateurs pertinents
6. Déterminer la chronologie
7. Documenter les résultats
8. Proposer des mesures de sécurité

---

## 🚀 Projet final

Construire un scénario complet :

```text
Activité dans le laboratoire
        ↓
Logs / trafic réseau
        ↓
Collecte
        ↓
Détection
        ↓
Alerte
        ↓
Investigation
        ↓
Rapport
        ↓
Mesures de sécurité
```

### Compétences finales

* Linux
* TCP/IP
* Analyse réseau
* Wireshark
* Logs
* Python
* Détection
* SIEM
* Investigation SOC
* Documentation technique
