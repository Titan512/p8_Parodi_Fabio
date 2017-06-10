#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe
generale Tree
"""

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

from .Leaf import Leaf

class Tree():
    """Class ListStatements
    una generalizzazione che identifica
    un albero
    """
    # Attributes:
    __id = None  # (int)
    __root = None  # (Node)
    __numBranch = None  # (int)
    __leafNumber = 0 #contatore per registrare l'id delle foglie

    # Operations
    #metodo ricorsivo per creare i nodi dell'albero leggendo la stringa di tag
    def createNode(self, node, string, integerPos):
        """ function createNode
        funzione ricorsiva per creare i nodi
        dell'albero leggendo la stringa
        di tag
        return i, la posizione del carattere
                  a cui è arrivata
        rtype: int
        """
        word = ""
        i = integerPos
        while i < len(string):
            character = string[i]
            if character == '(':
                #ho trovato un apertura. Salvo il valore del nodo e passo
                # ad analizzare cosa segue
                node.setValue(word)
                self.__leafNumber += 1
                myChild = Leaf(self.__leafNumber)
                node.addNodeAsChild(myChild)
                #ricorsivamente avvio questa funzione per il nodo figlio
                i = self.createNode(myChild, string, i+1)
            elif character == ')':
                #registro il numero di foglie presenti sotto questo nodo
                totalLeaf = node.calculateLeafUnderThisNode()
                node.setLeafUnderThisNode(totalLeaf)
                #termino la chiamata ricorsiva/torno al genitore
                return i
            elif character == ' ':
                #seguirà una parola. Memorizzo quanto trovato e passo al figlio
                node.setValue(word)
                self.__leafNumber += 1
                myChild = Leaf(self.__leafNumber)
                node.addNodeAsChild(myChild)
                i = self.createEasyNode(myChild, string, i+1)
            else:
                word = word + character
            i += 1

    #Metodo dedicato alla creazione di un nodo rilevata una sottostringa
    # rappresentante una parola [ad es: "after"]
    def createEasyNode(self, node, string, integerPos):
        """function createEasyNode
        funzione per creare un nodo contenente
        non un tag, ma la parola vera e propria
        dalla stringa passata
        return i, la posizione del carattere
                  a cui è arrivata
        rtype: int
        """
        word = ""
        i = integerPos
        while i < len(string):
            character = string[i]
            if character == ')':
                node.setValue(word)
                return i-1
            else:
                word = word + character
            i = i+1

    