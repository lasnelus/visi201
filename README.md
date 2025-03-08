# Projet VISI201 : Pavage de Polyominos et Nombre de Heggs

Ce projet, réalisé dans le cadre du cours VISI201, explore le pavage de polyominos et le calcul du nombre de Heggs. Il génère des clauses logiques pour un solveur SAT afin de trouver des solutions à des problèmes de pavage en utilisant des polyominos. Le projet est principalement développé en Python.

## Contenu du projet

- `affichage_piece.py` : Contient une fonction permettant d'afficher des polyominos sous forme de lettres dans un tableau de taille fixe.
- `conv_res.py` : Comprend la fonction `execSAT13` (description à compléter).
- `createur_de_clause_v3.py` : Génère des clauses pour le solveur SAT en fonction des polyominos et du pavage souhaité.
- `creation_polyominos.py` : Contient des fonctions pour créer et manipuler des polyominos, notamment la génération de toutes les versions (rotations et symétries) d'une pièce.
- `formule_exemple_hyvernat.sat` : Fichier d'exemple contenant des formules SAT spécifiques (à détailler davantage).
- `clausepavage.txt` : Fichier contenant les clauses générées pour le pavage (à détailler davantage).
- `piece.txt` : Fichier décrivant les polyominos utilisés (à détailler davantage).
- `resSAT13.txt` : Résultats obtenus après résolution des clauses SAT. Par exemple, une ligne comme `P0_0_0 C_1_2 C_0_2 C_0_1 C_0_0` indique une solution spécifique.
- `tab.txt` : Fichier contenant des informations tabulaires spécifiques (à détailler davantage).
- `temp.txt` : Contient une fonction `version_piece` qui génère toutes les versions (rotations et symétries) d'une pièce donnée.

*Remarque : Certaines descriptions de fichiers nécessitent des compléments d'information.*

## Prérequis

- Python 3.x

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/lasnelus/visi201.git
