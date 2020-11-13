import SerialHandler as SH
import NetworkCommunication

NC = NetworkCommunication.NetworkCommunication

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
    grips = NC.receiveTCP()

    dataSplit = grips.split(";")

    global gripsArray
    gripsArray = dataSplit[0] + "\n" + dataSplit[1] + "\n" + dataSplit[2] + "\n"
        
    return gripsArray

def saveGrips():
    SH.writeLinesToFile("/home/pi/conf/grips/grips.txt", gripsArray)

def loadGrips():
    grips = SH.readFromFile("/home/pi/conf/grips/grips.txt")

    global gripsArray
    gripsArray = grips.split("\n")

    return gripsArray;
