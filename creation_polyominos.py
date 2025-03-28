#création polyominos
#lasnelus


def rotationPiece(piece: list) -> list:
    """
    Rotation de 90° vers la droite d'un polyomino
    """
    nouvelle_piece = [[-y, x] for x, y in piece]

    # Trouver les plus petites coordonnées pour recentrer la pièce à l'origine
    min_x = min(x for x, y in nouvelle_piece)
    min_y = min(y for x, y in nouvelle_piece)

    # Recentrer la pièce pour éviter des coordonnées négatives
    return [[x - min_x, y - min_y] for x, y in nouvelle_piece]


def symetriePiece(piece: list) -> list:
    """
    Applique une symétrie verticale à la pièce
    """
    nouvellePiece = [[-x, y] for x, y in piece]

    min_x = min(x for x, y in nouvellePiece)
    min_y = min(y for x, y in nouvellePiece)

    return [[x - min_x, y - min_y] for x, y in nouvellePiece]

