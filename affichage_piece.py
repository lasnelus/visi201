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

def recuperation_origine (piece:str)->list:
    """
    permet de connaitre l'origine d'une piece placé
    """
    return [int(piece[3]), int(piece [5])]

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
    baseAffichage = determiner_taille_grille("resSAT13.txt") # Copie de la grille

    lettres = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            x, y = pieces[i][j]
            baseAffichage[y][x] = lettres[i]  # Correction indices

    visualisation = open("piece.txt", "w")
    for ligne in baseAffichage:
        visualisation.write(" ".join(ligne) + "\n")
    visualisation.close()

affichageNouvellePiece(recupere_list_coordonne("resSAT13.txt"))