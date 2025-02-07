#création polyominos
#lasnelus

from affichage_piece import *
L = [[0,0],[1,0],[2,0],[2,1]] #piece de tetris formant un L orienté vers la droite de 3 de haut, pour 2 de large

def rotationPiece(piece: list)-> list:
    """
    permet de faire la rotation de 90° vers la droite d'un polyomino
    """
    nouvellePiece = []
    for i in range(len(piece)):
        nouvellePiece += [[-(piece[i][1]), piece[i][0]]]

    min_x = min(coord[0] for coord in nouvellePiece)
    min_y = min(coord[1] for coord in nouvellePiece)

    nouvellePiece = [[x - min_x, y - min_y] for x, y in nouvellePiece]
    return nouvellePiece

def symetriePiece(piece:list)->list:
    """
    permet de faire la symetrie d'un polyomino
    """
    max_y = max(y for _, y in piece)  # Trouve la plus grande valeur de Y

    return [[x, max_y - y] for x, y in piece]

affichageNouvellePiece([rotationPiece(rotationPiece(rotationPiece(L)))])
