import serial

hand = serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.3:1.0', 115200, timeout=1)

def sendCommand(command):
    hand.write(command.encode())
