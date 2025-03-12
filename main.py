import os
from createur_de_clause_v3 import generates_clauses, piece, tab
from conv_res import ecriture_fichier
from affichage_piece import affichageNouvellePiece, recupere_list_coordonne

def full_exec ():
    generates_clauses(piece, tab)
    ecriture_fichier("clausepavage.txt")
    affichageNouvellePiece(recupere_list_coordonne("resSAT13.txt"))
    
    
full_exec()