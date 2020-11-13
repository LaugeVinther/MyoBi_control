def readFromFile(file):
    f = open(file, "r")
    return f.read()

def writeToFile(file, text):
    f = open(filename, "x")
    f.write(text)

def writeLinesToFile(file, array):
    f = open(filname, "w")
    for i in range(len(array)):
        f.write(array[i])
