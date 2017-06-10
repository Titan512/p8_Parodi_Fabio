import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if(os.name =="nt"):
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.Leaf import Leaf

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testSetValue():
    listValueExpected = ["TEST1", "TEST2"]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testLeaf = Leaf(0)
        testLeaf.setValue(listValueExpected[i])
        value = testLeaf.getValue() 
        assert value == listValueExpected[i], "\nERRORE\n"

def testInsertChild():
    listValueExpected = ["CHILD1", "CHILD2"]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        leaf = Leaf(0)
        child = Leaf(1)
        child.setValue(listValueExpected[i])
        #inserisco nodo figlio
        leaf.addNodeAsChild(child)
        #prendo la lista dei figli
        listChild = leaf.getChildList()
        value = listChild[0].getValue()
        assert value == listValueExpected[i], "\nERRORE\n"

def testGetNumberLeaf():
    listValueExpected = [4, 7, 5]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testLeaf = Leaf(0)
        testLeaf.setLeafUnderThisNode(listValueExpected[i])
        value = testLeaf.getLeafUnderThisNode()
        assert value == listValueExpected[i], "\nERRORE\n"

def testMatcher():
    listValueExpected = [0, 1, 2, 3]
    #Caso no-match
    testLeaf1 = Leaf(0)
    testLeaf1.setValue("MATCH1")
    testLeaf2 = Leaf(1)
    testLeaf2.setValue("NOMATCH")
    number = testLeaf1.matcher(testLeaf2)
    assert number == listValueExpected[0], "\nERRORE\n"
    #Caso singleMatch
    testLeaf1 = Leaf(0)
    testLeaf1.setValue("MATCH1")
    testLeaf2 = Leaf(1)
    testLeaf2.setValue("MATCH1")
    child1 = Leaf(3)
    child2 = Leaf(4)
    child3 = Leaf(5)
    child1.setValue("1")
    child2.setValue("2")
    child3.setValue("3")
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    testLeaf2.addNodeAsChild(child3)
    number = testLeaf1.matcher(testLeaf2)
    assert number == listValueExpected[1], "\nERRORE\n"
    #Caso 2 match
    testLeaf1 = Leaf(0)
    testLeaf1.setValue("MATCH1")
    testLeaf2 = Leaf(1)
    testLeaf2.setValue("MATCH1")
    child1 = Leaf(3)
    child2 = Leaf(4)
    child3 = Leaf(5)
    child4 = Leaf(6)
    child1.setValue("1")
    child2.setValue("2")
    child3.setValue("1")
    child4.setValue("3")
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    testLeaf2.addNodeAsChild(child3)
    testLeaf2.addNodeAsChild(child4)
    number = testLeaf1.matcher(testLeaf2)
    assert number == listValueExpected[2], "\nERRORE\n"
    #caso 3match
    testLeaf1 = Leaf(0)
    testLeaf1.setValue("MATCH1")
    testLeaf2 = Leaf(1)
    testLeaf2.setValue("MATCH1")
    child1 = Leaf(3)
    child2 = Leaf(4)
    child3 = Leaf(5)
    child4 = Leaf(6)
    child1.setValue("1")
    child2.setValue("2")
    child3.setValue("1")
    child4.setValue("2")
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    testLeaf2.addNodeAsChild(child3)
    testLeaf2.addNodeAsChild(child4)
    number = testLeaf1.matcher(testLeaf2)
    assert number == listValueExpected[3], "\nERRORE\n"

def testCalcLeaf():
    listValueExpected = [0, 1, 4]
    #Caso 0 figli
    testLeaf1 = Leaf(0)
    child1 = Leaf(1)
    child2 = Leaf(2)
    child3 = Leaf(3)
    number = testLeaf1.calculateLeafUnderThisNode()
    assert number == listValueExpected[0], "\nERRORE\n"
    #Caso 1 figli
    testLeaf1 = Leaf(0)
    child1 = Leaf(1)
    child2 = Leaf(2)
    child3 = Leaf(3)
    testLeaf1.addNodeAsChild(child1)
    number = testLeaf1.calculateLeafUnderThisNode()
    assert number == listValueExpected[1], "\nERRORE\n"
    #Caso 4 figli
    testLeaf1 = Leaf(0)
    child1 = Leaf(1)
    child2 = Leaf(2)
    child3 = Leaf(3)
    child4 = Leaf(4)
    child3.addNodeAsChild(child4)
    child3.setLeafUnderThisNode(1)
    child2.addNodeAsChild(child3)
    child2.setLeafUnderThisNode(2)
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    number = testLeaf1.calculateLeafUnderThisNode()
    assert number == listValueExpected[2], "\nERRORE\n"

def testPrintTrace():
    trace = ""
    testLeaf1 = Leaf(0)
    testLeaf1.setValue("main")
    child1 = Leaf(1)
    child1.setValue("Son1")
    child2 = Leaf(2)
    child2.setValue("Son2")
    child3 = Leaf(3)
    child3.setValue("Son3")
    child1.addNodeAsChild(child3)
    testLeaf1.addNodeAsChild(child1)
    testLeaf1.addNodeAsChild(child2)
    trace = testLeaf1.printChild(trace)
    assert trace == "(Son1(Son3))(Son2)", "\nERRORE\n"

def test3():
    testSetValue()
    testInsertChild()
    testGetNumberLeaf()
    testMatcher()
    testCalcLeaf()
    testPrintTrace()
