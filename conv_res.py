import subprocess

def execSAT13 (file: str) -> str:
    """execute le sat13"""
    res = subprocess.run("./sat13.exe <" + file, shell=True, capture_output=True, text=True)
    print(res)
    return str(res.stdout)
    
def ecriture_fichier (file:str):
    """
    écrit les résultat du SAT solver dans un fichier a part
    """
    fichier = open("resSAT13.txt", "w")
    fichier.write(execSAT13(file))
    fichier.close()
    


ecriture_fichier("clausepavage.txt")