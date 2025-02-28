#création polyominos
#lasnelus

from affichage_piece import *
L = [[0,0],[1,0],[2,0],[2,1]] #piece de tetris formant un L orienté vers la droite de 3 de haut, pour 2 de large

def rotationPiece(piece: list) -> list:
    """
    Rotation de 90° vers la droite d'un polyomino
    """
    nouvellePiece = [[-y, x] for x, y in piece]  # Rotation mathématique correcte

    # Trouver les nouvelles coordonnées minimales pour recentrer
    min_x = min(x for x, y in nouvellePiece)
    min_y = min(y for x, y in nouvellePiece)

    # Décaler pour que les coordonnées restent positives
    return [[x - min_x, y - min_y] for x, y in nouvellePiece]

def symetriePiece(piece: list) -> list:
    """
    Applique une symétrie verticale à la pièce
    """
    return [[x, -y] for x, y in piece]

