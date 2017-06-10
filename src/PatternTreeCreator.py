#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pickle
from sys import path
if os.name == "nt":
    path.append("Class\\")
else:
    path.append("Class/")
from Class.InputTree import InputTree
from Class.PatternTree import PatternTree
from Class.Token import Token
from Class.AbsolutePath import getAbsolutePath

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

"""
algoritmo per creare i vari alberi di pattern
da usare come training set
"""

#pulisco il terminale
print("\n\n\n\n")
os.system("cls" if os.name == "nt" else "clear")
for idReq in range(1, 13):

    #leggo l'albero da file
    tree = InputTree(idReq)
    file = getAbsolutePath("/resources/inputTree/pattern"+str(idReq)+".txt")
    tree.loadTreeFromFile(file, None)
    patternRoot = tree.getRoot()
    #Analizzo questa stringa
    path = getAbsolutePath("/resources/patternTree/SNL"+str(idReq)+".txt")
    fileMod = open(path, "r")
    string = fileMod.readline()
    fileMod.close()
    #Rielaboro questa stringa
    string = string.replace(" ", " &sp ")
    string = string.replace("(", "( ")
    string = string.replace(")", " )")
    string = string.replace(",", " ,")
    string = string.replace("Globally ,", "Globally,")
    string = string.replace(".", " .")
    stringList = string.split(" ")
    #Passo alla decisione del valore
    inp = ""
    counter = 0
    tokenList = []
    #analizzo le varie parole e gli assegno il tag appropriato
    for element in stringList:
        counter += 1
        if element == "&sp":
            inp = "space"
        elif element == "Globally,":
            inp = "GLB"
        elif element == "(":
            inp = "op"
        elif element == ")":
            inp = "cl"
        elif element == "=" or element == ">" or element == "<":
            inp = "Operator"
        elif element == "," or element == ".":
            inp = "EP"
        elif element[0] == "{":
            inp = "SIG"
            element = "{SIGNAL}"
        elif element.isdigit():
            inp = "VT"
            element = "VALUE"
        else:
            inp = "Word"
        #NOTA:  "element" ---> VALUE
        #       "inp"     ---> TYPE
        #       "counter" ---> ID
        if inp != "GLB":
            myToken = Token(counter, element, inp)
            tokenList.append(myToken)
    #carico nell'albero la radice
    patternRoot.setTokenList(tokenList)
    #devo caricare per ogni ramo logico la rispettiva tokenList
    childList = patternRoot.getChildList()
    builderList = []
    branchNumber = 0
    for myToken in tokenList:
        builderList.append(myToken)
        if myToken.getType() == "EP":
            #se trovo un terminatore di frase, passo al branch successivo
            childList[branchNumber].setTokenList(builderList)
            branchNumber += 1
            builderList = []
    #conversione in PatternTree
    root = tree.getRoot()
    numB = tree.getNumBranch()
    patternTree = PatternTree(idReq, root, numB)
    #memorizzo in file esterno
    path = getAbsolutePath("/resources/patternTree/pTree"+str(idReq)+".pkl")
    file = open(path, "wb")
    # Pickle.
    pickle.dump(patternTree, file)
    file.close()
print("**CREATO SET DI ALBERI PER IL CONFRONTO")
