#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pickle
from sys import path
from .InputTree import InputTree
from .PatternTree import PatternTree
from .Token import Token
from .AbsolutePath import getAbsolutePath

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

class Translation:
    """Class Translation
    Rappresenta il processo di traduzione.
    NOTA: attualmente è possibile l'utilizzo
    dei soli requisiti forniti dal professor
    Tacchella.
    In futuro bisognerà cambiare il sistema
    di scelta da "requisito num. N"
    a "file immesso"
    """
    # Attributes:
    __id = None  # ()
    __inputTree = None
    __patternTreeList = []
    __TokenList = []


    # Operations
    def __init__(self, val):
        self.__id = val
        self.__inputTree = None
        self.__patternTreeList = []
        #carico i patternTree salvati in precedenza
        for idReq in range(1, 13):
            #A causa di alcuni problemi di apertura,
            #ricorro all'indirizzo assoluto
            path = getAbsolutePath("/resources/patternTree/pTree"+str(idReq)+".pkl")
            #apro il file
            pkl_file = open(path, "rb")
            patternTree = PatternTree(1, None, None)
            patternTree = pickle.load(pkl_file)
            self.__patternTreeList.append(patternTree)
            pkl_file.close()
        self.__TokenList = []

    def loadInputTree(self, treeNumber):
        """ function loadInputTree
        Funzione per convertire una stringa
        in un albero sintattico
        :return None
        """
        #inizializzo l'albero
        self.__inputTree = InputTree(treeNumber)
        #prendo i dati relativi all'albero che voglio analizzare
        treeFile = getAbsolutePath("/resources/inputTree/pattern"+str(treeNumber)+".txt")
        #del relativo albero, prendo anche la stringa di parole corrispondente
        wordListFile = getAbsolutePath("/resources/req/requisito"+str(treeNumber)+".txt")
        #creo l'albero, passandogli tutti i dati
        self.__inputTree.loadTreeFromFile(treeFile, wordListFile)
        return None



    #DIAGRAMMA DI FLUSSO PRINCIPALE  (1.0)
    def translateRequirement(self, treeNumber, isTest=False):
        """ function translateRequirement
        Funzione per avviare la traduzione del requisito
        Ottiene e rielabora il FSP più probabile
        :return string
        """
        enableGlobalMatch = False
        formalSpecPat = ""
        #carico il requisito scelto.
        #[NOTA: reworkTree ora è direttamente avviato
        #       dalla classe albero al termine della
        #       conversione da stringa ad albero
        self.loadInputTree(treeNumber)
        #faccio un confronto con ogni albero
        #       CORREZIONE!!
        # sostituito il "forEach p in patternTreeList"
        #per poter distinguere il "TrainingSet"
        #dal "TestSet"
        maxRange = len(self.__patternTreeList)
        for i in range(0, maxRange):
            #se è un Test, evito il confronto
            #con lo stesso albero
            if not(isTest and i == treeNumber-1):
                patternTree = self.__patternTreeList[i]
                globalMatch = self.__inputTree.matchTrees(patternTree)
                #se rilevo un match totale:
                if globalMatch is True:
                    enableGlobalMatch = True
                    break
        #ottengo la lista [PAROLE del mio requisito, FSP più probabile]
        completedList = self.__inputTree.getPatternAndWords(enableGlobalMatch)
        outputPattern = self.compilePattern(completedList)
        #CORREZIONE: per un maggior controllo,
        #porto l'outputPattern in stringa
        formalSpecPat = self.convertePatternInString(outputPattern)
        return formalSpecPat

    #DIAGRAMMA DI FLUSSO 1.4: creazione del FSP
    def compilePattern(self, wordAndPatternList):
        """function compilePattern
        data la lista [PAROLE del mio requisito, FSP più probabile],
        rielabora la lista delle parole per ottenere un FSP
        quanto più coerente possibile
        """
        wordList = wordAndPatternList[0]
        #CORREZIONE: eseguo una copia per sicurezza
        patternList = wordAndPatternList[1].copy()
        #CORREZIONE: manca la gestione del "Globally"
        if patternList[1].getValue() == "it":
            globalToken = Token(-1, "Globally,", "GLB")
            patternList = [globalToken] + patternList
        for element in patternList:
            #"type" è una parola riservata da python .. rinomino
            #la variabile "type" in "tag"
            tag = element.getType()
            if tag == "SIG" or tag == "VT":
                for word in wordList:
                    wordType = word.getType()
                    if wordType == tag:
                        wordString = word.getValue()
                        element.setValue(wordString)
                        #CORREZIONE: per non ritrovarmi in
                        #seguito lo stesso token, lo rimuovo
                        wordList.remove(word)
                        break
        return patternList

    #NUOVA FUNZIONE
    #Usata per l'esame di software engineering
    #più comodo visualizzare i risultati in stringa
    def convertePatternInString(self, list):
        """function convertePatternInString
        converte una tokenList in stringa,
        prendendo ogni valore del token
        ed inserendolo in una stringa
        return string
        """
        string = ""
        for element in list:
            typeAnalized = element.getType()
            if typeAnalized == "space":
                string += " "
            else:
                string = string + element.getValue()
        return string


