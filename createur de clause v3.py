from creation_polyominos import *

piece = [[0,0],[1,0],[2,0],[2,1]]

def lecteur_tab (file: str)-> list:
    """
    créé une liste correspondant à toute les cases utilisable
    """
    fichier = open(file, "r")
    res=[]
    ligne = fichier.readline()
    i = 0
    while ligne != "":
        for j in range(len(ligne)):
            if ligne[j] == "#":
                res.append([j, i])
        ligne = fichier.readline()
        i+=1
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


def placement_piece (origine: list, piece: list)->list:
    """
    donne une list correspondant à une piece placé celon une origine donnée
    """
    res=[]
    for case in piece:
        res.append([case[0]+origine[0], case[1]+origine[1]])
    return res


def verif_version (origine: list, piece: list, tab: list)-> list:
    """
    vérifie si les version d'une pièce possible pour une origine donnée sont possible
    """
    res = []
    piece_placé = placement_piece(origine, piece)
    versionpiece = [
        piece_placé,
        rotationPiece(piece_placé),
        rotationPiece(rotationPiece(piece_placé)),
        rotationPiece(rotationPiece(rotationPiece(piece_placé))),
        symetriePiece(piece_placé),
        rotationPiece(symetriePiece(piece_placé)),
        rotationPiece(rotationPiece(symetriePiece(piece_placé))),
        rotationPiece(rotationPiece(rotationPiece(symetriePiece(piece_placé))))
    ]
    
    for version in versionpiece:
        valide = True
        for dx, dy in version:
            if not([dx, dy] in tab):
                valide = False
                break
        
        if valide:
            res += [version]
    return res

def creation_clause_origine(origine:list, piece:list, tab: list) -> str:
    """
    créer les clauses pour toutes les pièces possible sur une case
    """
    res =""
    versionpiece = verif_version(origine, piece, tab)
    for i in range(len(versionpiece)):
        for case in versionpiece[i]:
            part1 = "~P"+str(i)+"_"+str(origine[0])+"_"+str(origine[1])+" "
            part2 = "C_"+str(case[0])+"_"+str(case[1])+"\n"
            res += part1+part2
    return res


def creation_clause_tab (piece:list, tab:list)->str:
    """
    créer les clauses pour la totalité du tableau
    """
    res=""
    for case in tab:
        res += creation_clause_origine([case[0], case[1]], piece, tab)
    return res

def creation_clause_complet (tab:list)->str:
    """
    créé toutes les clauses pour que chaque case soit utilisé
    """
    res=""
    for case in tab:
        res += "C_"+str(case[0])+"_"+str(case[1])+"\n"
    return res

def ecriture_clause (clause: str)-> None:
    """
    écrit dans un fichier les clauses
    """
    fichier = open("clausepavage.txt", "w")
    fichier.write(clause)
    fichier.close()


ecriture_clause(str(creation_clause_tab(piece, lecteur_tab("tab.txt")))+str(creation_clause_complet(lecteur_tab("tab.txt"))))