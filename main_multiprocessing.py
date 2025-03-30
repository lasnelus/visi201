import os
from multiprocessing import Pool, cpu_count
from createur_de_clause_v3 import generates_clauses, piece, tab
from conv_res import ecriture_fichier
from visualisation import affichageNouvellePiece, recupere_list_coordonne

def generate_clauses_parallel():
    """Étape 1: Génération des clauses (peut être parallélisée si generates_clauses le permet)"""
    generates_clauses(piece, tab)
    return "Clauses générées"

def run_sat_solver():
    """Étape 2: Exécution du solveur SAT"""
    ecriture_fichier("clausepavage.txt")
    return "Solveur SAT exécuté"

def visualize_results():
    """Étape 3: Visualisation des résultats"""
    affichageNouvellePiece(recupere_list_coordonne("resSAT13.txt"), tab)
    return "Visualisation terminée"

def full_exec_parallel():
    """Exécution parallèle des étapes indépendantes"""
    with Pool(processes=min(3, cpu_count())) as pool:  # Max 3 processus
        results = pool.starmap(
            func=[generate_clauses_parallel, run_sat_solver, visualize_results],
            iterable=[]
        )
        
        for result in results:
            print(result)

if __name__ == "__main__":
    # Version séquentielle (pour debug)
    # full_exec() 
    
    # Version parallèle
    full_exec_parallel()