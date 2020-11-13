import socket

class NetworkCommunication:

    def __init__(self):
        # Opsætning
        self.IP = '172.20.10.5'

        self.UDP_PORT = 8201
        self.UDP_ADDR = (self.IP, self.UDP_PORT)
        self.UDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.TCP_PORT = 8202
        self.TCP_ADDR = (self.IP, self.TCP_PORT)
        self.TCP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.BUFFER_SIZE = 1024  # Skiftet fra 20

    # TCP
    def receiveTCP(self):

        self.TCP_SOCK.bind(self.TCP_ADDR)
        self.TCP_SOCK.listen(1)
        print("Lytter på TCP")
        conn, addr = self.TCP_SOCK.accept()

        print("Inde i while loopet")
        data = conn.recv(self.BUFFER_SIZE)
        print(data)
        conn.send(data)  # echo
        conn.close()

        print("Ude af loopet")
        return data 


    # UDP
    def sendUDP(self, message):
        sock.sendto(MESSAGE, self.UDP_ADDR)

    def receiveUDP(self):
        sock.bind(self.UDP_ADDR)

        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes - skal måske ændres (til 4096) hvis der kommer fejl?
        print("received message: %s" % data)
         
        

