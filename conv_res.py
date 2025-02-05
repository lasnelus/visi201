import subprocess


def creationClauses()-> None:
    """
    création de clauses pour le solveur SAT13,
    """
    config = open("instructionSAT13.txt", "w")
    config.write()
    config.close()

def execSAT13 (file: str) -> str:
    """execute le """
    res = subprocess.run("./sat13.exe <" + file, shell=True, capture_output=True, text=True)
    return str(res.stdout)
    

def miseEnForme (file:str) -> None:
    output = execSAT13(file)
    resultat=[0,0,0,0,0,0]
    res=""
    for i in range(len(output)):
        if output[i] in ["1","2","3","4","5","6"] and output[i-1]==" " and output[i+2] != " ":
            resultat[int(output[i])-1] = output[i+2]

    for i in range(len(resultat)):
        res += resultat[i]
    sol = open("resSAT13.txt", "w")
    sol.write(str(res))
    sol.close()


miseEnForme("new_try.txt")