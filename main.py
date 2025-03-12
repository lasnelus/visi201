import os
from createur_de_clause_v3 import generates_clauses, piece, tab
from conv_res import ecriture_fichier
from affichage_piece import affichageNouvellePiece, recupere_list_coordonne
"""
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
"""

def full_exec ():
    generates_clauses(piece, tab)
    ecriture_fichier("clausepavage.txt")
    affichageNouvellePiece(recupere_list_coordonne("resSAT13.txt"))
    
    
full_exec()