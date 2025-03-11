import os
from createur_de_clause_v3 import generate_clauses
from conv_res import execSAT13
from affichage_piece import display_pieces

def main():
    # Étape 1 : Génération des clauses pour le solveur SAT
    clauses_file = 'clauses.sat'
    generate_clauses(lecteur_tab("tab.txt"))
    print(f"Clauses générées et sauvegardées dans {clauses_file}")
    # Étape 2 : Exécution du solveur SAT sur les clauses générées
    ecriture_fichier("resSAT13.txt")
    print(f"Résultats du solveur SAT sauvegardés dans resSAT13")

    # Étape 3 : Affichage des pièces à partir des résultats
    affichageNouvellePiece(recupere_list_coordonne("resSAT13.txt"))
    print(f"Affichage des pièces basé sur {results_file}")

if __name__ == "__main__":
    main()
