#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo che contiene la classe
Token, rappresentante un associazione
tra parola e tag
"""

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

class Token():
    """Class Token
    """
    # Attributes:
    __id = 0
    __value = None
    __type = None


    # Operations
    def __init__(self, id, string, type):
        self.__id = id
        self.__value = string
        self.__type = type

    def getValue(self):
        return self.__value

    def setValue(self, val):
        self.__value = val

    def getType(self):
        return self.__type
