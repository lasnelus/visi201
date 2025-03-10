import os
from createur_de_clause_v3 import generate_clauses
from conv_res import execSAT13
from affichage_piece import display_pieces

def main():
    # Étape 1 : Génération des clauses pour le solveur SAT
    clauses_file = 'clauses.sat'
    generate_clauses(clauses_file)
    print(f"Clauses générées et sauvegardées dans {clauses_file}")

    # Étape 2 : Exécution du solveur SAT sur les clauses générées
    results_file = 'resSAT13.txt'
    ecriture_fichier()
    print(f"Résultats du solveur SAT sauvegardés dans {results_file}")

    # Étape 3 : Affichage des pièces à partir des résultats
    display_pieces(results_file)
    print(f"Affichage des pièces basé sur {results_file}")

if __name__ == "__main__":
    main()
