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
    
    
def miseEnForme (file:str) -> None:
    output = execSAT13(file)
    resultat=[0,0,0,0,0,0]
    res=""
    for i in range(len(output)):
        if output[i] in ["1","2","3","4","5","6"] and output[i-1]==" " and output[i+2] != " ":
            resultat[int(output[i])-1] = output[i+2]
    print(resultat)
    for i in range(len(resultat)):
        res += str(resultat[i])
    return res


ecriture_fichier("clausepavage.txt")