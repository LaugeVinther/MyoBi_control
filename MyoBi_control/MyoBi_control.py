import handConnect as hC
import ADCreader as ADC
import time
import statistics


Voltage = []
gripDone = False

start = time.monotonic()
samples = 0

try:
	while True:

		data = ADC.getData()
		samples += 1 #tidsmåling


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
					print('Spænding under 2.5')
				else:
					hC.sendCommand(b'F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r')
					gripDone = False
					Voltage.clear()
					time.sleep(1)
					print('Spænding over 2.5')
except KeyboardInterrupt:
	pass

end = time.monotonic() #tidsmåling

total_time = end - start #tidsmåling

print("Time of capture: {}s".format(total_time)) #tidsmåling
print("Sample rate={}".format(samples / total_time)) #tidsmåling
print('\nSamples:' + str(samples))







