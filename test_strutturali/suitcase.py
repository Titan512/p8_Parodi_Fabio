from coverage import Coverage
cov = Coverage()
cov.start()
import os
import sys
from sys import path
scriptDir = os.path.split(sys.path[0])[0]
if(os.name =="nt"):
    path.insert(1,scriptDir+"\\src")
else:
    path.insert(1,scriptDir+"/src")
from STAbsolutePath import test1
from STInputTree import test2
from STLeaf import test3
from STLogicalBranch import test4
from STNode import test5
from STPatternTree import test6
from STToken import test7
from STTranslation import test8
from STTree import test9

#pulisco il terminale
os.system("cls" if os.name == "nt" else "clear")
#eseguo i vari test
#presentati con nomi standard e numerati perchè
#da eseguire concettualmente in sequenza
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
#fermo la copertura
cov.stop()
#mostro solo la copertura delle classi
#escludendo il codice dei test
fileToShow = []
#creo il percorso assoluto
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.split(scriptPath)[0]
scriptDir = os.path.split(scriptDir)[0]
#inserisco il percorso relativo delle classi
if os.name == "nt":
    fileToShow.append(scriptDir+"\src\Class\AbsolutePath.py")
    fileToShow.append(scriptDir+"\src\Class\InputTree.py")
    fileToShow.append(scriptDir+"\src\Class\Leaf.py")
    fileToShow.append(scriptDir+"\src\Class\LogicalBranch.py")
    fileToShow.append(scriptDir+"\src\Class\\Node.py")
    fileToShow.append(scriptDir+"\src\Class\PatternTree.py")
    fileToShow.append(scriptDir+"\src\Class\Token.py")
    fileToShow.append(scriptDir+"\src\Class\Translation.py")
    fileToShow.append(scriptDir+"\src\Class\Tree.py")
else:
    fileToShow.append(scriptDir+"/src/Class/AbsolutePath.py")
    fileToShow.append(scriptDir+"/src/Class/InputTree.py")
    fileToShow.append(scriptDir+"/src/Class/Leaf.py")
    fileToShow.append(scriptDir+"/src/Class/LogicalBranch.py")
    fileToShow.append(scriptDir+"/src/Class/Node.py")
    fileToShow.append(scriptDir+"/src/Class/PatternTree.py")
    fileToShow.append(scriptDir+"/src/Class/Token.py")
    fileToShow.append(scriptDir+"/src/Class/Translation.py")
    fileToShow.append(scriptDir+"/src/Class/Tree.py")
cov.report(include=fileToShow)
#Nota per la copertura
print("\nNOTA: AbsolutePath non raggiunge il 100% ", end="")
print("a causa della scelta tra SO Linux o Windows")
