#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe
Leaf, foglia dell'albero
"""

from .Node import Node

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

class Leaf(Node):
    """Class Leaf,
    foglia contenente un
    particolare tag
    """
    # Attributes:
    __id = 0
    __value = None
    __childList = []
    __leafUnderThisNode = None


    # Operations
    def __init__(self, val):
        self.__id = val
        self.__value = None
        self.__childList = [] # (Node[])
        self.__leafUnderThisNode = 0

    def getValue(self):
        return self.__value

    def setValue(self, val):
        self.__value = val

    def addNodeAsChild(self, node):
        self.__childList.append(node)

    def getChildList(self):
        return self.__childList

    def getLeafUnderThisNode(self):
        return self.__leafUnderThisNode

    def setLeafUnderThisNode(self, num):
        self.__leafUnderThisNode = num

    #DIAGRAMMA DI FLUSSO 1.3
    #FUNZIONE RICORSIVA PER IL MATCH
    #DI NODI LEAF TRA DUE ALBERI
    def matcher(self, node):
        """function matcher, confronta due
        foglie (e relativi figli).
        Torna il numero di match positivi
        rilevati
        :return numberOfMatches
        :rtype int
        """
        numberOfMatches = 0
        myString = self.getValue()
        myLeafList = self.getChildList()
        targetString = node.getValue()
        if myString == targetString:
            numberOfMatches += 1
            patternLeafList = node.getChildList()
            for children in myLeafList:
                for target in patternLeafList:
                    counter = children.matcher(target)
                    numberOfMatches += counter
        return numberOfMatches

    #Nuovo metodo usato per il debugging/testing
    def printChild(self, trace):
        """function printChild()
        stampa il tag presente nella foglia
        :return string
        """
        for node in self.__childList:
            trace = trace+"("
            trace = trace+str(node.getValue())
            trace = node.printChild(trace)
            trace = trace+")"
        return trace

    def calculateLeafUnderThisNode(self):
        """ function calculateLeafUnderThisNode
        calcola il numero di foglie sotto
        questo nodo
        :return total
        :rtype int
        """
        total = 0
        for node in self.__childList:
            total += node.getLeafUnderThisNode()
            total += 1
        return total
        