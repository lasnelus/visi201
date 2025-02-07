#créateur de clause
#lasnelus

from affichage_piece import *

"""
TODO
création d'un programme, qui permet de générer les conditions, pour que le SAT comprennent les pièces.
créé les clauses, pour que plusieur pièce ne puisse pas se superposé, et créé les clauses pour que toute les case soient occupé
"""
def clausesL (tab)-> str:
    """
    création 
    """
    res =""
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            #1
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"
    for i in range(len(tab)):
        for j in range(2, len(tab[i]), 3):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j-2)+"_1\n"
    
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_3 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_3 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_3 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"

            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"

            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"

            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_6 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_6 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_6 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"

            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"

            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"
    res += "\n"
    print(res)
    return res
    
"""
clausesL([[".",".",".","."],
          [".",".",".","."],
          [".",".",".","."],
          [".",".",".","."]])
"""
"""clause = open("clausepavage.txt", "w")
    visualisation.write(" ".join(ligne) + "\n")
    visualisation.close()
"""