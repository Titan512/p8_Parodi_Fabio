#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe
Node, nodo generico dell'albero
"""

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

class Node:
    """Class Node
    """
    # Attributes:
    __id = None  # (int)
    __value = None  # (String)
    __leafUnderThisNode = 0 # (int)
    __childList = None # (Node[])


    # Operations
    def insertInList(self, list1, list2):
        """ function insertInList
        inserisce ogni elemento in list2
        in list1

        return list1
        :rtype list[]
        """
        for element in list2:
            list1.append(element)
        return list1

    def formDoubleList(self, firstList, secondList):
        """ function insertInList
        forma una doppia lista dalle due
        passate

        return doubleList
        :rtype list[[],[]]
        """
        doubleList = []
        doubleList.append(firstList)
        doubleList.append(secondList)
        return doubleList

 