def readFromFile(file):
    f = open(file, "r")
    return f.read()

def writeToFile(file, text):
    f = open(file, "w")
    f.write(text)

def writeLinesToFile(file, array):
    f = open(file, "w")
    for i in range(len(array)):
        f.write(array[i])
