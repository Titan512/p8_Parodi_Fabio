#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe LogicalBranch, rappresentante
un ramo logico del requisito direttamente associabile con
un sottopattern
"""

from .Node import Node
from .Leaf import Leaf

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

class LogicalBranch(Node):
    """Class LogicalBranch
    nodo rappresentante il
    ramo logico dell'albero,
    collegato con un
    sottopattern
    """
    # Attributes:
    __matchProbability = None  # (float)
    __similarBranch = None  # (LogicalBranch)
    __tokenList = None  # (Token[])


    # Operations
    def __init__(self, idNum, string):
        self.__id = idNum
        self.__value = string
        self.__matchProbability = 0
        self.__similarBranch = None
        self.__leafUnderThisNode = 0
        self.__childList = [] # (Node[])
        self.__tokenList = [] # (Token[])

    def getValue(self):
        return self.__value

    def setValue(self, val):
        self.__value = val

    def getMatchProb(self):
        return self.__matchProbability

    def setMatchProb(self,perc):
        self.__matchProbability = perc

    def getSimilarBranch(self):
        return self.__similarBranch

    def setSimilarBranch(self, branch):
        self.__similarBranch = branch

    def addNodeAsChild(self, node):
        self.__childList.append(node)

    def removeNodeAsChild(self, number):
        del self.__childList[number]

    def getNumberOfChild(self):
        return len(self.__childList)

    def getChildList(self):
        return self.__childList

    def getLeafUnderThisNode(self):
        return self.__leafUnderThisNode

    def setLeafUnderThisNode(self, num):
        self.__leafUnderThisNode = num

    def getTokenList(self):
        return self.__tokenList

    def setTokenList(self, list):
        self.__tokenList = list

    #DIAGRAMMA DI FLUSSO 1.1:
    #RIMODELLAZIONE DEI NODI DELL'ALBERO
    def adjustLogicalBranches(self):
        """function adjustLogicalBranches,
        funzione per riorganizzare l'albero
        in sottorami logici.
        Passa da una radice con fogli Leaf
        ad una radice con figli LogicalBranches
        :return None
        """
        idCounter = 0
        if self.getNumberOfChild() == 0:
            return None
        while self.rootHasLeafNodeAsChild() is True:
            #creo il branch
            idCounter -= 1
            branch = LogicalBranch(idCounter, "BRANCH")
            #finchè non rilevo un terminatire di frase
            #CORREZIONE:
            #aggiunta condizione "rootHasLeafNodeAsChild"
            #per evitare il sorgere di errori
            while self.getNumberOfChild() > 0 and self.childIsEndSentence(0) is False \
                  and self.rootHasLeafNodeAsChild():
                #sposto il nodo figlio nel branch
                branch.addNodeAsChild(self.__childList[0])
                self.removeNodeAsChild(0)
            #CORREZIONE:
            #aggiunto check di controllo per
            #verificare di non scorrere una lista vuota
            if self.getNumberOfChild() > 0:
                if self.childIsEndSentence(0) is True:
                    #rimuovo il terminatore di frase
                    self.removeNodeAsChild(0)
                    #rimuovo il conteggio di questi nodi
                    #(un tag ed una parola (punto o virgola))
                    num = self.getLeafUnderThisNode()
                    self.setLeafUnderThisNode(num-2)
            #calcolo quindi il numero di foglie nel ramo
            nLeaf = branch.calculateLeafUnderThisNode()
            branch.setLeafUnderThisNode(nLeaf)
            self.addNodeAsChild(branch)
        return None

    def rootHasLeafNodeAsChild(self):
        """function rootHasLeafNodeAsChild
        torna True se il primo nodo figlio
        è di tipo Leaf
        """
        return type(self.__childList[0]) is Leaf

    #La funzione viene usata per dire se la foglia rappresenta un terminatore di frase.
    def childIsEndSentence(self, childNumber):
        """function childIsEndSentence
        Torna TRUE se il figlio numero childNumber
        rappresenta un terminatore di frase
        """
        if self.__childList[childNumber].getValue() == "EP":
            return True
        else:
            return False

    #DIAGRAMMA DI FLUSSO 1.2
    #MATCHING DI UNA RADICE
    #CON UNA RADICE DI PATTERNTREE
    def matcher(self, node):
        """function matcher
        funzione per il confronto tra due radici
        torna TRUE se ogni singolo ramo
        fà riferimento allo stesso albero
        [è possibile un confronto globale]
        return: boolean
        """
        myBranchList = self.getChildList()
        globalMatch = True
        branchMatching = False
        totalProb = 1
        patternBranchList = node.getChildList()
        #Confronto i vari rami presenti sotto le radici
        for myBranch in myBranchList:
            matching = False
            for branchTarget in patternBranchList:
                matching = myBranch.branchMatcher(branchTarget)
                #memorizzo la corrispondenza:
                #di tutti i match con il ramo myBranch, me ne basta uno
                #per affermare di avere un ottima corrispondenza
                branchMatching = branchMatching or matching
                #se c'è un ottima corrispondenza, non vado oltre
                if matching == True:
                    break
            #con questa verifico che ogni ramo abbia un ottima corrispondenza
            globalMatch = globalMatch and branchMatching
        #se posso eseguire un confronto globale, memorizzo la corrispondenza
        #con la radice
        if globalMatch is True:
            #calcolo la % di corrispondenza
            for myBranch in myBranchList:
                prob = myBranch.getMatchProb()
                totalProb = totalProb * prob
            #se questa è maggiore, aggiorno i parametri
            myExProb = self.getMatchProb()
            if totalProb >= myExProb:
                self.setSimilarBranch(node)
                self.setMatchProb(totalProb)
                #Se la % è sopra una certa soglia, posso cercare subito
                #il match globale
                if totalProb >= 0.9:
                    return True
        return False

    #DIAGRAMMA DI FLUSSO 1.2
    #MATCHING DI UN BRANCH
    #CON UN BRANCH DI UN PATTERNTREE
    def branchMatcher(self, branchTarget):
        """function branchMatcher
        funzione per il confronto tra
        due rami logici
        Torna TRUE se ho rilevato
        un ottimo matching tra i rami
        return: boolean
        """
        #CORREZIONE:per una maggiore chiarezza,
        #cambio l'ordine dell'inizializzazione
        #delle variabili
        #ottengo le liste dei figli
        myNodeList = self.getChildList()
        patternBranchList = branchTarget.getChildList()
        #inizializzo variabili per il calcolo delle probabilita
        numberMyLeaf = self.getLeafUnderThisNode()
        numberPatternLeaf = branchTarget.getLeafUnderThisNode()
        numberOfCorrispondence = 0
        #indico la possibilità che ci sia un match totale tra branch
        #CORREZIONE: cambio nome "matching" in "totalMatching"
        #per una maggiore chiarezza
        totalMatching = False
        #confronto le foglie nei relativi rami
        #NOTA: per ogni foglia vi è al massimo una corrispondenza
        for myLeaf in myNodeList:
            for patternLeaf in patternBranchList:
                numberOfMatch = myLeaf.matcher(patternLeaf)
                numberOfCorrispondence += numberOfMatch
        #Ottenuto il numero di confronti tra questo ramo ed il bersaglio,
        #calcolo la % di matching
        probability = self.calculateProbability(numberOfCorrispondence,
                                                numberMyLeaf, numberPatternLeaf)
        #carico la precedente % salvata. Se è inferiore, salvo la nuova
        matchProbability = self.getMatchProb()
        if probability >= matchProbability:
            self.setMatchProb(probability)
            self.setSimilarBranch(branchTarget)
            #se la probabilità è sopra una certa soglia, allora
            #indico che il ramo ha un ottimo matching
            if probability >= 0.99:
                totalMatching = True
        return totalMatching

    def calculateProbability(self, numberOfMatches, numberInputLeafInBranch,
                             numberLeafInPatternBranch):
        """ function calculateProbability
        calcola la % di matching tra due
        rami logici
        returns float
        """
        maxNumberOfLeaf = 0
        if numberInputLeafInBranch >= numberLeafInPatternBranch:
            maxNumberOfLeaf = numberInputLeafInBranch
        else:
            maxNumberOfLeaf = numberLeafInPatternBranch
        probability = numberOfMatches/maxNumberOfLeaf
        return probability

    def getData(self):
        """function getData
        CONFRONTO GLOBALE
        torna una doppia lista contenente
            -0 la lista delle parole del requisito
            analizzato
            -1 il pattern più probabile rilevato

        returns completePatternList
        :rtype list[[] []]
        """
        patternList = self.__similarBranch.getTokenList()
        myList = self.getTokenList()
        completePatternList = self.formDoubleList(myList, patternList)
        return completePatternList

    def getCompositeData(self):
        completePatternList = []
        branchesList = self.getChildList()
        patternList = []
        for branch in branchesList:
            patternList = branch.getData()
            completePatternList = self.insertInList(completePatternList, patternList[1])
        myList = self.getTokenList()
        #per maggiore chiarezza, chiamo la lista
        #di ritorno "returnList"
        returnList = self.formDoubleList(myList, completePatternList)
        return returnList

    #NUOVO METODO!!!
    def printChild(self, string):
        """function getData
        stampa il tag del ramo
        e dei suoi figli
        return None
        """
        for node in self.__childList:
            string = string +"("
            string = string + node.getValue()
            string = node.printChild(string)
            string = string +")"
        return string

    """
    def debugging(self):
        print("\n*******\n")
        print("ID: ",self.__id)
        print("Stringa: ",self.__value)
        print("#figli: ",self.__leafUnderThisNode)
        print("%Matching: ",self.__matchProbability)
        print("Branch Simile: ",self.__similarBranch)
        print("Figli: [",end="")
        for node in self.__childList:
            print("",node.getValue(), end="")
        print(" ]\nTokenList: [", end="")
        for token in self.__tokenList:
            print("[",token.getValue(),"-",token.getType(),"] ",end="")  
        print("]\n*******\n")
    """

    def calculateLeafUnderThisNode(self):
        """ function calculateLeafUnderThisNode
        calcola il numero di nodi Leaf sotto
        questo ramo logico
        returns total
        :rtype int
        """
        total = 0
        for node in self.__childList:
            total += node.getLeafUnderThisNode()
            total += 1
        return total
