import handConnect as hC
import ADCreader as ADC
import time
import statistics


# if
    # Noget er større end noget andet
    # hC.sendCommand(

Voltage = []
gripDone = False

while True:

	data = ADC.getData()

	if(len(Voltage)<50):
		Voltage.append(data)
	else:
		for i in range(len(Voltage)-1):
			Voltage[i]=Voltage[i+1]
		del Voltage[-1]
		Voltage.append(data)
		

		if(statistics.mean(Voltage) > 2.5):
			if(gripDone == False):
				hC.sendCommand(b'F0 P100 \n\r F1 P100 \n\r F2 P0 \n\r F3 P100 \n\r')
				gripDone = True
				Voltage.clear()
				time.sleep(1)
			else:
				hC.sendCommand(b'F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r')
				gripDone = False
				Voltage.clear()
				time.sleep(1)








