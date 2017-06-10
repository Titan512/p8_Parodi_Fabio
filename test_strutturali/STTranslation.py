import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.Translation import Translation
from Class.AbsolutePath import getAbsolutePath

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testTestTranslation():
    #Lista delle risposte aspettate
    responseList = []
    for idReq in range(1, 13):
        path = getAbsolutePath("/resources/patternTree/SNL"+str(idReq)+".txt")
        fileMod = open(path, "r")
        string = fileMod.readline()
        fileMod.close()
        responseList.append(string)
    #pulisco il terminale
    os.system("cls" if os.name == "nt" else "clear")
    #testo i vari requisiti
    maxRange = 12
    match = 0
    for reqAnalized in range(1, maxRange+1):
        translator = Translation(0)
        isTest = False
        translation = translator.translateRequirement(reqAnalized, isTest)
        assert translation == responseList[reqAnalized-1], "\nERRORE\n"+translation+"\n must be equal to \n"+responseList[reqAnalized-1]

def test8():
    testTestTranslation()
