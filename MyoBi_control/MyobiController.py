import ADCreader as ADC
import time
import statistics
import ConfigurationController as CC
import threading
import handConnect as HC

gripDone = False

sensor0 = []
sensor1 = []
sensor2 = []
sensor3 = []


def listenState():
	stateThread = threading.Thread(target=CC.listenForStateChange)
	stateThread.daemon = True
	stateThread.start()

def listenThreshold():
	thresholdThread = threading.Thread(target=CC.getThresholdsFromPC)
	thresholdThread.daemon = True
	thresholdThread.start()

listenState()
grips = CC.loadGrips()
thresholds = CC.loadThresholds()

while True:

	if (CC.state == "operation"):

		data = ADC.getData()

		if(len(sensor0)<25): #Ændret fra 50
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
			
			if(statistics.mean(sensor1) > float(thresholds[0])):
				if(gripDone == False):
					HC.sendCommand(grips[0])
					gripDone = True
					print(str(statistics.mean(sensor1)))
					print(grips[0])
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)
					
				else:
					HC.sendCommand("F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r")
					gripDone = False
					print(str(statistics.mean(sensor1)))
					print('Går tilbage til åben hånd \n\r')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)

			elif(statistics.mean(sensor2) > float(thresholds[1])):
				if(gripDone == False):
					HC.sendCommand(grips[1])
					gripDone = True
					print(str(statistics.mean(sensor2)))
					print(grips[1])
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)
					
				else:
					HC.sendCommand("F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r")
					gripDone = False
					print(str(statistics.mean(sensor2)))
					print('Går tilbage til åben hånd\n\r')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)

			elif(statistics.mean(sensor3) > float(thresholds[2])):
				if(gripDone == False):
					HC.sendCommand(grips[2])
					gripDone = True
					print(str(statistics.mean(sensor3)))
					print(grips[2])
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)
					
				else:
					HC.sendCommand("F0 P0 \n\r F1 P0 \n\r F2 P0 \n\r F3 P0 \n\r")
					gripDone = False
					print(str(statistics.mean(sensor3)))
					print('Går tilbage til åben hånd \n\r')
					sensor0.clear()
					sensor1.clear()
					sensor2.clear()
					sensor3.clear()
					time.sleep(1)

	elif (CC.state == "grips"):
		print("I grips state")

		PCgrips = CC.getGripsFromPC()

		if (CC.cancelled == True):
			CC.cancelled = False
			print("Grips er cancelled")
		else:
			grips = PCgrips
			print(grips[0] + ", " + grips[1] + ", " + grips[2])
			CC.saveGrips()

				
		CC.state = "operation"
		listenState()

	elif (CC.state == "thresholds"):
		print("I thresholds state")

		listenThreshold() #Listen for TCP message with thresholds

		while (CC.listeningForThresholds == True):
				data = ADC.getData()
				dataString = str(data[0]) + ";" + str(data[1]) + ";" + str(data[2]) + ";" + str(data[3])
				CC.sendDataToPC(dataString)
		
		if (CC.cancelled == True):
			CC.cancelled = False
			print("Thresholds er cancelled")
			print("While loopet i thresholds brudt")

		else:
			print("While loopet i thresholds brudt")
			CC.saveThresholds()
			thresholds = CC.loadThresholds()

		CC.state = "operation"
		listenState() #When loop is finished, start listenState() thread again







