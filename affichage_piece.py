#affichage piece
#lasnelus

def affichageNouvellePiece (piece:list)->None:
    """
    permet l'affichage d'un nouvelle piece dans un fichier txt
    """
    baseAffichage = [[".",".","."],
                     [".",".","."],
                     [".",".","."]]
    for i in range(len(piece)):
        baseAffichage[piece[i][0]][piece[i][1]] = "a"


    visualisation = open("piece.txt", "w")
    for ligne in baseAffichage:
        visualisation.write(" ".join(ligne) + "\n")
    visualisation.close()

affichageNouvellePiece([[0,0],[1,0],[2,0],[2,1]])