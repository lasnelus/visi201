Projet Visi201

Ce projet est le résultat du cours visi201, sur le sujet de pavage de polyomino, et de nombre de Heggs.
L'objectif du projet est de fournir des clauses logique à un SAT solver, afin que celui-ci puisse trouver des solutions à des problème de pavage à l'aide de polyomino, et d'étudier le nombre de Heggs.
C projet est principalement réalisé en python.

On peut retrouver dans ce projet:
- le module affichage_piece.py, comprenant pour le moment une seule fonction, permettant d'afficher des polyomino sous forme de lettre dans un tableau de taille fixe pour le moment.
- le module conv_res.py, comprennant la fonction execSAT13 permettant d'éxecuté le SAT solver dans, et la fonction ecriture_fichier, permettant d'écrire dans un fichier .txt le résultat donnée par un SAT solver.
- le module creation_polyominos.py, qui permet la crétation des différente variation de polyominos, comprennant donc les fonction rotation_piece, éxecutant un rotation de 90° vers la droite, et la fonction symetrie_piece, éxecutant un symétrie verticale de la piece
- le module createur_de_clause.py, module principale, qui est celui qui permet la création des clauses, il comprend donc les fonctions:
    * lecteur_tab, qui permet de 
