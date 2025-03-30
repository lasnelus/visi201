from creation_polyominos import *

piece = [[0,0],[0,1],[0,2],[1,2]]

def lecteur_tab(file: str) -> list:
    """
    Crée une liste correspondant à toutes les cases utilisables.
    """
    res = []
    
    with open(file, "r") as fichier:  # Utilisation du gestionnaire de contexte
        for i, ligne in enumerate(fichier):
            for j, char in enumerate(ligne.strip()):
                if char == "#":
                    res.append([j, i])
    
    return res

def trouve_origine(piece: list) -> tuple:
    """
    Trouve le point en haut à gauche d'une pièce (son origine).
    """
    x_origine, y_origine = map(min, zip(*piece))
    return [x_origine, y_origine]


def placement_piece (origine: list, piece: list)->list:
    """
    donne une list correspondant à une piece placé celon une origine donnée
    """
    x0, y0 = origine
    return [[x + x0, y + y0] for x, y in piece]


assert(placement_piece([0,0], [[0,0],[1,0],[2,0],[2,1]])==[[0,0],[1,0],[2,0],[2,1]])
assert(placement_piece([1,0], [[0,0],[1,0],[2,0],[2,1]])==[[1,0],[2,0],[3,0],[3,1]])
assert(placement_piece([0,1], [[0,0],[0,1],[0,2],[1,2]])==[[0,1],[0,2],[0,3],[1,3]])


def version_piece (piece: list)-> list:
    """
    créer une liste de liste, où toute les versions la piece sont stocké
    """
    versionpiece = [piece]
    for _ in range(3):  # Génère 3 rotations supplémentaires
        versionpiece.append(rotationPiece(versionpiece[-1]))
    
    sym = symetriePiece(piece)
    versionpiece.append(sym)
    for _ in range(3):  # Génère 3 rotations supplémentaires pour la symétrie
        versionpiece.append(rotationPiece(versionpiece[-1]))

    return versionpiece

    
def verif_version(origine: list, pieces: list, tab: list) -> list:
    res = []
    tab_set = {tuple(case) for case in tab}  # Convertir les éléments de tab en tuples

    for i, version in enumerate(pieces):
        version_placee = placement_piece(origine, version)
        if all(tuple(case) in tab_set for case in version_placee):
            res.append((i, version_placee))
        else:
            print(f"Échec pour version {i} à l'origine {origine}, certaines cases ne sont pas dans tab")

    return res


def creation_clause_origine(origine: list, piece: list, tab: list) -> str:
    """
    Crée les clauses pour toutes les pièces possibles sur une case.
    """
    res = ""
    versions_valides = verif_version(origine, version_piece(piece), tab)

    return "".join(
        f"~P{index_original}_{origine[0]}_{origine[1]} C_{case[0]}_{case[1]}\n"
        for index_original, version in versions_valides
        for case in version
    )


def creation_clause_tab (piece:list, tab:list)->str:
    """
    créer les clauses pour la totalité du tableau
    """
    return "".join(creation_clause_origine([case[0], case[1]], piece, tab) for case in tab)


def piece_couvrante(case: list, piece: list, tab: list) -> list:
    """
    Retourne la liste des identifiants des pièces pouvant recouvrir une case donnée.
    """
    return [
        f"P{index_original}_{origine[0]}_{origine[1]}"
        for origine in tab
        for index_original, version in verif_version(origine, version_piece(piece), tab)
        if case in version
    ]



def creation_contrainte_unicite(tab: list, piece: list) -> str:
    """
    Crée les clauses interdisant qu'une case soit occupée par plus d'une pièce.
    """
    res = ""
    
    return "".join(
        f"~{pieces[i]} ~{pieces[j]}\n"
        for case in tab
        if (pieces := piece_couvrante(case, piece, tab)) and len(pieces) > 1
        for i in range(len(pieces))
        for j in range(i + 1, len(pieces))
    )

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

def generates_clauses(piece, tab):
    """
    génère toutes les clauses
    """
    ecriture_clause(
    creation_clause_tab(piece, tab) +
    creation_clause_complet(tab) +
    creation_contrainte_unicite(tab, piece) +
    creation_contrainte_couverture(tab, piece)
    )