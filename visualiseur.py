def lire_resultat_sat(fichier):
    """
    Lit le fichier contenant le résultat du SAT solver et extrait les placements valides.
    """
    with open(fichier, "r") as f:
        clauses = f.read().split()

    # Extraction des pièces placées (on ignore les négations "~P")
    pieces_placees = [clause for clause in clauses if clause.startswith("P") and not clause.startswith("~")]
    
    return pieces_placees

def generer_grille(pieces, taille=10):
    """
    Génère une grille vide et place les pièces détectées.
    """
    grille = [["." for _ in range(taille)] for _ in range(taille)]
    symboles = {}  # Associe chaque pièce à un caractère unique
    lettre_actuelle = iter("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for piece in pieces:
        version, x, y = piece.split("_")
        x, y = int(x), int(y)

        # Associer un symbole unique à chaque version
        if version not in symboles:
            symboles[version] = next(lettre_actuelle)

        # Placer la pièce sur la grille
        grille[y][x] = symboles[version]

    return grille

def ecrire_grille(grille, fichier_sortie="piece.txt"):
    """
    Écrit la grille dans un fichier.
    """
    with open(fichier_sortie, "w") as f:
        for ligne in grille:
            f.write(" ".join(ligne) + "\n")

def main():
    fichier_sat = "resSAT13.txt"  # Fichier contenant le résultat SAT
    pieces_placees = lire_resultat_sat(fichier_sat)
    
    grille = generer_grille(pieces_placees, taille=10)
    ecrire_grille(grille)

main()
