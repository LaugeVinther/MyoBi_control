import serial

arduino = serial.Serial('COM3',115200, timeout=None, write_timeout=None)

#arduino.write(b'F0 P100 \n\r F1 P100 \n\r F2 P100 \n\r F3 P100 \n\r')
#arduino.write(b'F1 P0 \r')


def sendCommand(command):
    with serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.3:1.0', 115200, timeout=1) as ser:
        ser.write(command)
