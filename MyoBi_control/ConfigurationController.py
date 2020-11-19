import SerialHandler as SH
import NetworkCommunication

NC = NetworkCommunication.NetworkCommunication()

gripsArray = []
thresholdArray = []
state = "operation"
listeningForThresholds = False

def listenForStateChange():
    data = NC.receiveTCP()
    data = data.decode('utf-8')

    print(data)
    global state

    if(data == "1"):
        state = "operation"
    elif(data == "2"):
        print("State ændret til grips")
        state = "grips"
    elif(data == "3"):
        print("State ændret til thresholds")
        state = "thresholds"


def sendDataToPC(data):
    NC.sendUDP(data)


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


def getThresholdsFromPC():
    listeningForThresholds = True
    print("Listening for thresholds = true")

    thresholds = NC.receiveTCP()
    thresholds = thresholds.decode('utf-8')

    global thresholdArray
    thresholdArray = thresholds.split(";")

    listeningForThresholds = False
    print("Listening for thresholds = false")



def saveThresholds():
    global thresholdArray
    thresholdTxt = thresholdArray[0] + ";" + thresholdArray[1] + ";" + thresholdArray[2]
    SH.writeToFile("/home/pi/conf/thresholds/thresholds.txt", thresholdTxt)


def loadThresholds():
    thresholds = SH.readFromFile("/home/pi/conf/thresholds/thresholds.txt")

    global thresholdArray
    thresholdArray = thresholds.split(";")

    return thresholdArray;
