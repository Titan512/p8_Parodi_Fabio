import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if os.name =="nt":
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from Class.AbsolutePath import getAbsolutePath

__author__ = "Fabio Parodi"
__version__ = "1.0.0"

def testGetAbsolutePath():
    test = "/Path/da/testare"
    scriptPath = os.path.abspath(__file__)
    scriptDir = os.path.split(scriptPath)[0]
    scriptDir = os.path.split(scriptDir)[0]
    if os.name =="nt":
        test = test.replace("/", "\\")
    else:
        test = test.replace("\\", "/")
    objective = scriptDir + test
    returnPath = getAbsolutePath(test)
    assert objective == returnPath, "\nERRORE\n"

def test1():
    testGetAbsolutePath()
