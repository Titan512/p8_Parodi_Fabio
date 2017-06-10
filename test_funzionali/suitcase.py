import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1, scriptDir+"\\src")
else:
    path.insert(1, scriptDir+"/src")
from Class.InputTree import InputTree
from Class.Token import Token
from Class.Translation import Translation
from Class.AbsolutePath import getAbsolutePath

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

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
#Analizzo ed inserisco a video i risultati
print("\n\n\n\n")
maxRange = 12
match = 0
print("-----------")
for reqAnalized in range(1, maxRange+1):
    translator = Translation(0)
    isTest = True
    translation = translator.translateRequirement(reqAnalized, isTest)
    print(translation)
    print(responseList[reqAnalized-1])
    if translation == responseList[reqAnalized-1]:
        match += 1
        print("True")
    else:
        print("False")
    print("-----------")
result = match/maxRange
print("Individuati", match, " requisiti su", maxRange, ".\nPercentuale: ", round(result,2), "%")
