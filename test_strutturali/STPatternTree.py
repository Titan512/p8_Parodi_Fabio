import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.PatternTree import PatternTree
from Class.Leaf import Leaf
from Class.LogicalBranch import LogicalBranch

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testGetSetRoot():
    listValueExpected = [8, 4, 7, 3]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testTree = PatternTree(0, 0, 0)
        testTree.setRoot(listValueExpected[i])
        value = testTree.getRoot()
        assert value == listValueExpected[i], "\nERRORE\n"

def testGetSetNumBranch():
    listValueExpected = [5, 12, 23, 3]
    maxRange = len(listValueExpected)
    for i in range(0, maxRange):
        testTree = PatternTree(0, 0, 0)
        testTree.setNumBranch(listValueExpected[i])
        value = testTree.getNumBranch()
        assert value == listValueExpected[i], "\nERRORE\n"

def testPrintTree():
    testTree = PatternTree(0, 0, 0)
    testRoot = LogicalBranch(0, "Root")
    testBranch = LogicalBranch(0, "Branch")
    testRoot.addNodeAsChild(testBranch)
    testTree.setRoot(testRoot)
    string = testTree.printTree()
    assert "(Branch)" == string, "\nERRORE\n"
    testTree = PatternTree(0, 0, 0)
    testRoot = LogicalBranch(0, "Root")
    testBranch = LogicalBranch(0, "Branch")
    testLeaf = Leaf(0)
    testLeaf.setValue("leaf")
    testBranch.addNodeAsChild(testLeaf)
    testRoot.addNodeAsChild(testBranch)
    testTree.setRoot(testRoot)
    string = testTree.printTree()
    assert string == "(Branch(leaf))", "\nERRORE\n"

def test6():
    testGetSetRoot()
    testGetSetNumBranch()
    testPrintTree()
    