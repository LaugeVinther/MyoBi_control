import socket

class NetworkCommunication:

    def __init__(self):
        # Opsætning
        self.IP = socket.gethostbyname(socket.gethostname())

        self.UDP_PORT = 8201
        self.UDP_ADDR = (IP, UDP_PORT)
        self.UDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.TCP_PORT = 8202
        self.TCP_ADDR = (IP, TCP_PORT)
        self.TCP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.BUFFER_SIZE = 1024  # Skiftet fra 20

    # TCP
    def receiveTCP(self):

        self.TCP_SOCK.bind(self.TCP_ADDR)
        self.TCP_SOCK.listen(1)
        conn, addr = self.TCP_SOCK.accept()

        while 1:
            data = conn.recv(self.BUFFER_SIZE)
            if not data: break # Skal måske fjernes
            conn.send(data)  # echo
        conn.close()
        return data #ikke sikker på denne


    # UDP
    def sendUDP(self, message):
        sock.sendto(MESSAGE, self.UDP_ADDR)

    def receiveUDP(self):
        sock.bind(self.UDP_ADDR)

        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes - skal måske ændres (til 4096) hvis der kommer fejl?
        print("received message: %s" % data)
         
        

