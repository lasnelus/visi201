from creation_polyominos import *

piece = [[0,0],[0,1],[0,2],[1,2]]

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
            ligne.strip()
            if ligne[j] == "#":
                res.append([j, i])
        ligne = fichier.readline()
        i+=1
    
    return res

def trouve_origine (piece:list) -> list:
    """
    trouve le point en haut à gauche d'une pièce (sont origine)
    """
    x_origine = min(x for x, _ in piece)
    y_origine = min(y for _, y in piece)
    return [x_origine, y_origine]


def placement_piece (origine: list, piece: list)->list:
    """
    donne une list correspondant à une piece placé celon une origine donnée
    """
    res=[]
    for case in piece:
        res.append([case[0]+origine[0], case[1]+origine[1]])

    return res

assert(placement_piece([0,0], [[0,0],[1,0],[2,0],[2,1]])==[[0,0],[1,0],[2,0],[2,1]])
assert(placement_piece([1,0], [[0,0],[1,0],[2,0],[2,1]])==[[1,0],[2,0],[3,0],[3,1]])
assert(placement_piece([0,1], [[0,0],[0,1],[0,2],[1,2]])==[[0,1],[0,2],[0,3],[1,3]])


def version_piece (piece: list)-> list:
    """
    créer une liste de liste, où toute les versions la piece sont stocké
    """
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

    return versionpiece

def verif_version(origine: list, pieces: list, tab: list) -> list:
    """
    Vérifie les versions valides pour chaque origine et conserve leurs indices d'origine.
    """
    res = []
    
    for i, version in enumerate(pieces):  # On conserve l'index d'origine
        version_placee = placement_piece(origine, version)
        if all([dx, dy] in tab for dx, dy in version_placee):  # Vérifie si toutes les cases sont valides
            res.append((i, version_placee))  # On stocke l'index original et la version placée
    
    return res



def creation_clause_origine(origine: list, piece: list, tab: list) -> str:
    """
    Crée les clauses pour toutes les pièces possibles sur une case.
    """
    res = ""
    versions_valides = verif_version(origine, version_piece(piece), tab)

    print(f"Origine testée : {origine}")
    for index_original, version in versions_valides:  # On récupère l'index original
        for case in version:
            part1 = f"~P{index_original}_{origine[0]}_{origine[1]} "
            part2 = f"C_{case[0]}_{case[1]}\n"
            res += part1 + part2

    return res



def creation_clause_tab (piece:list, tab:list)->str:
    """
    créer les clauses pour la totalité du tableau
    """
    res=""
    for case in tab:
        res += creation_clause_origine([case[0], case[1]], piece, tab)
    return res

def piece_couvrante(case: list, piece: list, tab: list) -> list:
    """
    Retourne la liste de toutes les pièces pouvant recouvrir une case donnée.
    """
    case_occupees = []  # Liste des pièces pouvant couvrir la case
    
    for origine in tab:
        versions_valides = verif_version(origine, version_piece(piece), tab)
        for i, version in enumerate(versions_valides):
            if case in version:
                case_occupees.append(f"P{i}_{origine[0]}_{origine[1]}")
    
    return case_occupees


def creation_contrainte_unicite(tab: list, piece: list) -> str:
    """
    Crée les clauses interdisant qu'une case soit occupée par plus d'une pièce.
    """
    res = ""
    
    for case in tab:
        pieces = piece_couvrante(case, piece, tab)
        for i in range(len(pieces)):
            for j in range(i + 1, len(pieces)):
                res += f"~{pieces[i]} ~{pieces[j]}\n"  # Pas deux pièces sur la même case
    
    return res

def creation_contrainte_couverture(tab: list, piece: list) -> str:
    """
    Génère les clauses imposant que chaque case soit occupée par au moins une pièce.
    """
    res = ""
    
    for case in tab:
        pieces = piece_couvrante(case, piece, tab)
        if pieces:
            res += " ".join(pieces) + "\n"  # CNF : Au moins une de ces pièces est présente
    
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

tab = lecteur_tab("tab.txt")

ecriture_clause(
    creation_clause_tab(piece, tab) +
    creation_clause_complet(tab) +
    creation_contrainte_unicite(tab, piece) +
    creation_contrainte_couverture(tab, piece)
)