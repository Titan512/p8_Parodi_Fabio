import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.Node import Node
from Class.LogicalBranch import LogicalBranch

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testInsertInList():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7]
    test = LogicalBranch(2, "test")
    returnList = test.insertInList(list1, list2)
    assert returnList == [1, 2, 3, 4, 5, 6, 7], "\nERRORE\n"
    list1 = [22, "Ciao", 3.8, 787]
    list2 = ["test", 22, 22]
    test = LogicalBranch(2, "test")
    returnList = test.insertInList(list1, list2)
    assert returnList == [22, "Ciao", 3.8, 787, "test", 22, 22], "\nERRORE\n"

def testFormDoubleList():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7]
    test = LogicalBranch(2, "test")
    returnList = test.formDoubleList(list1, list2)
    assert len(returnList) == 2,"\nERRORE\n"
    assert returnList[0] == list1, "\nERRORE\n"
    assert returnList[1] == list2, "\nERRORE\n"
    list1 = [22, "Ciao", 3.8, 787]
    list2 = ["test", 22, 22]
    test = LogicalBranch(2, "test")
    returnList = test.formDoubleList(list1, list2)
    assert len(returnList) == 2, "\nERRORE\n"
    assert returnList[0] == list1, "\nERRORE\n"
    assert returnList[1] == list2, "\nERRORE\n"

def test5():
    testInsertInList()
    testFormDoubleList()