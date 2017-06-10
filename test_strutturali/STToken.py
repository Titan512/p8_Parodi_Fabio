import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.Token import Token

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testSetGetValue():
    test = Token(0, "value", "type")
    assert test.getValue() == "value", "\nERRORE\n"
    test.setValue("NewValue")
    assert test.getValue() == "NewValue", "\nERRORE\n"

def testGetType():
    test = Token(0, "value", "type")
    assert test.getType() == "type", "\nERRORE\n"
    test = Token(0, "value", "otherType")
    assert test.getType() == "otherType", "\nERRORE\n"
    test = Token(0, "value", "strangeType")
    assert test.getType() == "strangeType", "\nERRORE\n"

def test7():
    testSetGetValue()
    testGetType()
