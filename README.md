#  CYBERCAFÉ

## Présentation

Cybercafé est un jeu développé en Python dans lequel le joueur doit gérer son propre cybercafé.

L'objectif principal est de développer son activité, accueillir des clients, gérer les imprévus et surtout rembourser une dette de 400 000 FCFA en 30 jours maximum.

##  Objectif du jeu

Tu disposes de 30 jours pour rembourser intégralement ta dette.

Pour y parvenir, tu dois :
- Accueillir des clients et gagner de l'argent.
- Gérer les postes informatiques.
- Réparer les ordinateurs endommagés.
- Faire face aux coupures de courant.
- Gérer les attaques de rats.
- Effectuer des remboursements pour réduire ta dette.

Si tu ne rembourses pas ta dette dans les délais, tu perds la partie.

##  Commandes

| Touche | Action |
|---|---|
| S | Sauvegarder la partie |
| R | Mettre le jeu en pause |
| Q | Quitter le jeu |
| A | Passer au jour suivant |
| W | Rembourser la dette |

##  Système économique

- Argent initial : 250 000 FCFA.
- Dette initiale : 400 000 FCFA.
- Prix d'une session client : 2 500 FCFA.
- Remboursement minimum : 50 000 FCFA.
- Durée maximale : 30 jours.

##  Fonctionnalités

- Gestion des clients.
- Gestion des revenus.
- Gestion des dettes.
- Gestion des ordinateurs.
- Événements aléatoires.
- Système de pause.
- Système de sauvegarde et de chargement.

## Technologies utilisées

- Python 3
- Bibliothèque `random`
- Bibliothèque `time`
- Bibliothèque `json`
- Bibliothèque `select`
- Bibliothèque `termios`
- Bibliothèque `tty`

##  Structure du projet

```text
Cybercafe/
│
├── main.py
├── joueur.py
├── cybercafe.py
├── clients.py
├── temps.py
├── dette.py
├── pause.py
├── sauvegarde.py
│
├── sauvegarde.json
├── README.md
└── JOURNAL.md
```

##  Installation et lancement

1. Installer Python 3.
2. Télécharger ou cloner le projet.
3. Ouvrir un terminal dans le dossier Cybercafe.
4. Lancer la commande :

```bash
python3 main.py
```

## Sauvegarde

Pendant une journée, appuie sur `S` pour sauvegarder ta progression.

Au prochain lancement, choisis `C` pour continuer ta partie.

##  Auteur

Projet personnel de programmation réalisé dans le cadre de l'apprentissage du langage Python.

---

**CYBERCAFÉ – Gère ton cybercafé, gagne de l'argent et rembourse ta dette !**