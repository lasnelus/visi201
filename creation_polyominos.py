#création polyominos
#lasnelus

L = [[0,1],[1,1],[2,1],[2,0]] #piece de tetris formant un L orienté vers la droite de 3 de haut, pour 2 de large

def rotationPiece(piece: list)-> list:
    """
    permet de faire la rotation de 90° vers la ... d'un polyomino
    """
    nouvellePiece = []
    for i in range(len(piece)):
        nouvellePiece += [[-(piece[i][1]), piece[i][0]]]

    config = open("piece.txt", "w")
    config.write(str(nouvellePiece))
    config.close()
    return nouvellePiece

rotationPiece(L)
def symetriePiece():
    """
    permet de faire la symetrie d'un polyomino
    """
    return