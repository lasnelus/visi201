# @lasnelus
# MISPI 11/CMI
from PIL import Image
import string
from createur_de_clause_v3 import piece, version_piece, placement_piece, tab

colors = {
    0: (255, 255, 255),  # Blanc
    1: (255, 0, 0),      # Rouge
    2: (0, 0, 255),      # Bleu
    3: (0, 255, 0),      # Vert
    4: (255, 255, 0),    # Jaune
    5: (165,42,42),      # marron
    6: (238,130,238),    # violet
    7: (255, 128, 0),    # orange
    8: (255,192,203),    # rose
    9: (143,40,60)       # bordeau
}


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


def affichageNouvellePiece(pieces: list, tab) -> None:
    """
    Permet l'affichage d'une nouvelle pièce dans un fichier txt.
    """
    if pieces!= []:
        coords = recupere_list_coordonne("resSAT13.txt")
        width, height = max(x for piece in coords for x,y in piece)+1, max(y for piece in coords for x,y in piece)+1
        size = 50 #taille des cases
        
        tableau = [[0 for _ in range(width)] for _ in range(height)]
        
        for i in range(len(pieces)):
            for j in range(len(pieces[i])):
                x, y = pieces[i][j]
                if 0 <= y< height and 0 <= x < width:
                    tableau[y][x] = colors[(i % (len(colors)-1))+1]
                else:
                    print(f"Coordonnées hors limites: ({y}, {x})")

        img = Image.new("RGB", (width*50, height*50), (255,255,255))

        
        for y in range(height):
            for x in range(width):
                color = tableau[y][x]
                if color != (255, 255, 255):
                    for dy in range(size):
                        for dx in range(size):
                            img.putpixel(((x *size)+dx, y*size +dy), color)

                
        print([width, height])
        img.show()
        img.save("grille.png")
    else:
        print("on a un pb captain")