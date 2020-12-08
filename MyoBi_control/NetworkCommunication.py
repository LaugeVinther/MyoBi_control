import socket

class NetworkCommunication:

    def __init__(self):
        # Opsætning
        self.UDP_IP = '172.20.10.3'
        self.UDP_PORT = 8201
        self.UDP_ADDR = (self.UDP_IP, self.UDP_PORT)
        self.UDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.TCP_IP = '172.20.10.6  '
        self.TCP_PORT = 8202
        self.TCP_ADDR = (self.TCP_IP, self.TCP_PORT)
        self.TCP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP_SOCK.bind(self.TCP_ADDR)

        self.BUFFER_SIZE = 1024  # Skiftet fra 20


    # TCP
    def receiveTCP(self):

        self.TCP_SOCK.listen(1)
        conn, addr = self.TCP_SOCK.accept()

        data = conn.recv(self.BUFFER_SIZE)
        print(data)
        conn.send(data)  # echo
        conn.close()

        return data 


    # UDP
    def sendUDP(self, message):
        message = message.encode()
        self.UDP_SOCK.sendto(message, self.UDP_ADDR)

    def receiveUDP(self):
        self.UDP_SOCK.bind(self.UDP_ADDR)

        data, addr = self.UDP_SOCK.recvfrom(1024) # buffer size is 1024 bytes - skal måske ændres (til 4096) hvis der kommer fejl?
        print("received message: %s" % data)
         
        

