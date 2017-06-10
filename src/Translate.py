#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pickle
from sys import path
from Class.InputTree import InputTree
from Class.Token import Token
from Class.Translation import Translation

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

"""
Codice per testare manualmente i requisiti da tradurre.
Come riportato in AGGIUNTE.txt, grazie alle semplificazioni
non è necessario inserire l'albero sintattico, basta
selezionare quello desiderato dalla lista proposta
"""
#pulisco il terminale
os.system("cls" if os.name == "nt" else "clear")
numberOfTraduction = 0
#prendo in ingresso l'albero da tradurre
print("\n\n*******************************")
while(numberOfTraduction<=0 or numberOfTraduction>12):
    try:
        print("\nalbero da tradurre?    [da 1 a 12]\nInput: ", end="")
        numberOfTraduction = input()
        numberOfTraduction = int(numberOfTraduction)
    except ValueError:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nOops!  That was not a valid number.")
        numberOfTraduction = 0
    if(numberOfTraduction<0 or numberOfTraduction>12):
        os.system("cls" if os.name == "nt" else "clear")
#traduco l'albero
translator = Translation(0)
print("\n")
translation = translator.translateRequirement(numberOfTraduction, False)
print(translation,"\n\n\n*******************************")