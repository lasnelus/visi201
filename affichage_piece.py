#affichage piece
#lasnelus


baseAffichage = [    [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".",".","."]]
def affichageNouvellePiece (pieces:list)->None:
    """
    permet l'affichage d'un nouvelle piece dans un fichier txt
    """

    for i in range(len(pieces)):
        lettres ="abcdefghijklmnopqrstuvwxyz"
        for j in range(len(pieces[i])):
            baseAffichage[pieces[i][j][0]][pieces[i][j][1]] = lettres[i]


    visualisation = open("piece.txt", "w")
    for ligne in baseAffichage:
        visualisation.write(" ".join(ligne) + "\n")
    visualisation.close()

"""
affichageNouvellePiece(
                       [
                        [
                         [0,0],[1,0],[2,0],[2,1]],
                        [
                         [0,2],[1,2],[2,2],[2,3]],
                        ]
                        )
"""