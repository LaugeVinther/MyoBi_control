import SerialHandler as SH
import NetworkCommunication as NC

gripsArray = []
operationState = True

def listenForStateChange():
    state = NC.receiveTCP()
    
    if(state == "1"):
        global operationState
        operationState = True
    elif(state == "2"):
        operationState = False

def getGripsFromPC():
    data = NC.receiveTCP()

    dataSplit = data.split(";")

    global gripsArray
    gripsArray = dataSplit[0] + "\n" + dataSplit[1] + "\n" + dataSplit[2] + "\n"
        
    return gripsArray

def saveGrips():
    SH.writeLinesToFile("/conf/grips/grips.txt", gripsArray)

def loadGrips():
    grips = SH.readFromFile("/conf/grips/grips.txt")

    global gripsArray
    gripsArray = data.split("\n")

    return gripsArray;
