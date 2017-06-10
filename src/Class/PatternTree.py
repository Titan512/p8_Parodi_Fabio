#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe
PatternTree, rappresentante la lista
di alberi sintattici noti e comparabili
"""

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

from .Tree import Tree

class PatternTree(Tree):
    """Class PatternTree
    """
    # Attributes:


    # Operations
    def __init__(self, val, root, numB):
        self.__id = val
        self.__root = root
        self.__numBranch = numB

    def getRoot(self):
        return self.__root

    def setRoot(self, node):
        self.__root = node

    def getNumBranch(self):
        return self.__numBranch

    def setNumBranch(self,num):
        self.__numBranch = num

    #FUNZIONE PER IL DEBUGGING
    def printTree(self):
        """function printTree
        stampa a terminale l'albero
        sottoforma di stringa
        Usato per il debugging
        return: string
        """
        return self.__root.printChild("")
