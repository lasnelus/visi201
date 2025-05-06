from creation_polyominos import *

def lecteur_tab(file: str) -> tuple[list, list]:
    """
    Crée deux listes :
    - la grille complète (toutes les coordonnées)
    - les cases utilisables (avec un '#')
    """
    cases_utilisables = []
    grille_complete = []

    with open(file, "r") as fichier:
        for i, ligne in enumerate(fichier):
            for j, char in enumerate(ligne.strip()):
                grille_complete.append([j, i])
                if char == "#":
                    cases_utilisables.append([j, i])

    return grille_complete, cases_utilisables

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
    """
    Retourne la liste des tuples (index, version_placée, est_valide)
    """
    res = []
    tab_set = {tuple(case) for case in tab}
    seen = set()

    for i, version in enumerate(pieces):
        version_placee = placement_piece(origine, version)
        version_tuple = tuple(sorted(tuple(coord) for coord in version_placee))

        if version_tuple in seen:
            continue  # pour éviter les duplicatas
        seen.add(version_tuple)

        est_valide = all(tuple(coord) in tab_set for coord in version_placee)
        res.append((i, version_placee, est_valide))

    return res


def creation_clause_origine(origine: list, piece: list, tab: list) -> str:
    """
    Crée les clauses pour toutes les pièces valides sur une case.
    (Mais teste toutes les versions)
    """
    res = ""
    for index_original, version, est_valide in verif_version(origine, version_piece(piece), tab):
        if est_valide:
            res += "".join(f"~P{index_original}_{origine[0]}_{origine[1]} C_{case[0]}_{case[1]}\n" for case in version)
        else:
            print(f"Version {index_original} à {origine} invalide : {version}")
    return res

def creation_clause_tab(piece: list, grille: list, tab: list) -> str:
    """
    créer les clauses pour la totalité du tableau
    """
    return "".join(creation_clause_origine([case[0], case[1]], piece, tab) for case in tab)


def piece_couvrante(case: list, piece: list, tab: list, grille: list) -> list:
    """
    Retourne la liste des identifiants des pièces pouvant recouvrir une case donnée.
    Explore toutes les origines possibles (grille complète).
    """
    version_piecee = version_piece(piece)
    return [
        f"P{index_original}_{origine[0]}_{origine[1]}"
        for origine in grille
        for index_original, version, est_valide in verif_version(origine, version_piecee, tab)
        if est_valide and case in version
    ]


def creation_contrainte_unicite(tab: list, piece: list, grille: list) -> str:
    return "".join(
        f"~{pieces[i]} ~{pieces[j]}\n"
        for case in tab
        if (pieces := piece_couvrante(case, piece, tab, grille)) and len(pieces) > 1
        for i in range(len(pieces))
        for j in range(i + 1, len(pieces))
    )

def creation_contrainte_couverture(tab: list, piece: list, grille: list) -> str:
    clauses = []
    for case in tab:
        pieces = piece_couvrante(case, piece, tab, grille)
        if pieces:
            clauses.append(" ".join(pieces))
    return "\n".join(clauses) + "\n" if clauses else ""

def creation_clause_complet (tab:list)->str:
    """
    créé toutes les clauses pour que chaque case soit utilisé
    """
    return "\n".join(f"C_{x}_{y}" for x, y in tab) + "\n" if tab else ""

def ecriture_clause (clause: str)-> None:
    """
    écrit dans un fichier les clauses
    """
    with open("clausepavage.txt", "w") as fichier:
        fichier.write(clause)


grille, tab = lecteur_tab("tab.txt")
print(tab)

def generates_clauses(piece, grille, tab):
    """
    Génère toutes les clauses pour un pavage avec une pièce donnée.
    """
    ecriture_clause(
        creation_clause_tab(piece, grille, tab) +
        creation_clause_complet(tab) +
        creation_contrainte_unicite(tab, piece, grille) +
        creation_contrainte_couverture(tab, piece, grille)
    )
"""
# Mock data for testing
mock_piece = [[0, 0], [1, 0], [2, 0], [2, 1]]
mock_tab = [[0, 0], [1, 0], [2, 0], [2, 1], [0, 1], [1, 1], [2, 1], [3, 1]]
mock_origine = [0, 0]

# Test lecteur_tab
with open("test_tab.txt", "w") as f:
    f.write("#.#\n.#.\n###")
assert lecteur_tab("test_tab.txt") == [[0, 0], [2, 0], [1, 1], [0, 2], [1, 2], [2, 2]]

# Test trouve_origine
assert trouve_origine(mock_piece) == [0, 0]
assert trouve_origine([[1, 1], [2, 1], [3, 1], [3, 2]]) == [1, 1]

# Test placement_piece
assert placement_piece([0, 0], mock_piece) == [[0, 0], [1, 0], [2, 0], [2, 1]]
assert placement_piece([1, 1], mock_piece) == [[1, 1], [2, 1], [3, 1], [3, 2]]

# Test version_piece
mock_rotated_piece = [[0, 0], [0, 1], [0, 2], [1, 2]]
mock_symmetric_piece = [[0, 0], [1, 0], [2, 0], [2, 1]]
versionpiece = version_piece(mock_piece)
assert mock_piece in versionpiece, ""
assert mock_rotated_piece in versionpiece, ""
assert mock_symmetric_piece in versionpiece, ""

# Test verif_version
valid_versions = verif_version(mock_origine, version_piece(mock_piece), mock_tab)
assert len(valid_versions) > 0
assert all(all(tuple(case) in {tuple(c) for c in mock_tab} for case in version) for _, version in valid_versions)

# Test creation_clause_origine
clause_origine = creation_clause_origine(mock_origine, mock_piece, mock_tab)
assert isinstance(clause_origine, str)
assert len(clause_origine) > 0

# Test creation_clause_tab
clause_tab = creation_clause_tab(mock_piece, mock_tab)
assert isinstance(clause_tab, str)
assert len(clause_tab) > 0

# Test piece_couvrante
covering_pieces = piece_couvrante([0, 0], mock_piece, mock_tab)
assert isinstance(covering_pieces, list)
assert all(isinstance(p, str) for p in covering_pieces)

# Test creation_contrainte_unicite
unicite_clause = creation_contrainte_unicite(mock_tab, mock_piece)
assert isinstance(unicite_clause, str)
assert len(unicite_clause) > 0

# Test creation_contrainte_couverture
couverture_clause = creation_contrainte_couverture(mock_tab, mock_piece)
assert isinstance(couverture_clause, str)
assert len(couverture_clause) > 0

# Test creation_clause_complet
complet_clause = creation_clause_complet(mock_tab)
assert isinstance(complet_clause, str)
assert len(complet_clause) > 0
"""