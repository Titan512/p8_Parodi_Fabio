import os
def getAbsolutePath(path):
    """ function getAbsolutePath
    Dato che il cambiare computer ha
    dato problemi con la lettura degli
    indirizzi, questa funzione restituisce
    l'indirizzo assoluto del file
    che si sta analizzando
    [gestisce anche il cambio di notazione
    del percorso tra windows\linux]
    return string
    """
    scriptPath = os.path.abspath(__file__)
    scriptDir = os.path.split(scriptPath)[0]
    scriptDir = os.path.split(scriptDir)[0]
    scriptDir = os.path.split(scriptDir)[0]
    if os.name == "nt":
        path = path.replace("/", "\\")
    else:
        path = path.replace("\\", "/")
    absFilePath = scriptDir + path
    return absFilePath
