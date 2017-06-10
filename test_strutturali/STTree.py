import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.Tree import Tree
from Class.LogicalBranch import LogicalBranch

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testCreateTreeStructure():
    string = "(Tag(Tag(tag value)(tag value))(tag value)))"
    testRoot = LogicalBranch(0, "ROOT")
    testTree = Tree()
    testTree.createNode(testRoot, string, 0)
    returnString = testRoot.printChild("")
    assert returnString == "(Tag(Tag(tag(value))(tag(value)))(tag(value)))", "\nERRORE\n"

def test9():
    testCreateTreeStructure()
