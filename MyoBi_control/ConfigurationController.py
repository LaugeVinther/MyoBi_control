import SerialHandler as SH
import NetworkCommunication

NC = NetworkCommunication.NetworkCommunication()

gripsArray = []
operationState = True


def listenForStateChange():
    data = NC.receiveTCP()
    data = data.decode('utf-8')

    print(data)

    if(data == "1"):
        global operationState
        operationState = True
    elif(data == "2"):
        print("Operation state ændret til false")
        operationState = False

def getGripsFromPC():
    grips = NC.receiveTCP()
    grips = grips.decode('utf-8')
    
    global gripsArray
    gripsArray = grips.split(";")

   # gripsArray = dataSplit[0] + dataSplit[1] + dataSplit[2]
        
    return gripsArray

def saveGrips():
    global gripsArray
    gripsTxt = gripsArray[0] + ";" + gripsArray[1] + ";" + gripsArray[2]
    SH.writeLinesToFile("/home/pi/conf/grips/grips.txt", gripsTxt)

def loadGrips():
    grips = SH.readFromFile("/home/pi/conf/grips/grips.txt")

    global gripsArray
    gripsArray = grips.split(";")

    return gripsArray;
