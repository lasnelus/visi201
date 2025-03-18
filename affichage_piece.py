#affichage piece
#lasnelus

from createur_de_clause_v3 import piece, version_piece, placement_piece


def recup_pieces (nomfichier:str)->list:
    """
    permet la récupération de toutes les pieces placé par SAT13
    """
    tab=[]
    fichier = open(nomfichier, "r")
    ligne = fichier.readline().strip()
    elements = ligne.split()
    for elem in elements:
        if elem.startswith("P") and not elem.startswith("~P"):  
            tab.append(elem)  # Récupérer seulement les pièces positives
            
    fichier.close()
    return tab

import re

def recuperation_origine(piece: str) -> list:
    """
    Extrait les coordonnées X et Y d'une pièce sous la forme 'PV_X_Y'.
    Gère les nombres de plusieurs chiffres et les valeurs négatives.
    """
    match = re.match(r'P\d+_(-?\d+)_(-?\d+)', piece)  # Capture X et Y

    if match:
        x, y = int(match.group(1)), int(match.group(2))
        return [x, y]

def recuperation_version (piece:str)->int:
    """
    permet de recupérer la version d'un piece placé
    """
    return int(piece[1])

def recupere_list_coordonne (nomfichier):
    """
    permet de récupérer une liste de coordonnee, correspondant au piece placé par SAT13:
    """
    tab=[]
    versions_piece = version_piece(piece)
    piecestr= recup_pieces(nomfichier)
    for i in range(len(piecestr)):
        version = recuperation_version(piecestr[i])
        origine = recuperation_origine(piecestr[i])
        tab.append(placement_piece(origine, versions_piece[version]))
    return tab

def determiner_taille_grille(nomfichier: str) -> list:
    """
    Détermine la taille exacte de la grille en fonction des coordonnées maximales trouvées dans le fichier.
    """
    max_x = 0
    max_y = 0
    fichier = open(nomfichier, "r")
    elements = fichier.readline().strip().split()
        
    for elem in elements:
        if elem.startswith("C"):
            parts = elem.split("_")
            x, y = int(parts[1]), int(parts[2])
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    fichier.close()
    # Création d'une grille de la taille exacte détectée
    return [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]


def affichageNouvellePiece(pieces: list) -> None:
    """
    Permet l'affichage d'une nouvelle pièce dans un fichier txt.
    """
    baseAffichage = determiner_taille_grille("resSAT13.txt")
    print(len(baseAffichage))
    print(len(baseAffichage[0]))
    
    lettres = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            x, y = pieces[i][j]
            print([x, y])
            if 0 <= y< len(baseAffichage) and 0 <= x < len(baseAffichage[0]):
                baseAffichage[y][x] = lettres[i]
            else:
                print(f"Coordonnées hors limites: ({y}, {x})")

    visualisation = open("piece.txt", "w")
    for ligne in baseAffichage:
        visualisation.write(" ".join(ligne) + "\n")
    visualisation.close()

affichageNouvellePiece(recupere_list_coordonne("resSAT13.txt"))



### TEST ###
assert(recup_pieces("piecetest.txt")==['P0_16_5', 'P6_6_4', 'P4_8_7', 'P1_9_6', 'P0_4_3', 'P4_6_5', 'P2_4_2', 'P1_6_1', 'P2_8_0', 'P2_7_2', 'P7_9_3', 'P3_10_4', 'P2_12_3', 'P1_11_2', 'P4_10_3']), "problème recup_piece"
assert(recuperation_origine("P0_16_5")==[16,5]),"pb recupération origine"
assert(recuperation_version("P0_16_5")==0),"pb recupération version"
assert(recupere_list_coordonne("piecetest.txt")==[[[16, 5], [16, 6], [16, 7], [17, 7]], [[6, 6], [6, 5], [6, 4], [7, 4]], [[9, 7], [9, 8], [9, 9], [8, 9]], [[11, 6], [10, 6], [9, 6], [9, 7]], [[4, 3], [4, 4], [4, 5], [5, 5]], [[7, 5], [7, 6], [7, 7], [6, 7]], [[5, 4], [5, 3], [5, 2], [4, 2]], [[8, 1], [7, 1], [6, 1], [6, 2]], [[9, 2], [9, 1], [9, 0], [8, 0]], [[8, 4], [8, 3], [8, 2], [7, 2]], [[9, 3], [10, 3], [11, 3], [11, 4]], [[10, 5], [11, 5], [12, 5], [12, 4]], [[13, 5], [13, 4], [13, 3], [12, 3]], [[13, 2], [12, 2], [11, 2], [11, 3]], [[11, 3], [11, 4], [11, 5], [10, 5]]]), "pb recupère liste coordonnée"