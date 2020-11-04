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

	data = ADC.getData

	if(len(Voltage)<100):
		Voltage.append(data)
	else:
		for i in range(len(Voltage)-1):
			Voltage[i]=Voltage[i+1]
		del Voltage[-1]
		Voltage.append(data)
		
		if(statistics.mean(Voltage) > 25):
			if(gripDone == False):
				# hC.sendCommand(
				gripDone = True
				#Sleep
			else:
				# hC.sendCommand(
				gripDone = False

	time.sleep(0.01)







