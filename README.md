---
title : 2048 en python (Projet Conception Logiciel)
author : Stievenard Emma, Mezouar Chahinez et Szewczyk Clément
date : 13/09/2024 - 07/01/2025

---


<!-- TOC -->

- [Résumé du projet](#résumé-du-projet)
- [Installation  / Prérequis](#installation---prérequis)
- [Structure du projet](#structure-du-projet)
- [Jouer au jeu](#jouer-au-jeu)
  - [Lancer le gestionnaire de base de données](#lancer-le-gestionnaire-de-base-de-données)
  - [Gérer la connexion à la base de données](#gérer-la-connexion-à-la-base-de-données)
  - [Lancer le jeu](#lancer-le-jeu)
  - [Connexion / Inscription](#connexion--inscription)
  - [Règles du jeu](#règles-du-jeu)

# Résumé du projet

Projet du cours Conception Logiciel réalisé par : 

- Stievenard Emma, 
- Mezouar Chahinez 
- Szewczyk Clément

Ce projet implémente le jeu 2048 en Python en utilisant **Pygame**. Le but du jeu est de déplacer les tuiles sur une grille pour combiner des valeurs égales et atteindre la valeur cible de 2048. L'application inclut une gestion simple des tuiles, une connexion avec une base de données pour enregistrer les scores et permet de rejouer ou de quitter une partie. 

Le projet est consultable sur le dépôt GitHub : [2048 en python](https://github.com/Clement-Szewczyk/2048_SDN)


# Installation  / Prérequis

- Avoir une version de **Python 3.11.4** ou supérieure installée sur votre machine. \ 

Vous pouvez télécharger Python sur le site officiel : [Python](https://www.python.org/downloads/)

- Avoir installé le module **Pygame**. \
Pour installer Pygame, ouvrez un terminal et tapez la commande suivante : 

```bash
pip install pygame
```

- Avoir installé le module **mysql-connector-python**. \

Pour installer mysql-connector-python, ouvrez un terminal et tapez la commande suivante : 

```bash
pip install mysql-connector-python
```

- Avoir installé le module **bcrypt**. \

Pour installer bcrypt, ouvrez un terminal et tapez la commande suivante : 

```bash
pip install bcrypt
```


- Récupérer le projet sur GitHub. \
Pour récupérer le projet, vous pouvez cloner le dépôt GitHub en utilisant la commande suivante : 

```bash
git clone <https://github.com/Clement-Szewczyk/2048_SDN>

cd 2048_SDN
```

- Avoir un gestionnaire de base de données (pouvant utiliser des bases de données MYSQL)

Vous devez importer la base de données du jeu. Pour cela, vous pouvez utiliser le fichier `2048.sql` situé dans le dossier `BDD`. 


# Structure du projet 

- `2048_SDN` : Dossier principale
  - doc : Dossier contenant la documentation du projet
    - `doc.md` : Fichier contenant la documentation du projet au format Markdown
  - BDD : Dossier contenant le fichier SQL de la base de données
    - `2048.sql` : Fichier SQL de la base de données
  - src : Dossier contenant le code source du projet
    - `main.py` : Fichier principal du jeu 2048 
    - `classTuile.py` : Fichier de la classe Tuile (Gestion des tuiles)
    - `classGrille.py` : Fichier de la classe Grille (Gestion de la grille)
    - `classJeu.py` : Fichier de la classe Jeu (Gestion de la logique du jeu)
    - `classeEcran.py` : Fichier de la classe Ecran (Gestion de l'affichage)
    - `classeBandeau.py` : Fichier de la classe Bandeau (Gestion de l'affichage du bandeau)
    - `authentificationVisu.py` : Fichier gérant le visuel de l'authentification
    - `authentification.py` : Fichier gérant l'authentification
  - `README.md` : Fichier README du projet
  - `.gitignore` : Fichier pour ignorer certains fichiers lors de l'ajout sur le dépôt GitHub
  

# Jouer au jeu

## Lancer le gestionnaire de base de données

Afin de pouvoir lancer le jeu sans erreur, vous devez lancer le gestionnaire de base de données. 

## Gérer la connexion à la base de données

Pour gérer la connexion à la base de données, vous devez modifier les informations de connexion dans le fichier `authentification.py` situé dans le dossier `src`. 

```python

    def __init__(self, host="localhost", user="root", 
                 password="root", database="jeu2048", port=3305):
        """Initialise la connexion à la base de données et prépare le curseur."""
        # Connexion à la base de données MySQL
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.db.cursor()
```

Vous devez mettre à jour les informations suivantes :
- `host` : Adresse IP de votre serveur MySQL
- `user` : Nom d'utilisateur de votre base de données
- `password` : Mot de passe de votre base de données
- `database` : Nom de la base de données
- `port` : Port de connexion à la base de données

## Lancer le jeu

Pour lancer le jeu, ouvrez un terminal. Placez-vous dans le dossier `src` du projet et tapez la commande suivante : 

```bash
python main.py
```

Le jeu 2048 s'ouvre dans une fenêtre Pygame. 

## Connexion / Inscription

Au lancement du jeu, une fenêtre d'authentification s'ouvre. Vous pouvez vous connecter avec un compte existant ou vous inscrire.

Dans la base de données fournie, il existe le compte suivant :
- Identifiant : `L3SDN@gmail.com`
- Mot de passe : `L3SDN`
  
Vous pouvez utiliser ce compte pour vous connecter et jouer au jeu.

Vous pouvez également vous inscrire en cliquant sur le bouton `Inscription`.

## Règles du jeu

Le but du jeu est de déplacer les tuiles sur une grille pour combiner des valeurs égales et atteindre la valeur cible de 2048.

- Utilisez les flèches directionnelles pour déplacer les tuiles vers le haut, le bas, la gauche ou la droite.
- Lorsque deux tuiles avec la même valeur se touchent, elles fusionnent en une seule tuile avec la somme des deux valeurs.
- Une nouvelle tuile apparaît après chaque déplacement.
- Pour gagner la partie, vous devez atteindre une tuile de `2048`.
- Vous pouvez continuer à jouer après avoir atteint `2048` pour obtenir un score plus élevé.
- Si la grille est pleine et que vous ne pouvez plus déplacer les tuiles, la partie est terminée.



