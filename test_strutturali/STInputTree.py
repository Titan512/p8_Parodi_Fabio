import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if(os.name =="nt"):
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
import pickle
from Class.InputTree import InputTree
from Class.Leaf import Leaf
from Class.LogicalBranch import LogicalBranch
from Class.PatternTree import PatternTree
from Class.AbsolutePath import getAbsolutePath

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testGetSetRoot():
    listValueExpected = [8, 4, 7, 3]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testTree = InputTree(0)
        testTree.setRoot(listValueExpected[i])
        value = testTree.getRoot()
        assert value == listValueExpected[i], "\nERRORE\n"

def testGetSetNumBranch():
    listValueExpected = [5, 12, 23, 3]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testTree = InputTree(0)
        testTree.setNumBranch(listValueExpected[i])
        value = testTree.getNumBranch()
        assert value == listValueExpected[i], "\nERRORE\n"

def testReworkTree():
    listValueExpected = [0, 2, 1]
    testLeaf = LogicalBranch(0, "")
    leafChild1 = Leaf(1)
    leafChild1.setValue("child1")
    leafChild1b = Leaf(11)
    leafChild1b.setValue("child1b")
    leafChild1.addNodeAsChild(leafChild1b)
    leafChild2 = Leaf(2)
    leafChild2.setValue("child2")
    leafChild3 = Leaf(3)
    leafChild3.setValue("EP")
    leafChild4 = Leaf(4)
    leafChild4.setValue("child4")
    #CASO NO FIGLI
    testTree = InputTree(0)
    testTree.setRoot(testLeaf)
    testTree.reworkTree()
    childList = testLeaf.getChildList()
    #nessun cambiamento fatto nella lista dei figli
    assert len(childList) == listValueExpected[0], "\nERRORE\n"
    #CASO DUE FIGLI
    testLeaf = LogicalBranch(0, "")
    testLeaf.addNodeAsChild(leafChild1)
    testLeaf.addNodeAsChild(leafChild2)
    #aziono la funzione, e guardo che mi abbia restituito
    #un figlio "logicalBranch" corretto
    testTree = InputTree(0)
    testTree.setRoot(testLeaf)
    testTree.reworkTree()
    childList = testLeaf.getChildList()
    assert len(childList) == 1, "\nERRORE\n"
    #analizzo il figlio
    newChild = childList[0]
    assert len(newChild.getChildList()) == listValueExpected[1]
    #CASO TRE FIGLI (con separatore di frase)
    testLeaf = LogicalBranch(0, "")
    testLeaf.addNodeAsChild(leafChild1)
    testLeaf.addNodeAsChild(leafChild2)
    testLeaf.addNodeAsChild(leafChild3)
    testLeaf.addNodeAsChild(leafChild4)
    #aziono
    testTree = InputTree(0)
    testTree.setRoot(testLeaf)
    testTree.reworkTree()
    childList = testLeaf.getChildList()
    assert len(childList) == 2
    #analizzo il figlio
    newChild = childList[0]
    assert len(newChild.getChildList()) == listValueExpected[1]
    #analizzo il secondo
    newChild = childList[1]
    assert len(newChild.getChildList()) == listValueExpected[2]

def testMatchTrees():
    testRoot1 = LogicalBranch(1, "root")
    testRoot2 = LogicalBranch(2, "root")
    testBranch1 = LogicalBranch(1, "branch")
    testBranch2 = LogicalBranch(2, "branch")
    leaf1 = Leaf(0)
    leaf1.setValue("this")
    leaf2 = Leaf(1)
    leaf2.setValue("this")
    #PERFECT MATCHING
    testBranch1.addNodeAsChild(leaf1)
    testBranch2.addNodeAsChild(leaf2)
    testRoot1.addNodeAsChild(testBranch1)
    testRoot2.addNodeAsChild(testBranch2)
    testRoot1.setLeafUnderThisNode(1)
    testRoot2.setLeafUnderThisNode(1)
    testBranch1.setLeafUnderThisNode(1)
    testBranch2.setLeafUnderThisNode(1)
    testTree1 = InputTree(0)
    testTree1.setRoot(testRoot1)
    testTree2 = InputTree(1)
    testTree2.setRoot(testRoot2)
    assert testTree1.matchTrees(testTree2) == True, "\nERRORE\n"
    prob = testRoot1.getMatchProb()
    assert prob == 1, "\nERRORE\n"
    #NEGATIVE MATCHING
    testRoot1 = LogicalBranch(1, "root")
    testRoot2 = LogicalBranch(2, "root")
    testBranch1 = LogicalBranch(1, "branch")
    testBranch2 = LogicalBranch(2, "branch")
    leaf1 = Leaf(0)
    leaf1.setValue("this")
    leaf2 = Leaf(1)
    leaf2.setValue("that")
    testBranch1.addNodeAsChild(leaf1)
    testBranch2.addNodeAsChild(leaf2)
    testRoot1.addNodeAsChild(testBranch1)
    testRoot2.addNodeAsChild(testBranch2)
    testRoot1.setLeafUnderThisNode(1)
    testRoot2.setLeafUnderThisNode(1)
    testBranch1.setLeafUnderThisNode(1)
    testBranch2.setLeafUnderThisNode(1)
    testTree1 = InputTree(0)
    testTree1.setRoot(testRoot1)
    testTree2 = InputTree(1)
    testTree2.setRoot(testRoot2)
    assert testTree1.matchTrees(testTree2) == False, "\nERRORE\n"
    prob = testRoot1.getMatchProb()
    assert prob == 0, "\nERRORE\n"
    #Matching parziale
    testRoot1 = LogicalBranch(1, "root")
    testRoot2 = LogicalBranch(2, "root")
    testBranch1 = LogicalBranch(1, "branch")
    testBranch2 = LogicalBranch(2, "branch")
    leaf1 = Leaf(0)
    leaf1.setValue("this")
    leaf2 = Leaf(1)
    leaf2.setValue("this")
    leaf3 = Leaf(2)
    leaf3.setValue("that")
    testBranch1.addNodeAsChild(leaf1)
    testBranch2.addNodeAsChild(leaf2)
    testBranch2.addNodeAsChild(leaf3)
    testRoot1.addNodeAsChild(testBranch1)
    testRoot2.addNodeAsChild(testBranch2)
    testRoot1.setLeafUnderThisNode(1)
    testRoot2.setLeafUnderThisNode(2)
    testBranch1.setLeafUnderThisNode(1)
    testBranch2.setLeafUnderThisNode(2)
    testTree1 = InputTree(0)
    testTree1.setRoot(testRoot1)
    testTree1.setNumBranch(1)
    testTree2 = InputTree(1)
    testTree2.setRoot(testRoot2)
    testTree2.setNumBranch(2)
    assert testTree1.matchTrees(testTree2) == False, "\nERRORE\n"
    prob = testRoot1.getMatchProb()
    assert prob == 0, "\nERRORE\n"
    prob = testBranch1.getMatchProb()
    assert prob == 0.5, "\nERRORE\n"

def testGetPatternAndWords():
    #Ottengo i dati in seguito ad un
    #match totale
    testRoot1 = LogicalBranch(1, "root")
    testRoot1.setTokenList(["Word"])
    testRoot2 = LogicalBranch(2, "root")
    testRoot2.setTokenList([50, 50])
    testRoot1.setSimilarBranch(testRoot2)
    #creo i vari branch
    testBranch1 = LogicalBranch(1, "branch")
    testBranch2 = LogicalBranch(2, "branch")
    testBranch3 = LogicalBranch(3, "branch")
    testBranch3.setTokenList([100])
    testBranch4 = LogicalBranch(4, "branch")
    testBranch4.setTokenList([200])
    testBranch1.setSimilarBranch(testBranch3)
    testBranch2.setSimilarBranch(testBranch4)
    testRoot1.addNodeAsChild(testBranch1)
    testRoot1.addNodeAsChild(testBranch2)
    testRoot2.addNodeAsChild(testBranch3)
    testRoot2.addNodeAsChild(testBranch4)
    testTree1 = InputTree(0)
    testTree1.setRoot(testRoot1)
    testTree1.setNumBranch(2)
    testTree2 = InputTree(1)
    testTree2.setRoot(testRoot2)
    testTree2.setNumBranch(2)
    data = testTree1.getPatternAndWords(True)
    assert len(data) == 2, "\nERRORE\n"
    assert data[0] == ["Word"] and data[1] == [50, 50], "\nERRORE\n"
    #match parziale
    data = testTree1.getPatternAndWords(False)
    assert len(data) == 2, "\nERRORE\n"
    assert data[0] == ["Word"] and data[1] == [100, 200], "\nERRORE\n"

def testLoadTreeFromFile():
    for idReq in range(1, 13):
        #A causa di alcuni problemi di apertura,
        #ricorro all'indirizzo assoluto
        path = getAbsolutePath("/resources/patternTree/pTree"+str(idReq)+".pkl")
        #apro il file
        pkl_file = open(path, "rb")
        patternTree = PatternTree(1, None, None)
        patternTree = pickle.load(pkl_file)
        treeFile = getAbsolutePath("/resources/inputTree/pattern"+str(idReq)+".txt")
        #del relativo albero, prendo anche la stringa di parole corrispondente
        wordListFile = getAbsolutePath("/resources/req/requisito"+str(idReq)+".txt")
        #creo l'albero, passandogli tutti i dati
        testTree = InputTree(0)
        testTree.loadTreeFromFile(treeFile, wordListFile)
        assert patternTree.printTree() == testTree.printTree(), "\nERRORE\n"
        pkl_file.close()

def test2():
    testGetSetRoot()
    testGetSetNumBranch()
    testReworkTree()
    testMatchTrees()
    testGetPatternAndWords()
    testLoadTreeFromFile()
    