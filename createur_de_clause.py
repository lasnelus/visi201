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
    #1
    for i in range(len(tab)-2):
        for j in range(len(tab[i])-1):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_1 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_1\n"

            #done
    #2
    for i in range(len(tab)-1):
        for j in range(2, len(tab[i]), 3):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2 X_"+str((i+1))+"_"+str(j-1)+"_"+str(i)+"_"+str(j-2)+"_2\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j-2)+"_2 X_"+str((i+1))+"_"+str((j-2))+"_"+str(i)+"_"+str(j-2)+"_2\n"

            #done
    #3
    for i in range(len(tab)-2):
        for j in range(len(tab[i])-1):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_3 X_"+(str(i))+"_"+str(j+1)+"_"+str(i)+"_"+str(j)+"_3\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_3 X_"+str((i+1))+"_"+str(j+1)+"_"+str(i)+"_"+str(j)+"_3\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_3 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_3\n"

            #done
    #4
    for i in range(len(tab)-1):
        for j in range(len(tab[i])-2):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4 X_"+(str(i))+"_"+str(j+1)+"_"+str(i)+"_"+str(j)+"_4\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4 X_"+str(i)+"_"+str(j+2)+"_"+str(i)+"_"+str(j)+"_4\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4 X_"+str((i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_4\n"

            #done
    #5
    for i in range(len(tab)):
        for j in range(1, len(tab[i]), 2):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5 X_"+str((i+2))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_5 X_"+str((i+2))+"_"+str((j+1))+"_"+str(i)+"_"+str(j)+"_5\n"

            #done
    #6
    for i in range(len(tab)):
        for j in range(len(tab[i])-2):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_6 X_"+(str(i))+"_"+str(j+1)+"_"+str(i)+"_"+str(j)+"_6\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_6 X_"+str((i))+"_"+str(j+2)+"_"+str(i)+"_"+str(j)+"_6\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_6 X_"+str((i+1))+"_"+str((j+2))+"_"+str(i)+"_"+str(j)+"_6\n"
            
            #done
    #7
    for i in range(len(tab)):
        for i in range(len(tab[i])-1):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7 X_"+(str(i))+"_"+str(j+1)+"_"+str(i)+"_"+str(j)+"_7\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7 X_"+str((i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_7 X_"+str((i+2))+"_"+str((j))+"_"+str(i)+"_"+str(j)+"_7\n"

            #done
    #8
    for i in range(len(tab)):
        for i in range(len(tab[i])-2):
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8 X_"+(str(i+1))+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8 X_"+str((i+1))+"_"+str(j+1)+"_"+str(i)+"_"+str(j)+"_8\n"
            res+= "~X_"+str(i)+"_"+str(j)+"_"+str(i)+"_"+str(j)+"_8 X_"+str((i+1))+"_"+str((j+2))+"_"+str(i)+"_"+str(j)+"_8\n"
    res += "\n"
    return res
    



clause = open("clausepavage.txt", "w")
clause.write(clausesL([[".",".",".","."],
          [".",".",".","."],
          [".",".",".","."],
          [".",".",".","."]]))
clause.close()
