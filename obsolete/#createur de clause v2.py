#createur de clause v2
#lasnelus
from creation_polyominos import *


piece = [[0,0],[1,0],[2,0],[2,1]]

def creation_tab(longueur:int, hauteur:int)-> list:
    """
    créer un tableau de hauteur et longueur données
    """
    res = []
    for i in range(hauteur):
        contenue = []
        for j in range(longueur):
            contenue+= "."
        res+=[contenue]
    return res

def trouve_origine (piece:list) -> list:
    """
    trouve le point en haut à gauche d'une pièce (sont origine)
    """
    x_origine = piece[0][0]
    y_origine = piece[0][1]
    for case in piece:
        x_case_actuel = case[0]
        y_case_actuel = case[1]
        if x_case_actuel < x_origine:
            x_origine = x_case_actuel
        if y_case_actuel < y_origine:
            y_origine = y_case_actuel

    return [x_origine, y_origine]

def version_possible(case: list, piece: list, tab: list) -> list:
    """
    Renvoie une liste des versions de la pièce possibles à une case donnée,
    """
    res = []
    # Génération de toutes les versions possibles de la pièce
    versionpiece = [
        piece,
        rotationPiece(piece),
        rotationPiece(rotationPiece(piece)),
        rotationPiece(rotationPiece(rotationPiece(piece))),
        symetriePiece(piece),
        rotationPiece(symetriePiece(piece)),
        rotationPiece(rotationPiece(symetriePiece(piece))),
        rotationPiece(rotationPiece(rotationPiece(symetriePiece(piece))))
    ]
    
    hauteur = len(tab)
    if hauteur >0:
        largeur = len(tab[0])


    for version in versionpiece:
        valide = True
        for dx, dy in version:
            x = case[0] + dx
            y = case[1] + dy
            if not (0 <= x < largeur and 0 <= y < hauteur):
                valide = False
                break
        
        if valide:
            res += [version]
    return res

def creation_clause_case(case:list, piece:list, tab: list) -> str:
    """
    créer les clauses pour toutes les pièces possible sur une case
    """
    res =""
    versionpiece = version_possible(case, piece, tab)
    for version in range(len(versionpiece)):
        origine = trouve_origine(versionpiece[version])
        for case in versionpiece[version]:
            x_case_actuel= case[0]
            y_case_actuel= case[1]
            part1 = "~X_"+ str(x_case_actuel)+"_"+str(y_case_actuel)+"_"+str(origine[0])+"_"+str(origine[1])+"_"+str(version)+" "
            for i in range(len(versionpiece[version])):
                if versionpiece[version][i] == case:
                    continue
                x_case_2= versionpiece[version][i][0]
                y_case_2= versionpiece[version][i][1]
                part2 = "X_"+str(x_case_2)+"_"+str(y_case_2)+"_"+str(origine[0])+"_"+str(origine[1])+"_"+str(version)+"\n"
                res += part1+part2
    return res

def creation_clause_tab (piece:list, tab:list):
    """
    créer les clauses pour la totalité du tableau
    """
    res=""
    for hauteur in range(len(tab)):
        for longueur in range(len(tab[0])):
            res += creation_clause_case([longueur, hauteur], piece, tab)

    clause = open("clausepavage.txt", "w")
    clause.write(res)
    clause.close()

creation_clause_tab(piece, creation_tab(10, 10))