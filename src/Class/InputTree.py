#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe
InputTree, che gestisce l'albero sintattico
da tradurre
"""

from .Tree import Tree
from .LogicalBranch import LogicalBranch
from .Token import Token

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

class InputTree(Tree):
    """Class InputTree,
    albero sintattico
    """
    # Operations
    def __init__(self, val):
        self.__id = val
        self.__root = None
        self.__numBranch = None

    def getRoot(self):
        return self.__root

    def setRoot(self, node):
        self.__root = node

    def getNumBranch(self):
        return self.__numBranch

    def setNumBranch(self, value):
        self.__numBranch = value

    #INIZIO DIAGRAMMA DI FLUSSO 1.1
    #RIMODELLAZIONE DELL'ALBERO
    def reworkTree(self):
        """  function reworkTree, rielabora i nodi
        figli della radice per creare sotto di essa
        dei rami logici
        :return None
        """
        self.__root.adjustLogicalBranches()
        return None

    #INIZO DIAGRAMMA DI FLUSSO 1.2
    #MATCHING DI UN ALBERO SINTATTICO
    #CON UN PATTERNTREE
    def matchTrees(self, patternTree):
        """
        functions matchTrees, compara l'albero
        con quello passato, caricando eventuali
        comparazioni direttamente nei nodi
        LogicalBranch (radici e rami logici)
        :return True o False, a seconda se è possibile
            eseguire una comparazione globale
        :rtype boolean
        """
        patternTreeRoot = patternTree.getRoot()
        globalMatch = self.__root.matcher(patternTreeRoot)
        #considero il numero di rami logici.
        branchPTree = patternTree.getNumBranch()
        #se il numero è diverso, non posso eseguire
        #un confronto globale
        if self.__numBranch != branchPTree:
            globalMatch = False
        return globalMatch

    def getPatternAndWords(self, globalMatchIsEnabled):
        """  function reworkTree, eseguito il
        confronto tra alberi ottiene la lista di parole
        da se stesso e il pattern più probabile
        :return completePatternList, una lista contenente:
            -0 la lista delle parole
            -1 la lista contenente il pattern
        :return list[[][]]
        """
        if globalMatchIsEnabled:
            completePatternList = self.getRoot().getData()
        else:
            completePatternList = self.getRoot().getCompositeData()
        return completePatternList

    #NUOVI METODI
    #Metodo per creare un albero da un file, con successiva definizione di rami
    def loadTreeFromFile(self, fileDir, fileTokenList):
        """ function loadTreeFromFile, crea l'albero
        dato un file contenente un espressione in stringa
        ed un file contenente la lista di parole da associare
        :return None
        """
        file = open(fileDir, "r")
        firstLineReader = file.readline().replace(" (", "(")
        firstLineReader = firstLineReader.replace(") ", ")")
        #NOTA: da qui in poi sono sicuro di non avere piu spazi(ad eccezione
        # delle sottostringhe rappresentanti le parole)
        self.__root = LogicalBranch(0, "ROOT")
        #controllo se la stringa inizia correttamente.
        if firstLineReader[0] == '(':
            word = ""
            i = 1
            #come prima parola dovrei trovare "ROOT"
            while i < len(firstLineReader):
                character = firstLineReader[i]
                if character == '(':
                    i += 1
                    break
                else:
                    word = word + character
                i += 1
            if word == "ROOT":
                #Stringa inizializzata correttamente.
                #Procedo all'assegnazione dei nodi
                self.createNode(self.__root, firstLineReader, 1)
        file.close()
        if fileTokenList != None:
            #carico la tokenlist
            file = open(fileTokenList, 'r')
            id = 0
            tokenList = []
            for line in file:
                id += 1
                readerList = line.split(" ")
                myToken = Token(id, readerList[0], readerList[1].strip("\n"))
                tokenList.append(myToken)
            self.__root.setTokenList(tokenList)
            file.close()
        #creo i rami logici
        self.__root.adjustLogicalBranches()
        #salvo il numero di branch dell'albero
        branchNumber = self.__root.getNumberOfChild()
        self.setNumBranch(branchNumber)

    def printTree(self):
        """function printTree
        stampa a terminale l'albero
        sottoforma di stringa
        Usato per il debugging
        return: string
        """
        return self.__root.printChild("")