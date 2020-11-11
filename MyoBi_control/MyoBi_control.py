import handConnect as hC
import ADCreader as ADC
import time
import statistics


sensor0 = []
sensor1 = []
sensor2 = []
sensor3 = []

bagGripDone = False
pinchGripDone = False
bottleGripDone = False
pointGripDone = False
gripDone = False


start = time.monotonic()
samples = 0

try:
	while True:

		data = ADC.getData()

		samples += 1 #tidsmåling


		if(len(sensor0)<50):
			sensor0.append(data[0])
			sensor1.append(data[1])
			sensor2.append(data[2])
			sensor3.append(data[3])

		else:
			for i in range(len(sensor0)-1):

				sensor0[i]=sensor0[i+1]
				sensor1[i]=sensor1[i+1]
				sensor2[i]=sensor2[i+1]
				sensor3[i]=sensor3[i+1]

			del sensor0[-1]
			del sensor1[-1]
			del sensor2[-1]
			del sensor3[-1]

			sensor0.append(data[0])
			sensor1.append(data[1])
			sensor2.append(data[2])
			sensor3.append(data[3])
					

			if(statistics.mean(sensor2) > 2):
				if(gripDone == False):
					hC.sendCommand(b'G0 C \n\r F0 P0 \n\r')
					gripDone = True
					print(str(statistics.mean(sensor2)))
					print('\GripDone skifter til true')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)
					

				else:
					hC.sendCommand(b'F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r')
					gripDone = False
					print(str(statistics.mean(sensor2)))
					print('\nGripDone skifter til false')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)

			elif(statistics.mean(sensor3) > 1.5):
				if(gripDone == False):
					hC.sendCommand(b'F0 P75 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r')
					gripDone = True
					print(str(statistics.mean(sensor3)))
					print('\nGripDone skifter til true')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)
					

				else:
					hC.sendCommand(b'F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r')
					gripDone = False
					print(str(statistics.mean(sensor3)))
					print('\nGripDone skifter til false')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)
					

except KeyboardInterrupt:
	pass

end = time.monotonic() #tidsmåling

total_time = end - start #tidsmåling

print("Time of capture: {}s".format(total_time)) #tidsmåling
print("Sample rate={}".format(samples / total_time)) #tidsmåling
print('\nSamples:' + str(samples))







