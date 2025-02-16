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
            if ligne[i] == "#":
                res.append([j, i])
        ligne = fichier.readline()
        i+=1
    print(res)
    return res

def nouveaux_verif ()
    

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
   