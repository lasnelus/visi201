# Projet VISI201 : Pavage de Polyominos et Nombre de Heggs

Ce projet, réalisé dans le cadre du cours VISI201, explore le pavage de polyominos et le calcul du nombre de Heggs. Il génère des clauses logiques pour un solveur SAT afin de trouver des solutions à des problèmes de pavage en utilisant des polyominos. Le projet est principalement développé en Python.

## Contenu du projet

Contenu du projet
Le répertoire contient les fichiers et dossiers suivants :

 - affichage_piece.py : Fonctions pour afficher des polyominos sous forme de lettres dans un tableau de taille fixe.​

 - conv_res.py : Comprend la fonction execSAT13 pour exécuter le solveur SAT et traiter les résultats.​

 - createur_de_clause_v3.py : Génère les clauses logiques nécessaires pour le solveur SAT en fonction des polyominos et de la grille spécifiée.​

 - creation_polyominos.py : Contient des définitions et des transformations de polyominos, y compris des fonctions pour la rotation et la symétrie.​

 - main.py : Point d'entrée principal du projet, coordonne la génération des clauses, l'exécution du solveur SAT et l'affichage des résultats.​

 - tab.txt : Fichier de configuration définissant la grille de pavage, où chaque cellule utilisable est marquée par un #.​

 - piece.txt, piecetest.txt : Fichiers contenant des définitions de polyominos utilisés pour le pavage.​

 - resSAT13.txt : Fichier généré contenant les résultats de l'exécution du solveur SAT.​

 - clausepavage.txt : Fichier généré contenant les clauses logiques pour le solveur SAT.​



## Prérequis

- Python 3.x
- GCC (utilisation des fichier présent dans le repo, afin d'installer SAT13)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/lasnelus/visi201.git

2. Accédez au répertoire du projet :

    ```bash
    cd visi201

Utilisation
Préparation de la grille et des polyominos :

Modifiez le fichier tab.txt pour définir la grille de pavage. Chaque cellule utilisable doit être marquée par un #.​

Définissez les polyominos dans les fichiers piece.txt ou piecetest.txt selon vos besoins.​

Génération des clauses logiques :

Exécutez le script createur_de_clause_v3.py pour générer le fichier clausepavage.txt contenant les clauses logiques pour le solveur SAT.​

Exécution du solveur SAT :

Utilisez le script conv_res.py pour exécuter le solveur SAT sur les clauses générées et obtenir les résultats dans resSAT13.txt.​

Visualisation des résultats :

Lancez affichage_piece.py pour afficher graphiquement les solutions de pavage obtenues.​

Alternativement, vous pouvez exécuter le script principal main.py qui orchestre ces étapes de manière séquentielle.​

Exemple d'exécution
Voici un exemple de la manière d'exécuter le projet en ligne de commande :​

bash
Copy
Edit
python main.py
Assurez-vous que les fichiers de configuration (tab.txt, piece.txt, etc.) sont correctement définis avant d'exécuter le script.

## Auteur(s)

- [Etienne MALABRE](https://github.com/lasnelus/)

## License
- la license n'est pas encore déterminé

# temps passé sur le projet depuis le 24 février 2025
[![wakatime](https://wakatime.com/badge/user/5faeb795-a990-47af-8333-7f49032c5997.svg)](https://wakatime.com/@5faeb795-a990-47af-8333-7f49032c5997)
