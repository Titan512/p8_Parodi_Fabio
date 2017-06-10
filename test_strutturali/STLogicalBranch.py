import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if(os.name =="nt"):
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.LogicalBranch import LogicalBranch
from Class.Leaf import Leaf

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testSetGetValue():
    listValueExpected = ["TEST1", "TEST2", "TEST3"]
    maxRange = len(listValueExpected)
    testLeaf = LogicalBranch(0, listValueExpected[0])
    value = testLeaf.getValue()
    assert value == listValueExpected[0], "\nERRORE\n"
    for i in range(1, maxRange):
        testLeaf = LogicalBranch(0, listValueExpected[i])
        testLeaf.setValue(listValueExpected[i])
        value = testLeaf.getValue()
        assert value == listValueExpected[i], "\nERRORE\n"

def testGetSetProb():
    listValueExpected = [6, 0.2, 0.4, 1]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testLeaf = LogicalBranch(0, "")
        testLeaf.setMatchProb(listValueExpected[i])
        value = testLeaf.getMatchProb()
        assert value == listValueExpected[i], "\nERRORE\n"

def testGetSetSimilarBranch():
    listValueExpected = []
    node1 = LogicalBranch(0, "0")
    listValueExpected.append(node1)
    node2 = LogicalBranch(1, "1")
    listValueExpected.append(node2)
    node3 = LogicalBranch(2, "2")
    listValueExpected.append(node3)
    maxRange = len(listValueExpected)
    for i in range(0,maxRange):
        testLeaf = LogicalBranch(0, "")
        testLeaf.setSimilarBranch(listValueExpected[i])
        value = testLeaf.getSimilarBranch()
        assert value == listValueExpected[i], "\nERRORE\n"

def testGetSetNumberLeaf():
    listValueExpected = [5, 3, 1, 7]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testLeaf = LogicalBranch(0, "")
        testLeaf.setLeafUnderThisNode(listValueExpected[i])
        value = testLeaf.getLeafUnderThisNode()
        assert value == listValueExpected[i], "\nERRORE\n"

def testHandleNodeAsChild():
    listValueExpected = [0, 1, 2, 3]
    testLeaf = LogicalBranch(0, "")
    child1 = LogicalBranch(1, listValueExpected[1])
    child2 = LogicalBranch(2, listValueExpected[2])
    child3 = LogicalBranch(3, listValueExpected[3])
    #TESTO L'INSERIMENTO DEI FIGLI
    value = testLeaf.getNumberOfChild()
    assert value == listValueExpected[0], "\nERRORE\n"
    testLeaf.addNodeAsChild(child1)
    value = testLeaf.getNumberOfChild()
    assert value == listValueExpected[1], "\nERRORE\n"
    testLeaf.addNodeAsChild(child2)
    value = testLeaf.getNumberOfChild()
    assert value == listValueExpected[2], "\nERRORE\n"
    testLeaf.addNodeAsChild(child3)
    value = testLeaf.getNumberOfChild()
    assert value == listValueExpected[3], "\nERRORE\n"
    #TESTO IL RITORNO DELLA LISTA
    childList = testLeaf.getChildList()
    maxRange = len(childList)
    assert maxRange == len(listValueExpected)-1, "\nERRORE\n"
    #TESTO CHE OGNI FIGLIO ABBIA IL RELATIVO VALORE
    for i in range(0, maxRange):
        child = childList[i]
        value = child.getValue()
        assert value == listValueExpected[i]+1, "\nERRORE\n"
    #TESTO LA RIMOZIONE DEI FIGLI
    testLeaf.removeNodeAsChild(1)
    value = testLeaf.getNumberOfChild()
    assert value == maxRange-1, "\nERRORE\n"
    #TESTO IL RITORNO DELLA LISTA
    childList = testLeaf.getChildList()
    getChild1 = childList[0]
    getChild2 = childList[1]
    assert getChild1.getValue() == listValueExpected[1], "\nERRORE\n"
    assert getChild2.getValue() == listValueExpected[3], "\nERRORE\n"

def testGetSetTokenList():
    tokenList = [5, 7, 2, 5]
    testLeaf = LogicalBranch(0, "")
    testLeaf.setTokenList(tokenList)
    returnList = testLeaf.getTokenList()
    assert tokenList == returnList, "\nERRORE\n"

def testAdjustLogicalBranches():
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
    testLeaf.adjustLogicalBranches()
    childList = testLeaf.getChildList()
    #nessun cambiamento fatto nella lista dei figli
    assert len(childList) == listValueExpected[0], "\nERRORE\n"
    #CASO DUE FIGLI
    testLeaf = LogicalBranch(0, "")
    testLeaf.addNodeAsChild(leafChild1)
    testLeaf.addNodeAsChild(leafChild2)
    #aziono la funzione, e guardo che mi abbia restituito
    #un figlio "logicalBranch" corretto
    testLeaf.adjustLogicalBranches()
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
    testLeaf.adjustLogicalBranches()
    childList = testLeaf.getChildList()
    assert len(childList) == 2
    #analizzo il figlio
    newChild = childList[0]
    assert len(newChild.getChildList()) == listValueExpected[1]
    #analizzo il secondo
    newChild = childList[1]
    assert len(newChild.getChildList()) == listValueExpected[2]

def testRootHasLeafNodeAsChild():
    testLeaf = LogicalBranch(0, "")
    leafChild = Leaf(1)
    branchChild = LogicalBranch(1, "")
    testLeaf.addNodeAsChild(leafChild)
    testLeaf.addNodeAsChild(branchChild)
    assert testLeaf.rootHasLeafNodeAsChild() == True, "\nERRORE\n"
    testLeaf = LogicalBranch(0, "")
    leafChild = Leaf(1)
    branchChild = LogicalBranch(1, "")
    testLeaf.addNodeAsChild(branchChild)
    assert testLeaf.rootHasLeafNodeAsChild() == False, "\nERRORE\n"

def testChildIsEndSentence():
    testLeaf = LogicalBranch(0, "")
    leafChild1 = Leaf(1)
    leafChild1.setValue("EP")
    leafChild2 = Leaf(2)
    leafChild2.setValue("Other")
    testLeaf.addNodeAsChild(leafChild1)
    testLeaf.addNodeAsChild(leafChild2)
    assert testLeaf.childIsEndSentence(0) == True, "\nERRORE\n"
    assert testLeaf.childIsEndSentence(1) == False, "\nERRORE\n"

def branchMatcher():
    testLeaf1 = LogicalBranch(1, "main")
    child1 = Leaf(1)
    child1.setValue("Child1")
    child2 = Leaf(2)
    child2.setValue("Child2")
    child3 = Leaf(3)
    child3.setValue("Child3")
    testLeaf2 = LogicalBranch(2, "main")
    #Test Perfettamente Uguali
    child2.addNodeAsChild(child3)
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    testLeaf2.addNodeAsChild(child1)
    testLeaf2.addNodeAsChild(child2)
    testLeaf1.setLeafUnderThisNode(3)
    testLeaf2.setLeafUnderThisNode(3)
    #guardo il matching dei due
    assert testLeaf1.branchMatcher(testLeaf2) == True, "\nERRORE\n"
    prob = testLeaf1.getMatchProb()
    assert prob == 1, "\nERRORE\n"
    #Test alberi Diversi
    testLeaf1 = LogicalBranch(1, "main")
    child1 = Leaf(1)
    child1.setValue("Child1")
    child2 = Leaf(2)
    child2.setValue("Child2")
    child3 = Leaf(3)
    child3.setValue("Child3")
    child2.addNodeAsChild(child3)
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    testLeaf2 = LogicalBranch(2, "main")
    child4 = Leaf(4)
    child4.setValue("Child4")
    child5 = Leaf(5)
    child5.setValue("Child5")
    child6 = Leaf(6)
    child6.setValue("Child6")
    child5.addNodeAsChild(child6)
    testLeaf2.addNodeAsChild(child4)
    testLeaf2.addNodeAsChild(child5)
    testLeaf1.setLeafUnderThisNode(3)
    testLeaf2.setLeafUnderThisNode(3)
    assert testLeaf1.branchMatcher(testLeaf2) == False, "\nERRORE\n"
    prob = testLeaf1.getMatchProb()
    assert prob == 0, "\nERRORE\n"
    #Test alberi differenti
    testLeaf1 = LogicalBranch(1, "main")
    child1 = Leaf(1)
    child1.setValue("Child1")
    child2 = Leaf(2)
    child2.setValue("Child2")
    child3 = Leaf(3)
    child3.setValue("Child3")
    child2.addNodeAsChild(child3)
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    testLeaf2 = LogicalBranch(2, "main")
    child4 = Leaf(4)
    child4.setValue("Child3")
    child5 = Leaf(5)
    child5.setValue("Child1")
    child6 = Leaf(6)
    child6.setValue("Child6")
    child5.addNodeAsChild(child6)
    testLeaf2.addNodeAsChild(child4)
    testLeaf2.addNodeAsChild(child5)
    testLeaf1.setLeafUnderThisNode(3)
    testLeaf2.setLeafUnderThisNode(3)
    assert testLeaf1.branchMatcher(testLeaf2) == False, "\nERRORE\n"
    prob = testLeaf1.getMatchProb()
    assert prob < 0.4 and prob > 0.2, "\nERRORE\n"

def rootMatcher():
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
    assert testRoot1.matcher(testRoot2) == True, "\nERRORE\n"
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
    assert testRoot1.matcher(testRoot2) == False, "\nERRORE\n"
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
    assert testRoot1.matcher(testRoot2) == False, "\nERRORE\n"
    prob = testRoot1.getMatchProb()
    assert prob == 0, "\nERRORE\n"
    prob = testBranch1.getMatchProb()
    assert prob == 0.5, "\nERRORE\n"

def testGetData():
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
    data = testRoot1.getData()
    assert len(data) == 2, "\nERRORE\n"
    assert data[0] == ["Word"] and data[1] == [50, 50], "\nERRORE\n"
    #match parziale
    data = testRoot1.getCompositeData()
    assert len(data) == 2, "\nERRORE\n"
    assert data[0] == ["Word"] and data[1] == [100, 200], "\nERRORE\n"

def testPrintChild():
    testRoot1 = LogicalBranch(1, "root")
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
    testRoot1.addNodeAsChild(testBranch2)
    string = testRoot1.printChild("")
    assert string == "(branch(this))(branch(this)(that))", "\nERRORE\n"

def testCalculateLeaf():
    testBranch = LogicalBranch(1, "branch")
    leaf1 = Leaf(0)
    leaf1.setValue("this")
    leaf2 = Leaf(1)
    leaf2.setValue("this")
    leaf3 = Leaf(2)
    leaf3.setValue("that")
    leaf4 = Leaf(3)
    leaf4.setValue("that2")
    leaf3.addNodeAsChild(leaf4)
    leaf2.addNodeAsChild(leaf3)
    testBranch.addNodeAsChild(leaf1)
    testBranch.addNodeAsChild(leaf2)
    leaf1.setLeafUnderThisNode(0)
    leaf1.setLeafUnderThisNode(2)
    result = testBranch.calculateLeafUnderThisNode()
    assert result == 4, "\nERRORE\n"

def test4():
    testSetGetValue()
    testGetSetProb()
    testGetSetSimilarBranch()
    testGetSetNumberLeaf()
    testHandleNodeAsChild()
    testGetSetTokenList()
    testAdjustLogicalBranches()
    testRootHasLeafNodeAsChild()
    testChildIsEndSentence()
    branchMatcher()
    rootMatcher()
    testGetData()
    testPrintChild()
    testCalculateLeaf()
    