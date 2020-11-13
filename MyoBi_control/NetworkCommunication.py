import socket

class NetworkCommunication:

    def __init__():
        # Opsætning
        IP = socket.gethostbyname(socket.gethostname())

        UDP_PORT = 8201
        UDP_ADDR = (IP, UDP_PORT)
        UDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        TCP_PORT = 8202
        TCP_ADDR = (IP, TCP_PORT)
        TCP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        BUFFER_SIZE = 1024  # Skiftet fra 20

    # TCP
    def receiveTCP():

        TCP_SOCK.bind(TCP_ADDR)
        TCP_SOCK.listen(1)
        conn, addr = TCP_SOCK.accept()

        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break # Skal måske fjernes
            conn.send(data)  # echo
        conn.close()
        return data #ikke sikker på denne


    # UDP
    def sendUDP(message):
        sock.sendto(MESSAGE, UDP_ADDR)

    def receiveUDP():
        sock.bind(UDP_ADDR)

        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes - skal måske ændres (til 4096) hvis der kommer fejl?
        print("received message: %s" % data)
         
        

