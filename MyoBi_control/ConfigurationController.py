import SerialHandler as SH
import NetworkCommunication

NC = NetworkCommunication.NetworkCommunication()

gripsArray = []
state = "operation"


def listenForStateChange():
    data = NC.receiveTCP()
    data = data.decode('utf-8')

    print(data)

    if(data == "1"):
        global operationState
        state = "operation"
    elif(data == "2"):
        print("Operation state ændret til false")
        state = "grips"
    elif(data == "3"):
        print("Operation state ændret til false")
        state = "thresholds"

def getGripsFromPC():
    grips = NC.receiveTCP()
    grips = grips.decode('utf-8')

    global gripsArray
    gripsArray = grips.split(";")

    for i in range(len(gripsArray)):
        gripsArray[i] = gripsArray[i].replace("nr", "\n\r")

   # gripsArray = dataSplit[0] + dataSplit[1] + dataSplit[2]
        
    return gripsArray

def saveGrips():
    global gripsArray
    gripsTxt = gripsArray[0] + ";" + gripsArray[1] + ";" + gripsArray[2]
    SH.writeToFile("/home/pi/conf/grips/grips.txt", gripsTxt)

def loadGrips():
    grips = SH.readFromFile("/home/pi/conf/grips/grips.txt")

    global gripsArray
    gripsArray = grips.split(";")

    for i in range(len(gripsArray)):
        gripsArray[i] = gripsArray[i].replace("nr", "\n\r")

    return gripsArray;

def sendDataToPC(data):
    NC.sendUDP(data)
